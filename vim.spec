%define WITH_SELINUX 1
%define desktop_file 1
%if %{desktop_file}
%define desktop_file_utils_version 0.2.93
%endif

# Set this to 1 if you're building the enterprise version
%define enterprise 0

%if %{enterprise}
# don't build gvim
%define withgui 0
# don't include ruby interpreter
%define withruby 0
%else
%define withgui 1
%define withruby 0
%define withnetbeans 0
%endif


%define baseversion 6.3
%define vimdir vim63
%define patchlevel 071

Summary: The VIM editor.
Name: vim
Version: %{baseversion}.%{patchlevel}
Release: 3
License: freeware
Group: Applications/Editors
Source0: ftp://ftp.vim.org/pub/vim/unix/vim-%{baseversion}.tar.bz2
Source1: ftp://ftp.vim.org/pub/vim/extra/vim-%{baseversion}-lang.tar.gz
Source2: ftp://ftp.vim.org/pub/vim/extra/vim-%{baseversion}-extra.tar.gz
Source3: gvim.desktop
Source4: vimrc
Source5: ftp://ftp.vim.org/pub/vim/patches/README.patches
Source6: spec.vim
Source7: gvim16.png
Source8: gvim32.png
Source9: gvim48.png
Source10: gvim64.png
Source11: Changelog.rpm
Patch2000: vim-4.2-speed_t.patch
Patch2001: vim-5.6a-paths.patch
Patch2002: vim-6.0-fixkeys.patch
Patch2003: vim-6.2-specsyntax.patch
Patch2004: vim-6.0r-crv.patch
Patch2005: vim-6.3-tmpfile.patch
Patch2010: xxd-locale.patch
# Patches 001 < 999 are patches from the base maintainer.
# If you're as lazy as me, generate the list using
# for i in `seq 1 14`; do printf "Patch%03d: ftp://ftp.vim.org/pub/vim/patches/6.2.%03d\n" $i $i; done
Patch001: ftp://ftp.vim.org/pub/vim/patches/6.3.001
Patch002: ftp://ftp.vim.org/pub/vim/patches/6.3.002
Patch003: ftp://ftp.vim.org/pub/vim/patches/6.3.003
Patch004: ftp://ftp.vim.org/pub/vim/patches/6.3.004
Patch005: ftp://ftp.vim.org/pub/vim/patches/6.3.005
Patch006: ftp://ftp.vim.org/pub/vim/patches/6.3.006
Patch007: ftp://ftp.vim.org/pub/vim/patches/6.3.007
Patch008: ftp://ftp.vim.org/pub/vim/patches/6.3.008
Patch009: ftp://ftp.vim.org/pub/vim/patches/6.3.009
Patch010: ftp://ftp.vim.org/pub/vim/patches/6.3.010
Patch011: ftp://ftp.vim.org/pub/vim/patches/6.3.011
Patch012: ftp://ftp.vim.org/pub/vim/patches/6.3.012
Patch013: ftp://ftp.vim.org/pub/vim/patches/6.3.013
Patch014: ftp://ftp.vim.org/pub/vim/patches/6.3.014
Patch015: ftp://ftp.vim.org/pub/vim/patches/6.3.015
Patch016: ftp://ftp.vim.org/pub/vim/patches/6.3.016
Patch017: ftp://ftp.vim.org/pub/vim/patches/6.3.017
Patch018: ftp://ftp.vim.org/pub/vim/patches/6.3.018
Patch019: ftp://ftp.vim.org/pub/vim/patches/6.3.019
Patch020: ftp://ftp.vim.org/pub/vim/patches/6.3.020
Patch021: ftp://ftp.vim.org/pub/vim/patches/6.3.021
Patch022: ftp://ftp.vim.org/pub/vim/patches/6.3.022
Patch023: ftp://ftp.vim.org/pub/vim/patches/6.3.023
Patch024: ftp://ftp.vim.org/pub/vim/patches/6.3.024
Patch025: ftp://ftp.vim.org/pub/vim/patches/6.3.025
Patch026: ftp://ftp.vim.org/pub/vim/patches/6.3.026
Patch027: ftp://ftp.vim.org/pub/vim/patches/6.3.027
Patch028: ftp://ftp.vim.org/pub/vim/patches/6.3.028
Patch029: ftp://ftp.vim.org/pub/vim/patches/6.3.029
Patch030: ftp://ftp.vim.org/pub/vim/patches/6.3.030
Patch031: ftp://ftp.vim.org/pub/vim/patches/6.3.031
Patch032: ftp://ftp.vim.org/pub/vim/patches/6.3.032
Patch033: ftp://ftp.vim.org/pub/vim/patches/6.3.033
Patch034: ftp://ftp.vim.org/pub/vim/patches/6.3.034
Patch035: ftp://ftp.vim.org/pub/vim/patches/6.3.035
Patch036: ftp://ftp.vim.org/pub/vim/patches/6.3.036
Patch037: ftp://ftp.vim.org/pub/vim/patches/6.3.037
Patch038: ftp://ftp.vim.org/pub/vim/patches/6.3.038
Patch039: ftp://ftp.vim.org/pub/vim/patches/6.3.039
Patch040: ftp://ftp.vim.org/pub/vim/patches/6.3.040
Patch041: ftp://ftp.vim.org/pub/vim/patches/6.3.041
Patch042: ftp://ftp.vim.org/pub/vim/patches/6.3.042
Patch043: ftp://ftp.vim.org/pub/vim/patches/6.3.043
Patch044: ftp://ftp.vim.org/pub/vim/patches/6.3.044
Patch045: ftp://ftp.vim.org/pub/vim/patches/6.3.045
Patch046: ftp://ftp.vim.org/pub/vim/patches/6.3.046
Patch047: ftp://ftp.vim.org/pub/vim/patches/6.3.047
Patch048: ftp://ftp.vim.org/pub/vim/patches/6.3.048
Patch049: ftp://ftp.vim.org/pub/vim/patches/6.3.049
Patch050: ftp://ftp.vim.org/pub/vim/patches/6.3.050
Patch051: ftp://ftp.vim.org/pub/vim/patches/6.3.051
Patch052: ftp://ftp.vim.org/pub/vim/patches/6.3.052
Patch053: ftp://ftp.vim.org/pub/vim/patches/6.3.053
Patch054: ftp://ftp.vim.org/pub/vim/patches/6.3.054
Patch055: ftp://ftp.vim.org/pub/vim/patches/6.3.055
Patch056: ftp://ftp.vim.org/pub/vim/patches/6.3.056
Patch057: ftp://ftp.vim.org/pub/vim/patches/6.3.057
Patch058: ftp://ftp.vim.org/pub/vim/patches/6.3.058
Patch059: ftp://ftp.vim.org/pub/vim/patches/6.3.059
Patch060: ftp://ftp.vim.org/pub/vim/patches/6.3.060
Patch061: ftp://ftp.vim.org/pub/vim/patches/6.3.061
Patch062: ftp://ftp.vim.org/pub/vim/patches/6.3.062
Patch063: ftp://ftp.vim.org/pub/vim/patches/6.3.063
Patch064: ftp://ftp.vim.org/pub/vim/patches/6.3.064
Patch065: ftp://ftp.vim.org/pub/vim/patches/6.3.065
Patch066: ftp://ftp.vim.org/pub/vim/patches/6.3.066
Patch067: ftp://ftp.vim.org/pub/vim/patches/6.3.067
Patch068: ftp://ftp.vim.org/pub/vim/patches/6.3.068
Patch069: ftp://ftp.vim.org/pub/vim/patches/6.3.069
Patch070: ftp://ftp.vim.org/pub/vim/patches/6.3.070
Patch071: ftp://ftp.vim.org/pub/vim/patches/6.3.071

