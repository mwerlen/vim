Summary: The VIM editor.
Name: vim
Version: 5.8
%define vimversion vim58
Release: 4
License: freeware
Group: Applications/Editors
Source0: ftp://ftp.home.vim.org/pub/vim/unix/vim-%{version}-src.tar.bz2
Source1: ftp://ftp.home.vim.org/pub/vim/unix/vim-%{version}-rt.tar.bz2
Source2: ftp://ftp.home.vim.org/pub/vim/extra/vim-%{version}-extra.tar.bz2
Source3: vimrc
Source4: pfmain.vim
Patch0: vim-4.2-speed_t.patch
Patch1: vim-5.1-vimnotvi.patch
Patch2: vim-5.6a-paths.patch
Patch3: vim-5.6-fixkeys.patch
Patch4: vim-5.6-destdir.patch
Patch5: vim-5.7-redhat.patch
Patch6: vim-5.7-docpath.patch
Patch7: vim-5.7-crv.patch
Patch8: vim-5.8-mkstemp.patch
Patch9: vim-5.8-lilosyntax.patch
Patch102: ftp://ftp.vim.org/pub/vim/patches/5.8.002
Patch103: ftp://ftp.vim.org/pub/vim/patches/5.8.003
Patch104: ftp://ftp.vim.org/pub/vim/patches/5.8.004
Patch105: ftp://ftp.vim.org/pub/vim/patches/5.8.005

Buildroot: %{_tmppath}/vim-root
Buildrequires: python-devel, perl, gtk+-devel, libtermcap-devel
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

If you are installing any version of the VIM editor, you'll also need
to the vim-common package installed.

%package minimal
Summary: A minimal version of the VIM editor.
Group: Applications/Editors
Requires: vim-common
Obsoletes:  vim

%description minimal
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more. The
vim-minimal package includes a minimal version of VIM, which is
installed into /bin/vi for use when only the root partition is
present.

%package enhanced
Summary: A version of the VIM editor which includes recent enhancements.
Group: Applications/Editors
Requires: vim-common
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

%package X11
Summary: The VIM version of the vi editor for the X Window System.
Group: Applications/Editors
Requires: vim-common

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
%setup -q -b 1 -b 2
%patch1 -p1 -b .vim
# fix rogue dependencies from sample code
chmod -x runtime/tools/mve.awk
%patch2 -p1 -b .paths
find . -name \*.paths | xargs rm -f
%patch3 -p1 -b .fixkeys
%patch4 -p1 -b .destdir
%patch5 -p1 -b .redhat
%patch6 -p1 -b .docs
%patch7 -p1 -b .crv
%patch8 -p1 -b .mkstemp
%patch9 -p1 -b .lilo

%patch102 -p0 -b .pl2
%patch103 -p0 -b .pl3
%patch104 -p0 -b .pl4
%patch105 -p0 -b .pl5

perl -pi -e "s,bin/nawk,bin/awk,g" runtime/tools/mve.awk

%build
cd src
perl -pi -e "s,\\\$VIMRUNTIME,%{_datadir}/vim/%{vimversion},g" os_unix.h
perl -pi -e "s,\\\$VIM,%{_datadir}/vim/%{vimversion}/macros,g" os_unix.h
# Build gvim.
%configure --enable-max-features=yes --enable-pythoninterp --enable-perlinterp --disable-tclinterp --with-x=yes --enable-gui=gtk --exec-prefix=/usr/X11R6
make 
cp vim gvim
make clean

# Build vim.
%configure --prefix=%{_prefix} --enable-max-features=yes --enable-pythoninterp \
 --enable-perlinterp --disable-tclinterp --with-x=no --enable-gui=no \
 --exec-prefix=%{_prefix}
make
cp vim enhanced-vim
make clean

# Build "vi".
%configure --prefix=/ --enable-min-features=yes --with-x=no \
  --disable-pythoninterp --disable-perlinterp --disable-tclinterp \
  --with-tlib=termcap --enable-gui=no --disable-gpm --exec-prefix=/
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/bin
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_mandir},%{_datadir}/vim}
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin

cd src
%makeinstall BINDIR=$RPM_BUILD_ROOT/bin DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/bin/xxd $RPM_BUILD_ROOT%{_bindir}/
make installmacros DESTDIR=$RPM_BUILD_ROOT
install -m755 gvim $RPM_BUILD_ROOT/usr/X11R6/bin/
install -m755 enhanced-vim $RPM_BUILD_ROOT%{_bindir}/vim

