%define desktop_file 1
%if %{desktop_file}
%define desktop_file_utils_version 0.2.93
%endif
# Set this to 0 if you don't want to build gvim:
%define withgui 1

Summary: The VIM editor.
Name: vim
Version: 6.1
%define vimversion vim61
Release: 29
License: freeware
Group: Applications/Editors
Source0: ftp://ftp.vim.org/pub/vim/unix/vim-%{version}.tar.bz2
Source1: ftp://ftp.vim.org/pub/vim/unreleased/extra/vim-%{version}-lang.tar.bz2
Source2: gvim.desktop
Source3: vimrc
Source4: ftp://ftp.vim.org/pub/vim/patches/README.patches
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
# Patch 2 is Windows only
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
# Patch 16 is Windows only
Patch1017: ftp://ftp.vim.org/pub/vim/patches/6.1.017
Patch1018: ftp://ftp.vim.org/pub/vim/patches/6.1.018
# Patch 19 is Windows only
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
# Patch 35 is Windows only
Patch1036: ftp://ftp.vim.org/pub/vim/patches/6.1.036
Patch1037: ftp://ftp.vim.org/pub/vim/patches/6.1.037
Patch1038: ftp://ftp.vim.org/pub/vim/patches/6.1.038
Patch1039: ftp://ftp.vim.org/pub/vim/patches/6.1.039
Patch1040: ftp://ftp.vim.org/pub/vim/patches/6.1.040
Patch1041: ftp://ftp.vim.org/pub/vim/patches/6.1.041
Patch1042: ftp://ftp.vim.org/pub/vim/patches/6.1.042
Patch1043: ftp://ftp.vim.org/pub/vim/patches/6.1.043
# Patch 44 is Windows only
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
# Patch 88 is Windows only
Patch1089: ftp://ftp.vim.org/pub/vim/patches/6.1.089
Patch1090: ftp://ftp.vim.org/pub/vim/patches/6.1.090
Patch1091: ftp://ftp.vim.org/pub/vim/patches/6.1.091
Patch1092: ftp://ftp.vim.org/pub/vim/patches/6.1.092
# Patch 93 is Windows  and Mac only
Patch1094: ftp://ftp.vim.org/pub/vim/patches/6.1.094
Patch1095: ftp://ftp.vim.org/pub/vim/patches/6.1.095
Patch1096: ftp://ftp.vim.org/pub/vim/patches/6.1.096
Patch1097: ftp://ftp.vim.org/pub/vim/patches/6.1.097
Patch1098: ftp://ftp.vim.org/pub/vim/patches/6.1.098
Patch1099: ftp://ftp.vim.org/pub/vim/patches/6.1.099
# Patch 100 is Windows only
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
Patch1166: ftp://ftp.vim.org/pub/vim/patches/6.1.166
Patch1167: ftp://ftp.vim.org/pub/vim/patches/6.1.167
Patch1168: ftp://ftp.vim.org/pub/vim/patches/6.1.168
Patch1169: ftp://ftp.vim.org/pub/vim/patches/6.1.169
Patch1170: ftp://ftp.vim.org/pub/vim/patches/6.1.170
Patch1171: ftp://ftp.vim.org/pub/vim/patches/6.1.171
Patch1172: ftp://ftp.vim.org/pub/vim/patches/6.1.172
# Modified patch, removed VisVim part:
Patch1173: ftp://ftp.vim.org/pub/vim/patches/6.1.173
Patch1174: ftp://ftp.vim.org/pub/vim/patches/6.1.174
Patch1175: ftp://ftp.vim.org/pub/vim/patches/6.1.175
Patch1176: ftp://ftp.vim.org/pub/vim/patches/6.1.176
Patch1177: ftp://ftp.vim.org/pub/vim/patches/6.1.177
Patch1178: ftp://ftp.vim.org/pub/vim/patches/6.1.178
Patch1179: ftp://ftp.vim.org/pub/vim/patches/6.1.179
Patch1180: ftp://ftp.vim.org/pub/vim/patches/6.1.180
Patch1181: ftp://ftp.vim.org/pub/vim/patches/6.1.181
Patch1182: ftp://ftp.vim.org/pub/vim/patches/6.1.182
Patch1183: ftp://ftp.vim.org/pub/vim/patches/6.1.183
Patch1184: ftp://ftp.vim.org/pub/vim/patches/6.1.184
Patch1185: ftp://ftp.vim.org/pub/vim/patches/6.1.185
Patch1186: ftp://ftp.vim.org/pub/vim/patches/6.1.186
Patch1187: ftp://ftp.vim.org/pub/vim/patches/6.1.187
Patch1188: ftp://ftp.vim.org/pub/vim/patches/6.1.188
Patch1189: ftp://ftp.vim.org/pub/vim/patches/6.1.189
Patch1190: ftp://ftp.vim.org/pub/vim/patches/6.1.190
Patch1191: ftp://ftp.vim.org/pub/vim/patches/6.1.191
Patch1192: ftp://ftp.vim.org/pub/vim/patches/6.1.192
Patch1193: ftp://ftp.vim.org/pub/vim/patches/6.1.193
Patch1194: ftp://ftp.vim.org/pub/vim/patches/6.1.194
Patch1195: ftp://ftp.vim.org/pub/vim/patches/6.1.195
Patch1196: ftp://ftp.vim.org/pub/vim/patches/6.1.196
Patch1197: ftp://ftp.vim.org/pub/vim/patches/6.1.197
Patch1198: ftp://ftp.vim.org/pub/vim/patches/6.1.198
Patch1199: ftp://ftp.vim.org/pub/vim/patches/6.1.199
Patch1200: ftp://ftp.vim.org/pub/vim/patches/6.1.200
Patch1201: ftp://ftp.vim.org/pub/vim/patches/6.1.201
Patch1202: ftp://ftp.vim.org/pub/vim/patches/6.1.202
Patch1203: ftp://ftp.vim.org/pub/vim/patches/6.1.203
Patch1204: ftp://ftp.vim.org/pub/vim/patches/6.1.204
Patch1205: ftp://ftp.vim.org/pub/vim/patches/6.1.205
Patch1206: ftp://ftp.vim.org/pub/vim/patches/6.1.206
Patch1207: ftp://ftp.vim.org/pub/vim/patches/6.1.207
Patch1208: ftp://ftp.vim.org/pub/vim/patches/6.1.208
Patch1209: ftp://ftp.vim.org/pub/vim/patches/6.1.209
Patch1210: ftp://ftp.vim.org/pub/vim/patches/6.1.210
Patch1211: ftp://ftp.vim.org/pub/vim/patches/6.1.211
Patch1212: ftp://ftp.vim.org/pub/vim/patches/6.1.212
Patch1213: ftp://ftp.vim.org/pub/vim/patches/6.1.213
Patch1214: ftp://ftp.vim.org/pub/vim/patches/6.1.214
Patch1215: ftp://ftp.vim.org/pub/vim/patches/6.1.215
Patch1216: ftp://ftp.vim.org/pub/vim/patches/6.1.216
Patch1217: ftp://ftp.vim.org/pub/vim/patches/6.1.217
Patch1218: ftp://ftp.vim.org/pub/vim/patches/6.1.218
Patch1219: ftp://ftp.vim.org/pub/vim/patches/6.1.219
Patch1220: ftp://ftp.vim.org/pub/vim/patches/6.1.220
# modified patch, removed other OS stuff:
Patch1221: ftp://ftp.vim.org/pub/vim/patches/6.1.221
Patch1222: ftp://ftp.vim.org/pub/vim/patches/6.1.222
# modified patch, removed other OS stuff:
Patch1223: ftp://ftp.vim.org/pub/vim/patches/6.1.223
Patch1224: ftp://ftp.vim.org/pub/vim/patches/6.1.224
Patch1225: ftp://ftp.vim.org/pub/vim/patches/6.1.225
Patch1226: ftp://ftp.vim.org/pub/vim/patches/6.1.226
Patch1227: ftp://ftp.vim.org/pub/vim/patches/6.1.227
# Win32 only:
#Patch1228: ftp://ftp.vim.org/pub/vim/patches/6.1.228
#Patch1229: ftp://ftp.vim.org/pub/vim/patches/6.1.229
#Patch1230: ftp://ftp.vim.org/pub/vim/patches/6.1.230
Patch1231: ftp://ftp.vim.org/pub/vim/patches/6.1.231
Patch1232: ftp://ftp.vim.org/pub/vim/patches/6.1.232
Patch1233: ftp://ftp.vim.org/pub/vim/patches/6.1.233
Patch1234: ftp://ftp.vim.org/pub/vim/patches/6.1.234
Patch1235: ftp://ftp.vim.org/pub/vim/patches/6.1.235
Patch1236: ftp://ftp.vim.org/pub/vim/patches/6.1.236
Patch1237: ftp://ftp.vim.org/pub/vim/patches/6.1.237
# Modifed patch, removed w32_gui stuff:
Patch1238: ftp://ftp.vim.org/pub/vim/patches/6.1.238
Patch1239: ftp://ftp.vim.org/pub/vim/patches/6.1.239
# Win32 only:
#Patch1240: ftp://ftp.vim.org/pub/vim/patches/6.1.240
Patch1241: ftp://ftp.vim.org/pub/vim/patches/6.1.241
Patch1242: ftp://ftp.vim.org/pub/vim/patches/6.1.242
# Win32 only:
#Patch1243: ftp://ftp.vim.org/pub/vim/patches/6.1.243
Patch1244: ftp://ftp.vim.org/pub/vim/patches/6.1.244
Patch1245: ftp://ftp.vim.org/pub/vim/patches/6.1.245
Patch1246: ftp://ftp.vim.org/pub/vim/patches/6.1.246
Patch1247: ftp://ftp.vim.org/pub/vim/patches/6.1.247
Patch1248: ftp://ftp.vim.org/pub/vim/patches/6.1.248
Patch1249: ftp://ftp.vim.org/pub/vim/patches/6.1.249
Patch1250: ftp://ftp.vim.org/pub/vim/patches/6.1.250
Patch1251: ftp://ftp.vim.org/pub/vim/patches/6.1.251
Patch1252: ftp://ftp.vim.org/pub/vim/patches/6.1.252
# Win32 only:
#Patch1253: ftp://ftp.vim.org/pub/vim/patches/6.1.253
Patch1254: ftp://ftp.vim.org/pub/vim/patches/6.1.254
Patch1255: ftp://ftp.vim.org/pub/vim/patches/6.1.255
Patch1256: ftp://ftp.vim.org/pub/vim/patches/6.1.256
Patch1257: ftp://ftp.vim.org/pub/vim/patches/6.1.257
Patch1258: ftp://ftp.vim.org/pub/vim/patches/6.1.258
# Mac only:
#Patch1259: ftp://ftp.vim.org/pub/vim/patches/6.1.259
Patch1260: ftp://ftp.vim.org/pub/vim/patches/6.1.260
Patch1261: ftp://ftp.vim.org/pub/vim/patches/6.1.261
Patch1262: ftp://ftp.vim.org/pub/vim/patches/6.1.262
Patch1263: ftp://ftp.vim.org/pub/vim/patches/6.1.263
Patch1264: ftp://ftp.vim.org/pub/vim/patches/6.1.264
Patch1265: ftp://ftp.vim.org/pub/vim/patches/6.1.265
Patch1266: ftp://ftp.vim.org/pub/vim/patches/6.1.266
Patch1267: ftp://ftp.vim.org/pub/vim/patches/6.1.267
Patch1268: ftp://ftp.vim.org/pub/vim/patches/6.1.268
Patch1269: ftp://ftp.vim.org/pub/vim/patches/6.1.269
Patch1270: ftp://ftp.vim.org/pub/vim/patches/6.1.270
Patch1271: ftp://ftp.vim.org/pub/vim/patches/6.1.271
Patch1272: ftp://ftp.vim.org/pub/vim/patches/6.1.272
Patch1273: ftp://ftp.vim.org/pub/vim/patches/6.1.273
Patch1274: ftp://ftp.vim.org/pub/vim/patches/6.1.274
Patch1275: ftp://ftp.vim.org/pub/vim/patches/6.1.275
Patch1276: ftp://ftp.vim.org/pub/vim/patches/6.1.276
Patch1277: ftp://ftp.vim.org/pub/vim/patches/6.1.277
Patch1278: ftp://ftp.vim.org/pub/vim/patches/6.1.278
Patch1279: ftp://ftp.vim.org/pub/vim/patches/6.1.279
Patch1280: ftp://ftp.vim.org/pub/vim/patches/6.1.280
Patch1281: ftp://ftp.vim.org/pub/vim/patches/6.1.281
Patch1282: ftp://ftp.vim.org/pub/vim/patches/6.1.282
Patch1283: ftp://ftp.vim.org/pub/vim/patches/6.1.283
Patch1284: ftp://ftp.vim.org/pub/vim/patches/6.1.284
Patch1285: ftp://ftp.vim.org/pub/vim/patches/6.1.285
Patch1286: ftp://ftp.vim.org/pub/vim/patches/6.1.286
Patch1287: ftp://ftp.vim.org/pub/vim/patches/6.1.287
Patch1288: ftp://ftp.vim.org/pub/vim/patches/6.1.288
Patch1289: ftp://ftp.vim.org/pub/vim/patches/6.1.289
# Patches 290-292 are Win32 only
Patch1293: ftp://ftp.vim.org/pub/vim/patches/6.1.293
Patch1294: ftp://ftp.vim.org/pub/vim/patches/6.1.294
Patch1295: ftp://ftp.vim.org/pub/vim/patches/6.1.295
# Patch 296 is Win32 only
Patch1297: ftp://ftp.vim.org/pub/vim/patches/6.1.297
Patch1298: ftp://ftp.vim.org/pub/vim/patches/6.1.298
Patch1299: ftp://ftp.vim.org/pub/vim/patches/6.1.299
# Patch 300 is Win32 only
Patch1301: ftp://ftp.vim.org/pub/vim/patches/6.1.301
Patch1302: ftp://ftp.vim.org/pub/vim/patches/6.1.302
# Patches 303-304 are win32 only
Patch1305: ftp://ftp.vim.org/pub/vim/patches/6.1.305
Patch1306: ftp://ftp.vim.org/pub/vim/patches/6.1.306
Patch1307: ftp://ftp.vim.org/pub/vim/patches/6.1.307
Patch1308: ftp://ftp.vim.org/pub/vim/patches/6.1.308
Patch1309: ftp://ftp.vim.org/pub/vim/patches/6.1.309
Patch1310: ftp://ftp.vim.org/pub/vim/patches/6.1.310
# patch 311 is VMS only
Patch1312: ftp://ftp.vim.org/pub/vim/patches/6.1.312
Patch1313: ftp://ftp.vim.org/pub/vim/patches/6.1.313
Patch1314: ftp://ftp.vim.org/pub/vim/patches/6.1.314
# modified patch, removed other OS stuff:
Patch1315: ftp://ftp.vim.org/pub/vim/patches/6.1.315
Patch1316: ftp://ftp.vim.org/pub/vim/patches/6.1.316
Patch1317: ftp://ftp.vim.org/pub/vim/patches/6.1.317
Patch1318: ftp://ftp.vim.org/pub/vim/patches/6.1.318
Patch1319: ftp://ftp.vim.org/pub/vim/patches/6.1.319
Patch1320: ftp://ftp.vim.org/pub/vim/patches/6.1.320