Patch3000: vim-6.1-syntax.patch
Patch3001: vim-6.2-rh1.patch
Patch3002: vim-6.1-rh2.patch
Patch3003: vim-6.1-rh3.patch
Patch3004: vim-6.2-rclocation.patch
Patch3005: vim-6.2-rh4.patch
Patch3006: vim-6.2-rh5.patch
Patch3007: vim-6.3-dnssyntax.patch

Patch3100: vim-selinux.patch

Buildroot: %{_tmppath}/%{name}-%{version}-root
Buildrequires: python-devel perl libtermcap-devel gettext
Buildrequires: libacl-devel gpm-devel
%if "%{withruby}" == "1"
Buildrequires: ruby ruby-devel
%endif
%if %{WITH_SELINUX}
Buildrequires: libselinux-devel
%endif
%if %{desktop_file}
Requires: /usr/bin/desktop-file-install
BuildPrereq: desktop-file-utils >= %{desktop_file_utils_version}
%endif
Epoch: 1

%description
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.

%package common
Summary: The common files needed by any version of the VIM editor.
Group: Applications/Editors

%description common
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.  The
vim-common package contains files which every VIM binary will need in
order to run.

If you are installing vim-enhanced or vim-X11, you'll also need
to install the vim-common package.

%package minimal
Summary: A minimal version of the VIM editor.
Group: Applications/Editors
Obsoletes:  vim

