# used for CVS snapshots:
%define CVSDATE %{nil}
%if %{?WITH_SELINUX:0}%{!?WITH_SELINUX:1}
%define WITH_SELINUX 1
%endif
%define desktop_file 1
%if %{desktop_file}
%define desktop_file_utils_version 0.2.93
%endif

%define withnetbeans 0

%define withvimspell 0
%define withhunspell 0
%define withruby 1

%define baseversion 7.1
#used for pre-releases:
%define beta %{nil}
%define vimdir vim71%{?beta}
%define patchlevel 283

Summary: The VIM editor
URL:     http://www.vim.org/
Name: vim
Version: %{baseversion}.%{beta}%{patchlevel}
Release: 1%{?dist}
License: Vim
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
Source12: vi_help.txt
%if %{withvimspell}
Source13: vim-spell-files.tar.bz2
%endif
Source14: spec-template

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
Patch003: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.003
Patch004: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.004
Patch005: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.005
Patch006: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.006
Patch007: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.007
Patch008: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.008
Patch009: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.009
Patch010: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.010
Patch011: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.011
Patch012: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.012
Patch013: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.013
Patch014: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.014
Patch015: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.015
Patch016: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.016
Patch017: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.017
Patch018: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.018
Patch019: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.019
Patch020: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.020
Patch021: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.021
Patch022: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.022
Patch023: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.023
Patch024: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.024
Patch025: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.025
Patch026: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.026
Patch027: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.027
Patch028: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.028
Patch029: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.029
Patch030: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.030
Patch031: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.031
Patch032: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.032
Patch033: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.033
Patch034: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.034
Patch035: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.035
Patch036: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.036
Patch037: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.037
Patch038: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.038
Patch039: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.039
Patch040: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.040
Patch041: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.041
Patch042: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.042
Patch043: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.043
Patch044: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.044
Patch045: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.045
Patch046: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.046
Patch047: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.047
Patch048: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.048
Patch049: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.049
Patch050: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.050
Patch051: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.051
Patch052: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.052
Patch053: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.053
Patch054: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.054
Patch055: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.055
Patch056: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.056
Patch057: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.057
Patch058: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.058
Patch059: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.059
Patch060: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.060
Patch061: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.061
Patch062: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.062
Patch063: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.063
Patch064: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.064
Patch065: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.065
Patch066: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.066
Patch067: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.067
Patch068: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.068
Patch069: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.069
Patch070: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.070
Patch071: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.071
Patch072: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.072
Patch073: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.073
Patch074: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.074
Patch075: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.075
Patch076: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.076
Patch077: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.077
Patch078: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.078
Patch079: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.079
Patch080: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.080
Patch081: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.081
Patch082: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.082
Patch083: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.083
Patch084: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.084
Patch085: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.085
Patch086: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.086
Patch087: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.087
Patch088: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.088
Patch089: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.089
Patch090: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.090
Patch091: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.091
Patch092: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.092
Patch093: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.093
Patch094: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.094
Patch095: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.095
Patch096: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.096
Patch097: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.097
Patch098: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.098
Patch099: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.099
Patch100: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.100
Patch101: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.101
Patch102: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.102
Patch103: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.103
Patch104: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.104
Patch105: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.105
Patch106: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.106
Patch107: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.107
Patch108: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.108
Patch109: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.109
Patch110: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.110
Patch111: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.111
Patch112: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.112
Patch113: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.113
Patch114: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.114
Patch115: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.115
Patch116: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.116
Patch117: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.117
Patch118: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.118
Patch119: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.119
Patch120: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.120
Patch121: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.121
Patch122: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.122
Patch123: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.123
Patch124: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.124
Patch125: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.125
Patch126: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.126
Patch127: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.127
Patch128: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.128
Patch129: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.129
Patch130: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.130
Patch131: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.131
Patch132: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.132
Patch133: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.133
Patch134: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.134
Patch135: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.135
Patch136: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.136
Patch137: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.137
Patch138: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.138
Patch139: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.139
Patch140: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.140
Patch141: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.141
Patch142: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.142
Patch143: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.143
Patch144: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.144
Patch145: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.145
Patch146: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.146
Patch147: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.147
Patch148: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.148
Patch149: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.149
Patch150: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.150
Patch151: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.151
Patch152: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.152
Patch153: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.153
Patch154: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.154
Patch155: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.155
Patch156: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.156
Patch157: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.157
Patch158: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.158
Patch159: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.159
Patch160: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.160
Patch161: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.161
Patch162: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.162
Patch163: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.163
Patch164: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.164
Patch165: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.165
Patch166: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.166
Patch167: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.167
Patch168: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.168
Patch169: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.169
Patch170: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.170
Patch171: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.171
Patch172: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.172
Patch173: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.173
Patch174: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.174
Patch175: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.175
Patch176: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.176
Patch177: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.177
Patch178: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.178
Patch179: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.179
Patch180: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.180
Patch181: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.181
Patch182: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.182
Patch183: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.183
Patch184: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.184
Patch185: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.185
Patch186: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.186
Patch187: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.187
Patch188: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.188
Patch189: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.189
Patch190: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.190
Patch191: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.191
Patch192: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.192
Patch193: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.193
Patch194: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.194
Patch195: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.195
Patch196: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.196
Patch197: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.197
Patch198: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.198
Patch199: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.199
Patch200: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.200
Patch201: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.201
Patch202: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.202
Patch203: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.203
Patch204: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.204
Patch205: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.205
Patch206: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.206
Patch207: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.207
Patch208: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.208
Patch209: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.209
Patch210: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.210
Patch211: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.211
Patch212: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.212
Patch213: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.213
Patch214: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.214
Patch215: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.215
Patch216: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.216
Patch217: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.217
Patch218: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.218
Patch219: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.219
Patch220: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.220
Patch221: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.221
Patch222: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.222
Patch223: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.223
Patch224: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.224
Patch225: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.225
Patch226: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.226
Patch227: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.227
Patch228: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.228
Patch229: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.229
Patch230: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.230
Patch231: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.231
Patch232: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.232
Patch233: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.233
Patch234: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.234
Patch235: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.235
Patch236: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.236
Patch237: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.237
Patch238: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.238
Patch239: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.239
Patch240: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.240
Patch241: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.241
Patch242: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.242
Patch243: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.243
Patch244: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.244
Patch245: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.245
Patch246: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.246
Patch247: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.247
Patch248: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.248
Patch249: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.249
Patch250: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.250
Patch251: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.251
Patch252: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.252
Patch253: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.253
Patch254: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.254
Patch255: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.255
Patch256: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.256
Patch257: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.257
Patch258: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.258
Patch259: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.259
Patch260: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.260
Patch261: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.261
Patch262: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.262
Patch263: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.263
Patch264: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.264
Patch265: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.265
Patch266: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.266
Patch267: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.267
Patch268: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.268
Patch269: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.269
Patch270: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.270
Patch271: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.271
Patch272: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.272
Patch273: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.273
Patch274: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.274
Patch275: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.275
Patch276: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.276
Patch277: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.277
Patch278: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.278
Patch279: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.279
Patch280: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.280
Patch281: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.281
Patch282: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.282
Patch283: ftp://ftp.vim.org/pub/vim/patches/7.1/7.1.283

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
# Remove this one when the runtime files get updated (#246378):
Patch3013: vim-7.1-ada.patch
#
Patch3014: vim-7.1-erlang.patch
Patch3100: vim-selinux.patch
Patch3101: vim-selinux2.patch

Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python-devel ncurses-devel gettext perl-devel
BuildRequires: perl(ExtUtils::Embed)
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
Requires: vim-common = %{epoch}:%{version}-%{release} which
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
%setup -q -b 0 -n %{vimdir}
%setup -q -D -b 1 -n %{vimdir}
%setup -q -D -b 2 -n %{vimdir}
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
%patch022 -p0 
%patch023 -p0 
%patch024 -p0 
%patch025 -p0 
%patch026 -p0 
%patch027 -p0 
%patch028 -p0 
%patch029 -p0
%patch030 -p0
%patch031 -p0
%patch032 -p0
%patch033 -p0
%patch034 -p0
%patch035 -p0
%patch036 -p0
%patch037 -p0
%patch038 -p0
%patch039 -p0
%patch040 -p0
%patch041 -p0
%patch042 -p0
%patch043 -p0
%patch044 -p0
%patch045 -p0
%patch046 -p0
%patch047 -p0
%patch048 -p0
%patch049 -p0
%patch050 -p0
%patch051 -p0
%patch052 -p0
%patch053 -p0
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
%patch072 -p0 
%patch073 -p0 
%patch074 -p0 
%patch075 -p0 
%patch076 -p0 
%patch077 -p0 
%patch078 -p0 
%patch079 -p0 
%patch080 -p0 
%patch081 -p0 
%patch082 -p0 
%patch083 -p0 
%patch084 -p0 
%patch085 -p0 
%patch086 -p0 
%patch087 -p0 
%patch088 -p0 
%patch089 -p0 
%patch090 -p0 
%patch091 -p0 
%patch092 -p0 
%patch093 -p0 
%patch094 -p0 
%patch095 -p0 
%patch096 -p0 
%patch097 -p0 
%patch098 -p0 
%patch099 -p0 
%patch100 -p0 
%patch101 -p0 
%patch102 -p0 
%patch103 -p0 
%patch104 -p0 
%patch105 -p0 
%patch106 -p0 
%patch107 -p0 
%patch108 -p0 
%patch109 -p0 
%patch110 -p0 
%patch111 -p0 
%patch112 -p0 
%patch113 -p0 
%patch114 -p0 
%patch115 -p0 
%patch116 -p0 
%patch117 -p0 
%patch118 -p0 
%patch119 -p0 
%patch120 -p0 
%patch121 -p0 
%patch122 -p0 
%patch123 -p0
%patch124 -p0
%patch125 -p0
%patch126 -p0
%patch127 -p0
%patch128 -p0
%patch129 -p0
%patch130 -p0
%patch131 -p0
%patch132 -p0
%patch133 -p0
%patch134 -p0
%patch135 -p0
%patch136 -p0
%patch137 -p0
%patch138 -p0
%patch139 -p0
%patch140 -p0
%patch141 -p0
%patch142 -p0
%patch143 -p0
%patch144 -p0
%patch145 -p0
%patch146 -p0
%patch147 -p0
%patch148 -p0
%patch149 -p0
%patch150 -p0
%patch151 -p0
%patch152 -p0
%patch153 -p0
%patch154 -p0
%patch155 -p0
%patch156 -p0
%patch157 -p0
%patch158 -p0
%patch159 -p0
%patch160 -p0
%patch161 -p0
%patch162 -p0
%patch163 -p0
%patch164 -p0
%patch165 -p0
%patch166 -p0
%patch167 -p0
%patch168 -p0
%patch169 -p0
%patch170 -p0
%patch171 -p0
%patch172 -p0
%patch173 -p0
%patch174 -p0
%patch175 -p0
%patch176 -p0 
%patch177 -p0 
%patch178 -p0 
%patch179 -p0 
%patch180 -p0 
%patch181 -p0 
%patch182 -p0 
%patch183 -p0 
%patch184 -p0 
%patch185 -p0 
%patch186 -p0 
%patch187 -p0 
%patch188 -p0 
%patch189 -p0 
%patch190 -p0 
%patch191 -p0 
%patch192 -p0 
%patch193 -p0 
%patch194 -p0 
%patch195 -p0 
%patch196 -p0 
%patch197 -p0 
%patch198 -p0 
%patch199 -p0 
%patch200 -p0 
%patch201 -p0 
%patch202 -p0 
%patch203 -p0 
%patch204 -p0 
%patch205 -p0 
%patch206 -p0 
%patch207 -p0 
%patch208 -p0 
%patch209 -p0 
%patch210 -p0 
%patch211 -p0 
%patch212 -p0
%patch213 -p0
%patch214 -p0
%patch215 -p0
%patch216 -p0
%patch217 -p0
%patch218 -p0
%patch219 -p0
%patch220 -p0
%patch221 -p0
%patch222 -p0
%patch223 -p0
%patch224 -p0
%patch225 -p0
%patch226 -p0
%patch227 -p0
%patch228 -p0
%patch229 -p0
%patch230 -p0
%patch231 -p0
%patch232 -p0
%patch233 -p0
%patch234 -p0
%patch235 -p0
%patch236 -p0
%patch237 -p0
%patch238 -p0
%patch239 -p0
%patch240 -p0
%patch241 -p0
%patch242 -p0
%patch243 -p0
%patch244 -p0
%patch245 -p0
%patch246 -p0
%patch247 -p0
%patch248 -p0
%patch249 -p0
%patch250 -p0
%patch251 -p0
%patch252 -p0
%patch253 -p0
%patch254 -p0
%patch255 -p0
%patch256 -p0
%patch257 -p0
%patch258 -p0
%patch259 -p0
%patch260 -p0
%patch261 -p0
%patch262 -p0
%patch263 -p0
%patch264 -p0
%patch265 -p0
%patch266 -p0
%patch267 -p0
%patch268 -p0
%patch269 -p0
%patch270 -p0
%patch271 -p0
%patch272 -p0
%patch273 -p0
%patch274 -p0
%patch275 -p0
%patch276 -p0
%patch277 -p0
%patch278 -p0
%patch279 -p0
%patch280 -p0
%patch281 -p0
%patch282 -p0
%patch283 -p0


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
%patch3013 -p1
%patch3014 -p1

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
%if "%{withruby}" == "1"
  --enable-rubyinterp \
