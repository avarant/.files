# .files

vim and zsh configurations



**install zsh**
  sudo apt install zsh


**install [ohmyzsh](https://ohmyz.sh/#install)**
  sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"


**install [powerlevel10k](https://github.com/romkatv/powerlevel10k) theme**
  git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k


**install [zsh-syntax-highlighting plugin](https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md) plugin**
Clone this repository in oh-my-zsh's plugins directory:
  git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting


**restart zsh**
  source .zshrc