%description minimal
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more. The
vim-minimal package includes a minimal version of VIM, which is
installed into /bin/vi for use when only the root partition is
present. NOTE: The online help is only available when the vim-common
package is installed.

%package enhanced
Summary: A version of the VIM editor which includes recent enhancements.
Group: Applications/Editors
Requires: vim-common = %{epoch}:%{version}-%{release}
Requires: %(perl -le 'printf("perl >= %vd\n",$^V);')
Obsoletes: vim-color

%description enhanced
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.  The
vim-enhanced package contains a version of VIM with extra, recently
introduced features like Python and Perl interpreters.

Install the vim-enhanced package if you'd like to use a version of the
VIM editor which includes recently added enhancements like
interpreters for the Python and Perl scripting languages.  You'll also
need to install the vim-common package.

%if "%{withgui}" == "1"
%package X11
Summary: The VIM version of the vi editor for the X Window System.
Group: Applications/Editors
Requires: vim-common = %{epoch}:%{version}-%{release} libattr
BuildRequires: gtk2-devel
Prereq: gtk2 >= 2.6

%description X11
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and
more. VIM-X11 is a version of the VIM editor which will run within the
X Window System.  If you install this package, you can run VIM as an X
application with a full GUI interface and mouse support.

Install the vim-X11 package if you'd like to try out a version of vi
with graphics and mouse capabilities.  You'll also need to install the
vim-common package.
%endif

%prep
%setup -q -b 1 -n %{vimdir}
cp -f %{SOURCE6} runtime/ftplugin/spec.vim
%patch2000 -p1
# fix rogue dependencies from sample code
chmod -x runtime/tools/mve.awk
%patch2001 -p1
%patch2002 -p1
%patch2003 -p1
%patch2004 -p1
%patch2005 -p1
%patch2010 -p1
perl -pi -e "s,bin/nawk,bin/awk,g" runtime/tools/mve.awk

# Base patches...
# for i in `seq 1 14`; do printf "%%patch%03d -p0 \n" $i; done
%patch001 -p0
%patch002 -p0
%patch003 -p0
%patch004 -p0
%patch005 -p0
%patch006 -p0
%patch007 -p0
%patch008 -p0
%patch009 -p0
%patch010 -p0
%patch011 -p0
%patch012 -p0
%patch013 -p0
%patch014 -p0
%patch015 -p0
%patch016 -p0
%patch017 -p0
%patch018 -p0
%patch019 -p0
%patch020 -p0
%patch021 -p0
# Win32 %patch022 -p0
%patch023 -p0
%patch024 -p0
# Win32 %patch025 -p0
%patch26 -p0
# VMS %patch27 -p0
%patch28 -p0
%patch29 -p0
%patch30 -p0
%patch31 -p0
%patch32 -p0
%patch33 -p0
%patch34 -p0
#%patch35 -p0
%patch36 -p0
%patch37 -p0
# Win32
#%patch38 -p0
%patch39 -p0
%patch40 -p0
# Win32
#%patch41 -p0
%patch42 -p0
%patch043 -p0
# Win32
#%patch044 -p0
%patch045 -p0
%patch046 -p0
# Win XP
#%patch047 -p0
# VMS
#%patch048 -p0
%patch049 -p0
%patch050 -p0
%patch051 -p0
# Win 98
#%patch052 -p0
# Win 32
#%patch053 -p0
%patch054 -p0
%patch055 -p0
%patch056 -p0
%patch057 -p0
%patch058 -p0
%patch059 -p0
%patch060 -p0
%patch061 -p0
%patch062 -p0
%patch063 -p0
%patch064 -p0
%patch065 -p0
%patch066 -p0
%patch067 -p0
%patch068 -p0
%patch069 -p0
%patch070 -p0
%patch071 -p0