Patch3000: vim-6.1-kh1.patch
Patch3001: vim-6.1-syntax.patch
Patch3002: vim-6.1-rh1.patch
Patch3003: vim-6.1-rh2.patch
Patch3004: vim-6.1-rh3.patch
Buildroot: %{_tmppath}/%{name}-%{version}-root
Buildrequires: python-devel perl
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
# for i in `seq 312 320`; do echo "%patch`expr 1000 + $i` -p0 -b .pl`expr 1000 + $i | sed -e 's,^.,,'`"; done
%patch1001 -p0
%patch1003 -p0
%patch1004 -p0
%patch1005 -p0
%patch1006 -p0
%patch1007 -p0
%patch1008 -p0
%patch1009 -p0
%patch1010 -p0
%patch1011 -p0
%patch1012 -p0
%patch1013 -p0
%patch1014 -p0
%patch1015 -p0
%patch1017 -p0
%patch1018 -p0
%patch1020 -p0
%patch1021 -p0
%patch1022 -p0
%patch1024 -p0
%patch1025 -p0
%patch1026 -p0
%patch1027 -p0
%patch1028 -p0
%patch1029 -p0
%patch1030 -p0
%patch1031 -p0
%patch1032 -p0
%patch1033 -p0
%patch1034 -p0
%patch1036 -p0
%patch1037 -p0
%patch1038 -p0
%patch1039 -p0
%patch1040 -p0
%patch1041 -p0
%patch1042 -p0
%patch1043 -p0
%patch1045 -p0
%patch1046 -p0
%patch1047 -p0
%patch1048 -p0
%patch1049 -p0
%patch1051 -p0
%patch1052 -p0
%patch1053 -p0
%patch1054 -p0
%patch1055 -p0
%patch1056 -p0
%patch1057 -p0
%patch1058 -p0
%patch1059 -p0
%patch1060 -p0
%patch1061 -p0
%patch1062 -p0
%patch1063 -p0
%patch1064 -p0
%patch1065 -p0
%patch1066 -p0
%patch1067 -p0
%patch1068 -p0
%patch1069 -p0
%patch1070 -p0
%patch1071 -p0
%patch1072 -p0
%patch1074 -p0
%patch1075 -p0
%patch1077 -p0
%patch1078 -p0
%patch1079 -p0
%patch1080 -p0
%patch1081 -p0
%patch1082 -p0
%patch1083 -p0
#%patch1084 -p0
%patch1085 -p0
%patch1086 -p0
%patch1087 -p0
%patch1089 -p0
%patch1090 -p0
%patch1091 -p0
%patch1092 -p0
%patch1094 -p0
%patch1095 -p0
%patch1096 -p0
%patch1097 -p0
%patch1098 -p0
%patch1099 -p0
%patch1101 -p0
%patch1102 -p0
%patch1103 -p0
%patch1104 -p0
%patch1105 -p0
%patch1106 -p0
%patch1107 -p0
%patch1108 -p0
%patch1109 -p0
%patch1110 -p0
%patch1111 -p0
%patch1112 -p0
%patch1113 -p0
%patch1114 -p0
%patch1115 -p0
%patch1116 -p0
%patch1117 -p0
%patch1118 -p0
#%patch1119 -p0
%patch1120 -p0
%patch1121 -p0
%patch1122 -p0
%patch1123 -p0
%patch1124 -p0
%patch1125 -p0
%patch1126 -p0
%patch1127 -p0
%patch1128 -p0
%patch1129 -p0
%patch1130 -p0
%patch1131 -p0
%patch1132 -p0
%patch1133 -p0
%patch1134 -p0
%patch1135 -p0
%patch1136 -p0
%patch1137 -p0
%patch1138 -p0
%patch1139 -p0
%patch1140 -p0
%patch1141 -p0
%patch1142 -p0
%patch1143 -p0
%patch1144 -p0
%patch1145 -p0
%patch1146 -p0
%patch1150 -p0
%patch1151 -p0
%patch1152 -p0
%patch1153 -p0
%patch1157 -p0
%patch1158 -p0
%patch1159 -p0
%patch1160 -p0
%patch1161 -p0
%patch1162 -p0
%patch1163 -p0
%patch1164 -p0
%patch1165 -p0
%patch1166 -p0
%patch1167 -p0
%patch1168 -p0
%patch1169 -p0
%patch1170 -p0
%patch1171 -p0
%patch1172 -p0
%patch1173 -p0
%patch1174 -p0
%patch1175 -p0
%patch1176 -p0
%patch1177 -p0
%patch1178 -p0
%patch1179 -p0
%patch1180 -p0
%patch1181 -p0
%patch1182 -p0
%patch1183 -p0
# %patch1184 -p0 # Win32
%patch1185 -p0
%patch1186 -p0
%patch1187 -p0
%patch1188 -p0
%patch1189 -p0
# %patch1190 -p0 # VMS 
%patch1191 -p0
%patch1192 -p0
%patch1193 -p0
%patch1194 -p0
%patch1195 -p0
# %patch1196 -p0 # Patch doesn't apply, but seems to be Mac only
%patch1197 -p0
# %patch1198 -p0 # This one is Mac only
# %patch1199 -p0 # Win32
%patch1200 -p0
%patch1201 -p0
# %patch1202 -p0 # Win32
%patch1203 -p0
%patch1204 -p0
%patch1205 -p0
%patch1206 -p0
%patch1207 -p0
%patch1208 -p0
%patch1209 -p0
%patch1210 -p0
%patch1211 -p0
%patch1212 -p0
%patch1213 -p0
%patch1214 -p0
%patch1215 -p0
%patch1216 -p0
%patch1217 -p0
%patch1218 -p0
%patch1219 -p0
%patch1220 -p0
%patch1221 -p0
%patch1222 -p0
%patch1223 -p0
%patch1224 -p0
%patch1225 -p0
%patch1226 -p0
%patch1227 -p0
#%patch1228 -p0 # Win32
#%patch1229 -p0 # Win32
#%patch1230 -p0 # Win16
%patch1231 -p0
%patch1232 -p0
%patch1233 -p0
%patch1234 -p0
%patch1235 -p0
%patch1236 -p0
%patch1237 -p0
%patch1238 -p0
%patch1239 -p0
#%patch1240 -p0 # Win32
%patch1241 -p0
%patch1242 -p0
#%patch1243 -p0 # Win32
%patch1244 -p0
%patch1245 -p0
%patch1246 -p0
%patch1247 -p0
%patch1248 -p0
%patch1249 -p0
%patch1250 -p0
%patch1251 -p0
%patch1252 -p0
#%patch1253 -p0 # Win32
%patch1254 -p0
%patch1255 -p0
%patch1256 -p0
%patch1257 -p0
%patch1258 -p0
# %patch1259 -p0 # Mac
%patch1260 -p0
%patch1261 -p0
%patch1262 -p0
%patch1263 -p0
%patch1264 -p0
%patch1265 -p0
%patch1266 -p0
%patch1267 -p0
%patch1268 -p0
%patch1269 -p0
%patch1270 -p0
%patch1271 -p0
%patch1272 -p0
%patch1273 -p0
%patch1274 -p0
%patch1275 -p0
%patch1276 -p0
%patch1277 -p0
%patch1278 -p0
%patch1279 -p0
%patch1280 -p0
%patch1281 -p0
%patch1282 -p0
%patch1283 -p0
%patch1284 -p0
%patch1285 -p0
%patch1286 -p0
%patch1287 -p0
%patch1288 -p0
%patch1289 -p0
%patch1293 -p0
%patch1294 -p0
%patch1295 -p0
%patch1297 -p0
%patch1298 -p0
%patch1299 -p0
# patch 300 is win32 only
%patch1301 -p0
%patch1302 -p0
# patches 303-304 are win32 only
%patch1305 -p0
%patch1306 -p0
%patch1307 -p0
%patch1308 -p0
%patch1309 -p0
%patch1310 -p0
# patch 311 is VMS only
%patch1312 -p0 -b .pl312
%patch1313 -p0 -b .pl313
%patch1314 -p0 -b .pl314
%patch1315 -p0 -b .pl315
%patch1316 -p0 -b .pl316
%patch1317 -p0 -b .pl317
%patch1318 -p0 -b .pl318
%patch1319 -p0 -b .pl319
%patch1320 -p0 -b .pl320

