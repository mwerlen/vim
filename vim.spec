%define desktop_file 1
%if %{desktop_file}
%define desktop_file_utils_version 0.2.93
%endif
# Set this to 0 if you don't want to build gvim:
%define withgui 1

%define rescue %{nil}
Summary: The VIM editor.
Name: vim
Version: 6.1
%define alpha %{nil}
%define vimversion vim61%{alpha}
%define rel 14
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
Source4: hardlink.c
Patch0: vim-4.2-speed_t.patch
Patch1: vim-5.1-vimnotvi.patch
Patch2: vim-5.6a-paths.patch
Patch3: vim-6.0-fixkeys.patch
Patch4: vim-6.0-specsyntax.patch
Patch5: vim-6.0r-crv.patch
Patch10: xxd-locale.patch
Patch11: vim-6.0-gcc31.patch
# Patches 1000 and up are patches from the base maintainer.
# If you're as lazy as me, generate the list using
# (for i in `seq 1 57`; do echo "Patch`expr 1000 + $i`: ftp://ftp.vim.org/pub/vim/patches/6.1.`expr 1000 + $i | sed -e 's,^.,,'`"; done) >vimpatches
Patch1001: ftp://ftp.vim.org/pub/vim/patches/6.1.001
# Patch 2 is Windoze only
Patch1003: ftp://ftp.vim.org/pub/vim/patches/6.1.003
Patch1004: ftp://ftp.vim.org/pub/vim/patches/6.1.004
Patch1005: ftp://ftp.vim.org/pub/vim/patches/6.1.005
Patch1006: ftp://ftp.vim.org/pub/vim/patches/6.1.006
Patch1007: ftp://ftp.vim.org/pub/vim/patches/6.1.007
Patch1008: ftp://ftp.vim.org/pub/vim/patches/6.1.008
Patch1009: ftp://ftp.vim.org/pub/vim/patches/6.1.009
Patch1010: ftp://ftp.vim.org/pub/vim/patches/6.1.010
Patch1011: ftp://ftp.vim.org/pub/vim/patches/6.1.011
Patch1012: ftp://ftp.vim.org/pub/vim/patches/6.1.012
Patch1013: ftp://ftp.vim.org/pub/vim/patches/6.1.013
Patch1014: ftp://ftp.vim.org/pub/vim/patches/6.1.014
Patch1015: ftp://ftp.vim.org/pub/vim/patches/6.1.015
# Patch 16 is Windoze only
Patch1017: ftp://ftp.vim.org/pub/vim/patches/6.1.017
Patch1018: ftp://ftp.vim.org/pub/vim/patches/6.1.018
# Patch 19 is Windoze only
Patch1020: ftp://ftp.vim.org/pub/vim/patches/6.1.020
Patch1021: ftp://ftp.vim.org/pub/vim/patches/6.1.021
Patch1022: ftp://ftp.vim.org/pub/vim/patches/6.1.022
# Patch 23 is VMS only
Patch1024: ftp://ftp.vim.org/pub/vim/patches/6.1.024
Patch1025: ftp://ftp.vim.org/pub/vim/patches/6.1.025
Patch1026: ftp://ftp.vim.org/pub/vim/patches/6.1.026
Patch1027: ftp://ftp.vim.org/pub/vim/patches/6.1.027
Patch1028: ftp://ftp.vim.org/pub/vim/patches/6.1.028
Patch1029: ftp://ftp.vim.org/pub/vim/patches/6.1.029
Patch1030: ftp://ftp.vim.org/pub/vim/patches/6.1.030
Patch1031: ftp://ftp.vim.org/pub/vim/patches/6.1.031
Patch1032: ftp://ftp.vim.org/pub/vim/patches/6.1.032
Patch1033: ftp://ftp.vim.org/pub/vim/patches/6.1.033
Patch1034: ftp://ftp.vim.org/pub/vim/patches/6.1.034
# Patch 35 is Windoze only
Patch1036: ftp://ftp.vim.org/pub/vim/patches/6.1.036
Patch1037: ftp://ftp.vim.org/pub/vim/patches/6.1.037
Patch1038: ftp://ftp.vim.org/pub/vim/patches/6.1.038
Patch1039: ftp://ftp.vim.org/pub/vim/patches/6.1.039
Patch1040: ftp://ftp.vim.org/pub/vim/patches/6.1.040
Patch1041: ftp://ftp.vim.org/pub/vim/patches/6.1.041
Patch1042: ftp://ftp.vim.org/pub/vim/patches/6.1.042
Patch1043: ftp://ftp.vim.org/pub/vim/patches/6.1.043
# Patch 44 is Windoze only
Patch1045: ftp://ftp.vim.org/pub/vim/patches/6.1.045
Patch1046: ftp://ftp.vim.org/pub/vim/patches/6.1.046
Patch1047: ftp://ftp.vim.org/pub/vim/patches/6.1.047
Patch1048: ftp://ftp.vim.org/pub/vim/patches/6.1.048
Patch1049: ftp://ftp.vim.org/pub/vim/patches/6.1.049
# Patch 50 is just a fix for 49
Patch1051: ftp://ftp.vim.org/pub/vim/patches/6.1.051
Patch1052: ftp://ftp.vim.org/pub/vim/patches/6.1.052
Patch1053: ftp://ftp.vim.org/pub/vim/patches/6.1.053
Patch1054: ftp://ftp.vim.org/pub/vim/patches/6.1.054
Patch1055: ftp://ftp.vim.org/pub/vim/patches/6.1.055
Patch1056: ftp://ftp.vim.org/pub/vim/patches/6.1.056
Patch1057: ftp://ftp.vim.org/pub/vim/patches/6.1.057
Patch1058: ftp://ftp.vim.org/pub/vim/patches/6.1.058
Patch1059: ftp://ftp.vim.org/pub/vim/patches/6.1.059
Patch1060: ftp://ftp.vim.org/pub/vim/patches/6.1.060
Patch1061: ftp://ftp.vim.org/pub/vim/patches/6.1.061
Patch1062: ftp://ftp.vim.org/pub/vim/patches/6.1.062
Patch1063: ftp://ftp.vim.org/pub/vim/patches/6.1.063
Patch1064: ftp://ftp.vim.org/pub/vim/patches/6.1.064
Patch1065: ftp://ftp.vim.org/pub/vim/patches/6.1.065
Patch1066: ftp://ftp.vim.org/pub/vim/patches/6.1.066
Patch1067: ftp://ftp.vim.org/pub/vim/patches/6.1.067
Patch1068: ftp://ftp.vim.org/pub/vim/patches/6.1.068
Patch1069: ftp://ftp.vim.org/pub/vim/patches/6.1.069
Patch1070: ftp://ftp.vim.org/pub/vim/patches/6.1.070
Patch1071: ftp://ftp.vim.org/pub/vim/patches/6.1.071
Patch1072: ftp://ftp.vim.org/pub/vim/patches/6.1.072
# Patch 73 is just for PC5
Patch1074: ftp://ftp.vim.org/pub/vim/patches/6.1.074
Patch1075: ftp://ftp.vim.org/pub/vim/patches/6.1.075
# Patch 76 is just for Mac
Patch1077: ftp://ftp.vim.org/pub/vim/patches/6.1.077
Patch1078: ftp://ftp.vim.org/pub/vim/patches/6.1.078
Patch1079: ftp://ftp.vim.org/pub/vim/patches/6.1.079
Patch1080: ftp://ftp.vim.org/pub/vim/patches/6.1.080
Patch1081: ftp://ftp.vim.org/pub/vim/patches/6.1.081
Patch1082: ftp://ftp.vim.org/pub/vim/patches/6.1.082
Patch1083: ftp://ftp.vim.org/pub/vim/patches/6.1.083
# Patch 84 needs to be redone someday
Patch1084: ftp://ftp.vim.org/pub/vim/patches/6.1.084
Patch1085: ftp://ftp.vim.org/pub/vim/patches/6.1.085
Patch1086: ftp://ftp.vim.org/pub/vim/patches/6.1.086
Patch1087: ftp://ftp.vim.org/pub/vim/patches/6.1.087
# Patch 88 is Windoze only
Patch1089: ftp://ftp.vim.org/pub/vim/patches/6.1.089
Patch1090: ftp://ftp.vim.org/pub/vim/patches/6.1.090
Patch1091: ftp://ftp.vim.org/pub/vim/patches/6.1.091
Patch1092: ftp://ftp.vim.org/pub/vim/patches/6.1.092
# Patch 93 is Windoze  and Mac only
Patch1094: ftp://ftp.vim.org/pub/vim/patches/6.1.094
Patch1095: ftp://ftp.vim.org/pub/vim/patches/6.1.095
Patch1096: ftp://ftp.vim.org/pub/vim/patches/6.1.096
Patch1097: ftp://ftp.vim.org/pub/vim/patches/6.1.097
Patch1098: ftp://ftp.vim.org/pub/vim/patches/6.1.098
Patch1099: ftp://ftp.vim.org/pub/vim/patches/6.1.099
# Patch 100 is Windoze only
Patch1101: ftp://ftp.vim.org/pub/vim/patches/6.1.101
Patch1102: ftp://ftp.vim.org/pub/vim/patches/6.1.102
Patch1103: ftp://ftp.vim.org/pub/vim/patches/6.1.103
Patch1104: ftp://ftp.vim.org/pub/vim/patches/6.1.104
Patch1105: ftp://ftp.vim.org/pub/vim/patches/6.1.105
Patch1106: ftp://ftp.vim.org/pub/vim/patches/6.1.106
Patch1107: ftp://ftp.vim.org/pub/vim/patches/6.1.107
Patch1108: ftp://ftp.vim.org/pub/vim/patches/6.1.108
Patch1109: ftp://ftp.vim.org/pub/vim/patches/6.1.109
Patch1110: ftp://ftp.vim.org/pub/vim/patches/6.1.110
Patch1111: ftp://ftp.vim.org/pub/vim/patches/6.1.111
Patch1112: ftp://ftp.vim.org/pub/vim/patches/6.1.112
Patch1113: ftp://ftp.vim.org/pub/vim/patches/6.1.113
Patch1114: ftp://ftp.vim.org/pub/vim/patches/6.1.114
Patch1115: ftp://ftp.vim.org/pub/vim/patches/6.1.115
Patch1116: ftp://ftp.vim.org/pub/vim/patches/6.1.116
Patch1117: ftp://ftp.vim.org/pub/vim/patches/6.1.117
Patch1118: ftp://ftp.vim.org/pub/vim/patches/6.1.118
Patch1119: ftp://ftp.vim.org/pub/vim/patches/6.1.119
Patch1120: ftp://ftp.vim.org/pub/vim/patches/6.1.120
Patch1121: ftp://ftp.vim.org/pub/vim/patches/6.1.121
Patch1122: ftp://ftp.vim.org/pub/vim/patches/6.1.122
Patch1123: ftp://ftp.vim.org/pub/vim/patches/6.1.123
Patch1124: ftp://ftp.vim.org/pub/vim/patches/6.1.124
Patch1125: ftp://ftp.vim.org/pub/vim/patches/6.1.125
Patch1126: ftp://ftp.vim.org/pub/vim/patches/6.1.126
Patch1127: ftp://ftp.vim.org/pub/vim/patches/6.1.127
Patch1128: ftp://ftp.vim.org/pub/vim/patches/6.1.128
Patch1129: ftp://ftp.vim.org/pub/vim/patches/6.1.129
Patch1130: ftp://ftp.vim.org/pub/vim/patches/6.1.130
Patch1131: ftp://ftp.vim.org/pub/vim/patches/6.1.131
Patch1132: ftp://ftp.vim.org/pub/vim/patches/6.1.132
Patch1133: ftp://ftp.vim.org/pub/vim/patches/6.1.133
Patch1134: ftp://ftp.vim.org/pub/vim/patches/6.1.134
Patch1135: ftp://ftp.vim.org/pub/vim/patches/6.1.135
Patch1136: ftp://ftp.vim.org/pub/vim/patches/6.1.136
Patch1137: ftp://ftp.vim.org/pub/vim/patches/6.1.137
Patch1138: ftp://ftp.vim.org/pub/vim/patches/6.1.138
Patch1139: ftp://ftp.vim.org/pub/vim/patches/6.1.139
Patch1140: ftp://ftp.vim.org/pub/vim/patches/6.1.140
Patch1141: ftp://ftp.vim.org/pub/vim/patches/6.1.141
Patch1142: ftp://ftp.vim.org/pub/vim/patches/6.1.142
Patch1143: ftp://ftp.vim.org/pub/vim/patches/6.1.143
Patch1144: ftp://ftp.vim.org/pub/vim/patches/6.1.144
Patch1145: ftp://ftp.vim.org/pub/vim/patches/6.1.145
Patch1146: ftp://ftp.vim.org/pub/vim/patches/6.1.146
# 147-149 are windows only
Patch1150: ftp://ftp.vim.org/pub/vim/patches/6.1.150
# Modified patch to not include w32 parts:
Patch1151: ftp://ftp.vim.org/pub/vim/patches/6.1.151
Patch1152: ftp://ftp.vim.org/pub/vim/patches/6.1.152
Patch1153: ftp://ftp.vim.org/pub/vim/patches/6.1.153
# 154 is MSDOS only
Patch1157: ftp://ftp.vim.org/pub/vim/patches/6.1.157
Patch1158: ftp://ftp.vim.org/pub/vim/patches/6.1.158
Patch1159: ftp://ftp.vim.org/pub/vim/patches/6.1.159
Patch1160: ftp://ftp.vim.org/pub/vim/patches/6.1.160
Patch1161: ftp://ftp.vim.org/pub/vim/patches/6.1.161
Patch1162: ftp://ftp.vim.org/pub/vim/patches/6.1.162
Patch1163: ftp://ftp.vim.org/pub/vim/patches/6.1.163
Patch1164: ftp://ftp.vim.org/pub/vim/patches/6.1.164
Patch1165: ftp://ftp.vim.org/pub/vim/patches/6.1.165