%patch3000 -p1
%patch3001 -p1
%patch3002 -p1
%patch3003 -p1
%patch3004 -p1
%patch3005 -p1
%patch3006 -p1
%patch3007 -p1

%if %{WITH_SELINUX}
%patch3100 -p1
%endif

%build
cd src
autoconf
perl -pi -e "s,\\\$VIMRUNTIME,/usr/share/vim/%{vimdir},g" os_unix.h
perl -pi -e "s,\\\$VIM,/usr/share/vim/%{vimdir}/macros,g" os_unix.h

export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_FORTIFY_SOURCE=2"
export CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_FORTIFY_SOURCE=2"
%if "%{withruby}" == "1"
export  RUBY_CFLAGS=-I$(ruby -r rbconfig -e 'p Config::CONFIG["archdir"]')
%endif

%if "%{withgui}" == "1"
%configure --with-features=huge --enable-pythoninterp --enable-perlinterp \
  --disable-tclinterp --with-x=yes --exec-prefix=/usr/X11R6 \
  --enable-xim --enable-multibyte \
  --enable-gtk2-check --enable-gui=gtk2 \
  --with-compiledby="<bugzilla@redhat.com>" --enable-cscope \
  --with-modified-by="<bugzilla@redhat.com>" \
%if "%{withnetbeans}" == "1"
  --enable-netbeans \
%else
  --disable-netbeans \
%endif
%if "%{withruby}" == "1"
  --enable-rubyinterp
%endif
%
make
cp vim gvim
make clean
%endif

%configure --prefix=/usr --with-features=huge --enable-pythoninterp \
 --enable-perlinterp --disable-tclinterp --with-x=no \
 --enable-gui=no --exec-prefix=/usr --enable-multibyte \
 --disable-netbeans --enable-cscope --with-modified-by="<bugzilla@redhat.com>" \
 --with-compiledby="<bugzilla@redhat.com>" \
%if "%{withnetbeans}" == "1"
  --enable-netbeans \
%else
  --disable-netbeans \
%endif
%if "%{withruby}" == "1"
  --enable-rubyinterp
%endif

make
cp vim enhanced-vim
make clean

%configure --prefix='${DEST}'/usr --with-features=tiny --with-x=no \
  --enable-multibyte \
  --disable-netbeans \
  --disable-pythoninterp --disable-perlinterp --disable-tclinterp \
  --with-tlib=termcap --enable-gui=no --disable-gpm --exec-prefix=/ --with-compiledby="<bugzilla@redhat.com>"

make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/bin
mkdir -p $RPM_BUILD_ROOT/usr/{bin,share/vim,X11R6/bin}
cp -f %{SOURCE5} .

cd src
%makeinstall BINDIR=/bin DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/bin/xxd $RPM_BUILD_ROOT/usr/bin
make installmacros DESTDIR=$RPM_BUILD_ROOT
%if "%{withgui}" == "1"
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{16x16,32x32,48x48,64x64}/apps
install -m755 gvim $RPM_BUILD_ROOT/usr/X11R6/bin
install -m644 %{SOURCE7} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/gvim.png
install -m644 %{SOURCE8} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/gvim.png
install -m644 %{SOURCE9} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/gvim.png
install -m644 %{SOURCE10} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/gvim.png
%endif
install -m755 enhanced-vim $RPM_BUILD_ROOT/usr/bin/vim

