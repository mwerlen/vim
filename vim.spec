%define rescue %{nil}
Summary: The VIM editor.
Name: vim
Version: 6.0
%define alpha %{nil}
%define vimversion vim60%{alpha}
%define rel 7.13
%if "%{alpha}" != ""
Release: 0.%{alpha}.%{rel}%{rescue}
%else
Release: %{rel}%{rescue}
%endif
License: freeware
Group: Applications/Editors
Source0: ftp://ftp.vim.org/pub/vim/unix/vim-%{version}%{alpha}.tar.bz2
Source1: ftp://ftp.vim.org/pub/vim/unreleased/extra/vim-%{version}%{alpha}-lang.tar.bz2
Source2: gvim.desktop
Source3: vimrc
Patch0: vim-4.2-speed_t.patch
Patch1: vim-5.1-vimnotvi.patch
Patch2: vim-5.6a-paths.patch
Patch3: vim-6.0-fixkeys.patch
Patch4: vim-6.0-specsyntax.patch
Patch5: vim-6.0r-crv.patch
Patch7: vim-6.0t-phphighlight.patch
Patch8: vim-6.0at-lilo.patch
Patch9: vim-6.0ad-xsd.patch
Patch10: xxd-locale.patch
Patch11: vim-6.0-gcc31.patch
Patch100: 6.0.001
Patch101: 6.0.002
Patch102: 6.0.003
Patch103: 6.0.004
Patch104: 6.0.005
Patch105: 6.0.006
Patch106: 6.0.007
Patch107: 6.0.008
Patch108: 6.0.009
Patch109: 6.0.010
Patch110: 6.0.011
Patch111: 6.0.012
Patch112: 6.0.013
Patch113: 6.0.014
Patch114: 6.0.015
Patch115: 6.0.016
Patch116: 6.0.017
Patch117: 6.0.018
Patch118: 6.0.019
Patch119: 6.0.020
Patch120: 6.0.021
Patch121: 6.0.022
Patch122: 6.0.023
Patch123: 6.0.024
Patch124: 6.0.025
Patch125: 6.0.026
Patch126: 6.0.027
Patch127: 6.0.028
Patch128: 6.0.029
Patch129: 6.0.030
Patch130: 6.0.031
Patch131: 6.0.032
Patch132: 6.0.033
Patch133: 6.0.034
Patch134: 6.0.035
Patch135: 6.0.036
Patch136: 6.0.037
Patch137: 6.0.038
Patch138: 6.0.039
Patch139: 6.0.040
Patch140: 6.0.041
Patch141: 6.0.042
Patch142: 6.0.043
Patch143: 6.0.044
Patch144: 6.0.045
Patch145: 6.0.046
Patch146: 6.0.047
Patch147: 6.0.048
Patch148: 6.0.049
Patch149: 6.0.050
Patch150: 6.0.051
Patch151: 6.0.052
Patch152: 6.0.053
Patch153: 6.0.054
Patch154: 6.0.055
Patch155: 6.0.056
Patch156: 6.0.057
Patch157: 6.0.058
Patch158: 6.0.059
Patch159: 6.0.060
Patch160: 6.0.061
Patch161: 6.0.062
Patch162: 6.0.063
Patch163: 6.0.064
Patch164: 6.0.065
Patch165: 6.0.066
Patch166: 6.0.067
Patch167: 6.0.068
Patch168: 6.0.069
# Patch 6.0.070 fixed to apply on non-Windoze
Patch169: 6.0.070.bero
Patch170: 6.0.071
Patch171: 6.0.072
Patch172: 6.0.073
Patch173: 6.0.074
Patch174: 6.0.075
Patch175: 6.0.076
Patch176: 6.0.077
Patch177: 6.0.078
Patch178: 6.0.079
Patch179: 6.0.080
Patch180: 6.0.081
Patch181: 6.0.082
Patch182: 6.0.083
Patch183: 6.0.084
Patch184: 6.0.085
Patch185: 6.0.086
Patch186: 6.0.087
Patch187: 6.0.088
Patch188: 6.0.089
Patch189: 6.0.090
Patch190: 6.0.091
Patch191: 6.0.092
Patch192: 6.0.093
Patch193: 6.0.094
Patch194: 6.0.095
Patch195: 6.0.096
Patch196: 6.0.097
Patch197: 6.0.098
Patch198: 6.0.099
Patch199: 6.0.100
Patch200: 6.0.101
Patch201: 6.0.102
Patch202: 6.0.103
Patch203: 6.0.104
Patch204: 6.0.105
Patch207: 6.0.108
Patch208: 6.0.109
Patch209: 6.0.110
Patch210: 6.0.111
Patch211: 6.0.112
Patch212: 6.0.113
Patch213: 6.0.114
Patch217: 6.0.118
Patch219: 6.0.120
Patch223: 6.0.124
Patch225: 6.0.126
Patch226: 6.0.127
Patch227: 6.0.128
Patch228: 6.0.129
Patch229: 6.0.130
Patch230: 6.0.131
Patch231: 6.0.132
Patch232: 6.0.133
Patch233: 6.0.134
Patch234: 6.0.135.bero
Patch235: 6.0.136
Patch236: 6.0.137
Patch237: 6.0.138
Patch238: 6.0.139
Patch239: 6.0.140
Patch240: 6.0.141
Patch241: 6.0.142
Patch242: 6.0.143
Patch243: 6.0.144
Patch244: 6.0.145
Patch245: 6.0.146
Patch246: 6.0.147
Patch247: 6.0.148
Patch248: 6.0.149
Patch249: 6.0.150
Patch250: 6.0.151
Patch251: 6.0.152
Buildroot: %{_tmppath}/%{name}-%{version}-root
Buildrequires: python-devel perl gtk+-devel
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
%setup -q -n %{vimversion}
%patch0 -p1 -b .4.2
%patch1 -p1 -b .vim
# fix rogue dependencies from sample code
chmod -x runtime/tools/mve.awk
%patch2 -p1 -b .paths
find . -name \*.paths | xargs rm -f
%patch3 -p1 -b .fixkeys
%patch4 -p1 -b .highlite
%patch5 -p1 -b .crv
%patch7 -p1 -b .php
%patch8 -p1 -b .lilo
%patch9 -p1 -b .xsd
%patch10 -p1 -b .xxdloc
%patch11 -p1 -b .gcc31
%patch100 -p0 -b .pl1
%patch101 -p0 -b .pl2
%patch102 -p0 -b .pl3
%patch103 -p0 -b .pl4
%patch104 -p0 -b .pl5
%patch105 -p0 -b .pl6
%patch106 -p0 -b .pl7
%patch107 -p0 -b .pl8
%patch108 -p0 -b .pl9
%patch109 -p0 -b .pl10
%patch110 -p0 -b .pl11
# %patch111 -p0 -b .pl12
%patch112 -p0 -b .pl13
%patch113 -p0 -b .pl14
%patch114 -p0 -b .pl15
%patch115 -p0 -b .pl16
%patch116 -p0 -b .pl17
%patch117 -p0 -b .pl18
%patch118 -p0 -b .pl19
%patch119 -p0 -b .pl20
%patch120 -p0 -b .pl21
%patch121 -p0 -b .pl22
%patch122 -p0 -b .pl23
%patch123 -p0 -b .pl24
%patch124 -p0 -b .pl25
%patch125 -p0 -b .pl26
# %patch126 -p0 -b .pl27 VMS crap
%patch127 -p0 -b .pl28
%patch128 -p0 -b .pl29
%patch129 -p0 -b .pl30
%patch130 -p0 -b .pl31
%patch131 -p0 -b .pl32
%patch132 -p0 -b .pl33
%patch133 -p0 -b .pl34
%patch134 -p0 -b .pl35
%patch135 -p0 -b .pl36
%patch136 -p0 -b .pl37
%patch137 -p0 -b .pl38
%patch138 -p0 -b .pl39
%patch139 -p0 -b .pl40
%patch140 -p0 -b .pl41
%patch141 -p0 -b .pl42
%patch142 -p0 -b .pl43
%patch143 -p0 -b .pl44
%patch144 -p0 -b .pl45
%patch145 -p0 -b .pl46
%patch146 -p0 -b .pl47
# %patch147 -p0 -b .pl48 Windoze crap
%patch148 -p0 -b .pl49
%patch149 -p0 -b .pl50
%patch150 -p0 -b .pl51
%patch151 -p0 -b .pl52
# %patch152 -p0 -b .pl53 This is QNX only stuff
%patch153 -p0 -b .pl54
%patch154 -p0 -b .pl55
%patch155 -p0 -b .pl56
%patch156 -p0 -b .pl57
%patch157 -p0 -b .pl58
%patch158 -p0 -b .pl59
%patch159 -p0 -b .pl60
%patch160 -p0 -b .pl61
%patch161 -p0 -b .pl62
%patch162 -p0 -b .pl63
# %patch163 -p0 -b .pl64 Windoze only
%patch164 -p0 -b .pl65
%patch165 -p0 -b .pl66
%patch166 -p0 -b .pl67
%patch167 -p0 -b .pl68
%patch168 -p0 -b .pl69
%patch169 -p0 -b .pl70
%patch170 -p0 -b .pl71
%patch171 -p0 -b .pl72
# %patch172 -p0 -b .pl73 DOS only
%patch173 -p0 -b .pl74
%patch174 -p0 -b .pl75
%patch175 -p0 -b .pl76
%patch176 -p0 -b .pl77
%patch177 -p0 -b .pl78
%patch178 -p0 -b .pl79
%patch179 -p0 -b .pl80
%patch180 -p0 -b .pl81
%patch181 -p0 -b .pl82
%patch182 -p0 -b .pl83
%patch183 -p0 -b .pl84
%patch184 -p0 -b .pl85
%patch185 -p0 -b .pl86
# %patch186 -p0 -b .pl87 N/A
%patch187 -p0 -b .pl88
%patch188 -p0 -b .pl89
%patch189 -p0 -b .pl90
%patch190 -p0 -b .pl91
%patch191 -p0 -b .pl92
%patch192 -p0 -b .pl93
%patch193 -p0 -b .pl94
%patch194 -p0 -b .pl95
%patch195 -p0 -b .pl96
%patch196 -p0 -b .pl97
%patch197 -p0 -b .pl98
%patch198 -p0 -b .pl99
%patch199 -p0 -b .pl100
%patch200 -p0 -b .pl101
%patch201 -p0 -b .pl102
%patch202 -p0 -b .pl103
%patch203 -p0 -b .pl104
%patch204 -p0 -b .pl105
%patch207 -p0 -b .pl108
%patch208 -p0 -b .pl109
%patch209 -p0 -b .pl110
%patch210 -p0 -b .pl111
%patch211 -p0 -b .pl112
%patch212 -p0 -b .pl113
%patch213 -p0 -b .pl114
%patch217 -p0 -b .pl118
%patch219 -p0 -b .pl120
%patch223 -p0 -b .pl124
%patch225 -p0 -b .pl126
%patch226 -p0 -b .pl127
%patch227 -p0 -b .pl128
%patch228 -p0 -b .pl129
%patch229 -p0 -b .pl130
%patch230 -p0 -b .pl131
%patch231 -p0 -b .pl132
%patch232 -p0 -b .pl133
%patch233 -p0 -b .pl134
%patch234 -p0 -b .pl135
%patch235 -p0 -b .pl136
%patch236 -p0 -b .pl137
%patch237 -p0 -b .pl138
%patch238 -p0 -b .pl139
%patch239 -p0 -b .pl140
%patch240 -p0 -b .pl141
%patch241 -p0 -b .pl142
%patch242 -p0 -b .pl143
%patch243 -p0 -b .pl144
%patch244 -p0 -b .pl145
%patch245 -p0 -b .pl146
%patch246 -p0 -b .pl147
%patch247 -p0 -b .pl148
%patch248 -p0 -b .pl149
%patch249 -p0 -b .pl150
%patch250 -p0 -b .pl151
%patch251 -p0 -b .pl152