Patch2000: vim-6.1-kh1.patch
Buildroot: %{_tmppath}/%{name}-%{version}-root
Buildrequires: python-devel perl
%if %{desktop_file}
Requires: /usr/bin/desktop-file-install
BuildPrereq: desktop-file-utils >= %{desktop_file_utils_version}
%endif
Epoch: 1
# FIXME: Remove this as soon as the alpha build environment is fixed
#Excludearch: alpha

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

%if "%{withgui}" == "1"
%package X11
Summary: The VIM version of the vi editor for the X Window System.
Group: Applications/Editors
Requires: vim-common
BuildRequires: gtk+-devel

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
%setup -q -b 1 -n %{vimversion}
%patch0 -p1 -b .4.2
%patch1 -p1 -b .vim
# fix rogue dependencies from sample code
chmod -x runtime/tools/mve.awk
%patch2 -p1 -b .paths
find . -name \*.paths | xargs rm -f
%patch3 -p1 -b .fixkeys
%patch4 -p1 -b .highlite
%patch5 -p1 -b .crv
%patch10 -p1 -b .xxdloc
%patch11 -p1 -b .gcc31
perl -pi -e "s,bin/nawk,bin/awk,g" runtime/tools/mve.awk

# Base patches...
%patch1001 -p0 -b .pl1
%patch1003 -p0 -b .pl3
%patch1004 -p0 -b .pl4
%patch1005 -p0 -b .pl5
%patch1006 -p0 -b .pl6
%patch1007 -p0 -b .pl7
%patch1008 -p0 -b .pl8
%patch1009 -p0 -b .pl9
%patch1010 -p0 -b .pl10
%patch1011 -p0 -b .pl11
%patch1012 -p0 -b .pl12
%patch1013 -p0 -b .pl13
%patch1014 -p0 -b .pl14
%patch1015 -p0 -b .pl15
%patch1017 -p0 -b .pl17
%patch1018 -p0 -b .pl18
%patch1020 -p0 -b .pl20
%patch1021 -p0 -b .pl21
%patch1022 -p0 -b .pl22
%patch1024 -p0 -b .pl24
%patch1025 -p0 -b .pl25
%patch1026 -p0 -b .pl26
%patch1027 -p0 -b .pl27
%patch1028 -p0 -b .pl28
%patch1029 -p0 -b .pl29
%patch1030 -p0 -b .pl30
%patch1031 -p0 -b .pl31
%patch1032 -p0 -b .pl32
%patch1033 -p0 -b .pl33
%patch1034 -p0 -b .pl34
%patch1036 -p0 -b .pl36
%patch1037 -p0 -b .pl37
%patch1038 -p0 -b .pl38
%patch1039 -p0 -b .pl39
%patch1040 -p0 -b .pl40
%patch1041 -p0 -b .pl41
%patch1042 -p0 -b .pl42
%patch1043 -p0 -b .pl43
%patch1045 -p0 -b .pl45
%patch1046 -p0 -b .pl46
%patch1047 -p0 -b .pl47
%patch1048 -p0 -b .pl48
%patch1049 -p0 -b .pl49
%patch1051 -p0 -b .pl51
%patch1052 -p0 -b .pl52
%patch1053 -p0 -b .pl53
%patch1054 -p0 -b .pl54
%patch1055 -p0 -b .pl55
%patch1056 -p0 -b .pl56
%patch1057 -p0 -b .pl57
%patch1058 -p0 -b .pl58
%patch1059 -p0 -b .pl59
%patch1060 -p0 -b .pl60
%patch1061 -p0 -b .pl61
%patch1062 -p0 -b .pl62
%patch1063 -p0 -b .pl63
%patch1064 -p0 -b .pl64
%patch1065 -p0 -b .pl65
%patch1066 -p0 -b .pl66
%patch1067 -p0 -b .pl67
%patch1068 -p0 -b .pl68
%patch1069 -p0 -b .pl69
%patch1070 -p0 -b .pl70
%patch1071 -p0 -b .pl71
%patch1072 -p0 -b .pl72
%patch1074 -p0 -b .pl74
%patch1075 -p0 -b .pl75
%patch1077 -p0 -b .pl77
%patch1078 -p0 -b .pl78
%patch1079 -p0 -b .pl79
%patch1080 -p0 -b .pl80
%patch1081 -p0 -b .pl81
%patch1082 -p0 -b .pl82
%patch1083 -p0 -b .pl83
#%patch1084 -p0 -b .pl84
%patch1085 -p0 -b .pl85
%patch1086 -p0 -b .pl86
%patch1087 -p0 -b .pl87
%patch1089 -p0 -b .pl89
%patch1090 -p0 -b .pl90
%patch1091 -p0 -b .pl91
%patch1092 -p0 -b .pl92
%patch1094 -p0 -b .pl94
%patch1095 -p0 -b .pl95
%patch1096 -p0 -b .pl96
%patch1097 -p0 -b .pl97
%patch1098 -p0 -b .pl98
%patch1099 -p0 -b .pl99
%patch1101 -p0 -b .pl101
%patch1102 -p0 -b .pl102
%patch1103 -p0 -b .pl103
%patch1104 -p0 -b .pl104
%patch1105 -p0 -b .pl105
%patch1106 -p0 -b .pl106
%patch1107 -p0 -b .pl107
%patch1108 -p0 -b .pl108
%patch1109 -p0 -b .pl109
%patch1110 -p0 -b .pl110
%patch1111 -p0 -b .pl111
%patch1112 -p0 -b .pl112
%patch1113 -p0 -b .pl113
%patch1114 -p0 -b .pl114
%patch1115 -p0 -b .pl115
%patch1116 -p0 -b .pl116
%patch1117 -p0 -b .pl117
%patch1118 -p0 -b .pl118
#%patch1119 -p0 -b .pl119
%patch1120 -p0 -b .pl120
%patch1121 -p0 -b .pl121
%patch1122 -p0 -b .pl122
%patch1123 -p0 -b .pl123
%patch1124 -p0 -b .pl124
%patch1125 -p0 -b .pl125
%patch1126 -p0 -b .pl126
%patch1127 -p0 -b .pl127
%patch1128 -p0 -b .pl128
%patch1129 -p0 -b .pl129
%patch1130 -p0 -b .pl130
%patch1131 -p0 -b .pl131
%patch1132 -p0 -b .pl132
%patch1133 -p0 -b .pl133
%patch1134 -p0 -b .pl134
%patch1135 -p0 -b .pl135
%patch1136 -p0 -b .pl136
%patch1137 -p0 -b .pl137
%patch1138 -p0 -b .pl138
%patch1139 -p0 -b .pl139
%patch1140 -p0 -b .pl140
%patch1141 -p0 -b .pl141
%patch1142 -p0 -b .pl142
%patch1143 -p0 -b .pl143
%patch1144 -p0 -b .pl144
%patch1145 -p0 -b .pl145
%patch1146 -p0 -b .pl146
%patch1150 -p0 -b .pl150
%patch1151 -p0 -b .pl151
%patch1152 -p0 -b .pl152
%patch1153 -p0 -b .pl153
%patch1157 -p0 -b .pl157
%patch1158 -p0 -b .pl158
%patch1159 -p0 -b .pl159
%patch1160 -p0 -b .pl160
%patch1161 -p0 -b .pl161
%patch1162 -p0 -b .pl162
%patch1163 -p0 -b .pl163
%patch1164 -p0 -b .pl164
%patch1165 -p0 -b .pl165

