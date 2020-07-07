
alias v='vim'

alias ll='ls -AlFG'
alias lr='ls -R | grep ":$" | sed -e '\''s/:$//'\'' -e '\''s/[^-][^\/]*\//--/g'\'' -e '\''s/^/   /'\'' -e '\''s/-/|/'\'' | less'

alias ..='cd ..'
alias ...='cd ../..'
alias ~='cd ~'
alias path='echo -e ${PATH//:/\\n}'

alias f='open -a Finder .'

alias c='clear'
alias d='du -hc'

alias record='arecord -f S16_LE -r 16000 -D default -c 1 audio/test.wav'
