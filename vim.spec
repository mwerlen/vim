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


%define baseversion 6.2
%define vimdir vim62
%define patchlevel 327

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
Patch2000: vim-4.2-speed_t.patch
Patch2001: vim-5.1-vimnotvi.patch
Patch2002: vim-5.6a-paths.patch
Patch2003: vim-6.0-fixkeys.patch
Patch2004: vim-6.2-specsyntax.patch
Patch2005: vim-6.0r-crv.patch
Patch2010: xxd-locale.patch
# Patches 001 < 999 are patches from the base maintainer.
# If you're as lazy as me, generate the list using
# (for i in `seq 1 14`; do printf "Patch%03d: ftp://ftp.vim.org/pub/vim/patches/6.2.%03d\n" $i $i; done)
Patch001: ftp://ftp.vim.org/pub/vim/patches/6.2.001
Patch002: ftp://ftp.vim.org/pub/vim/patches/6.2.002
Patch003: ftp://ftp.vim.org/pub/vim/patches/6.2.003
Patch004: ftp://ftp.vim.org/pub/vim/patches/6.2.004
Patch005: ftp://ftp.vim.org/pub/vim/patches/6.2.005
Patch006: ftp://ftp.vim.org/pub/vim/patches/6.2.006
Patch007: ftp://ftp.vim.org/pub/vim/patches/6.2.007
Patch008: ftp://ftp.vim.org/pub/vim/patches/6.2.008
Patch009: ftp://ftp.vim.org/pub/vim/patches/6.2.009
Patch010: ftp://ftp.vim.org/pub/vim/patches/6.2.010
Patch011: ftp://ftp.vim.org/pub/vim/patches/6.2.011
Patch012: ftp://ftp.vim.org/pub/vim/patches/6.2.012
Patch013: ftp://ftp.vim.org/pub/vim/patches/6.2.013
Patch014: ftp://ftp.vim.org/pub/vim/patches/6.2.014
Patch015: ftp://ftp.vim.org/pub/vim/patches/6.2.015
Patch016: ftp://ftp.vim.org/pub/vim/patches/6.2.016
Patch017: ftp://ftp.vim.org/pub/vim/patches/6.2.017
Patch018: ftp://ftp.vim.org/pub/vim/patches/6.2.018
Patch019: ftp://ftp.vim.org/pub/vim/patches/6.2.019
Patch020: ftp://ftp.vim.org/pub/vim/patches/6.2.020
Patch021: ftp://ftp.vim.org/pub/vim/patches/6.2.021
Patch022: ftp://ftp.vim.org/pub/vim/patches/6.2.022
Patch023: ftp://ftp.vim.org/pub/vim/patches/6.2.023
Patch024: ftp://ftp.vim.org/pub/vim/patches/6.2.024
Patch025: ftp://ftp.vim.org/pub/vim/patches/6.2.025
Patch026: ftp://ftp.vim.org/pub/vim/patches/6.2.026
Patch027: ftp://ftp.vim.org/pub/vim/patches/6.2.027
Patch028: ftp://ftp.vim.org/pub/vim/patches/6.2.028
Patch029: ftp://ftp.vim.org/pub/vim/patches/6.2.029
Patch030: ftp://ftp.vim.org/pub/vim/patches/6.2.030
Patch031: ftp://ftp.vim.org/pub/vim/patches/6.2.031
Patch032: ftp://ftp.vim.org/pub/vim/patches/6.2.032
Patch033: ftp://ftp.vim.org/pub/vim/patches/6.2.033
Patch034: ftp://ftp.vim.org/pub/vim/patches/6.2.034
Patch035: ftp://ftp.vim.org/pub/vim/patches/6.2.035
Patch036: ftp://ftp.vim.org/pub/vim/patches/6.2.036
Patch037: ftp://ftp.vim.org/pub/vim/patches/6.2.037
Patch038: ftp://ftp.vim.org/pub/vim/patches/6.2.038
Patch039: ftp://ftp.vim.org/pub/vim/patches/6.2.039
Patch040: ftp://ftp.vim.org/pub/vim/patches/6.2.040
Patch041: ftp://ftp.vim.org/pub/vim/patches/6.2.041
Patch042: ftp://ftp.vim.org/pub/vim/patches/6.2.042
Patch043: ftp://ftp.vim.org/pub/vim/patches/6.2.043
Patch044: ftp://ftp.vim.org/pub/vim/patches/6.2.044
Patch045: ftp://ftp.vim.org/pub/vim/patches/6.2.045
Patch046: ftp://ftp.vim.org/pub/vim/patches/6.2.046
Patch047: ftp://ftp.vim.org/pub/vim/patches/6.2.047
Patch048: ftp://ftp.vim.org/pub/vim/patches/6.2.048
Patch049: ftp://ftp.vim.org/pub/vim/patches/6.2.049
Patch050: ftp://ftp.vim.org/pub/vim/patches/6.2.050
Patch051: ftp://ftp.vim.org/pub/vim/patches/6.2.051
Patch052: ftp://ftp.vim.org/pub/vim/patches/6.2.052
Patch053: ftp://ftp.vim.org/pub/vim/patches/6.2.053
Patch054: ftp://ftp.vim.org/pub/vim/patches/6.2.054
Patch055: ftp://ftp.vim.org/pub/vim/patches/6.2.055
Patch056: ftp://ftp.vim.org/pub/vim/patches/6.2.056
Patch057: ftp://ftp.vim.org/pub/vim/patches/6.2.057
Patch058: ftp://ftp.vim.org/pub/vim/patches/6.2.058
Patch059: ftp://ftp.vim.org/pub/vim/patches/6.2.059
Patch060: ftp://ftp.vim.org/pub/vim/patches/6.2.060
Patch061: ftp://ftp.vim.org/pub/vim/patches/6.2.061
Patch062: ftp://ftp.vim.org/pub/vim/patches/6.2.062
Patch063: ftp://ftp.vim.org/pub/vim/patches/6.2.063
Patch064: ftp://ftp.vim.org/pub/vim/patches/6.2.064
Patch065: ftp://ftp.vim.org/pub/vim/patches/6.2.065
Patch066: ftp://ftp.vim.org/pub/vim/patches/6.2.066
Patch067: ftp://ftp.vim.org/pub/vim/patches/6.2.067
Patch068: ftp://ftp.vim.org/pub/vim/patches/6.2.068
Patch069: ftp://ftp.vim.org/pub/vim/patches/6.2.069
Patch070: ftp://ftp.vim.org/pub/vim/patches/6.2.070
Patch071: ftp://ftp.vim.org/pub/vim/patches/6.2.071
Patch072: ftp://ftp.vim.org/pub/vim/patches/6.2.072
Patch073: ftp://ftp.vim.org/pub/vim/patches/6.2.073
Patch074: ftp://ftp.vim.org/pub/vim/patches/6.2.074
Patch075: ftp://ftp.vim.org/pub/vim/patches/6.2.075
Patch076: ftp://ftp.vim.org/pub/vim/patches/6.2.076
Patch077: ftp://ftp.vim.org/pub/vim/patches/6.2.077
Patch078: ftp://ftp.vim.org/pub/vim/patches/6.2.078
Patch079: ftp://ftp.vim.org/pub/vim/patches/6.2.079
Patch080: ftp://ftp.vim.org/pub/vim/patches/6.2.080
Patch081: ftp://ftp.vim.org/pub/vim/patches/6.2.081
Patch082: ftp://ftp.vim.org/pub/vim/patches/6.2.082
Patch083: ftp://ftp.vim.org/pub/vim/patches/6.2.083
Patch084: ftp://ftp.vim.org/pub/vim/patches/6.2.084
Patch085: ftp://ftp.vim.org/pub/vim/patches/6.2.085
Patch086: ftp://ftp.vim.org/pub/vim/patches/6.2.086
Patch087: ftp://ftp.vim.org/pub/vim/patches/6.2.087
Patch088: ftp://ftp.vim.org/pub/vim/patches/6.2.088
Patch089: ftp://ftp.vim.org/pub/vim/patches/6.2.089
Patch090: ftp://ftp.vim.org/pub/vim/patches/6.2.090
Patch091: ftp://ftp.vim.org/pub/vim/patches/6.2.091
Patch092: ftp://ftp.vim.org/pub/vim/patches/6.2.092
Patch093: ftp://ftp.vim.org/pub/vim/patches/6.2.093
Patch094: ftp://ftp.vim.org/pub/vim/patches/6.2.094
Patch095: ftp://ftp.vim.org/pub/vim/patches/6.2.095
Patch096: ftp://ftp.vim.org/pub/vim/patches/6.2.096
Patch097: ftp://ftp.vim.org/pub/vim/patches/6.2.097
Patch098: ftp://ftp.vim.org/pub/vim/patches/6.2.098
Patch099: ftp://ftp.vim.org/pub/vim/patches/6.2.099
Patch100: ftp://ftp.vim.org/pub/vim/patches/6.2.100
Patch101: ftp://ftp.vim.org/pub/vim/patches/6.2.101
Patch102: ftp://ftp.vim.org/pub/vim/patches/6.2.102
Patch103: ftp://ftp.vim.org/pub/vim/patches/6.2.103
Patch104: ftp://ftp.vim.org/pub/vim/patches/6.2.104
Patch105: ftp://ftp.vim.org/pub/vim/patches/6.2.105
Patch106: ftp://ftp.vim.org/pub/vim/patches/6.2.106
Patch107: ftp://ftp.vim.org/pub/vim/patches/6.2.107
Patch108: ftp://ftp.vim.org/pub/vim/patches/6.2.108
Patch109: ftp://ftp.vim.org/pub/vim/patches/6.2.109
Patch110: ftp://ftp.vim.org/pub/vim/patches/6.2.110
Patch111: ftp://ftp.vim.org/pub/vim/patches/6.2.111
Patch112: ftp://ftp.vim.org/pub/vim/patches/6.2.112
Patch113: ftp://ftp.vim.org/pub/vim/patches/6.2.113
Patch114: ftp://ftp.vim.org/pub/vim/patches/6.2.114
Patch115: ftp://ftp.vim.org/pub/vim/patches/6.2.115
Patch116: ftp://ftp.vim.org/pub/vim/patches/6.2.116
Patch117: ftp://ftp.vim.org/pub/vim/patches/6.2.117
Patch118: ftp://ftp.vim.org/pub/vim/patches/6.2.118
Patch119: ftp://ftp.vim.org/pub/vim/patches/6.2.119
Patch120: ftp://ftp.vim.org/pub/vim/patches/6.2.120
Patch121: ftp://ftp.vim.org/pub/vim/patches/6.2.121
Patch122: ftp://ftp.vim.org/pub/vim/patches/6.2.122
Patch123: ftp://ftp.vim.org/pub/vim/patches/6.2.123
Patch124: ftp://ftp.vim.org/pub/vim/patches/6.2.124
Patch125: ftp://ftp.vim.org/pub/vim/patches/6.2.125
Patch126: ftp://ftp.vim.org/pub/vim/patches/6.2.126
Patch127: ftp://ftp.vim.org/pub/vim/patches/6.2.127
Patch128: ftp://ftp.vim.org/pub/vim/patches/6.2.128
Patch129: ftp://ftp.vim.org/pub/vim/patches/6.2.129
Patch130: ftp://ftp.vim.org/pub/vim/patches/6.2.130
Patch131: ftp://ftp.vim.org/pub/vim/patches/6.2.131
Patch132: ftp://ftp.vim.org/pub/vim/patches/6.2.132
Patch133: ftp://ftp.vim.org/pub/vim/patches/6.2.133
Patch134: ftp://ftp.vim.org/pub/vim/patches/6.2.134
Patch135: ftp://ftp.vim.org/pub/vim/patches/6.2.135
Patch136: ftp://ftp.vim.org/pub/vim/patches/6.2.136
Patch137: ftp://ftp.vim.org/pub/vim/patches/6.2.137
Patch138: ftp://ftp.vim.org/pub/vim/patches/6.2.138
Patch139: ftp://ftp.vim.org/pub/vim/patches/6.2.139
Patch140: ftp://ftp.vim.org/pub/vim/patches/6.2.140
Patch141: ftp://ftp.vim.org/pub/vim/patches/6.2.141
Patch142: ftp://ftp.vim.org/pub/vim/patches/6.2.142
Patch143: ftp://ftp.vim.org/pub/vim/patches/6.2.143
Patch144: ftp://ftp.vim.org/pub/vim/patches/6.2.144
Patch145: ftp://ftp.vim.org/pub/vim/patches/6.2.145
Patch146: ftp://ftp.vim.org/pub/vim/patches/6.2.146
Patch147: ftp://ftp.vim.org/pub/vim/patches/6.2.147
Patch148: ftp://ftp.vim.org/pub/vim/patches/6.2.148
Patch149: ftp://ftp.vim.org/pub/vim/patches/6.2.149
Patch150: ftp://ftp.vim.org/pub/vim/patches/6.2.150
Patch151: ftp://ftp.vim.org/pub/vim/patches/6.2.151
Patch152: ftp://ftp.vim.org/pub/vim/patches/6.2.152
Patch153: ftp://ftp.vim.org/pub/vim/patches/6.2.153
Patch154: ftp://ftp.vim.org/pub/vim/patches/6.2.154
Patch155: ftp://ftp.vim.org/pub/vim/patches/6.2.155
Patch156: ftp://ftp.vim.org/pub/vim/patches/6.2.156
Patch157: ftp://ftp.vim.org/pub/vim/patches/6.2.157
Patch158: ftp://ftp.vim.org/pub/vim/patches/6.2.158
Patch159: ftp://ftp.vim.org/pub/vim/patches/6.2.159
Patch160: ftp://ftp.vim.org/pub/vim/patches/6.2.160
Patch161: ftp://ftp.vim.org/pub/vim/patches/6.2.161
Patch162: ftp://ftp.vim.org/pub/vim/patches/6.2.162
Patch163: ftp://ftp.vim.org/pub/vim/patches/6.2.163
Patch164: ftp://ftp.vim.org/pub/vim/patches/6.2.164
Patch165: ftp://ftp.vim.org/pub/vim/patches/6.2.165
Patch166: ftp://ftp.vim.org/pub/vim/patches/6.2.166
Patch167: ftp://ftp.vim.org/pub/vim/patches/6.2.167
Patch168: ftp://ftp.vim.org/pub/vim/patches/6.2.168
Patch169: ftp://ftp.vim.org/pub/vim/patches/6.2.169
Patch170: ftp://ftp.vim.org/pub/vim/patches/6.2.170
Patch171: ftp://ftp.vim.org/pub/vim/patches/6.2.171
Patch172: ftp://ftp.vim.org/pub/vim/patches/6.2.172
Patch173: ftp://ftp.vim.org/pub/vim/patches/6.2.173
Patch174: ftp://ftp.vim.org/pub/vim/patches/6.2.174
Patch175: ftp://ftp.vim.org/pub/vim/patches/6.2.175
Patch176: ftp://ftp.vim.org/pub/vim/patches/6.2.176
Patch177: ftp://ftp.vim.org/pub/vim/patches/6.2.177
Patch178: ftp://ftp.vim.org/pub/vim/patches/6.2.178
Patch179: ftp://ftp.vim.org/pub/vim/patches/6.2.179
Patch180: ftp://ftp.vim.org/pub/vim/patches/6.2.180
Patch181: ftp://ftp.vim.org/pub/vim/patches/6.2.181
Patch182: ftp://ftp.vim.org/pub/vim/patches/6.2.182
Patch183: ftp://ftp.vim.org/pub/vim/patches/6.2.183
Patch184: ftp://ftp.vim.org/pub/vim/patches/6.2.184
Patch185: ftp://ftp.vim.org/pub/vim/patches/6.2.185
Patch186: ftp://ftp.vim.org/pub/vim/patches/6.2.186
Patch187: ftp://ftp.vim.org/pub/vim/patches/6.2.187
Patch188: ftp://ftp.vim.org/pub/vim/patches/6.2.188
Patch189: ftp://ftp.vim.org/pub/vim/patches/6.2.189
Patch190: ftp://ftp.vim.org/pub/vim/patches/6.2.190
Patch191: ftp://ftp.vim.org/pub/vim/patches/6.2.191
Patch192: ftp://ftp.vim.org/pub/vim/patches/6.2.192
Patch193: ftp://ftp.vim.org/pub/vim/patches/6.2.193
Patch194: ftp://ftp.vim.org/pub/vim/patches/6.2.194
Patch195: ftp://ftp.vim.org/pub/vim/patches/6.2.195
Patch196: ftp://ftp.vim.org/pub/vim/patches/6.2.196
Patch197: ftp://ftp.vim.org/pub/vim/patches/6.2.197
Patch198: ftp://ftp.vim.org/pub/vim/patches/6.2.198
Patch199: ftp://ftp.vim.org/pub/vim/patches/6.2.199
Patch200: ftp://ftp.vim.org/pub/vim/patches/6.2.200
Patch201: ftp://ftp.vim.org/pub/vim/patches/6.2.201
Patch202: ftp://ftp.vim.org/pub/vim/patches/6.2.202
Patch203: ftp://ftp.vim.org/pub/vim/patches/6.2.203
Patch204: ftp://ftp.vim.org/pub/vim/patches/6.2.204
Patch205: ftp://ftp.vim.org/pub/vim/patches/6.2.205
Patch206: ftp://ftp.vim.org/pub/vim/patches/6.2.206
Patch207: ftp://ftp.vim.org/pub/vim/patches/6.2.207
Patch208: ftp://ftp.vim.org/pub/vim/patches/6.2.208
Patch209: ftp://ftp.vim.org/pub/vim/patches/6.2.209
Patch210: ftp://ftp.vim.org/pub/vim/patches/6.2.210
Patch211: ftp://ftp.vim.org/pub/vim/patches/6.2.211
Patch212: ftp://ftp.vim.org/pub/vim/patches/6.2.212
Patch213: ftp://ftp.vim.org/pub/vim/patches/6.2.213
Patch214: ftp://ftp.vim.org/pub/vim/patches/6.2.214
Patch215: ftp://ftp.vim.org/pub/vim/patches/6.2.215
Patch216: ftp://ftp.vim.org/pub/vim/patches/6.2.216
Patch217: ftp://ftp.vim.org/pub/vim/patches/6.2.217
Patch218: ftp://ftp.vim.org/pub/vim/patches/6.2.218
Patch219: ftp://ftp.vim.org/pub/vim/patches/6.2.219
Patch220: ftp://ftp.vim.org/pub/vim/patches/6.2.220
Patch221: ftp://ftp.vim.org/pub/vim/patches/6.2.221
Patch222: ftp://ftp.vim.org/pub/vim/patches/6.2.222
Patch223: ftp://ftp.vim.org/pub/vim/patches/6.2.223
Patch224: ftp://ftp.vim.org/pub/vim/patches/6.2.224
Patch225: ftp://ftp.vim.org/pub/vim/patches/6.2.225
Patch226: ftp://ftp.vim.org/pub/vim/patches/6.2.226
Patch227: ftp://ftp.vim.org/pub/vim/patches/6.2.227
Patch228: ftp://ftp.vim.org/pub/vim/patches/6.2.228
Patch229: ftp://ftp.vim.org/pub/vim/patches/6.2.229
Patch230: ftp://ftp.vim.org/pub/vim/patches/6.2.230
Patch231: ftp://ftp.vim.org/pub/vim/patches/6.2.231
Patch232: ftp://ftp.vim.org/pub/vim/patches/6.2.232
Patch233: ftp://ftp.vim.org/pub/vim/patches/6.2.233
Patch234: ftp://ftp.vim.org/pub/vim/patches/6.2.234
Patch235: ftp://ftp.vim.org/pub/vim/patches/6.2.235
Patch236: ftp://ftp.vim.org/pub/vim/patches/6.2.236
Patch237: ftp://ftp.vim.org/pub/vim/patches/6.2.237
Patch238: ftp://ftp.vim.org/pub/vim/patches/6.2.238
Patch239: ftp://ftp.vim.org/pub/vim/patches/6.2.239
Patch240: ftp://ftp.vim.org/pub/vim/patches/6.2.240
Patch241: ftp://ftp.vim.org/pub/vim/patches/6.2.241
Patch242: ftp://ftp.vim.org/pub/vim/patches/6.2.242
Patch243: ftp://ftp.vim.org/pub/vim/patches/6.2.243
Patch244: ftp://ftp.vim.org/pub/vim/patches/6.2.244
Patch245: ftp://ftp.vim.org/pub/vim/patches/6.2.245
Patch246: ftp://ftp.vim.org/pub/vim/patches/6.2.246
Patch247: ftp://ftp.vim.org/pub/vim/patches/6.2.247
Patch248: ftp://ftp.vim.org/pub/vim/patches/6.2.248
Patch249: ftp://ftp.vim.org/pub/vim/patches/6.2.249
Patch250: ftp://ftp.vim.org/pub/vim/patches/6.2.250
Patch251: ftp://ftp.vim.org/pub/vim/patches/6.2.251
Patch252: ftp://ftp.vim.org/pub/vim/patches/6.2.252
Patch253: ftp://ftp.vim.org/pub/vim/patches/6.2.253
Patch254: ftp://ftp.vim.org/pub/vim/patches/6.2.254
Patch255: ftp://ftp.vim.org/pub/vim/patches/6.2.255
Patch256: ftp://ftp.vim.org/pub/vim/patches/6.2.256
Patch257: ftp://ftp.vim.org/pub/vim/patches/6.2.257
Patch258: ftp://ftp.vim.org/pub/vim/patches/6.2.258
Patch259: ftp://ftp.vim.org/pub/vim/patches/6.2.259
Patch260: ftp://ftp.vim.org/pub/vim/patches/6.2.260
Patch261: ftp://ftp.vim.org/pub/vim/patches/6.2.261
Patch262: ftp://ftp.vim.org/pub/vim/patches/6.2.262
Patch263: ftp://ftp.vim.org/pub/vim/patches/6.2.263
Patch264: ftp://ftp.vim.org/pub/vim/patches/6.2.264
Patch265: ftp://ftp.vim.org/pub/vim/patches/6.2.265
Patch266: ftp://ftp.vim.org/pub/vim/patches/6.2.266
Patch267: ftp://ftp.vim.org/pub/vim/patches/6.2.267
Patch268: ftp://ftp.vim.org/pub/vim/patches/6.2.268
Patch269: ftp://ftp.vim.org/pub/vim/patches/6.2.269
Patch270: ftp://ftp.vim.org/pub/vim/patches/6.2.270
Patch271: ftp://ftp.vim.org/pub/vim/patches/6.2.271
Patch272: ftp://ftp.vim.org/pub/vim/patches/6.2.272
Patch273: ftp://ftp.vim.org/pub/vim/patches/6.2.273
Patch274: ftp://ftp.vim.org/pub/vim/patches/6.2.274
Patch275: ftp://ftp.vim.org/pub/vim/patches/6.2.275
Patch276: ftp://ftp.vim.org/pub/vim/patches/6.2.276
Patch277: ftp://ftp.vim.org/pub/vim/patches/6.2.277
Patch278: ftp://ftp.vim.org/pub/vim/patches/6.2.278
Patch279: ftp://ftp.vim.org/pub/vim/patches/6.2.279
Patch280: ftp://ftp.vim.org/pub/vim/patches/6.2.280
Patch281: ftp://ftp.vim.org/pub/vim/patches/6.2.281
Patch282: ftp://ftp.vim.org/pub/vim/patches/6.2.282
Patch283: ftp://ftp.vim.org/pub/vim/patches/6.2.283
Patch284: ftp://ftp.vim.org/pub/vim/patches/6.2.284
Patch285: ftp://ftp.vim.org/pub/vim/patches/6.2.285
Patch286: ftp://ftp.vim.org/pub/vim/patches/6.2.286
Patch287: ftp://ftp.vim.org/pub/vim/patches/6.2.287
Patch288: ftp://ftp.vim.org/pub/vim/patches/6.2.288
Patch289: ftp://ftp.vim.org/pub/vim/patches/6.2.289
Patch290: ftp://ftp.vim.org/pub/vim/patches/6.2.290
Patch291: ftp://ftp.vim.org/pub/vim/patches/6.2.291
Patch292: ftp://ftp.vim.org/pub/vim/patches/6.2.292
Patch293: ftp://ftp.vim.org/pub/vim/patches/6.2.293
Patch294: ftp://ftp.vim.org/pub/vim/patches/6.2.294
Patch295: ftp://ftp.vim.org/pub/vim/patches/6.2.295
Patch296: ftp://ftp.vim.org/pub/vim/patches/6.2.296
Patch297: ftp://ftp.vim.org/pub/vim/patches/6.2.297
Patch298: ftp://ftp.vim.org/pub/vim/patches/6.2.298
Patch299: ftp://ftp.vim.org/pub/vim/patches/6.2.299
Patch300: ftp://ftp.vim.org/pub/vim/patches/6.2.300
Patch301: ftp://ftp.vim.org/pub/vim/patches/6.2.301
Patch302: ftp://ftp.vim.org/pub/vim/patches/6.2.302
Patch303: ftp://ftp.vim.org/pub/vim/patches/6.2.303
Patch304: ftp://ftp.vim.org/pub/vim/patches/6.2.304
Patch305: ftp://ftp.vim.org/pub/vim/patches/6.2.305
Patch306: ftp://ftp.vim.org/pub/vim/patches/6.2.306
Patch307: ftp://ftp.vim.org/pub/vim/patches/6.2.307
Patch308: ftp://ftp.vim.org/pub/vim/patches/6.2.308
Patch309: ftp://ftp.vim.org/pub/vim/patches/6.2.309
Patch310: ftp://ftp.vim.org/pub/vim/patches/6.2.310
Patch311: ftp://ftp.vim.org/pub/vim/patches/6.2.311
Patch312: ftp://ftp.vim.org/pub/vim/patches/6.2.312
Patch313: ftp://ftp.vim.org/pub/vim/patches/6.2.313
Patch314: ftp://ftp.vim.org/pub/vim/patches/6.2.314
Patch315: ftp://ftp.vim.org/pub/vim/patches/6.2.315
Patch316: ftp://ftp.vim.org/pub/vim/patches/6.2.316
Patch317: ftp://ftp.vim.org/pub/vim/patches/6.2.317
Patch318: ftp://ftp.vim.org/pub/vim/patches/6.2.318
Patch319: ftp://ftp.vim.org/pub/vim/patches/6.2.319
Patch320: ftp://ftp.vim.org/pub/vim/patches/6.2.320
Patch321: ftp://ftp.vim.org/pub/vim/patches/6.2.321
Patch322: ftp://ftp.vim.org/pub/vim/patches/6.2.322
Patch323: ftp://ftp.vim.org/pub/vim/patches/6.2.323
Patch324: ftp://ftp.vim.org/pub/vim/patches/6.2.324
Patch325: ftp://ftp.vim.org/pub/vim/patches/6.2.325
Patch326: ftp://ftp.vim.org/pub/vim/patches/6.2.326
Patch327: ftp://ftp.vim.org/pub/vim/patches/6.2.327