%else
  --disable-rubyinterp \
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
%if "%{withruby}" == "1"
  --enable-rubyinterp \
%else
  --disable-rubyinterp \
%endif

make %{?_smp_mflags}
cp vim enhanced-vim
make clean

perl -pi -e "s/help.txt/vi_help.txt/"  os_unix.h ex_cmds.c
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
cp -f %{SOURCE14} $RPM_BUILD_ROOT/%{_datadir}/%{name}/vimfiles/template.spec
cp runtime/doc/uganda.txt LICENSE


cd src
make install DESTDIR=$RPM_BUILD_ROOT BINDIR=/bin
mv $RPM_BUILD_ROOT/bin/xxd $RPM_BUILD_ROOT/%{_bindir}/xxd
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
 gzip -d help.txt.gz version7.txt.gz sponsor.txt.gz
 cp %{SOURCE12} .
 cat tags | sed -e 's/\t\(.*.txt\)\t/\t\1.gz\t/;s/\thelp.txt.gz\t/\thelp.txt\t/;s/\tversion7.txt.gz\t/\tversion7.txt\t/;s/\tsponsor.txt.gz\t/\tsponsor.txt\t/' > tags.new; mv -f tags.new tags
cat >> tags << EOF
vi_help.txt	vi_help.txt	/*vi_help.txt*
vi-author.txt	vi_help.txt	/*vi-author*
vi-Bram.txt	vi_help.txt	/*vi-Bram*
vi-Moolenaar.txt	vi_help.txt	/*vi-Moolenaar*
vi-credits.txt	vi_help.txt	/*vi-credits*
EOF
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
%{_datadir}/%{name}/vimfiles/template.spec
%{_datadir}/%{name}/%{vimdir}/autoload
%{_datadir}/%{name}/%{vimdir}/colors
%{_datadir}/%{name}/%{vimdir}/compiler
%{_datadir}/%{name}/%{vimdir}/doc
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
* Mon Mar 17 2008 Karsten Hopp <karsten@redhat.com> 7.1.283-1
- patchlevel 283, fixes leftover cscope files in /tmp

* Wed Mar 12 2008 Karsten Hopp <karsten@redhat.com> 7.1.273-1
- update to patchlevel 273, this fixes #436902

* Tue Mar 11 2008 Karsten Hopp <karsten@redhat.com> 7.1.270-1
- patchlevel 270
- don't write swapfile on most common locations for USB-sticks (#436752)
- add spec file template

* Mon Mar 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> 7.1.269-2
- BR: ExtUtils::Embed to find perl headers

* Mon Mar 10 2008 Karsten Hopp <karsten@redhat.com> 7.1.269-1
- patchlevel 269
- rebuild with new perl (#436731)

* Mon Mar 03 2008 Karsten Hopp <karsten@redhat.com> 7.1.266-1
- patchlevel 266
- add minimal help page for /bin/vi (#173974)

* Mon Feb 25 2008 Karsten Hopp <karsten@redhat.com> 7.1.262-1
- patchlevel 262
- add fix for #231124, BOM was ignored
- enable ruby interpreter (#215207)
- add filetype for Erlang header files (#417371)

* Mon Feb 11 2008 Karsten Hopp <karsten@redhat.com> 7.1.245-1
- patchlevel 245

* Sun Jan 27 2008 Karsten Hopp <karsten@redhat.com> 7.1.242-1
- patchlevel 242

* Fri Jan 18 2008 Karsten Hopp <karsten@redhat.com> 7.1.233-2
- silence taglist plugin (#429200)

* Fri Jan 18 2008 Karsten Hopp <karsten@redhat.com> 7.1.233-1
- patchlevel 233
- fix ada patch

* Wed Jan 16 2008 Karsten Hopp <karsten@redhat.com> 7.1.230-2
- add newer ada runtime files to fix bugzilla #246378

* Wed Jan 16 2008 Karsten Hopp <karsten@redhat.com> 7.1.230-1
- patchlevel 230, fixes memory leak

* Mon Jan 14 2008 Karsten Hopp <karsten@redhat.com> 7.1.228-1
- patchlevel 228
- allow overwriting WITH_SELING at build time (#427710)

* Thu Jan 10 2008 Karsten Hopp <karsten@redhat.com> 7.1.214-1
- patchlevel 214

* Mon Jan 07 2008 Karsten Hopp <karsten@redhat.com> 7.1.211-1
- patchlevel 211

* Sat Dec 22 2007 Karsten Hopp <karsten@redhat.com> 7.1.175-1
- patchlevel 175

* Thu Nov 22 2007 Karsten Hopp <karsten@redhat.com> 7.1.159-1
- patchlevel 159
- vim-enhanced requires which for vimtutor (#395371)

* Thu Oct 04 2007 Karsten Hopp <karsten@redhat.com> 7.1.135-1
- patchlevel 135

* Wed Sep 26 2007 Karsten Hopp <karsten@redhat.com> 7.1.122-1
- patchlevel 122

* Tue Sep 25 2007 Karsten Hopp <karsten@redhat.com> 7.1.119-1
- patchlevel 119

* Mon Sep 24 2007 Karsten Hopp <karsten@redhat.com> 7.1.116-1
- patchlevel 116

* Fri Sep 07 2007 Karsten Hopp <karsten@redhat.com> 7.1.100-1
- patchlevel 100

* Fri Aug 24 2007 Karsten Hopp <karsten@redhat.com> 7.1.87-1
- add build requirement perl-devel
- fix tarball unpacking
- patchlevel 87

* Wed Aug 15 2007 Karsten Hopp <karsten@redhat.com> 7.1.77-1
- patchlevel 77

* Mon Aug 13 2007 Karsten Hopp <karsten@redhat.com> 7.1.68-1
- patchlevel 68

* Thu Aug 02 2007 Karsten Hopp <karsten@redhat.com> 7.1.47-1
- patchlevel 47

* Wed Jul 11 2007 Karsten Hopp <karsten@redhat.com> 7.1.28-1
- patchlevel 28

* Wed Jun 27 2007 Karsten Hopp <karsten@redhat.com> 7.1.12-1
- Patchlevel 12

* Mon Jun 04 2007 Karsten Hopp <karsten@redhat.com> 7.1.2-1
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
