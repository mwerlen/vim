#!/bin/bash
debug=""
#debug="echo "
branches=( "master" "f28" "f27" "f26" )
releases=( "fc29" "fc28" "fc27" "fc26" )
regexps=( "fc29" "\|fc28" "\|fc27" "\|fc26" )
bodhi_enabled=( "0" "0" "1" "1")
branches_count=4
#releases_regexp=fc28\\\|fc27\\\|fc28

branches_index=0
release_index=0
regexp_index=0
bodhi_enabled_index=0
done_build=0
releases_regexp="${regexps[@]: regexp_index: 1}"
let "regexp_index+=1"

cd `dirname $0`
LANG=C
SPEC=vim.spec
CHANGES=1
force=0

if [ "x$1" == "x--force" ]; then
  force=1
fi

DATE=`date +"%a %b %d %Y"`
fedpkg switch-branch "${branches[@]: $branches_index: 1}"


if [ $? -ne 0 ]; then
  echo "Error with switching branch"
  exit 1
fi

MAJORVERSION=`grep "define baseversion" vim.spec | cut -d ' ' -f 3`
ORIGPL=`grep "define patchlevel" vim.spec | cut -d ' ' -f 3 | sed -e "s/^0*//g"`
ORIGPLFILLED=`printf "%03d" $ORIGPL`

if [ ! -d vim-upstream ]; then
   git clone https://github.com/vim/vim.git vim-upstream
else
   pushd vim-upstream
   git pull
   popd
fi

pushd vim-upstream

# get the latest tag. Might be tricky with other packages, but upstream vim uses just a single branch:
LASTTAG=$(git describe --tags $(git rev-list --tags --max-count=1))

# vim upstream tags have the form v7.4.123. Remove the 'v' and get major release and patchlevel:
UPSTREAMMAJOR=$(echo $LASTTAG | sed -e 's/v\([0-9]*\.[0-9]*\).*/\1/')
LASTPL=`echo $LASTTAG| sed -e 's/.*\.//;s/^0*//'`
LASTPLFILLED=`printf "%03d" $LASTPL`
if [ $force -ne 1 -a "$ORIGPLFILLED" == "$LASTPLFILLED" ]; then
    echo "No new patchlevel available"
    CHANGES=0
fi
rm -rf dist/* 2>/dev/null
make unixall

# include patchlevel in tarball name so that older sources won't get overwritten:
mv dist/vim-${UPSTREAMMAJOR}.tar.bz2 dist/vim-${UPSTREAMMAJOR}-${LASTPLFILLED}.tar.bz2

# We don't include the full upstream changelog in the rpm changelog, just ship a file with
# the changes:
popd

cp -f vim-upstream/dist/vim-${UPSTREAMMAJOR}-${LASTPLFILLED}.tar.bz2 .
#wget https://raw.githubusercontent.com/ignatenkobrain/vim-spec-plugin/master/ftplugin/spec.vim -O ftplugin-spec.vim
#wget https://raw.githubusercontent.com/ignatenkobrain/vim-spec-plugin/master/syntax/spec.vim -O syntax-spec.vim
if [ $CHANGES -ne 0 ]; then
   CHLOG="* $DATE Karsten Hopp <karsten@redhat.com> $UPSTREAMMAJOR"
   $debug sed -i -e "/Release: /cRelease: 1%{?dist}" $SPEC
   if [ "x$MAJORVERSION" != "x$UPSTREAMMAJOR" ]; then
      $debug sed -i -s "s/define baseversion: $MAJORVERSION/define baseversion: $UPSTREAMMAJOR=/" $SPEC
   fi
   $debug sed -i -e "s/define patchlevel $ORIGPLFILLED/define patchlevel $LASTPLFILLED/" $SPEC
   $debug sed -i -e "/\%changelog/a$CHLOG.$LASTPLFILLED-1\n- patchlevel $LASTPLFILLED\n" $SPEC
   $debug fedpkg new-sources vim-${UPSTREAMMAJOR}-${LASTPLFILLED}.tar.bz2
   $debug git add vim.spec
   $debug git commit -m "- patchlevel $LASTPL" 

   # mockbuild
   $debug fedpkg mockbuild
   if [ $? -ne 0 ]; then
     echo "Error: fedpkg mockbuild"
     exit 1
   fi

   # push
   $debug fedpkg push
   if [ $? -ne 0 ]; then
     echo "Error: fedpkg push"
     exit 1
   fi

   # Check if release has pending or testing update - if not, build package
   # and submit update for testing
   pending_update=`bodhi updates query --packages vim --status pending \
     | grep $releases_regexp`
   testing_update=`bodhi updates query --packages vim --status testing \
     | grep $releases_regexp`

   if [ "$pending_update" == "" ] && [ "$testing_update" == "" ]; then
     fedpkg build
     if [ $? -eq 0 ]; then
       done_build=1
     else
       echo "Error when building package in $branch"
       exit 1
     fi
   else
     echo "There are pending/testing updates, do not build package."
   fi

   let "release_index+=1"
   let "bodhi_enabled_index+=1"

   for branch in "${branches[@]:(1)}";
   do
     # switch to branch
     $debug fedpkg switch-branch $branch

     # merge with previous branch
     $debug bash -c "git merge ${branches[@]: $branches_index: 1} <<<':x'"
     if [ $? -ne 0 ]; then
       echo "Error: git merge ${branches[@]: $branches_index: 1}"
       exit 1
     fi

     # mockbuild
     $debug fedpkg mockbuild
     if [ $? -ne 0 ]; then
       echo "Error: fedpkg mockbuild failed"
       exit 1
     fi

     # push
     $debug fedpkg push
     if [ $? -ne 0 ]; then
       echo "Error: fedpkg push"
       exit 1
     fi

     # append next release to regexp - because we need to check if there aren't
     # any testing updates from higher branches (lower branch cannot have
     # bigger NVR than higher branch) in next iteration
     releases_regexp="$releases_regexp${regexps[@]: regexp_index: 1}"

     # Check if release has pending or testing update - if not, build package
     # and submit update for testing
     #  | grep $releases_regexp`
     # done_build is checking, if previous branch did build - lower branch can do
     # a build only when higher branch build was ok.
     testing_update=`bodhi updates query --packages vim --status testing \
       | grep $releases_regexp`
     if [[ "$testing_update" == ""  &&  $done_build -eq 1 ]]; then
       fedpkg build
       if [ $? -eq 0 ]; then
         # if branch isn't master or branch is enabled in bodhi, create update
         if [ $branch != "master" || "${bodhi_enabled[@]: $bodhi_enabled_index: 1}"=="1" ]; then
           bodhi updates new --user zdohnal --type enhancement --notes "The newest upstream commit" --request testing --autokarma --stable-karma 3 --unstable-karma -3 vim-${UPSTREAMMAJOR}.${LASTPLFILLED}-1.${releases[@]: $release_index: 1}
         fi
       else
         echo "Error when building package for $branch"
         exit 1
       fi
     else
       done_build=0
     fi

     # Increment index
     let "branches_index+=1"
     let "release_index+=1"
     let "regexp_index+=1"
     let "bodhi_enabled_index+=1"
   done
   #$debug git push
   #if [ $? -eq 0 ]; then
   #   $debug rm -f $HOME/.koji/config
   #   $debug fedpkg build
   #   $debug ln -sf ppc-config $HOME/.koji/config
   #else
   #   echo "GIT push failed"
   #fi
fi

#go back to master
$debug fedpkg switch-branch master

exit 0