Patch3001: vim-6.1-syntax.patch
Patch3002: vim-6.2-rh1.patch
Patch3003: vim-6.1-rh2.patch
Patch3004: vim-6.1-rh3.patch
Patch3005: vim-6.2-rclocation.patch
Patch3006: vim-6.2-rh4.patch
Patch3007: vim-6.2-rh5.patch
Patch3008: vim-6.2-perlthread.patch
Patch3009: vim-6.2-shsyntax.patch

Patch3100: vim-6.2-runtimeupdate.patch

Patch3101: vim-selinux.patch

Buildroot: %{_tmppath}/%{name}-%{version}-root
Buildrequires: python-devel perl libtermcap-devel gettext
%if "%{withruby}" == "1"
Buildrequires: ruby ruby-devel
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
# %patch2001 -p1 -b .vim
# fix rogue dependencies from sample code
chmod -x runtime/tools/mve.awk
%patch2002 -p1 -b .paths
find . -name \*.paths | xargs rm -f
%patch2003 -p1 -b .fixkeys
%patch2004 -p1 -b .highlite
%patch2005 -p1 -b .crv
%patch2010 -p1 -b .xxdloc
perl -pi -e "s,bin/nawk,bin/awk,g" runtime/tools/mve.awk

# Base patches...
# for i in `seq 1 14`; do printf "%%patch%03d -p0 -b .pl%03d\n" $i $i; done
%patch001 -p0
%patch002 -p0
%patch003 -p0
%patch004 -p0
%patch005 -p0
%patch006 -p0
%patch007 -p0
%patch008 -p0
# %patch009 -p0 # Win32
%patch010 -p0
%patch011 -p0
%patch012 -p0
# %patch013 -p0 # Win32
%patch014 -p0
%patch015 -p0
%patch016 -p0
%patch017 -p0
%patch018 -p0
%patch019 -p0
%patch020 -p0
%patch021 -p0
# %patch022 -p0 # Win32
# %patch023 -p0 # Win32
# %patch024 -p0 # Win32
%patch025 -p0
%patch026 -p0
%patch027 -p0
%patch028 -p0
%patch029 -p0
%patch030 -p0
%patch031 -p0
%patch032 -p0
# %patch033 -p0 # Mac
%patch034 -p0
%patch035 -p0
# %patch036 -p0 # Mac
%patch037 -p0
# %patch038 -p0 -b .pl038 # Win32
# %patch039 -p0 -b .pl039 # Win32
# %patch040 -p0 -b .pl040 # Mac
# %patch041 -p0 -b .pl041 # Win32
# %patch042 -p0 -b .pl042 # Cygwin
%patch043 -p0
%patch044 -p0
%patch045 -p0
%patch046 -p0
# %patch047 -p0 # Win32
%patch048 -p0
%patch049 -p0
%patch050 -p0
%patch051 -p0
%patch052 -p0
%patch053 -p0
%patch054 -p0
%patch055 -p0
# %patch056 -p0 # Win32
# %patch057 -p0 # Mac
%patch058 -p0
%patch059 -p0
# %patch060 -p0 # Win32
%patch061 -p0
%patch062 -p0
%patch063 -p0
%patch064 -p0
%patch065 -p0
# %patch066 -p0
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
# %patch090 -p0 # Win32
%patch091 -p0
%patch092 -p0
%patch093 -p0
%patch094 -p0
%patch095 -p0
# %patch096 -p0 # Win32
%patch097 -p0
%patch098 -p0
%patch099 -p0
%patch100 -p0
%patch101 -p0
%patch102 -p0
# %patch103 -p0 # Mac
%patch104 -p0
%patch105 -p0
%patch106 -p0
# %patch107 -p0 # Win32
%patch108 -p0
%patch109 -p0
%patch110 -p0
%patch111 -p0
%patch112 -p0
%patch113 -p0
%patch114 -p0
# %patch115 -p0 # Amiga
# %patch116 -p0 # Win
%patch117 -p0
# %patch118 -p0 # Mac
# %patch119 -p0 # Win
%patch120 -p0
# %patch121 -p0 # Mac
# %patch122 -p0 # Mac
# %patch123 -p0 # Mac
# %patch124 -p0 # Mac
# %patch125 -p0 # Win32
# %patch126 -p0 # Win32
#%patch127 -p0 # Win32
# %patch128 -p0 # Mac
%patch129 -p0
# %patch130 -p0 # Win32
# %patch131 -p0 # Win32
# %patch132 -p0 # Win32
%patch133 -p0
# %patch134 -p0 # Win32
%patch135 -p0
%patch136 -p0
%patch137 -p0
# %patch138 -p0 # VMS
%patch139 -p0
# %patch140 -p0 # Mac
# %patch141 -p0 # Mac
# %patch142 -p0 # Mac
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
#%patch153 -p0 # Win32
%patch154 -p0
#%patch155 -p0 # Win32
#%patch156 -p0 # Win32
%patch157 -p0
%patch158 -p0
%patch159 -p0
%patch160 -p0
#%patch161 -p0 # VMS
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
#%patch173 -p0 # Win32
%patch174 -p0
%patch175 -p0
%patch176 -p0
#%patch177 -p0 # VisVim
%patch178 -p0
%patch179 -p0
#%patch180 -p0 # Win32
%patch181 -p0
%patch182 -p0
%patch183 -p0
%patch184 -p0
%patch185 -p0
%patch186 -p0
%patch187 -p0
#%patch188 -p0 # Win32
%patch189 -p0
%patch190 -p0
%patch191 -p0
%patch192 -p0
%patch193 -p0
#%patch194 -p0 # Netbeans stuff doesn't apply
%patch195 -p0
%patch196 -p0
%patch197 -p0
%patch198 -p0
#%patch199 -p0 # NetBeans
%patch200 -p0
%patch201 -p0
%patch202 -p0
%patch203 -p0
%patch204 -p0
#%patch205 -p0 # Win32
%patch206 -p0
%patch207 -p0
%patch208 -p0
%patch209 -p0
#%patch210 -p0 # MacOSX
# Modified patch! Mac and W48 stuff deleted:
%patch211 -p0
#%patch212 # NetBeans
%patch213 -p0
#%patch214 -p0 # w48
#%patch215 -p0 # NetBeans
%patch216 -p0
%patch217 -p0
%patch218 -p0
%patch219 -p0
%patch220 -p0
%patch221 -p0
%patch222 -p0
%patch223 -p0
#%patch224 -p0 # Mac
%patch225 -p0
#%patch226 -p0 # Cygnus/Ming/MVC
#%patch227 -p0 # Cygnus/Ming/bc3/bc5
%patch228 -p0
%patch229 -p0
#%patch230 -p0 # Win32
%patch231 -p0
%patch232 -p0
#%patch233 -p0 # Mac
%patch234 -p0
#%patch235 -p0 # Win32
#%patch236 -p0 # NetBeans
%patch237 -p0
%patch238 -p0
%patch239 -p0
%patch240 -p0
%patch241 -p0
%patch242 -p0
#%patch243 -p0 # Mac
%patch244 -p0
%patch245 -p0
#%patch246 -p # Mac
%patch247 -p0
%patch248 -p0
%patch249 -p0
%patch250 -p0
%patch251 -p0
#%patch252 -p0 # Mac
%patch253 -p0
%patch254 -p0
%patch255 -p0
#%patch256 -p0 # Mac
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
#%patch267 -p0 # Win32
%patch268 -p0
%patch269 -p0
%patch270 -p0
#%patch271 -p0 # NetBeans
%patch272 -p0
%patch273 -p0
%patch274 -p0
#%patch275 -p0 # Win32
%patch276 -p0
%patch277 -p0
%patch278 -p0
%patch279 -p0
%patch280 -p0
%patch281 -p0
%patch282 -p0
%patch283 -p0
%patch284 -p0
%patch285 -p0
%patch286 -p0
%patch287 -p0
#%patch288 -p0 # Mac
%patch289 -p0
#%patch290 -p0 # Mac
#%patch291 -p # Mac0
%patch292 -p0
%patch293 -p0
#%patch294 -p0 # Mac
%patch295 -p0
#%patch296 -p0 # MSDOS, RiscOS, Amiga
%patch297 -p0
%patch298 -p0
%patch299 -p0
%patch300 -p0
%patch301 -p0
%patch302 -p0
%patch303 -p0
#%patch304 -p0 # Mac
%patch305 -p0
#%patch306 -p0 # Win32
%patch307 -p0
%patch308 -p0
%patch309 -p0
%patch310 -p0
%patch311 -p0
%patch312 -p0
%patch313 -p0
%patch314 -p0
%patch315 -p0
%patch316 -p0
%patch317 -p0
%patch318 -p0
#%patch319 -p0 # Win32
%patch320 -p0
%patch321 -p0
%patch322 -p0
#%patch323 -p0 # Win32
#%patch324 -p0 # Win32
%patch325 -p0
%patch326 -p0
%patch327 -p0

#%patch3000 -p1 -b .kh1
%patch3001 -p1 -b .syntx
%patch3002 -p1 -b .rh1
%patch3003 -p1 -b .rh2
%patch3004 -p1 -b .rh3
%patch3005 -p1 -b .rcloc
%patch3006 -p1 -b .rh4
%patch3007 -p1 -b .rh5
%patch3008 -p1 -b .perlthread
%patch3009 -p1 -b .stx

%patch3100 -p1

%if %{WITH_SELINUX}
%patch3101 -p1 -b .selinux
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
install -s -m755 gvim $RPM_BUILD_ROOT/usr/X11R6/bin
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
%endif

%changelog
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