%patch3000 -p1 -b .kh1
%patch3001 -p1 -b .syntx
%patch3002 -p1 -b .rh1
%patch3003 -p1 -b .rh2
%patch3004 -p1 -b .rh3

%build
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

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/bin
mkdir -p $RPM_BUILD_ROOT/usr/{bin,share/vim,X11R6/bin}

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
%if "%{withgui}" == "1"
  ln -sf gvim ./usr/X11R6/bin/gview
  ln -sf gvim ./usr/X11R6/bin/gex
%endif
  ln -sf gvim ./usr/X11R6/bin/evim
  perl -pi -e "s,$RPM_BUILD_ROOT,," .%{_mandir}/man1/vim.1 .%{_mandir}/man1/vimtutor.1
  rm -f .%{_mandir}/man1/rvim.1
  ln -sf vim.1.gz .%{_mandir}/man1/vi.1.gz
  ln -sf vim.1.gz .%{_mandir}/man1/rvi.1.gz
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
(cd ../runtime; rm -rf doc; ln -svf ../../vim/vim61/doc docs;)

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(-,root,root)
%doc README*.txt runtime/macros/README.txt runtime/tools/README.txt
%doc runtime/docs
/usr/share/vim
%config(noreplace) /usr/share/vim/vim61/macros/vimrc
%lang(af) /usr/share/vim/vim61/lang/af/*
%lang(cs) /usr/share/vim/vim61/lang/cs/*
%lang(de) /usr/share/vim/vim61/lang/de/*
%lang(es) /usr/share/vim/vim61/lang/es/*
%lang(fr) /usr/share/vim/vim61/lang/fr/*
%lang(it) /usr/share/vim/vim61/lang/it/*
%lang(ja) /usr/share/vim/vim61/lang/ja/*
%lang(ko) /usr/share/vim/vim61/lang/ko/*
%lang(pl) /usr/share/vim/vim61/lang/pl/*
%lang(sk) /usr/share/vim/vim61/lang/sk/*
%lang(uk) /usr/share/vim/vim61/lang/uk/*
%lang(zh_CN) /usr/share/vim/vim61/lang/zh_CN/*
%lang(zh_CN.UTF-8) /usr/share/vim/vim61/lang/zh_CN.UTF-8/*
%lang(zh_TW) /usr/share/vim/vim61/lang/zh_TW/*
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

%changelog
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