perl -pi -e "s,bin/nawk,bin/awk,g" runtime/tools/mve.awk

%build
%if "%{rescue}" == ""
cd src
perl -pi -e "s,\\\$VIMRUNTIME,/usr/share/vim/%{vimversion},g" os_unix.h
perl -pi -e "s,\\\$VIM,/usr/share/vim/%{vimversion}/macros,g" os_unix.h

export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64"
export CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64"

%configure --with-features=huge --enable-pythoninterp --enable-perlinterp --disable-tclinterp --with-x=yes --enable-gui=gnome --exec-prefix=/usr/X11R6 --enable-xim --enable-multibyte --enable-fontset
perl -pi -e "s,-I/usr/local/include,,g" auto/config.mk # FIXME: remove once perl is fixed
make 
cp vim gvim
make clean

%configure --prefix=/usr --with-features=huge --enable-pythoninterp \
 --enable-perlinterp --disable-tclinterp --with-x=no --enable-gui=no \
 --exec-prefix=/usr --enable-multibyte --enable-fontset
perl -pi -e "s,-I/usr/local/include,,g" auto/config.mk # FIXME: remove once perl is fixed
make
cp vim enhanced-vim
make clean

%configure --prefix='${DEST}'/usr --with-features=tiny --with-x=no \
  --disable-pythoninterp --disable-perlinterp --disable-tclinterp \
  --with-tlib=termcap --enable-gui=no --disable-gpm --exec-prefix=/
