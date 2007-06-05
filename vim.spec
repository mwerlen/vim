# used for CVS snapshots:
%define CVSDATE %{nil}
%define WITH_SELINUX 1
%define desktop_file 1
%if %{desktop_file}
%define desktop_file_utils_version 0.2.93
%endif

%define withnetbeans 0

%define withvimspell 0
%define withhunspell 0

%define baseversion 7.1
#used for pre-releases:
%define beta %{nil}
%define vimdir vim71%{?beta}
%define patchlevel 2

Summary: The VIM editor
URL:     http://www.vim.org/
Name: vim
Version: %{baseversion}.%{beta}%{patchlevel}
Release: 1%{?dist}
License: GPL
Group: Applications/Editors
Source0: ftp://ftp.vim.org/pub/vim/unix/vim-%{baseversion}%{?beta}%{?CVSDATE}.tar.bz2
Source1: ftp://ftp.vim.org/pub/vim/extra/vim-%{baseversion}%{?beta}-lang%{?CVSDATE}.tar.gz
Source2: ftp://ftp.vim.org/pub/vim/extra/vim-%{baseversion}%{?beta}-extra%{?CVSDATE}.tar.gz
Source3: gvim.desktop
Source4: vimrc
#Source5: ftp://ftp.vim.org/pub/vim/patches/README.patches
Source7: gvim16.png
Source8: gvim32.png
Source9: gvim48.png
Source10: gvim64.png
Source11: Changelog.rpm
#Source12: vi-help.txt
%if %{withvimspell}
Source13: vim-spell-files.tar.bz2
%endif

Patch2002: vim-7.0-fixkeys.patch
Patch2003: vim-6.2-specsyntax.patch
Patch2004: vim-7.0-crv.patch
Patch2010: xxd-locale.patch
%if %{withhunspell}
Patch2011: vim-7.0-hunspell.patch
BuildRequires: hunspell-devel
%endif
# Patches 001 < 999 are patches from the base maintainer.
# If you're as lazy as me, generate the list using
# for i in `seq 1 14`; do printf "Patch%03d: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.%03d\n" $i $i; done
Patch001: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.001
Patch002: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.002

Patch3000: vim-7.0-syntax.patch
Patch3002: vim-7.1-nowarnings.patch
Patch3003: vim-6.1-rh3.patch
Patch3004: vim-7.0-rclocation.patch
Patch3006: vim-6.4-checkhl.patch
Patch3007: vim-7.0-fstabsyntax.patch
Patch3008: vim-6.4-lib64.patch
Patch3009: vim-7.0-warning.patch
Patch3010: vim-7.0-syncolor.patch
Patch3011: vim-7.0-vimspelltypo.patch
Patch3012: vim-7.0-specedit.patch
#
Patch3100: vim-selinux.patch
Patch3101: vim-selinux2.patch

Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python-devel ncurses-devel gettext
BuildRequires: libacl-devel gpm-devel autoconf
%if %{WITH_SELINUX}
BuildRequires: libselinux-devel
%endif
%if %{desktop_file}
Requires: /usr/bin/desktop-file-install
BuildRequires: desktop-file-utils >= %{desktop_file_utils_version}
%endif
Epoch: 2

%description
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.

%package common
Summary: The common files needed by any version of the VIM editor
Group: Applications/Editors
Conflicts: man-pages-fr < 0.9.7-14
Conflicts: man-pages-it < 0.3.0-17
Conflicts: man-pages-pl < 0.24-2

%description common
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.  The
vim-common package contains files which every VIM binary will need in
order to run.

If you are installing vim-enhanced or vim-X11, you'll also need
to install the vim-common package.

%package spell
Summary: The dictionaries for spell checking. This package is optional
Group: Applications/Editors
Requires: vim-common = %{epoch}:%{version}-%{release}

%description spell
This subpackage contains dictionaries for vim spell checking in
many different languages.

%package minimal
Summary: A minimal version of the VIM editor
Group: Applications/Editors
Provides: vi = %{version}-%{release}

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
Summary: A version of the VIM editor which includes recent enhancements
Group: Applications/Editors
Requires: vim-common = %{epoch}:%{version}-%{release}
Provides: vim = %{version}-%{release}

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

