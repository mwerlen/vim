#!/bin/bash

LANG=C
SPEC=vim.spec

DATE=`date +"%a %b %d %Y"`
MAJORVERSION=`grep "define baseversion" vim.spec | cut -d ' ' -f 3`
CHLOG="* $DATE Karsten Hopp <karsten@redhat.com> $MAJORVERSION"
ORIGPL=`grep "define patchlevel" vim.spec | cut -d ' ' -f 3`
#ORIGPL=350
PL=$ORIGPL

while true; do
    PL=$((PL+1))
    PNAME="$MAJORVERSION.$PL"
    URL="ftp://ftp.vim.org/pub/vim/patches/$MAJORVERSION/$PNAME"
    wget -nc $URL 2>/dev/null
    if [ "$?" -ne "0" ]; then
        # Patchlevel not yet available, back down
        PL=$((PL-1))
        if [ "$PL" == "$ORIGPL" ]; then
            echo "No new patchlevel available"
            exit
        fi
        break
    else
        # echo "Got patchlevel $MAJORVERSION.$PL, current CVS is at $MAJORVERSION.$ORIGPL"
        cvs add $PNAME
        cvs ci -m "- patchlevel $PL" $PNAME
        sed -i -e "/Patch$((PL-1)): ftp:\/\/ftp.vim.org\/pub\/vim\/patches\/$MAJORVERSION\/$MAJORVERSION.$((PL-1))/aPatch$PL: ftp:\/\/ftp.vim.org\/pub\/vim\/patches\/$MAJORVERSION\/$MAJORVERSION.$PL" $SPEC
        sed -i -e "/patch$((PL-1)) -p0/a%patch$PL -p0" $SPEC
    fi
done
sed -i -e "s/define patchlevel $ORIGPL/define patchlevel $PL/" $SPEC
sed -i -e "/\%changelog/a$CHLOG.$PL-1\n- patchlevel $PL\n" $SPEC
wget ftp://ftp.vim.org/pub/vim/patches/$MAJORVERSION/README -O README.patches
cvs ci -m "- patchlevel $PL" 
make tag
make build