( cd $RPM_BUILD_ROOT
  mv ./bin/vimtutor ./usr/bin
  mv ./bin/vim ./bin/vi
  rm -f ./bin/rvim
  ln -sf vi ./bin/view
  ln -sf vi ./bin/ex
  ln -sf vi ./bin/rvi
  ln -sf vi ./bin/rview
  ln -sf vim ./usr/bin/ex
  ln -sf vim ./usr/bin/rvim
  ln -sf vim ./usr/bin/vimdiff
  perl -pi -e "s,$RPM_BUILD_ROOT,," .%{_mandir}/man1/vim.1 .%{_mandir}/man1/vimtutor.1
  rm -f .%{_mandir}/man1/rvim.1
  ln -sf vim.1.gz .%{_mandir}/man1/vi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/rvi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/rvim.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/vimdiff.1.gz
%if "%{withgui}" == "1"
  ln -sf gvim ./usr/X11R6/bin/gview
  ln -sf gvim ./usr/X11R6/bin/gex
  ln -sf gvim ./usr/X11R6/bin/evim
  ln -sf gvim ./usr/X11R6/bin/gvimdiff
  ln -sf vim.1.gz .%{_mandir}/man1/gvim.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/gvimdiff.1.gz
  ln -sf gvim ./usr/X11R6/bin/vimx
  %if "%{desktop_file}" == "1"
    mkdir -p $RPM_BUILD_ROOT/usr/share/applications
    desktop-file-install --vendor net \
        --dir $RPM_BUILD_ROOT/usr/share/applications \
        --add-category "Application;Development;X-Red-Hat-Base" \
        %{SOURCE3}
  %else
    mkdir -p ./etc/X11/applnk/Applications
    cp %{SOURCE3} ./etc/X11/applnk/Applications/gvim.desktop
  %endif
%else
  rm -f $RPM_BUILD_ROOT/%{_mandir}/man?/evim*
%endif
  # ja_JP.ujis is obsolete, ja_JP.eucJP is recommended.
  ( cd ./usr/share/vim/%{vimdir}/lang; \
    ln -sf menu_ja_jp.ujis.vim menu_ja_jp.eucjp.vim )
)

pushd $RPM_BUILD_ROOT/usr/share/vim/%{vimdir}/tutor
mkdir conv
   iconv -f CP1252 -t UTF8 tutor.ca > conv/tutor.ca
   iconv -f CP1252 -t UTF8 tutor.it > conv/tutor.it
   iconv -f CP1253 -t UTF8 tutor.gr > conv/tutor.gr
   iconv -f CP1252 -t UTF8 tutor.fr > conv/tutor.fr
   iconv -f CP1252 -t UTF8 tutor.es > conv/tutor.es
   iconv -f CP1252 -t UTF8 tutor.de > conv/tutor.de
   #iconv -f CP737 -t UTF8 tutor.gr.cp737 > conv/tutor.gr.cp737
   #iconv -f EUC-JP -t UTF8 tutor.ja.euc > conv/tutor.ja.euc
   #iconv -f SJIS -t UTF8 tutor.ja.sjis > conv/tutor.ja.sjis
   iconv -f UTF8 -t UTF8 tutor.ja.utf-8 > conv/tutor.ja.utf-8
   iconv -f UTF8 -t UTF8 tutor.ko.utf-8 > conv/tutor.ko.utf-8
   iconv -f CP1252 -t UTF8 tutor.no > conv/tutor.no
   iconv -f ISO-8859-2 -t UTF8 tutor.pl > conv/tutor.pl
   iconv -f ISO-8859-2 -t UTF8 tutor.sk > conv/tutor.sk
   iconv -f KOI8R -t UTF8 tutor.ru > conv/tutor.ru
   iconv -f CP1252 -t UTF8 tutor.sv > conv/tutor.sv
   mv -f tutor.gr.cp737 tutor.ja.euc tutor.ja.sjis tutor.ko.euc tutor.pl.cp1250 tutor.zh.big5 tutor.ru.cp1251 tutor.zh.euc conv/
   rm -f tutor.ca tutor.de tutor.es tutor.fr tutor.gr tutor.it tutor.ja.utf-8 tutor.ko.utf-8 tutor.no tutor.pl tutor.sk tutor.ru tutor.sv
