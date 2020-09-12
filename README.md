# .files

vim and zsh configurations

<br>

**install zsh**

  `sudo apt install zsh`

<br>

**install [ohmyzsh](https://ohmyz.sh/#install)**

  `sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`

<br>

**install [powerlevel10k](https://github.com/romkatv/powerlevel10k) theme**

  `git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k`

<br>

**install [zsh-syntax-highlighting plugin](https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md) plugin**

Clone this repository in oh-my-zsh's plugins directory:

  `git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting`

<br>

**restart zsh**

  `source .zshrc`