( cd $RPM_BUILD_ROOT
  mv ./bin/vim ./bin/vi
  mv ./bin/vimtutor ./%{_bindir}
  rm -f ./bin/rvim
  ln -sf vi ./bin/view
  ln -sf vi ./bin/ex
  ln -sf vi ./bin/rvi
  ln -sf vi ./bin/rview
  ln -sf vim ./usr/bin/ex
  perl -pi -e "s,$RPM_BUILD_ROOT,," .%{_mandir}/man1/vim.1 .%{_mandir}/man1/vimtutor.1
  rm -f .%{_mandir}/man1/rvim.1
  ln -sf vim.1.gz .%{_mandir}/man1/vi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/rvi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/gvim.1.gz
  ln -sf gvim ./usr/X11R6/bin/vimx
  mkdir -p ./etc/X11/applnk/Utilities
  cat > ./etc/X11/applnk/Utilities/gvim.desktop <<EOF
[Desktop Entry]
Name=gvim
Type=Application
Comment=VI editor for X11
Exec=gvim
EOF
  install -s -m644 %{SOURCE3} ./%{_datadir}/vim/%{vimversion}/macros/
  ln -s vimrc ./%{_datadir}/vim/%{vimversion}/macros/gvimrc
)

# Dependency cleanups
chmod 644 $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimversion}/doc/vim2html.pl \
 $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimversion}/tools/*.pl \
 $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimversion}/tools/vim132
chmod 644 ../runtime/doc/vim2html.pl

cp %{SOURCE4} $RPM_BUILD_ROOT/%{_datadir}/vim/%{vimversion}/syntax/pfmain.vim

mkdir -p $RPM_BUILD_ROOT/etc/profile.d
cat >$RPM_BUILD_ROOT/etc/profile.d/vim.sh <<EOF
# Use vim-enhanced if possible
vi() { /usr/bin/vim \$@; }
export -f vi
EOF
cat >$RPM_BUILD_ROOT/etc/profile.d/vim.csh <<EOF
# Use vim-enhanced if possible
alias vi 'vim'
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(-,root,root)
%doc README*.txt runtime/macros/README.txt runtime/tools/README.txt
%doc runtime/doc runtime/syntax runtime/termcap runtime/tutor
%doc runtime/*.vim
%{_bindir}/vimtutor
%{_bindir}/xxd

%{_datadir}/vim
%{_mandir}/man1/vim.*
%{_mandir}/man1/vimtutor.*
%{_mandir}/man1/ex.*
%{_mandir}/man1/vi.*
%{_mandir}/man1/view.*
%{_mandir}/man1/rvi.*
%{_mandir}/man1/rview.*
%{_mandir}/man1/xxd.*

%files minimal
%defattr(-,root,root)
/bin/ex
/bin/vi
/bin/view
/bin/rvi
/bin/rview

%files enhanced
%defattr(-,root,root)
%{_bindir}/vim
%{_bindir}/ex
%config /etc/profile.d/*

%files X11
%defattr(-,root,root)
%config(missingok) /etc/X11/applnk/Utilities/gvim.desktop
/usr/X11R6/bin/gvim
/usr/X11R6/bin/vimx
%{_mandir}/man1/gvim.*

%changelog
* Mon Jul 02 2001 Karsten Hopp <karsten@redhat.de>
- fix vim.sh (vi filename doesn't work, vim filename does)

* Wed Jun 27 2001 Bernhard Rosenkraenzer <bero@redhat.com> 5.8-3
- Fix up lilo.conf syntax highlighting (as done earlier)
- Alias vi to vim in vim-enhanced (as done earlier), fix #44050 while at it
- bzip2 source (as done earlier)
- Add BuildRequires (as done earlier)
- Get rid of patches that worked around bugs in Red Hat Linux 4.x (as done
  earlier)
- Send people who downgrade other people's packages WITHOUT AT THE VERY
  LEAST backporting fixes/patches to hell!!!!! >:-((
- Add fixes from the maintainer, we're now at 5.8.005
- Add postfix config syntax highlighting (RFE #44778)

* Fri Jun 15 2001 Nalin Dahyabhai <nalin@redhat.com>
- Update from 5.7 to 5.8.

* Mon Jan 29 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Apply bugfix patch #24, fixes security bug #25194

* Wed Dec 20 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix mktemp() potential DoS (#22594, #22595)
- Apply bugfix patches #9 to #19

* Sun Aug  6 2000 Tim Waugh <twaugh@redhat.com>
- xterm doesn't have request version string (#14570)

* Sat Aug  5 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Patchlevel 8

* Fri Aug  4 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix paths in vim.1 manpage (Bug #15387)

* Wed Jul 19 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix up vimtutor (Bug #11455)

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

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
