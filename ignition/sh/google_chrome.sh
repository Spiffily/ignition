#!/bin/bash
operation=$1
source=$2

package='chromium'
apt=true
snap=true
deb=true
pacman=true
flatpak=false
# package=$3 #For debugging purposes only

if [[ $operation == 'install' ]]; then
    if [[ $source == 'apt' && $apt == 'true' ]]; then
        sudo apt-get install -y chromium-browser chromium-chromedriver chromium-codecs-ffmpeg-extra
    elif [[ $source == 'snap' && $snap == 'true' ]]; then
        sudo snap install $package chromium-ffmpeg
    elif [[ $source == 'deb' && $deb == 'true' ]]; then
        mkdir ~/Downloads/
        cd ~/Downloads/
        wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
        sudo gdebi -n google-chrome-stable_current_amd64.deb
        rm google-chrome-stable_current_amd64.deb
    elif [[ $source == 'pacman' && $pacman == 'true' ]]; then
        sudo pacman -S $package
    elif [[ $source == 'flatpak' && $flatpak == 'true' ]]; then
        sudo flatpak install $package
    else
        echo -e '\e[91mERROR:\e[0m \e[33m'$package'\e[0m is not available as \e[94m'$source'\e[0m.'
        exit 1;
    fi

elif [[ $operation == 'remove' ]]; then
    if [[ $source == 'apt' && $apt == 'true' ]]; then
        sudo apt-get remove -y chromium-browser chromium-chromedriver chromium-codecs-ffmpeg-extra
    elif [[ $source == 'snap' && $snap == 'true' ]]; then
        sudo snap remove $package chromium-ffmpeg
    elif [[ $source == 'deb' && $deb == 'true' ]]; then
        sudo apt-get remove -y google-chrome
    elif [[ $source == 'pacman' && $pacman == 'true' ]]; then
        sudo pacman -? $package
    elif [[ $source == 'flatpak' && $flatpak == 'true' ]]; then
        sudo flatpak remove $package
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
    echo '    (More to come...)'
    echo

fi