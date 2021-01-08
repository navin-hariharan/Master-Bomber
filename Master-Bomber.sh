#!/bin/bash

detect_distro() {
    if [[ "$OSTYPE" == linux-android* ]]; then
            distro="termux"
    fi
    if [ -z "$distro" ]; then
        distro=$(ls /etc | awk 'match($0, "(.+?)[-_](?:release|version)", groups) {if(groups[1] != "os") {print groups[1]}}')
    fi
    if [ -z "$distro" ]; then
        if [ -f "/etc/os-release" ]; then
            distro="$(source /etc/os-release && echo $ID)"
        elif [ "$OSTYPE" == "darwin" ]; then
            distro="darwin"
        else 
            distro="invalid"
        fi
    fi
}

pause() {
    read -n1 -r -p "Press any key to continue..." key
}

banner() {
    clear
    if [[ "$OSTYPE" == "linux-gnu" ]]; then
    toilet -f ivrit 'Navin H' | boxes -d cat -a hc -p h8 | lolcat
    else
    cowsay 'Navin H' | lolcat
    fi
    echo 'This Bomber Was Created By Navin' | lolcat
    echo 'For Any Queries Contact Me!!!'| lolcat
    echo 'Intagram:- navin_hariharan'| lolcat
    echo ' '| lolcat
    echo 'Please use for Educational Purpose only!!!'| lolcat
    echo ' '| lolcat
}

init_environ(){
    declare -A backends; backends=(
        ["arch"]="pacman -S --noconfirm"
        ["debian"]="apt-get -y install"
        ["ubuntu"]="apt -y install"
        ["termux"]="apt -y install"
        ["fedora"]="yum -y install"
        ["redhat"]="yum -y install"
        ["SuSE"]="zypper -n install"
        ["sles"]="zypper -n install"
        ["darwin"]="brew install"
        ["alpine"]="apk add"
    )

    INSTALL="${backends[$distro]}"

    if [ "$distro" == "termux" ]; then
        PYTHON="python"
        SUDO=""
    else
        PYTHON="python3"
        SUDO="sudo"
    fi
    PIP="$PYTHON -m pip"
}

install_deps(){
    packages=(openssl git ruby boxes $PYTHON $PYTHON-pip figlet toilet boxes)
    if [ -n "$INSTALL" ];then
        for package in ${packages[@]}; do
            $SUDO $INSTALL $package
        done
        $PIP install -r requirements.txt
        if ! gem spec lolcat > /dev/null 2>&1; then
    	git clone https://github.com/busyloop/lolcat
    	cd lolcat
    	cd bin
    	sleep 2
    	gem install lolcat
    	sleep 1
    	cd ..
    	cd ..
    	rm -rf lolcat
    	else
    	    echo "Can't Install lolcat"
    	fi
    else
        echo "We could not install dependencies."
        exit
    fi
}


set_alias(){
    if [ "$distro" == "termux" ]; then
        cd;cd ..;cd usr;cd etc
	if grep -q "bomb" bash.bashrc; then
	    echo "Found...Skipping"
	    sleep 2
	    clear
	else    
	    echo 'alias bomb="cd;cd scripts;cd Social-Attacks;cd Master-Bomber;bash Master-Bomber.sh";' >> bash.bashrc
	    echo 'clear' >> bash.bashrc
	    echo 'PS1="\033[1;91mRoot[\033[1;93m\W\033[1;91m]:-\033[1;36m"' >> bash.bashrc
	    alias bomb="cd;cd scripts;cd Social-Attacks;cd Master-Bomber;bash Master-Bomber.sh";
	    clear
        fi
    else
        if grep -q "bomb" /root/.bashrc; then
	    echo "Found...Skipping"
	    sleep 2
	    clear
	else
            echo ' ' >> /root/.bashrc
	    echo 'alias bomb="cd;cd scripts;cd Social-Attacks;cd Master-Bomber;bash Master-Bomber.sh";' >> /root/.bashrc
	    alias bomb="cd;cd scripts;cd Social-Attacks;cd Master-Bomber;bash Master-Bomber.sh";
        fi	    
    fi
}