%patch2000 -p1 -b .kh1
%build
%if "%{rescue}" == ""
cd src
perl -pi -e "s,\\\$VIMRUNTIME,/usr/share/vim/%{vimversion},g" os_unix.h
perl -pi -e "s,\\\$VIM,/usr/share/vim/%{vimversion}/macros,g" os_unix.h

export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64"
export CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64"

%if %{withgui}
%configure --with-features=huge --enable-pythoninterp --enable-perlinterp --disable-tclinterp --with-x=yes --enable-gui=X11 --exec-prefix=/usr/X11R6 --enable-xim --enable-multibyte --enable-fontset --with-compiledby="<bugzilla@redhat.com>"
perl -pi -e "s,-I/usr/local/include,,g" auto/config.mk # FIXME: remove once perl is fixed
make
cp vim gvim
make clean
%endif

%configure --prefix=/usr --with-features=huge --enable-pythoninterp \
 --enable-perlinterp --disable-tclinterp --with-x=no --enable-gui=no \
 --exec-prefix=/usr --enable-multibyte --enable-fontset --with-compiledby="<bugzilla@redhat.com>"
perl -pi -e "s,-I/usr/local/include,,g" auto/config.mk # FIXME: remove once perl is fixed
make
cp vim enhanced-vim
make clean

