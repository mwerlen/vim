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
# don't build the gtk2 gui
%define withgtk2 0
# don't include ruby interpreter
%define withruby 0
%else
%define withgui 1
%define withgtk2 1
%define withruby 0
%endif


%define baseversion 6.3
%define vimdir vim63
%define patchlevel 013

Summary: The VIM editor.
Name: vim
Version: %{baseversion}.%{patchlevel}
Release: 1
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
Patch2000: vim-4.2-speed_t.patch
Patch2001: vim-5.6a-paths.patch
Patch2002: vim-6.0-fixkeys.patch
Patch2003: vim-6.2-specsyntax.patch
Patch2004: vim-6.0r-crv.patch
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

Patch3000: vim-6.1-syntax.patch
Patch3001: vim-6.2-rh1.patch
Patch3002: vim-6.1-rh2.patch
Patch3003: vim-6.1-rh3.patch
Patch3004: vim-6.2-rclocation.patch
Patch3005: vim-6.2-rh4.patch
Patch3006: vim-6.2-rh5.patch

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
Requires: vim-common 
Requires:  %(perl -le 'use Config;print $Config{archlibexp}')
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
Requires: vim-common libattr
%if "%{withgtk2}" == "1"
BuildRequires: gtk2-devel
%else
BuildRequires: gtk+-devel
%endif

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
%patch2000 -p1 -b .4.2
# fix rogue dependencies from sample code
chmod -x runtime/tools/mve.awk
%patch2001 -p1 -b .paths
find . -name \*.paths | xargs rm -f
%patch2002 -p1 -b .fixkeys
%patch2003 -p1 -b .highlite
%patch2004 -p1 -b .crv
%patch2010 -p1 -b .xxdloc
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

%patch3000 -p1 -b .syntx
%patch3001 -p1 -b .rh1
%patch3002 -p1 -b .rh2
%patch3003 -p1 -b .rh3
%patch3004 -p1 -b .rcloc
%patch3005 -p1 -b .rh4
%patch3006 -p1 -b .rh5

%if %{WITH_SELINUX}
%patch3100 -p1 -b .selinux
%endif

%build
cd src
autoconf
perl -pi -e "s,\\\$VIMRUNTIME,/usr/share/vim/%{vimdir},g" os_unix.h
perl -pi -e "s,\\\$VIM,/usr/share/vim/%{vimdir}/macros,g" os_unix.h

export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64"
export CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64"
%if "%{withruby}" == "1"
export  RUBY_CFLAGS=-I$(ruby -r rbconfig -e 'p Config::CONFIG["archdir"]')
%endif

%if "%{withgui}" == "1"
%configure --with-features=huge --enable-pythoninterp --enable-perlinterp \
  --disable-tclinterp --with-x=yes --exec-prefix=/usr/X11R6 \
  --enable-xim --enable-multibyte --enable-fontset \
  --disable-netbeans \
  --with-compiledby="<bugzilla@redhat.com>" \
%if "%{withruby}" == "1"
  --enable-rubyinterp \
%endif
%if "%{withgtk2}" == "1"
  --enable-gtk2-check --enable-gui=gtk2
%else
   --enable-gui=gtk
%endif
make
cp vim gvim
make clean
%endif

%configure --prefix=/usr --with-features=huge --enable-pythoninterp \
 --enable-perlinterp --disable-tclinterp --with-x=no \
 --enable-gui=no --exec-prefix=/usr --enable-multibyte --enable-fontset \
 --disable-netbeans \
 --with-compiledby="<bugzilla@redhat.com>" \
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
install -s -m755 gvim $RPM_BUILD_ROOT/usr/X11R6/bin
install -s -m644 %{SOURCE7} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/gvim.png
install -s -m644 %{SOURCE8} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/gvim.png
install -s -m644 %{SOURCE9} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/gvim.png
install -s -m644 %{SOURCE10} \
   $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/gvim.png
%endif
install -s -m755 enhanced-vim $RPM_BUILD_ROOT/usr/bin/vim

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
   iconv -f CP1250 -t UTF8 tutor.pl > conv/tutor.pl
   iconv -f CP1250 -t UTF8 tutor.sk > conv/tutor.sk
   iconv -f CP1251 -t UTF8 tutor.ru > conv/tutor.ru
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
  # for bash, pdksh and zsh, only if no alias is already set
  alias vi >/dev/null 2>&1 || alias vi=vim
