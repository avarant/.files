alias ..='cd ..'
alias ...='cd ../..'
alias ~='cd ~'

alias ll='ls -AlFG'
alias lr='ls -R | grep ":$" | sed -e '\''s/:$//'\'' -e '\''s/[^-][^\/]*\//--/g'\'' -e '\''s/^/   /'\'' -e '\''s/-/|/'\'' | less'

alias c='clear'
alias d='du -hc'
alias p='ps aux'
alias s='source'
alias t='tar zxvf'

alias path='echo -e ${PATH//:/\\n}'

alias v="vim"

alias record='arecord -f S16_LE -r 16000 -D default -c 1 audio/test.wav'