banner
pause
detect_distro
init_environ
if [ -f .update ];then
    echo "All Requirements Found...."
else
    echo 'Installing Requirements....'
    echo .
    echo .
    $PYTHON version_check.py || $PYTHON Core/version_check.py
    install_deps
    echo 'This Script Was Made By Navin Hariharan' > .update
    echo 'Requirements Installed....'
    set_alias
    pause
fi
while :
do
    banner
    echo -e "\e[4;31m Please Read Instruction Carefully !!! \e[0m"
    echo " "
    echo "Press 1 To  Start SMS  Bomber " | lolcat
    echo "Press 2 To  Start CALL Bomber "| lolcat
    echo "Press 3 To  Start MAIL Bomber " | lolcat
    echo "Press 0 To  Exit " | lolcat
    read ch
    cd Core
    clear
    if [ $ch -eq 1 ];then
        clear
        if [[ "$OSTYPE" == "linux-gnu" ]]; then
        toilet -f ivrit 'SMS BOMBER' | boxes -d cat -a hc -p h8 | lolcat
        else
        cowsay "SMS BOMBER" | lolcat
        fi
        $PYTHON bomber.py --sms
        exit
    elif [ $ch -eq 2 ];then
        clear
        if [[ "$OSTYPE" == "linux-gnu" ]]; then
        toilet -f ivrit 'CALL BOMBER' | boxes -d cat -a hc -p h8 | lolcat
        else
        cowsay "CALL BOMBER" | lolcat
        fi
        $PYTHON bomber.py --call
        exit
    elif [ $ch -eq 3 ];then
        clear
        if [[ "$OSTYPE" == "linux-gnu" ]]; then
        toilet -f ivrit 'MAIL BOMBER' | boxes -d cat -a hc -p h8 | lolcat
        else
        cowsay "MAIL BOMBER" | lolcat
        fi
        $PYTHON bomber.py --mail
        exit
    elif [ $ch -eq 4 ];then
        clear
        if [[ "$OSTYPE" == "linux-gnu" ]]; then
        toilet -f ivrit 'FEATURES' | boxes -d cat -a hc -p h8 | lolcat
        else
        cowsay "FEATURES" | lolcat
        fi
        echo "  [+] Unlimited And Super-Fast Bombing"| lolcat
	echo "  [+] Colourful Interface"| lolcat
	echo "  [+] SMS Bombing "| lolcat
	echo "  [+] Call Bombing "| lolcat
	echo "  [+] Mail Bombing "| lolcat
	#echo "  [+] Custom SMS Sending"| lolcat
	echo "  [+] Automated Future Updates"| lolcat
	echo "  [+] Easy To Use And Embed in Code"| lolcat
	echo ""
	echo -e "\e[1;31m This Script is Only For Educational Purposes or To Prank.\e[0m"| lolcat
	echo -e "\e[1;31m Do not Use This To Harm Others. \e[0m"| lolcat
	echo -e "\e[1;31m I Am Not Responsible For The Misuse Of The Script. \e[0m"| lolcat
	echo  " "
	echo -e "\e[4;31m That's All !!!\e[0m"| lolcat
	echo -e "\e[4;34m This Bomber Was Created By Navin \e[0m" | lolcat
	echo -e "\e[1;34m For Any Queries Contact Me!!!\e[0m"| lolcat
	echo -e "\e[1;32m   Intagram:- navin_hariharan\e[0m"| lolcat
	echo -e "\e[4;32m   Whatsapp: +917305574234 \e[0m"| lolcat
        exit
    elif [ $ch -eq 0 ];then
        banner
        exit
    else
        echo -e "\e[4;32m Invalid Input !!! \e[0m"
        pause
    fi
done