%package X11
Summary: The VIM version of the vi editor for the X Window System
Group: Applications/Editors
Requires: vim-common = %{epoch}:%{version}-%{release} libattr >= 2.4 gtk2 >= 2.6
Provides: gvim = %{version}-%{release}
BuildRequires: gtk2-devel libSM-devel libXt-devel libXpm-devel

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

%prep
%setup -q -b 1 -n %{vimdir}
%{__tar} xzf %{SOURCE1}
%{__tar} xzf %{SOURCE2}
# fix rogue dependencies from sample code
chmod -x runtime/tools/mve.awk
%patch2002 -p1
%patch2003 -p1
%patch2004 -p1
%patch2010 -p1
%if %{withhunspell}
%patch2011 -p1
%endif
perl -pi -e "s,bin/nawk,bin/awk,g" runtime/tools/mve.awk

# Base patches...
# for i in `seq 1 14`; do printf "%%patch%03d -p0 \n" $i; done
%patch001 -p0
%patch002 -p0

# install spell files
%if %{withvimspell}
%{__tar} xjf %{SOURCE13}
%endif

%patch3000 -p1
%patch3002 -p1
%patch3003 -p1
%patch3004 -p1

%patch3006 -p1
%patch3007 -p1
%patch3008 -p1
%patch3009 -p1
%patch3010 -p1
%patch3011 -p1
%patch3012 -p1

%if %{WITH_SELINUX}
%patch3100 -p1
%patch3101 -p1
%endif


%build
cd src
autoconf

export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_FORTIFY_SOURCE=2"
export CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_FORTIFY_SOURCE=2"

%configure --with-features=huge --enable-pythoninterp --enable-perlinterp \
  --disable-tclinterp --with-x=yes \
  --enable-xim --enable-multibyte \
  --with-tlib=ncurses \
  --enable-gtk2-check --enable-gui=gtk2 \
  --with-compiledby="<bugzilla@redhat.com>" --enable-cscope \
  --with-modified-by="<bugzilla@redhat.com>" \
%if "%{withnetbeans}" == "1"
  --enable-netbeans \
%else
  --disable-netbeans \
%endif

make %{?_smp_mflags}
cp vim gvim
make clean

%configure --prefix=%{_prefix} --with-features=huge --enable-pythoninterp \
 --enable-perlinterp --disable-tclinterp --with-x=no \
 --enable-gui=no --exec-prefix=%{_prefix} --enable-multibyte \
 --enable-cscope --with-modified-by="<bugzilla@redhat.com>" \
 --with-tlib=ncurses \
 --with-compiledby="<bugzilla@redhat.com>" \
%if "%{withnetbeans}" == "1"
  --enable-netbeans \
%else
  --disable-netbeans \
%endif

make %{?_smp_mflags}
cp vim enhanced-vim
make clean

#perl -pi -e "s/help.txt/vi-help.txt/"  os_unix.h ex_cmds.c
perl -pi -e "s/\/etc\/vimrc/\/etc\/virc/"  os_unix.h
%configure --prefix=%{_prefix} --with-features=small --with-x=no \
  --enable-multibyte \
  --disable-netbeans \
  --disable-pythoninterp --disable-perlinterp --disable-tclinterp \
  --with-tlib=ncurses --enable-gui=no --disable-gpm --exec-prefix=/ \
  --with-compiledby="<bugzilla@redhat.com>" \
  --with-modified-by="<bugzilla@redhat.com>"

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/bin
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}/vimfiles/after
cp -f %{SOURCE11} .
cp runtime/doc/uganda.txt LICENSE


cd src
make install DESTDIR=$RPM_BUILD_ROOT BINDIR=/bin
mv $RPM_BUILD_ROOT/bin/xxd $RPM_BUILD_ROOT/%{_bindir}/xxd
make installmacros DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{16x16,32x32,48x48,64x64}/apps
install -m755 gvim $RPM_BUILD_ROOT/%{_bindir}/gvim
install -p -m644 %{SOURCE7} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/gvim.png
install -p -m644 %{SOURCE8} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/gvim.png
install -p -m644 %{SOURCE9} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/gvim.png
install -p -m644 %{SOURCE10} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/gvim.png
install -m755 enhanced-vim $RPM_BUILD_ROOT/%{_bindir}/vim