fi
EOF
cat >$RPM_BUILD_ROOT/etc/profile.d/vim.csh <<EOF
alias vi vim
EOF
chmod 0755 $RPM_BUILD_ROOT/etc/profile.d/*
install -s -m644 %{SOURCE4} $RPM_BUILD_ROOT/etc/vimrc
(cd ../runtime; rm -rf doc; ln -svf ../../vim/%{vimdir}/doc docs;
 mv -f  macros/README.txt ../README.macros;
 mv -f  tools/README.txt ../README.tools;
)

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(-,root,root)
%config(noreplace) /etc/vimrc
%doc README*
%doc runtime/docs
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

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Jun 04 2004 Karsten Hopp <karsten@redhat.de> 6.2.532-4 
- enable build on ppc*

* Wed Jun 02 2004 Karsten Hopp <karsten@redhat.de> 6.2.532-3
- rebuild

* Wed Jun 02 2004 Karsten Hopp <karsten@redhat.de> 6.2.532-2
- rebuild

* Thu Jun 01 2004 Karsten Hopp <karsten@redhat.de> 6.2.532-1 
- patchlevel 532
- include vimrc in vim-minimal (#123205)
- add gvim icons (#110033)

* Wed Apr 07 2004 Karsten Hopp <karsten@redhat.de> 6.2.457-1 
- patchlevel 457

* Fri Mar 26 2004 Karsten Hopp <karsten@redhat.de> 6.2.403-1
- patchlevel 403

* Thu Mar 18 2004 Karsten Hopp <karsten@redhat.de> 6.2.380-1 
- patchlevel 380

* Mon Mar 08 2004 Karsten Hopp <karsten@redhat.de> 6.2.327-1 
- patchlevel 327

* Wed Mar 03 2004 Karsten Hopp <karsten@redhat.de> 6.2.311-1 
- patchlevel 311

* Mon Mar 01 2004 Karsten Hopp <karsten@redhat.de> 6.2.294-1 
- patchlevel 294

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 11 2004 Karsten Hopp <karsten@redhat.de> 6.2.253-1 
- patchlevel 253
- disable netbeans

* Thu Jan 29 2004 Karsten Hopp <karsten@redhat.de> 6.2.214-1 
- Patchlevel 214

* Mon Jan 26 2004 Dan Walsh <dwalsh@redhat.com> 1:6.2.195-5
- Fix call to is_selinux_enabled()

* Sat Jan 24 2004 Karsten Hopp <karsten@redhat.de> 6.2.195-4
- fix perl requirement

* Fri Jan 23 2004 Dan Walsh <dwalsh@redhat.com> 1:6.2.195-3
- Only attempt to change context if it is different

* Thu Jan 22 2004 Karsten Hopp <karsten@redhat.de> 6.2.195-1
- update to patchlevel 195
- enable ppc64 build

* Mon Jan 12 2004 Karsten Hopp <karsten@redhat.de> 6.2.180-2 
- vim-enhanced requires perl >= 5.8.2 (#111592)

* Mon Jan 12 2004 Karsten Hopp <karsten@redhat.de> 6.2.180-1 
- Patchlevel 180
- update spec.vim, use g:packager instead of {Packager} macro

* Tue Jan 6 2004 Dan Walsh <dwalsh@redhat.com> 1:6.2.154-7
- Enable selinux support for vim-minimal

* Wed Dec 17 2003 Dan Walsh <dwalsh@redhat.com> 1:6.2.154-6
- Enable selinux support

* Thu Dec 04 2003 Karsten Hopp <karsten@redhat.de> 1:6.2.154-5
- rebuild with new perl

* Wed Dec 03 2003 Karsten Hopp <karsten@redhat.de> 1:6.2.154-4
- fix sh.vim syntax file (#104312)

* Tue Dec 02 2003 Karsten Hopp <karsten@redhat.de> 1:6.2.154-3
- perl interface was disabled when perl had thread support.

* Thu Nov 27 2003 Karsten Hopp <karsten@redhat.de> 1:6.2.154-2
- fix date in specfile changelog entries

* Thu Nov 13 2003 Karsten Hopp <karsten@redhat.de> 1:6.2.154-1
- Patchlevel 154
- vim-minimal doesn't really require vim-common to run, removed dependency
  (#109819)

* Mon Nov 10 2003 Karsten Hopp <karsten@redhat.de> 1:6.2.149-1
- Patchlevel 149
- fix fstab syntax file (Robert G. (Doc) Savage)
- lots of updates for syntax files, macros, documentation
- disable vimnotvi patch so that vim's behaviour matches documentation
- clean up vimrc

* Thu Nov 06 2003 Karsten Hopp <karsten@redhat.de> 1:6.2.145-1
- rebuild with new Python
- Patchlevel 145

* Tue Oct 14 2003 Karsten Hopp <karsten@redhat.de> 1:6.2.121-1
- patchlevel 121
- fix buildrequires (#106824, #105832)

* Tue Sep 16 2003 Karsten Hopp <karsten@redhat.de> 1:6.2.98-1.1
- rebuilt

* Tue Sep 16 2003 Karsten Hopp <karsten@redhat.de> 1:6.2.98-1
- upstream fix for undeclared stop_insert_mode variable

* Tue Sep 16 2003 Karsten Hopp <karsten@redhat.de> 1:6.2.97-1
- patchlevel 97, see README for descriptions

* Mon Sep 01 2003 Karsten Hopp <karsten@redhat.de> 1:6.2.71-1
- several upstream fixes (PL 71)

* Tue Aug 05 2003 Karsten Hopp <karsten@redhat.de> 1:6.2.60-1.1
- rebuilt

* Mon Aug 04 2003 Karsten Hopp <karsten@redhat.de> 1:6.2.60-1
- update to fix cut&paste segfaults and UTF8 problems
- move vimrc to /etc (#2188)
- fix filelist

* Mon Aug 04 2003 Karsten Hopp <karsten@redhat.de> 1:6.2.57-2
- rebuilt

* Tue Jul 29 2003 Karsten Hopp <karsten@redhat.de> 1:6.2.57-1
-  update to patchlevel 57, this should take care of #100670

* Thu Jul 24 2003 Karsten Hopp <karsten@redhat.de> 6.2.21-1
- some minor upstream fixes (PL 21)

* Mon Jul 14 2003 Chip Turner <cturner@redhat.com>
- rebuild for new perl 5.8.1

* Fri Jul 04 2003 Karsten Hopp <karsten@redhat.de> 6.2.18-1
- update

* Wed Jun 10 2003 Karsten Hopp <karsten@redhat.de> 6.2.14-1
- update to 6.2

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun 03 2003 Karsten Hopp <karsten@redhat.de> 6.1.474-3
- rebuild

* Mon Jun 02 2003 Karsten Hopp <karsten@redhat.de> 6.1.474-2
- initialize variable before using it

* Tue May 06 2003 Karsten Hopp <karsten@redhat.de> 6.1.474-1
- patchlevel 474

* Wed Apr 23 2003 Karsten Hopp <karsten@redhat.de> 6.1.469-4
- add gvimdiff link (#89462)

* Sun Apr 20 2003 Karsten Hopp <karsten@redhat.de> 6.1.469-3
- rebuild with vim-X11 and gtk2
- don't hardcode ruby path (thanks to Ian Macdonald)

* Fri Apr 18 2003 Karsten Hopp <karsten@redhat.de> 6.1.469-2
- rebuild

* Thu Apr 17 2003 Karsten Hopp <karsten@redhat.de> 6.1.469-1
- enable ruby interpreter (#89045) and update to patchlevel 469

* Tue Apr 01 2003 Karsten Hopp <karsten@redhat.de> 6.1.434-1
- update to patchlevel 434
- update gtk2 patch and disable it for now

* Sun Mar 16 2003 Karsten Hopp <karsten@redhat.de> 1:6.1.406-1
- new versioning to match the official patchlevel
- new tarballs from the stable CVS tree to get rid of >300 patches
- add gtk2 patch fom gvim and build gtk2 gvim

* Wed Feb 12 2003 Karsten Hopp <karsten@redhat.de> 1:6.1-29
- clean up vimrc (fix #84088)
- clean up specfile so that it works with vim's specfile mode
- remove unused rescue stuff from specfile

* Mon Feb 10 2003 Karsten Hopp <karsten@redhat.de> 1.6.1-28
- patchlevel 320, to fix 'file changed' warning after :wq
- don't overwrite systemwide config file (#82037)

* Wed Jan 29 2003 Karsten Hopp <karsten@redhat.de> 6.1-27
- patchlevel 311
- fix #78837, only install message catalog for selected language

* Tue Jan 28 2003 Karsten Hopp <karsten@redhat.de> 6.1.26
- patchlevel 302
- added epoch to automated changelog entry (specs.vim)
- don't warn (vim-minimal) about not implemented functions

* Thu Jan 23 2003 Karsten Hopp <karsten@redhat.de> 6.1.25
- patchlevel 300

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jan 10 2003 Karsten Hopp <karsten@redhat.de> 6.1.23
- patchlevel 287

* Wed Jan 08 2003 Karsten Hopp <karsten@redhat.de> 6.1.22
- use Red Hat style for spec files

* Tue Jan 07 2003 Karsten Hopp <karsten@redhat.de> 6.1.21
- patchlevel 284

* Mon Dec 23 2002 Karsten Hopp <karsten@redhat.de> 6.1.20
- upstream patch for the modeline issue

* Sat Dec 21 2002 Karsten Hopp <karsten@redhat.de> 6.1-19
- disable libcall() and system() in modelines
- Patchlevel 264

* Tue Dec 17 2002 Karsten Hopp <karsten@redhat.de> 6.1-17
- Patchlevel 263
- gvim works again (#79355)
- don't backup all those patched files

* Tue Nov 12 2002 Karsten Hopp <karsten@redhat.de>
- added a lot of upstream patches + the README describing them
- fix alias for zsh (#77007)
- FIXME: gvim is currently broken

* Wed Oct 02 2002 Karsten Hopp <karsten@redhat.de>
- include the other httpd config files for syntax highlight

* Wed Oct 02 2002 Karsten Hopp <karsten@redhat.de>
- PL 206
- fix #74135

* Wed Aug 28 2002 Karsten Hopp <karsten@redhat.de>
- PL 165: 
 - when conversion to xxd fails 'filetype' was set anyway
 - undo information is corrupted when splitting a saved line
- add latin1 to fileencodings to fix 'conversion errors'

* Mon Aug 19 2002 Karsten Hopp <karsten@redhat.de>
- PL 159: expanding a multi-byte abbreviation deletes too much
- build /bin/vi with --enably-multibyte (#71282)

* Thu Aug 15 2002 Karsten Hopp <karsten@redhat.de>
- Patchlevel 153:
  translated menus are not used when lang contains "iso8859"
  searching in included files could loop recursively
- don't mark runtime files as %%doc or the files will be added to the package
  twice. (saves 2M)
- fix 'Installed (but unpackaged) file(s) found: .../gvim.desktop'
- work around rpm limitations, can't replace directories with
  symlinks

* Sun Aug 11 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- fix profile.d/vim.sh

* Thu Aug 08 2002 Karsten Hopp <karsten@redhat.de>
- Patchlevel 151

* Fri Jul 26 2002 Karsten Hopp <karsten@redhat.de>
- Patchlevel 141
- use desktop-file-utils (#69443)
- fix /etc/profile.d/vim.sh (#67264)

* Tue Jul 09 2002 Karsten Hopp <karsten@redhat.de> 6.1-8
- Update to patchlevel 125
- fix #59176, #65766, #59958, #55065, #62374, #62654, #63248
- reenable alpha

* Mon Jul  1 2002 Bernhard Rosenkraenzer <bero@redhat.com> 6.1-7
- Update to patchlevel 118
- Fix bug 64589

* Tue Jun 25 2002 Karsten Hopp <karsten@redhat.de> 6.1-6
- Update to patchlevel 112
- added a modified patch 49 for INVALCOLOR

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May  9 2002 Bernhard Rosenkraenzer <bero@redhat.com> 6.1-3
- Update to patchlevel 57
- Rebuild with current toolchain
- Temporarily exclude alpha, the build environment is broken
  (no db, no python 2.x)

* Wed Mar 27 2002 Bernhard Rosenkraenzer <bero@redhat.com> 6.1-2
- Rebuild with new perl

* Sun Mar 24 2002 Bernhard Rosenkraenzer <bero@redhat.com> 6.1-1
- Update to 6.1 (pure bugfix release)

* Mon Mar 11 2002 Bernhard Rosenkraenzer <bero@redhat.com> 6.0-14
- Patchlevel 270
- Move vimtutor to /usr/bin and vim-enhanced (#60772)

* Mon Jan 28 2002 Bernhard Rosenkraenzer <bero@redhat.com> 6.0-13
- Patchlevel 152
- Add symlinks for evim, rvim and vimdiff as described in vim docs

* Tue Jan 22 2002 Bernhard Rosenkraenzer <bero@redhat.com> 6.0-12
- Patchlevel 149

* Tue Jan 22 2002 Bernhard Rosenkraenzer <bero@redhat.com> 6.0-11
- Patchlevel 147

* Thu Dec 27 2001 Bernhard Rosenkraenzer <bero@redhat.com> 6.0-9
- Patchlevel 101

* Mon Nov 26 2001 Bernhard Rosenkraenzer <bero@redhat.com> 6.0-8
- Patchlevel 93

* Mon Nov  5 2001 Bernhard Rosenkraenzer <bero@redhat.com> 6.0-7
- 6.0pl78
- Move desktop file (Utilities -> Applications), #53503

* Thu Nov  1 2001 Bernhard Rosenkraenzer <bero@redhat.com> 6.0-6
- 6.0pl61

* Wed Oct 31 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 6.0pl44

* Mon Oct 29 2001 Bernhard Rosenkraenzer <bero@redhat.com> 6.0-5
- 6.0pl36
- Fix build with gcc 3.1

* Tue Oct 23 2001 Bernhard Rosenkraenzer <bero@redhat.com> 6.0-4
- 6.0pl21
- Don't show an error message when trying to "return" to a line
  that no longer exists (#54551)

* Mon Oct 22 2001 Bernhard Rosenkraenzer <bero@redhat.com> 6.0-3
- 6.0pl19

* Sun Sep 30 2001 Bernhard Rosenkraenzer <bero@redhat.com> 6.0-2
- 6.0pl11

* Wed Sep 26 2001 Bernhard Rosenkraenzer <bero@redhat.com> 6.0-1
- 6.0

* Thu Sep 13 2001 Bernhard Rosenkraenzer <bero@redhat.com> 6.0-0.av.1
- 6.0av
- Use -Os in rescue mode

* Tue Sep  4 2001 Bernhard Rosenkraenzer <bero@redhat.com> 6.0-0.au.1
- Update to 6.0au
- Allow rescue build

* Tue Aug 28 2001 Bernhard Rosenkraenzer <bero@redhat.com> 6.0-0.at.1
- vim 6.0at
- Increase epoch so we can update 7.2 systems

* Fri Jun  1 2001 Bernhard Rosenkraenzer <bero@redhat.com> 6.0-0.33
- 6.0ah
- Add a bash alias for vi=vim to the vim-enhanced package, too many people
  have complained about "missing features in vi even though I installed
  vim-enhanced".

* Mon May 21 2001 Bernhard Rosenkraenzer <bero@redhat.com> 6.0-0.32
- 6.0ag
- Make xxd locale aware (#37073)

* Mon May 14 2001 Bernhard Rosenkraenzer <bero@redhat.com> 6.0-0.31
- 6.0af

* Mon May  7 2001 Bernhard Rosenkraenzer <bero@redhat.com> 6.0-0.30
- 6.0ae

* Mon Apr 30 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 6.0ad
- XML .xsd files are still xml files - use the right syntax
  highlighting (RFE#38224)

* Sun Apr 15 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 6.0aa

* Fri Mar 30 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix large file handling (#34061)

* Mon Feb 26 2001 Trond Eivind Glomsrød <teg@redhat.com>
- use %%{_tmppath}

* Thu Feb 15 2001 Yukihiro Nakai <ynakai@redhat.com>
- vimrc update for 6.0v

* Mon Feb 12 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix "lba32" keyword in lilo.conf syntax highlighting
- Fix build with current glibc

* Fri Feb  2 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix crontab -e in vim-minimal (#25376)

* Tue Jan 30 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix segfault on q, up, up, q (Bug #25261)

* Mon Jan 22 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Set minlines=500 as default in PHP syntax highlighting (RFE #24374)
- Don't symlink gvimrc to vimrc (Bug #22518)
- Add symlinks gview -> gvim and gex -> gvim in -X11 (RFE #24394)
- 6.0t

* Mon Jan 15 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- More fixes to rpm specfile syntax highlighting:
  - recognize %%ifnarch
  - recognize "j" as a tar option
  - recognize %{_libdir}

* Sun Jan 14 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 6.0s

* Wed Jan  3 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 6.0r
- Restore crv patch (this should fix #23135 for whoever is seeing it;
  I'm not).

* Tue Dec 19 2000 Yukihiro Nakai <ynakai@redhat.com>
- Symbolic link to menu_ja_jp.ujis.vim to menu_ja_jp.eucjp.vim

* Mon Dec 18 2000 Yukihiro Nakai <ynakai@redhat.com>
- Delete i18n patch (already implmented by author)
- Add menu i18n patch
- Update vimrc to support CJK
- Add menu translations.

* Sun Dec 17 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 6.0q

* Sun Dec 17 2000 Yukihiro Nakai <ynakai@redhat.com>
- Add --enable-fontset to configure options.
- Add i18nrc patch and resources.

* Tue Dec 12 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 6.0p, new ncurses

* Mon Dec 11 2000 Karsten Hopp <karsten@redhat.de>
- rebuilt to fix permissions of /usr/share/doc/ and
  /usr/share/vim

* Mon Nov 13 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 6.0m

* Thu Nov  9 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 6.0l

* Mon Oct 30 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 6.0k

* Tue Oct 17 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 6.0i
- add new desktop file w/ translations

* Thu Aug 31 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 6.0h

* Wed Aug 30 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 6.0g

* Mon Aug 14 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 6.0f

* Wed Aug  9 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 6.0e

* Sun Jul 23 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 6.0c
- get rid of the DESTDIR patch, no longer needed

* Sun Jul 16 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 6.0b

* Mon Jul 10 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 6.0a

* Sun Jun 25 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 5.7 release
- some more fixes to .spec file syntax highlighting rules... About time it
  recognizes %%{_mandir}...

* Sun Jun 18 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 5.7a

* Sat Jun  3 2000 Bernhard Rosenkränzer <bero@redhat.com>
- patchlevel 74
- add %%makeinstall macro recognition to .spec file syntax highlighting rules
- fix up Makefiles

* Fri Apr 14 2000 Bernhard Rosenkränzer <bero@redhat.com>
- patchlevel 66
- fix compilation with perl 5.6.0

* Mon Mar 20 2000 Bernhard Rosenkränzer <bero@redhat.com>
- patchlevel 12

* Tue Mar 07 2000 Preston Brown <pbrown@redhat.com>
- fix home/end in vimrc (we did a term = rxvt, totally wrong)

* Tue Feb 29 2000 Preston Brown <pbrown@redhat.com>
- change F1-F4 keybindings for xterm builtin terminfo to match real terminfo

* Thu Feb 17 2000 Bill Nottingham <notting@redhat.com>
- kill autoindent

* Mon Feb 07 2000 Preston Brown <pbrown@redhat.com>
- wmconfig -> desktop

* Sat Feb  5 2000 Bernhard Rosenkränzer <bero@redhat.com>
- Patchlevel 11
- handle compressed man pages
- fix man page symlinks

* Wed Feb  2 2000 Bill Nottingham <notting@redhat.com>
- eliminate dependencies on X in vim-enhanced, and ncurses/gpm
  in vim-minimal

* Fri Jan 28 2000 Bill Nottingham <notting@redhat.com>
- eliminate dependencies on csh and perl in vim-common

* Wed Jan 19 2000 Bernhard Rosenrkänzer <bero@redhat.com>
- Use awk, not nawk

* Tue Jan 18 2000 Bernhard Rosenrkänzer <bero@redhat.com>
- 5.6
- patch 5.6.001
- remove /usr/bin/vi - if you want vim, type vim

* Tue Jan 11 2000 Bernhard Rosenkränzer <bero@redhat.com>
- 5.6a
- Remove dependency on nawk (introduced by base update)
- some tweaks to make updating easier

* Tue Nov  9 1999 Bernhard Rosenkränzer <bero@redhat.com>
- 5.5
- fix path to vimrc

* Tue Jul 27 1999 Michael K. Johnson <johnsonm@redhat.com>
- moved from athena to gtk widgets for X version
- removed vim.1 from X11 filelist because X11 depends on vim-common anyway
- fixed rogue dependencies from sample files

* Tue Jul 27 1999 Jeff Johnson <jbj@redhat.com>
- update to 5.4.

* Thu Jul 22 1999 Jeff Johnson <jbj@redhat.com>
- man page had buildroot pollution (#3629).

* Thu Mar 25 1999 Preston Brown <pbrown@redhat.com>
- with recent termcap/terminfo fixes, regular vim works in xterm/console
- in color, so vim-color package removed.

* Tue Mar 23 1999 Erik Troan <ewt@redhat.com>
- removed "set backupdir=/tmp/vim_backup" from default vimrc

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Thu Dec 17 1998 Michael Maher <mike@redaht.com>
- built pacakge for 6.0

* Tue Sep 15 1998 Michael Maher <mike@redhat.com>
- removed '--with-tlib=termcap' so that color-vim works

* Wed Sep  2 1998 Jeff Johnson <jbj@redhat.com>
- update to 5.3.

* Mon Aug 10 1998 Jeff Johnson <jbj@redhat.com>
- merge in Toshio's changes
- color-vim: changed "--disable-p" to "--disable-perlinterp --with-tlib=termcap"
- added minimal rvi/rview and man pages.
- move Obsoletes to same package as executable.

* Thu Aug 06 1998 Toshio Kuratomi <badger@prtr-13.ucsc.edu>
- Break the package apart similar to the way the netscape package was
  broken down to handle navigator or communicator: The vim package is
  Obsolete, now there is vim-common with all the common files, and a
  package for each binary: vim-minimal (has /bin/vi compiled with no
  frills), vim-enhanced (has /usr/bin/vim with extra perl and python
  interpreters), and vim-X11 (has /usr/X11R6/bin/gvim compiled with
  GUI support.)
- Enable the perl and python interpreters in the gui version (gvim).

* Tue Jun 30 1998 Michael Maher <mike@redhat.com>
- Fixed tutor help.
- cvim package added.  Thanks to Stevie Wills for finding this one :-)

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri May 01 1998 Donnie Barnes <djb@redhat.com>
- added patch to turn off the "vi compatibility" by default.  You can
  still get it via the -C command line option

* Thu Apr 23 1998 Donnie Barnes <djb@redhat.com>
- removed perl and python interpreters (sorry, but those don't belong
  in a /bin/vi and having two vi's seemed like overkill...complain
  to suggest@redhat.com if you care)

* Fri Apr 17 1998 Donnie Barnes <djb@redhat.com>
- fixed buildroot bug

* Sat Apr 11 1998 Donnie Barnes <djb@redhat.com>
- updated from 4.6 to 5.1
- moved to buildroot

* Sun Nov 09 1997 Donnie Barnes <djb@redhat.com>
- fixed missing man page

* Wed Oct 22 1997 Donnie Barnes <djb@redhat.com>
- added wmconfig entry to vim-X11

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- upgraded from 4.5 to 4.6

* Fri Jun 13 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Mar 25 1997 Michael K. Johnson <johnsonm@redhat.com>
- Upgraded to 4.5
- Added ex symlinks

* Tue Mar 11 1997 Michael K. Johnson <johnsonm@redhat.com>
- Added view symlink.