perl -pi -e "s,-I/usr/local/include,,g" auto/config.mk # FIXME: remove once perl is fixed
make
%else
# Rescue disk version - somewhat more featureful than vim-minimal,
# but not quite a vim-enhanced
%configure --prefix='${DEST}'/usr --with-features=small --with-x=no \
  --disable-pythoninterp --disable-perlinterp --disable-tclinterp \
  --with-tlib=ncurses --enable-gui=no --disable-gpm --exec-prefix=/
perl -pi -e "s,-I/usr/local/include,,g" auto/config.mk # FIXME: remove once perl is fixed
perl -pi -e "s,-O2,-O2 -Os,g" auto/config.mk
make
%endif


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/bin
mkdir -p $RPM_BUILD_ROOT/usr/{bin,share/vim,X11R6/bin}

cd src
%makeinstall BINDIR=/bin DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/bin/xxd $RPM_BUILD_ROOT/usr/bin
make installmacros DESTDIR=$RPM_BUILD_ROOT
%if "%{rescue}" == ""
install -s -m755 gvim $RPM_BUILD_ROOT/usr/X11R6/bin
install -s -m755 enhanced-vim $RPM_BUILD_ROOT/usr/bin/vim
%endif

( cd $RPM_BUILD_ROOT
  mv ./bin/vim ./bin/vi
  rm -f ./bin/rvim
  ln -sf vi ./bin/view
  ln -sf vi ./bin/ex
  ln -sf vi ./bin/rvi
  ln -sf vi ./bin/rview
%if "%{rescue}" == ""
  ln -sf vim ./usr/bin/ex
  ln -sf vim ./usr/bin/rvim
  ln -sf vim ./usr/bin/vimdiff
  ln -sf gvim ./usr/X11R6/bin/gview
  ln -sf gvim ./usr/X11R6/bin/gex
  ln -sf gvim ./usr/X11R6/bin/evim
%else
  ln -sf vi ./bin/vim
  ln -sf vi ./usr/bin/ex
%endif
  perl -pi -e "s,$RPM_BUILD_ROOT,," .%{_mandir}/man1/vim.1 .%{_mandir}/man1/vimtutor.1
  rm -f .%{_mandir}/man1/rvim.1
  ln -sf vim.1.gz .%{_mandir}/man1/vi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/rvi.1.gz
%if "%{rescue}" == ""
  ln -sf vim.1.gz .%{_mandir}/man1/gvim.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/evim.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/rvim.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/vimdiff.1.gz
  ln -sf gvim ./usr/X11R6/bin/vimx
  mkdir -p ./etc/X11/applnk/Applications
  cp %{SOURCE2} ./etc/X11/applnk/Applications/gvim.desktop
%endif
  install -s -m644 %{SOURCE3} ./usr/share/vim/%{vimversion}/macros/
  # Extract trick to translated menus
  tar xjvf %{SOURCE1} '*/runtime/lang/*' -C ./
  ( cd %{vimversion}/runtime; tar cf - lang/* )| \
    ( cd ./usr/share/vim/%{vimversion}/ ; tar xvf - )
  # ja_JP.ujis is obsolete, ja_JP.eucJP is recommended.
  ( cd ./usr/share/vim/%{vimversion}/lang; \
    ln -sf menu_ja_jp.ujis.vim menu_ja_jp.eucjp.vim )
)

# Dependency cleanups
chmod 644 $RPM_BUILD_ROOT/usr/share/vim/%{vimversion}/doc/vim2html.pl \
 $RPM_BUILD_ROOT/usr/share/vim/%{vimversion}/tools/*.pl \
 $RPM_BUILD_ROOT/usr/share/vim/%{vimversion}/tools/vim132
chmod 644 ../runtime/doc/vim2html.pl

%if "%{rescue}" == ""
mkdir -p $RPM_BUILD_ROOT/etc/profile.d
cat >$RPM_BUILD_ROOT/etc/profile.d/vim.sh <<EOF
if echo \$SHELL |grep bash 2>&1 >/dev/null; then # aliases are bash only
	alias vi=vim
fi
EOF
cat >$RPM_BUILD_ROOT/etc/profile.d/vim.csh <<EOF
alias vi vim
EOF
chmod 0755 $RPM_BUILD_ROOT/etc/profile.d/*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if "%{rescue}" != ""
%files
%defattr(-,root,root)
%doc README*.txt runtime/macros/README.txt runtime/tools/README.txt
%doc runtime/doc runtime/syntax runtime/termcap runtime/tutor
%doc runtime/*.vim
/usr/bin/xxd
/usr/share/vim
%{_mandir}/man1/vim.*
%{_mandir}/man1/ex.*
%{_mandir}/man1/vi.*
%{_mandir}/man1/view.*
%{_mandir}/man1/rvi.*
%{_mandir}/man1/rview.*
%{_mandir}/man1/xxd.*
/bin/ex
/bin/vi
/bin/vim
/bin/view
/bin/rvi
/bin/rview
%else
%files common
%defattr(-,root,root)
%doc README*.txt runtime/macros/README.txt runtime/tools/README.txt
%doc runtime/doc runtime/syntax runtime/termcap runtime/tutor
%doc runtime/*.vim
/bin/vimtutor
/usr/bin/xxd

/usr/share/vim
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
/usr/bin/vim
/usr/bin/rvim
/usr/bin/vimdiff
/usr/bin/ex
%config /etc/profile.d/vim.*
%{_mandir}/man1/rvim.*
%{_mandir}/man1/vimdiff.*

%files X11
%defattr(-,root,root)
%config(missingok) /etc/X11/applnk/*/gvim.desktop
/usr/X11R6/bin/gvim
/usr/X11R6/bin/evim
/usr/X11R6/bin/gview
/usr/X11R6/bin/gex
/usr/X11R6/bin/vimx
%{_mandir}/man1/gvim.*
%{_mandir}/man1/evim.*
%endif

%changelog
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