( cd $RPM_BUILD_ROOT
  mv ./bin/vimtutor ./%{_bindir}/vimtutor
  mv ./bin/vim ./bin/vi
  rm -f ./bin/rvim
  ln -sf vi ./bin/ex
  ln -sf vi ./bin/rvi
  ln -sf vi ./bin/rview
  ln -sf vi ./bin/view
  ln -sf vim ./%{_bindir}/ex
  ln -sf vim ./%{_bindir}/rvim
  ln -sf vim ./%{_bindir}/vimdiff
  perl -pi -e "s,$RPM_BUILD_ROOT,," .%{_mandir}/man1/vim.1 .%{_mandir}/man1/vimtutor.1
  rm -f .%{_mandir}/man1/rvim.1
  ln -sf vim.1.gz .%{_mandir}/man1/vi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/rvi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/rvim.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/vimdiff.1.gz
  ln -sf gvim ./%{_bindir}/gview
  ln -sf gvim ./%{_bindir}/gex
  ln -sf gvim ./%{_bindir}/evim
  ln -sf gvim ./%{_bindir}/gvimdiff
  ln -sf vim.1.gz .%{_mandir}/man1/gvim.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/gvimdiff.1.gz
  ln -sf gvim ./%{_bindir}/vimx
  %if "%{desktop_file}" == "1"
    mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
    desktop-file-install --vendor fedora \
        --dir $RPM_BUILD_ROOT/%{_datadir}/applications \
        --add-category "Application;Development;X-Red-Hat-Base" \
        %{SOURCE3}
  %else
    mkdir -p ./%{_sysconfdir}/X11/applnk/Applications
    cp %{SOURCE3} ./%{_sysconfdir}/X11/applnk/Applications/gvim.desktop
  %endif
  # ja_JP.ujis is obsolete, ja_JP.eucJP is recommended.
  ( cd ./%{_datadir}/%{name}/%{vimdir}/lang; \
    ln -sf menu_ja_jp.ujis.vim menu_ja_jp.eucjp.vim )
)