mv -f conv/* .
rmdir conv
popd

# Dependency cleanups
chmod 644 $RPM_BUILD_ROOT/usr/share/vim/%{vimdir}/doc/vim2html.pl \
 $RPM_BUILD_ROOT/usr/share/vim/%{vimdir}/tools/*.pl \
 $RPM_BUILD_ROOT/usr/share/vim/%{vimdir}/tools/vim132
chmod 644 ../runtime/doc/vim2html.pl

mkdir -p $RPM_BUILD_ROOT/etc/profile.d
cat >$RPM_BUILD_ROOT/etc/profile.d/vim.sh <<EOF
if [ -n "\$BASH_VERSION" -o -n "\$KSH_VERSION" -o -n "\$ZSH_VERSION" ]; then
  [ -x /usr/bin/id ] || return
  [ \`/usr/bin/id -u\` -le 100 ] && return
  # for bash and zsh, only if no alias is already set
  alias vi >/dev/null 2>&1 || alias vi=vim
fi
EOF
cat >$RPM_BUILD_ROOT/etc/profile.d/vim.csh <<EOF
[ -x /usr/bin/id ] || exit
[ \`/usr/bin/id -u\` -le 100 ] && exit
alias vi vim
EOF
chmod 0755 $RPM_BUILD_ROOT/etc/profile.d/*
install -m644 %{SOURCE4} $RPM_BUILD_ROOT/etc/vimrc
(cd $RPM_BUILD_ROOT/usr/share/vim/%{vimdir}/doc;
 gzip -9 *.txt; gzip -d help.txt.gz
 cat tags | sed -e 's/\t\(.*.txt\)\t/\t\1.gz\t/;s/\thelp.txt.gz\t/\thelp.txt\t/' > tags.new; mv -f tags.new tags)
(cd ../runtime; rm -rf doc; ln -svf ../../vim/%{vimdir}/doc docs;
 mv -f  macros/README.txt ../README.macros;
 mv -f  tools/README.txt ../README.tools;
)

%post X11
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%postun X11
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(-,root,root)
%config(noreplace) /etc/vimrc
%doc README*
%doc runtime/docs
%doc $RPM_SOURCE_DIR/Changelog.rpm
/usr/share/vim
%lang(af) /usr/share/vim/%{vimdir}/lang/af/*
%lang(cs) /usr/share/vim/%{vimdir}/lang/cs/*
%lang(de) /usr/share/vim/%{vimdir}/lang/de/*
%lang(es) /usr/share/vim/%{vimdir}/lang/es/*
%lang(fr) /usr/share/vim/%{vimdir}/lang/fr/*
%lang(it) /usr/share/vim/%{vimdir}/lang/it/*
%lang(ja) /usr/share/vim/%{vimdir}/lang/ja/*
%lang(ko) /usr/share/vim/%{vimdir}/lang/ko/*
%lang(pl) /usr/share/vim/%{vimdir}/lang/pl/*
%lang(sk) /usr/share/vim/%{vimdir}/lang/sk/*
%lang(uk) /usr/share/vim/%{vimdir}/lang/uk/*
%lang(zh_CN) /usr/share/vim/%{vimdir}/lang/zh_CN/*
%lang(zh_CN.UTF-8) /usr/share/vim/%{vimdir}/lang/zh_CN.UTF-8/*
%lang(zh_TW) /usr/share/vim/%{vimdir}/lang/zh_TW/*
/usr/bin/xxd
%{_mandir}/man1/vim.*
%{_mandir}/man1/ex.*
%{_mandir}/man1/vi.*
%{_mandir}/man1/view.*
%{_mandir}/man1/rvi.*
%{_mandir}/man1/rview.*
%{_mandir}/man1/xxd.*

%files minimal
%defattr(-,root,root)
%config(noreplace) /etc/vimrc
/bin/ex
/bin/vi
/bin/view
/bin/rvi
/bin/rview

%files enhanced
%defattr(-,root,root)
/usr/bin/vim
/usr/bin/rvim
/usr/bin/vimdiff
/usr/bin/ex
/usr/bin/vimtutor
%config /etc/profile.d/vim.*
%{_mandir}/man1/rvim.*
%{_mandir}/man1/vimdiff.*
%{_mandir}/man1/vimtutor.*

%if "%{withgui}" == "1"
%files X11
%defattr(-,root,root)
%if "%{desktop_file}" == "1"
/usr/share/applications/*
%else
/etc/X11/applnk/*/gvim.desktop
%endif
/usr/X11R6/bin/gvim
/usr/X11R6/bin/gvimdiff
/usr/X11R6/bin/gview
/usr/X11R6/bin/gex
/usr/X11R6/bin/vimx
/usr/X11R6/bin/evim
%{_mandir}/man1/evim.*
%{_mandir}/man1/gvim*
%{_datadir}/icons/hicolor/*/apps/*
%endif

%changelog
* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com> - 1:6.3.071-3
- silence %%post

* Mon Apr 18 2005 Karsten Hopp <karsten@redhat.de> 6.3.071-2
- fix wrong Russian code page for vimtutor (#155181)

* Mon Apr 11 2005 Karsten Hopp <karsten@redhat.de> 6.3.071-1
- patchlevel 71, fixes crashes when converting text with illegal characters
  and when moving the vertical separator to the far left (vertically splitted 
  window)

* Mon Apr 11 2005 Karsten Hopp <karsten@redhat.de> 6.3.068-2
- quote special characters in here documents (vim.sh/vim.csh) (#154321)

* Thu Mar 31 2005 Karsten Hopp <karsten@redhat.de> 6.3-068
- pathlevel 68 (can't write when editing symbolic link to compressed file)
- remove -s parameter from install, this should fix debuginfo packages

* Mon Mar 28 2005 Christopher Aillon <caillon@redhat.com>
- rebuilt

* Fri Mar 25 2005 Christopher Aillon <caillon@redhat.com> 6.3.067-2
- Update the GTK+ theme icon cache on (un)install

* Wed Mar 23 2005 Karsten Hopp <karsten@redhat.de> 6.3.067-1
- Newly created files got execute permission (caused by patch 66)
  #151667

* Fri Mar 18 2005 Karsten Hopp <karsten@redhat.de> 6.3.066-1
- patchlevel 66

* Mon Mar 14 2005 Karsten Hopp <karsten@redhat.de> 6.3.064-1
- patchlevel 64
- fix selinux warning (#150126)

* Wed Mar 02 2005 Karsten Hopp <karsten@redhat.de> 6.3.062-1
- patchlevel 62, build with gcc-4

* Thu Feb 10 2005 Karsten Hopp <karsten@redhat.de> 6.3.061-3
- spec.vim fix from Andrew Overholt

* Mon Feb 07 2005 Karsten Hopp <karsten@redhat.de> 6.3.061-2 
- fix tmpfile patch (#147192)

* Mon Jan 31 2005 Karsten Hopp <karsten@redhat.de> 6.3.061-1 
- patchlevel 61

* Tue Jan 18 2005 Chip Turner <cturner@redhat.com> 1:058-2
- rebuild for new perl

* Tue Jan 18 2005 Karsten Hopp <karsten@redhat.de> 6.3.058-1
- Patchlevel 58
- rebuild with new perl
- remove all rpm backup files

* Wed Jan 12 2005 Karsten Hopp <karsten@redhat.de> 6.3.054-2
- remove backup files

* Wed Jan 12 2005 Karsten Hopp <karsten@redhat.de> 6.3.054-1
- patchlevel 54
- fix unsecure tempfile usage (#144698)

* Mon Dec 06 2004 Karsten Hopp <karsten@redhat.de> 6.3.042-1 
- patchlevel 42

* Thu Dec 02 2004 Karsten Hopp <karsten@redhat.de> 6.3.035-2 
- fix compressed docs handling (#141565)

* Wed Dec 01 2004 Karsten Hopp <karsten@redhat.de> 6.3.035-1 
- patchlevel 35
- allow remapping of 'g' (#140747)

* Fri Nov 19 2004 Karsten Hopp <karsten@redhat.de> 6.3.033-1 
- patchlevel 33

* Tue Nov 02 2004 Karsten Hopp <karsten@redhat.de> 6.3.030-3 
- fix selinux patch, so that HAVE_SELINUX will not be defined on 
  non-selinux systems (#137860)

* Tue Oct 19 2004 Karsten Hopp <karsten@redhat.de> 6.3.030-3 
- fix dependencies on vim-common (#132371)

* Mon Oct 11 2004 Karsten Hopp <karsten@redhat.de> 6.3.030-2 
- add cscope to vimrc so that cscope DB will be used 
  automatically when available

* Fri Oct 08 2004 Karsten Hopp <karsten@redhat.de> 6.3.030-2
- patchlevel 30

* Wed Oct 06 2004 Karsten Hopp <karsten@redhat.de> 6.3.029-2 
- fix perl requirement
- patchlevel 29 to fix crash when inserting a line break

* Wed Sep 29 2004 Karsten Hopp <karsten@redhat.de> 6.3.028-2 
- add patch from Ulrich Drepper to fix syntax highlighting of 
  DNS config files (#133746)

* Tue Sep 21 2004 Than Ngo <than@redhat.com> 6.3.028-1
- add patchlevel 27,28

* Tue Sep 14 2004 Karsten Hopp <karsten@redhat.de> 6.3.026-1
- patchlevel 26 (fixes an endless loop in syntax highlighting)

* Wed Sep 08 2004 Karsten Hopp <karsten@redhat.de> 6.3.025-2 
- clean up spec file
- disable fontset
- enable cscope

* Mon Sep 06 2004 Karsten Hopp <karsten@redhat.de> 6.3.025-1 
- patchlevel 25

* Wed Sep 01 2004 Karsten Hopp <karsten@redhat.de> 6.3.020-1
- patchlevel 20

* Sun Aug 29 2004 Karsten Hopp <karsten@redhat.de> 6.3.017-1 
- patchlevel 17

* Fri Aug 06 2004 Karsten Hopp <karsten@redhat.de> 6.3.015-1
- update to patchlevel 15
- move older rpm changelog entries to Changelog.rpm

* Mon Jul 26 2004 Warren Togami <wtogami@redhat.com> 6.3.014-2
- future proof vim-enhanced perl dep

* Thu Jul 22 2004 Karsten Hopp <karsten@redhat.de> 6.3.014-1
- patchlevel 14, fixes 'helplang' default settings
- fix escape sequence in /etc/vimrc (#128344)

* Fri Jul 16 2004 Karsten Hopp <karsten@redhat.de> 6.3.013-2
- use different encoding for tutor.pl (#125376)

* Tue Jul 13 2004 Karsten Hopp <karsten@redhat.de> 6.3.013-1
- patchlevel 13 to fix some crashes with multi-line patterns 
  and when using CTRL-R in command mode

* Thu Jul 8 2004 Dan Walsh <dwalsh@redhat.com> 6.3.011-4
- Fix selinux patch to handle symlinks

* Wed Jul 07 2004 Karsten Hopp <karsten@redhat.de> 6.3.011-3
- rebuild with new gcc

* Mon Jul 05 2004 Karsten Hopp <karsten@redhat.de> 6.3.011-2 
- convert tutorial files to UTF8 (#125376)

* Sat Jul 03 2004 Karsten Hopp <karsten@redhat.de> 6.3.011-1 
- patchlevel 11

* Thu Jun 17 2004 Karsten Hopp <karsten@redhat.de> 6.3.006-1 
- update to new major release