%configure --prefix='${DEST}'/usr --with-features=tiny --with-x=no \
  --enable-multibyte \
  --disable-pythoninterp --disable-perlinterp --disable-tclinterp \
  --with-tlib=termcap --enable-gui=no --disable-gpm --exec-prefix=/ --with-compiledby="<bugzilla@redhat.com>"
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

gcc -O2 -o hardlink %{SOURCE4}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/bin
mkdir -p $RPM_BUILD_ROOT/usr/{bin,share/vim,X11R6/bin}

cd src
%makeinstall BINDIR=/bin DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/bin/xxd $RPM_BUILD_ROOT/usr/bin
make installmacros DESTDIR=$RPM_BUILD_ROOT
%if "%{rescue}" == "" 
%if "%{withgui}" == "1"
install -s -m755 gvim $RPM_BUILD_ROOT/usr/X11R6/bin
%endif
install -s -m755 enhanced-vim $RPM_BUILD_ROOT/usr/bin/vim
%endif

( cd $RPM_BUILD_ROOT
  mv ./bin/vimtutor ./usr/bin
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
%if "%{withgui}" == "1"
  ln -sf gvim ./usr/X11R6/bin/gview
  ln -sf gvim ./usr/X11R6/bin/gex
%endif
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
%if "%{withgui}" == "1"
  ln -sf gvim ./usr/X11R6/bin/vimx
  %if %{desktop_file}
    mkdir -p $RPM_BUILD_ROOT/usr/share/applications
    desktop-file-install --vendor net \
        --dir $RPM_BUILD_ROOT/usr/share/applications \
        --add-category "Application;Development;X-Red-Hat-Base" \
        %{SOURCE2}
  %else
    mkdir -p ./etc/X11/applnk/Applications
    cp %{SOURCE2} ./etc/X11/applnk/Applications/gvim.desktop
  %endif
%endif
%endif
  install -s -m644 %{SOURCE3} ./usr/share/vim/%{vimversion}/macros/
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
if [ -n "\$BASH_VERSION" -o -n "\$KSH_VERSION" ]; then
  # for bash and pdksh and if no alias is already set
  alias vi >/dev/null 2>&1 || alias vi=vim
fi
EOF
cat >$RPM_BUILD_ROOT/etc/profile.d/vim.csh <<EOF
alias vi vim
EOF
chmod 0755 $RPM_BUILD_ROOT/etc/profile.d/*
%endif
(cd ../runtime; rm -rf doc; ln -svf ../../vim/vim61/doc docs;)

%clean
rm -rf $RPM_BUILD_ROOT

%if "%{rescue}" != ""
%files
%defattr(-,root,root)
%doc README*.txt runtime/macros/README.txt runtime/tools/README.txt
%doc runtime/docs
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
%doc runtime/docs
/usr/bin/xxd

/usr/share/vim
%{_mandir}/man1/vim.*
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
/usr/bin/vimtutor
%config /etc/profile.d/vim.*
%{_mandir}/man1/rvim.*
%{_mandir}/man1/vimdiff.*
%{_mandir}/man1/vimtutor.*

%if "%{withgui}" == "1"
%files X11
%defattr(-,root,root)
%if %{desktop_file}
/usr/share/applications/*
%else
/etc/X11/applnk/*/gvim.desktop
%endif
/usr/X11R6/bin/gvim
/usr/X11R6/bin/evim
/usr/X11R6/bin/gview
/usr/X11R6/bin/gex
/usr/X11R6/bin/vimx
%{_mandir}/man1/gvim.*
%{_mandir}/man1/evim.*
%endif
%endif

%changelog
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