pushd $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/tutor
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
chmod 644 $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/doc/vim2html.pl \
 $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/tools/*.pl \
 $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/tools/vim132
chmod 644 ../runtime/doc/vim2html.pl

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d
cat >$RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/vim.sh <<EOF
if [ -n "\$BASH_VERSION" -o -n "\$KSH_VERSION" -o -n "\$ZSH_VERSION" ]; then
  [ -x /%{_bindir}/id ] || return
  [ \`/%{_bindir}/id -u\` -le 100 ] && return
  # for bash and zsh, only if no alias is already set
  alias vi >/dev/null 2>&1 || alias vi=vim
fi
EOF
cat >$RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/vim.csh <<EOF
[ -x /%{_bindir}/id ] || exit
[ \`/%{_bindir}/id -u\` -gt 100 ] && alias vi vim
EOF
chmod 0644 $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/*
install -p -m644 %{SOURCE4} $RPM_BUILD_ROOT/%{_sysconfdir}/vimrc
install -p -m644 %{SOURCE4} $RPM_BUILD_ROOT/%{_sysconfdir}/virc
(cd $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{vimdir}/doc;
 gzip -9 *.txt
 gzip -d help.txt.gz
 cat tags | sed -e 's/\t\(.*.txt\)\t/\t\1.gz\t/;s/\thelp.txt.gz\t/\thelp.txt\t/' > tags.new; mv -f tags.new tags
# cp %{SOURCE12} . 
 )
(cd ../runtime; rm -rf doc; ln -svf ../../vim/%{vimdir}/doc docs;) 
rm -f $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/macros/maze/maze*.c
rm -rf $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/tools
rm -rf $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/doc/vim2html.pl
rm -f $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimdir}/tutor/tutor.gr.utf-8~
( cd $RPM_BUILD_ROOT/%{_mandir}
  for i in `find ??/ -type f`; do
    bi=`basename $i`
    iconv -f latin1 -t UTF8 $i > $RPM_BUILD_ROOT/$bi
    mv -f $RPM_BUILD_ROOT/$bi $i
  done
)

%post X11
touch --no-create %{_datadir}/icons/hicolor
if [ -x /%{_bindir}/gtk-update-icon-cache ]; then
  gtk-update-icon-cache --ignore-theme-index -q %{_datadir}/icons/hicolor
fi
update-desktop-database &> /dev/null ||:

%postun X11
touch --no-create %{_datadir}/icons/hicolor
if [ -x /%{_bindir}/gtk-update-icon-cache ]; then
  gtk-update-icon-cache --ignore-theme-index -q %{_datadir}/icons/hicolor
fi
update-desktop-database &> /dev/null ||:

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/vimrc
%doc README* LICENSE
%doc runtime/docs
%doc Changelog.rpm
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{vimdir}
%dir %{_datadir}/%{name}/vimfiles
%dir %{_datadir}/%{name}/vimfiles/after
%{_datadir}/%{name}/%{vimdir}/autoload
%{_datadir}/%{name}/%{vimdir}/colors
%{_datadir}/%{name}/%{vimdir}/compiler
%{_datadir}/%{name}/%{vimdir}/doc
#exclude /%{_bindir}/vim/%{vimdir}/doc/vi-help.txt
%{_datadir}/%{name}/%{vimdir}/*.vim
%{_datadir}/%{name}/%{vimdir}/ftplugin
%{_datadir}/%{name}/%{vimdir}/indent
%{_datadir}/%{name}/%{vimdir}/keymap
%{_datadir}/%{name}/%{vimdir}/lang/*.vim
%{_datadir}/%{name}/%{vimdir}/lang/*.txt
%dir %{_datadir}/%{name}/%{vimdir}/lang
%{_datadir}/%{name}/%{vimdir}/macros
%{_datadir}/%{name}/%{vimdir}/plugin
%{_datadir}/%{name}/%{vimdir}/print
%{_datadir}/%{name}/%{vimdir}/syntax
%{_datadir}/%{name}/%{vimdir}/tutor
%if ! %{withvimspell}
%{_datadir}/%{name}/%{vimdir}/spell
%endif
%lang(af) %{_datadir}/%{name}/%{vimdir}/lang/af
%lang(ca) %{_datadir}/%{name}/%{vimdir}/lang/ca
%lang(cs) %{_datadir}/%{name}/%{vimdir}/lang/cs
%lang(de) %{_datadir}/%{name}/%{vimdir}/lang/de
%lang(en_GB) %{_datadir}/%{name}/%{vimdir}/lang/en_GB
%lang(es) %{_datadir}/%{name}/%{vimdir}/lang/es
%lang(fr) %{_datadir}/%{name}/%{vimdir}/lang/fr
%lang(ga) %{_datadir}/%{name}/%{vimdir}/lang/ga
%lang(it) %{_datadir}/%{name}/%{vimdir}/lang/it
%lang(ja) %{_datadir}/%{name}/%{vimdir}/lang/ja
%lang(ko) %{_datadir}/%{name}/%{vimdir}/lang/ko
%lang(no) %{_datadir}/%{name}/%{vimdir}/lang/no
%lang(pl) %{_datadir}/%{name}/%{vimdir}/lang/pl
%lang(ru) %{_datadir}/%{name}/%{vimdir}/lang/ru
%lang(sk) %{_datadir}/%{name}/%{vimdir}/lang/sk
%lang(sv) %{_datadir}/%{name}/%{vimdir}/lang/sv
%lang(uk) %{_datadir}/%{name}/%{vimdir}/lang/uk
%lang(vi) %{_datadir}/%{name}/%{vimdir}/lang/vi
%lang(zh_CN) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN
%lang(zh_TW) %{_datadir}/%{name}/%{vimdir}/lang/zh_TW
%lang(zh_CN.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/zh_CN.UTF-8
%lang(zh_TW.UTF-8) %{_datadir}/%{name}/%{vimdir}/lang/zh_TW.UTF-8
/%{_bindir}/xxd
%{_mandir}/man1/vim.*
%{_mandir}/man1/ex.*
%{_mandir}/man1/vi.*
%{_mandir}/man1/view.*
%{_mandir}/man1/rvi.*
%{_mandir}/man1/rview.*
%{_mandir}/man1/xxd.*
%lang(fr) %{_mandir}/fr*/*/*
%lang(it) %{_mandir}/it*/*/*
%lang(ru) %{_mandir}/ru*/*/*
%lang(pl) %{_mandir}/pl*/*/*

%if %{withvimspell}
%files spell
%defattr(-,root,root)
%dir %{_datadir}/%{name}/%{vimdir}/spell
%{_datadir}/%{name}/vim70/spell/cleanadd.vim
%lang(af) %{_datadir}/%{name}/%{vimdir}/spell/af.*
%lang(am) %{_datadir}/%{name}/%{vimdir}/spell/am.*
%lang(bg) %{_datadir}/%{name}/%{vimdir}/spell/bg.*
%lang(ca) %{_datadir}/%{name}/%{vimdir}/spell/ca.*
%lang(cs) %{_datadir}/%{name}/%{vimdir}/spell/cs.*
%lang(cy) %{_datadir}/%{name}/%{vimdir}/spell/cy.*
%lang(da) %{_datadir}/%{name}/%{vimdir}/spell/da.*
%lang(de) %{_datadir}/%{name}/%{vimdir}/spell/de.*
%lang(el) %{_datadir}/%{name}/%{vimdir}/spell/el.*
%lang(en) %{_datadir}/%{name}/%{vimdir}/spell/en.*
%lang(eo) %{_datadir}/%{name}/%{vimdir}/spell/eo.*
%lang(es) %{_datadir}/%{name}/%{vimdir}/spell/es.*
%lang(fo) %{_datadir}/%{name}/%{vimdir}/spell/fo.*
%lang(fr) %{_datadir}/%{name}/%{vimdir}/spell/fr.*
%lang(ga) %{_datadir}/%{name}/%{vimdir}/spell/ga.*
%lang(gd) %{_datadir}/%{name}/%{vimdir}/spell/gd.*
%lang(gl) %{_datadir}/%{name}/%{vimdir}/spell/gl.*
%lang(he) %{_datadir}/%{name}/%{vimdir}/spell/he.*
%lang(hr) %{_datadir}/%{name}/%{vimdir}/spell/hr.*
%lang(hu) %{_datadir}/%{name}/%{vimdir}/spell/hu.*
%lang(id) %{_datadir}/%{name}/%{vimdir}/spell/id.*
%lang(it) %{_datadir}/%{name}/%{vimdir}/spell/it.*
%lang(ku) %{_datadir}/%{name}/%{vimdir}/spell/ku.*
%lang(la) %{_datadir}/%{name}/%{vimdir}/spell/la.*
%lang(lt) %{_datadir}/%{name}/%{vimdir}/spell/lt.*
%lang(lv) %{_datadir}/%{name}/%{vimdir}/spell/lv.*
%lang(mg) %{_datadir}/%{name}/%{vimdir}/spell/mg.*
%lang(mi) %{_datadir}/%{name}/%{vimdir}/spell/mi.*
%lang(ms) %{_datadir}/%{name}/%{vimdir}/spell/ms.*
%lang(nb) %{_datadir}/%{name}/%{vimdir}/spell/nb.*
%lang(nl) %{_datadir}/%{name}/%{vimdir}/spell/nl.*
%lang(nn) %{_datadir}/%{name}/%{vimdir}/spell/nn.*
%lang(ny) %{_datadir}/%{name}/%{vimdir}/spell/ny.*
%lang(pl) %{_datadir}/%{name}/%{vimdir}/spell/pl.*
%lang(pt) %{_datadir}/%{name}/%{vimdir}/spell/pt.*
%lang(ro) %{_datadir}/%{name}/%{vimdir}/spell/ro.*
%lang(ru) %{_datadir}/%{name}/%{vimdir}/spell/ru.*
%lang(rw) %{_datadir}/%{name}/%{vimdir}/spell/rw.*
%lang(sk) %{_datadir}/%{name}/%{vimdir}/spell/sk.*
%lang(sl) %{_datadir}/%{name}/%{vimdir}/spell/sl.*
%lang(sv) %{_datadir}/%{name}/%{vimdir}/spell/sv.*
%lang(sw) %{_datadir}/%{name}/%{vimdir}/spell/sw.*
%lang(tet) %{_datadir}/%{name}/%{vimdir}/spell/tet.*
%lang(th) %{_datadir}/%{name}/%{vimdir}/spell/th.*
%lang(tl) %{_datadir}/%{name}/%{vimdir}/spell/tl.*
%lang(tn) %{_datadir}/%{name}/%{vimdir}/spell/tn.*
%lang(uk) %{_datadir}/%{name}/%{vimdir}/spell/uk.*
%lang(yi) %{_datadir}/%{name}/%{vimdir}/spell/yi.*
%lang(yi-tr) %{_datadir}/%{name}/%{vimdir}/spell/yi-tr.*
%lang(zu) %{_datadir}/%{name}/%{vimdir}/spell/zu.*
%endif

%files minimal
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/virc
/bin/ex
/bin/vi
/bin/view
/bin/rvi
/bin/rview
#%{_datadir}/%{name}/%{vimdir}/doc/vi-help.txt

%files enhanced
%defattr(-,root,root)
%{_bindir}/vim
%{_bindir}/rvim
%{_bindir}/vimdiff
%{_bindir}/ex
%{_bindir}/vimtutor
%config(noreplace) %{_sysconfdir}/profile.d/vim.*
%{_mandir}/man1/rvim.*
%{_mandir}/man1/vimdiff.*
%{_mandir}/man1/vimtutor.*

%files X11
%defattr(-,root,root)
%if "%{desktop_file}" == "1"
/%{_datadir}/applications/*
%else
/%{_sysconfdir}/X11/applnk/*/gvim.desktop
%endif
%{_bindir}/gvim
%{_bindir}/gvimdiff
%{_bindir}/gview
%{_bindir}/gex
%{_bindir}/vimx
%{_bindir}/evim
%{_mandir}/man1/evim.*
%{_mandir}/man1/gvim*
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Mon Jun 04 2007 Karsten Hopp <karsten@redhat.com> 7.1.%{nil}2-1
- vim 7.1
- drop 240 patches

