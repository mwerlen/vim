"" (for Chinese)
"" Set file encoding format as 'taiwan' for Chinese
"" Only fe is only set when in rxvt which defines COLORTERM 
"" environment variable
if exists("$COLORTERM")
     set fe=taiwan
endif

"" (for Chinese)
"" Set ruler on, you must set this to ensure
"" the Chinese functionality of gvim
set ru

"" Set visual bell and disable screen flash
:set vb t_vb=

"" Toggle on/off highlightsearch
map <F8> :set hls!<bar>set hls?<cr>

"" Toggle on/off paste mode
map <F9> :set paste!<bar>set paste?<cr>

"" You can toggle the syntax on/off with this command
if has("syntax_items") | syntax off | else | syntax on | endif
map <F7> :if has("syntax_items") <Bar> syntax off <Bar> else <Bar> syntax on <Bar> endif <CR>

syntax on

"" Set non-compatible with vi
set nocompatible 

"" Set backup extension
set backup
set backupext=.bak

"" Map for parenthesis matching
map \   %
