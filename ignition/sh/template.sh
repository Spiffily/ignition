#!/bin/bash
operation=$1
source=$2
url=''

package='gnome-software'
apt=true
snap=true
deb=true
pacman=true
flatpak=true
appimage=true
sh=false
# package=$3 #For debugging purposes only

if [[ $operation == 'install' ]]; then
    if [[ $source == 'apt' && $apt == 'true' ]]; then
        sudo apt-get install -y $package
    elif [[ $source == 'snap' && $snap == 'true' ]]; then
        sudo snap install $package
    elif [[ $source == 'deb' && $deb == 'true' ]]; then
        mkdir ~/Downloads/
        cd ~/Downloads/
        wget $url.deb
        sudo gdebi -n $package.deb
        rm $package.deb
    elif [[ $source == 'pacman' && $pacman == 'true' ]]; then
        sudo pacman -S $package
        # git clone $url; cd $package; makepkg -si # aur instead of pacman
    elif [[ $source == 'flatpak' && $flatpak == 'true' ]]; then
        sudo flatpak install $package
    elif [[ $source == 'appimage' && $appimage == 'true' ]]; then
        mkdir $HOME/apps/; cd $HOME/apps/
        wget $url
        chmod a+x $package.AppImage
        echo "[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec=exit
Name=Default
Icon=application-x-executable" >> $HOME/.local/share/applications/$package.desktop
    elif [[ $source == 'sh' && $sh == 'true']]; then
        # bash $package.sh or commands
    else
        echo -e '\e[91mERROR:\e[0m \e[33m'$package'\e[0m is not available as \e[94m'$source'\e[0m.'
        exit 1;
    fi

elif [[ $operation == 'remove' ]]; then
    if [[ $source == 'apt' && $apt == 'true' ]]; then
        sudo apt-get remove -y $package
    elif [[ $source == 'snap' && $snap == 'true' ]]; then
        sudo snap remove $package
    elif [[ $source == 'deb' && $deb == 'true' ]]; then
        sudo apt-get remove -y $package
    elif [[ $source == 'pacman' && $pacman == 'true' ]]; then
        sudo pacman -Rs $package
    elif [[ $source == 'flatpak' && $flatpak == 'true' ]]; then
        sudo flatpak uninstall $package
    elif [[ $source == 'appimage' && $appimage == 'true' ]]; then
        rm $HOME/apps/$package
        rm $HOME/.local/share/applications/$package.desktop
    elif [[ $source == 'sh' && $sh == 'true']]; then
        # It depends
    else
        echo -e '\e[91mERROR:\e[0m \e[33m'$package'\e[0m is not available as \e[94m'$source'\e[0m.'
        exit 1;
    fi

elif [[ $operation == 'check' ]]; then
    if [[ $source == 'apt' && $apt == 'true' ]]; then
        apt-mark showinstall | grep $package
    elif [[ $source == 'snap' && $snap == 'true' ]]; then
        snap list | grep $package
    elif [[ $source == 'deb' && $deb == 'true' ]]; then
        apt-mark showinstall | grep $package
    elif [[ $source == 'pacman' && $pacman == 'true' ]]; then
        pacman -Q | grep $package
    elif [[ $source == 'flatpak' && $flatpak == 'true' ]]; then
        flatpak list | grep $package
    elif [[ $source == 'appimage' && $appimage == 'true' ]]; then
        ls $HOME/.local/share/applications | grep $package
    elif [[ $source == 'sh' && $sh == 'true']]; then
        # It depends
    else
        echo -e '\e[91mERROR:\e[0m \e[33m'$package'\e[0m is not available as \e[94m'$source'\e[0m.'
        exit 1;
    fi

else
    echo -e '\e[33mUSAGE:\e[0m \e[36m<operation>\e[0m \e[94m<source>\e[0m <version>'
    echo -e '\e[36mOperations:\e[0m install, remove'
    echo -e '\e[94mSupported sources:\e[0m (More to come...)'
    echo '    aptitude (apt)'
    echo '    snappy (snap)'
    echo '    .deb files (deb)'
    echo '    pacman (pacman)'
    echo '    flatpak (flatpak)'
    echo '    .AppImage (appimage)'
    echo '    .sh files (sh)'
    echo '    (More to come...)'
    echo

fi