* Tue May 22 2007 Karsten Hopp <karsten@redhat.com> 7.0.235-1
- Don't wake up system with blinking gvim cursor:
  http://www.linuxpowertop.org/known.php

* Mon Apr 30 2007 Karsten Hopp <karsten@redhat.com> 7.0.235-1
- update to patchlevel 235, fixes modeline issues 

* Tue Apr 17 2007 Karsten Hopp <karsten@redhat.com> 7.0.224-3
- fix typo in require line (vim-X11 - 2:7.0.224-2.fc7.i386 requires 4)

* Mon Apr 16 2007 Karsten Hopp <karsten@redhat.com> 7.0.224-2
- use more macros
- drop BR perl
- move license to main doc directory
- set vendor to 'fedora' (desktop-file)
- don't own man directories
- preserve timestamps of non-generated files
- run update-desktop-database

* Thu Apr 05 2007 Karsten Hopp <karsten@redhat.com> 7.0.224-1
- vim-X11 provides gvim

* Fri Mar 30 2007 Karsten Hopp <karsten@redhat.com> 7.0.224-1
- patchlevel 224

* Wed Feb 21 2007 Karsten Hopp <karsten@redhat.com> 7.0.195-2
- rpmlint fixes (#226526)

* Tue Feb 13 2007 Karsten Hopp <karsten@redhat.com> 7.0.195-1
- patchlevel 195

* Mon Feb 12 2007 Karsten Hopp <karsten@redhat.com> 7.0.192-1
- patchlevel 192
- test fix for highlighting problems with curly brackets in #define (#203577)

* Tue Feb 06 2007 Karsten Hopp <karsten@redhat.com> 7.0.191-2
- uses ncurses instead of ncursesw

* Tue Feb 06 2007 Karsten Hopp <karsten@redhat.com> 7.0.191-1
- patchlevel 191
- clean up spec file for rpmlint
- drop cvim stuff

* Tue Jan 23 2007 Karsten Hopp <karsten@redhat.com> 7.0.188-3
- patchlevel 188

* Mon Jan 08 2007 Karsten Hopp <karsten@redhat.com> 7.0.178-3
- enable filetype plugin

* Thu Dec 14 2006 Karsten Hopp <karsten@redhat.com> 7.0.178-2
- build vim-minimal with features=small instead of tiny (#219605)

* Tue Dec 12 2006 Karsten Hopp <karsten@redhat.com> 7.0.178-1
- add vimfiles/after to list of owned directories

* Tue Dec 12 2006 Karsten Hopp <karsten@redhat.com> 7.0.178-1
- patchlevel 178
- use macros 
- Resolves: #219154
  add directory /usr/share/vim/vimfiles for plugins

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com>
- rebuild for python 2.5

* Wed Nov 22 2006 Karsten Hopp <karsten@redhat.com> 7.0.168-1
- patchlevel 168
- link with ncurses

* Tue Nov 21 2006 Karsten Hopp <karsten@redhat.com> 7.0.164-2
- patchlevel 164

* Mon Nov 13 2006 Karsten Hopp <karsten@redhat.com> 7.0.162-2
- fix lang problem in spec file mode
- use old g:packager variable when set

* Fri Nov 10 2006 Karsten Hopp <karsten@redhat.com> 7.0.162-1
- patchlevel 162

* Mon Nov 06 2006 Karsten Hopp <karsten@redhat.com> 7.0.158-1
- patchlevel 158

* Tue Oct 17 2006 Karsten Hopp <karsten@redhat.com> 7.0.139-1
- patchlevel 139
- provide vim, vi (#210950)

* Thu Sep 28 2006 Jeremy Katz <katzj@redhat.com> - 7.0.109-3
- disable vim-spell subpackage as it pushes us over CD boundaries

* Tue Sep 28 2006 Karsten Hopp <karsten@redhat.com> 7.0.109-2
- fix typo in vimspell.sh (#203178)

* Tue Sep 19 2006 Karsten Hopp <karsten@redhat.com> 7.0.109-1
- update to patchlevel 109 to fix some redraw problems
- fix invisible comments in diff mode (#204042)

* Tue Sep 12 2006 Karsten Hopp <karsten@redhat.com> 7.0.100-1
- Patchlevel 100
- replace runtime files with newer ones

* Mon Sep 11 2006 Karsten Hopp <karsten@redhat.de> 7.0.099-1
- Patchlevel 99

* Mon Sep 05 2006 Karsten Hopp <karsten@redhat.de> 7.0.086-1
- Patchlevel 86

* Mon Sep 04 2006 Karsten Hopp <karsten@redhat.de> 7.0.083-1
- Patchlevel 83

* Wed Aug 30 2006 Karsten Hopp <karsten@redhat.de> 7.0.076-1
- Patchlevel 76

* Thu Aug 25 2006 Karsten Hopp <karsten@redhat.de> 7.0.066-2
- fix vimdiff colors (#204042)

* Thu Aug 24 2006 Karsten Hopp <karsten@redhat.de> 7.0.066-1
- fix syntax patch (#203798)
- patchlevel 66

* Wed Aug 17 2006 Karsten Hopp <karsten@redhat.de> 7.0.063-1
- Patchlevel 63

* Wed Aug 15 2006 Karsten Hopp <karsten@redhat.de> 7.0.053-1
- Patchlevel 53
- Buildrequires libXpm-devel

* Wed Aug 09 2006 Karsten Hopp <karsten@redhat.de> 7.0.050-1
- Patchlevel 50

* Thu Aug 03 2006  Karsten Hopp <karsten@redhat.de> 7.0.042-2
- clean up spec file

* Mon Jul 24 2006 Karsten Hopp <karsten@redhat.de> 7.0.042-1
- patchlevel 42

* Wed Jul 20 2006 Karsten Hopp <karsten@redhat.de> 7.0.039-1
- patchlevel 39
- allow usage of $VIM variable (#199465)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2:7.0.035-1.1
- rebuild

* Tue Jun 27 2006 Karsten Hopp <karsten@redhat.de> 7.0.035-1
- patchlevel 35

* Wed Jun 21 2006 Karsten Hopp <karsten@redhat.de> 7.0.022-2
- add binfmt_misc rpc_pipefs to fstypes for better mtab highlighting

* Tue Jun 20 2006 Karsten Hopp <karsten@redhat.de> 7.0.022-1
- patchlevel 22

* Tue Jun 20 2006 Karsten Hopp <karsten@redhat.de> 7.0.020-1
- patchlevel 20

* Tue Jun 20 2006 Karsten Hopp <karsten@redhat.de> 7.0.019-1
- patchlevel 19
- buildrequire autoconf

* Tue May 30 2006 Karsten Hopp <karsten@redhat.de> 7.0.017-1
- patchlevel 17, although it affects just the Motif version
- own some directories (#192787)

* Sat May 13 2006 Karsten Hopp <karsten@redhat.de> 7.0.016-1
- patchlevel 016

* Fri May 12 2006 Karsten Hopp <karsten@redhat.de> 7.0.012-1
- patchlevel 012

* Thu May 11 2006 Karsten Hopp <karsten@redhat.de> 7.0.010-1
- patchlevel 010

* Wed May 10 2006 Karsten Hopp <karsten@redhat.de> 7.0.005-2
- patchlevel 005
- move older changelogs (<7.0) into a file, no need to keep them 
  in the rpm database

* Tue May 09 2006 Karsten Hopp <karsten@redhat.de> 7.0.000-2
- bump epoch, the buildsystem thinks 7.0.000-2 is older than 7.0.g001-1
  although rpm is quite happy with it.

* Mon May 08 2006 Karsten Hopp <karsten@redhat.de> 7.0.000-1
- vim-7.0 
- Spell checking support for about 50 languages
- Intelligent completion for C, HTML, Ruby, Python, PHP, etc.
- Tab pages, each containing multiple windows
- Undo branches: never accidentally lose text again
- Vim script supports Lists and Dictionaries (similar to Python)
- Vim script profiling
- Improved Unicode support
- Highlighting of cursor line, cursor column and matching braces
- Translated manual pages support.
- Internal grep; works on all platforms, searches compressed files
- Browsing remote directories, zip and tar archives
- Printing multi-byte text
- find details about the changes since vim-6.4 with :help version7

- fix SE Linux context of temporary (.swp) files (#189968)
- /bin/vi /vim-minimal is now using /etc/virc to avoid .rpmnew files
  when updating

* Tue May 02 2006 Karsten Hopp <karsten@redhat.de> 7.0.g001-1
- vim-7.0g BETA

* Fri Apr 28 2006 Karsten Hopp <karsten@redhat.de> 7.0.f001-1
- vim-7.0f3 BETA

* Thu Apr 20 2006 Karsten Hopp <karsten@redhat.de> 7.0.e001-1
- vim-7.0e BETA

* Tue Apr 11 2006 Karsten Hopp <karsten@redhat.de> 7.0.d001-1
- vim-7.0d BETA

* Fri Apr 07 2006 Karsten Hopp <karsten@redhat.de> 7.0c.000-3
- fix vimrc filename

* Thu Apr 06 2006 Karsten Hopp <karsten@redhat.de> 7.0c.000-2
- new snapshot

* Tue Apr 04 2006 Karsten Hopp <karsten@redhat.de> 7.0c.000-1
- vim-7.0c BETA

* Wed Mar 22 2006 Karsten Hopp <karsten@redhat.de> 7.0aa.000-3
- Rawhide build as vim, opposed to vim7 (prerelease)
- conflict with older man-pages-{it,fr} packages
- cleanup lang stuff

* Thu Mar 16 2006 Karsten Hopp <karsten@redhat.de> 7.0aa.000-2
- make it coexist with vim-6 (temporarily)
- new CVS snapshot

* Tue Mar 14 2006 Karsten Hopp <karsten@redhat.de> 7.0aa.000-1
- vim7 pre Release
- older changelogs available in Changelog.rpm

# vim:nrformats-=octal
