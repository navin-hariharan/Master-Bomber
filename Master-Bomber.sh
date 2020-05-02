#!/bin/bash
clear
python3 version_check.py
sleep 3
if ! gem spec lolcat > /dev/null 2>&1; then
git clone https://github.com/busyloop/lolcat
cd lolcat
cd bin
gem install lolcat
cd ..
cd ..
rm -rf lolcat
fi


if [[ -s update.Navin ]];then
clear
echo "All Requirements Found...." | lolcat
echo -e "Welcome to Bomber" | lolcat
echo "Press Enter To Continue" | lolcat
read ex1
if [[ "$OSTYPE" == "linux-gnu" ]]; then
clear
toilet -f ivrit 'Linux' | boxes -d cat -a hc -p h8 | lolcat
echo "Press Enter To Continue" | lolcat
read ex1
else
clear
fi

else
if [[ "$OSTYPE" == "linux-gnu" ]]; then
apt install toilet python3-pip
pip3 install boxes
pip3 install -r requirements.txt
else
pkg install toilet python
pip install -r requirements.txt
fi

echo 'Installing Requirements....'
echo .
echo .
if [[ "$OSTYPE" == "linux-gnu" ]]; then
apt install ruby figlet python curl tor openssl python3-pip toilet -y
pip3 install termdown fortune cowsay fake_useragent
else
pkg install ruby figlet python curl tor openssl toilet -y
pip install termdown fortune cowsay fake_useragent
fi
echo 'This Script Was Made By Navin : Version 5.3' >update.Navin
sleep 3


if [[ "$OSTYPE" == "linux-gnu" ]]; then
if grep -q "bomb" /root/.bashrc; then
echo "Found...Skipping"
sleep 2
clear


else
echo ' ' >> /root/.bashrc
echo 'alias bomb="cd;cd scripts;cd Social-Attacks;cd Master-Bomber;bash Master-Bomber.sh";' >> /root/.bashrc
alias bomb="cd;cd scripts;cd Social-Attacks;cd Master-Bomber;bash Master-Bomber.sh";
clear
fi


else
cd
cd ..
cd usr
cd etc
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
fi
bomb
fi




while :
do
cd Core
rm -rf temp.*
rm -rf *.xxx
rm *.xxx >/dev/null 2>&1
clear
echo -e "\e[1;31m"
echo -e "\e[1;34m Created By \e[1;32m" | lolcat
if [[ "$OSTYPE" == "linux-gnu" ]]; then
toilet -f ivrit 'Navin H' | boxes -d cat -a hc -p h8 | lolcat
else
cowsay "Navin H" | lolcat
fi


echo -e "\e[4;34m This Bomber Was Created By Navin\e[0m" | lolcat
echo -e "\e[1;34m For Any Queries Contact Me!!!\e[0m"| lolcat
echo -e "\e[1;32m   Intagram:- navin_hariharan\e[0m"| lolcat
echo -e "\e[4;32m   Whatsapp: +917305574234 \e[0m"| lolcat
echo " "| lolcat
echo -e "\e[4;31m Please use for #Educational Purpose# only!!! \e[0m"| lolcat
echo " "| lolcat
echo "Press 1 To  Start Normal Bomber "| lolcat
echo "Press 2 To  Start Time Bomber "| lolcat
echo "Press 3 To  Start Time-Tolarance Bomber "| lolcat
echo "Press 4 To  Mail Bomber "| lolcat
echo "Press 5 To  Send Custom-Sms "| lolcat
echo "Press 6 To  Anonymous Mail "| lolcat
echo "Press 7 To  View  Features "| lolcat
echo "Press 0 To  Exit"| lolcat
read ch
cd Core
if [ $ch -eq '1' ];then
while :
do
rm *.xxx >/dev/null 2>&1
clear
echo -e "\e[1;31m"
echo -e "\e[1;34m Created By \e[1;32m" | lolcat
if [[ "$OSTYPE" == "linux-gnu" ]]; then
clear
toilet -f ivrit 'BOMB' | boxes -d cat -a hc -p h8 | lolcat
else
cowsay "BOMB" | lolcat
fi
echo -e "\e[4;34m This Bomber Was Created By Navin\e[0m" | lolcat
echo -e "\e[1;34m For Any Queries Contact Me!!!\e[0m"| lolcat
echo -e "\e[1;32m   Intagram:- navin_hariharan\e[0m"| lolcat
echo -e "\e[4;32m   Whatsapp: +917305574234 \e[0m"| lolcat
echo " "| lolcat
echo -e "\e[4;31m Please Read Instruction Carefully !!! \e[0m"| lolcat
echo " "| lolcat
echo "Press 1 To  Start SMS Bomber "| lolcat
echo "Press 2 To  Start Call Bomber "| lolcat
read b
if [ $b -eq 1 ];then
clear
echo -e "\e[1;32m"
rm *.xxx >/dev/null 2>&1
if [[ "$OSTYPE" == "linux-gnu" ]]; then
python3 bomber.py
rm *.xxx >/dev/null 2>&1
exit 0
else
python bomber.py
rm *.xxx >/dev/null 2>&1
exit 0
fi
elif [ $b -eq 2 ];then
clear
echo -e "\e[1;32m"
echo 'Call Bomb By Navin'> call.xxx
if [[ "$OSTYPE" == "linux-gnu" ]]; then
python3 bomber.py call
rm *.xxx >/dev/null 2>&1
exit 0
else
python bomber.py call
rm *.xxx >/dev/null 2>&1
exit 0
fi
else
clear
echo -e "\e[4;32m Invalid Input !!! \e[0m"| lolcat
echo "Press Enter To Go Home"| lolcat
read a3
fi
clear
done


elif [ $ch -eq '2' ];then
while :
do
rm *.xxx >/dev/null 2>&1
clear
echo -e "\e[1;31m"
echo -e "\e[1;34m Created By \e[1;32m" | lolcat
if [[ "$OSTYPE" == "linux-gnu" ]]; then
clear
toilet -f ivrit 'TBOMB' | boxes -d cat -a hc -p h8 | lolcat
else
cowsay "TBOMB" | lolcat
fi
echo -e "\e[4;34m This Bomber Was Created By Navin\e[0m" | lolcat
echo -e "\e[1;34m For Any Queries Contact Me!!!\e[0m"| lolcat
echo -e "\e[1;32m   Intagram:- navin_hariharan\e[0m"| lolcat
echo -e "\e[4;32m   Whatsapp: +917305574234 \e[0m"| lolcat
echo " "| lolcat
echo -e "\e[4;31m Please Read Instruction Carefully !!! \e[0m"| lolcat
echo " "| lolcat
echo "Press 1 To  Start SMS Timed-Bomber "| lolcat
echo "Press 2 To  Start Call Timed-Bomber "| lolcat
read tb
if [ $tb -eq 1 ];then
clear
echo -e "\e[1;32m"
if [[ "$OSTYPE" == "linux-gnu" ]]; then
python3 Time-Bomber.py
rm *.xxx >/dev/null 2>&1
exit 0
else
python Time-Bomber.py
rm *.xxx >/dev/null 2>&1
exit 0
fi
elif [ $tb -eq 2 ];then
clear
echo -e "\e[1;32m"
echo 'Call Bomb By Navin'> call.xxx
if [[ "$OSTYPE" == "linux-gnu" ]]; then
python3 Time-Bomber.py call
rm *.xxx >/dev/null 2>&1
exit 0
else
python Time-Bomber.py call
rm *.xxx >/dev/null 2>&1
exit 0
fi
else
clear
echo -e "\e[4;32m Invalid Input !!! \e[0m"| lolcat
echo "Press Enter To Go Home"| lolcat
read a3
fi
clear
done


elif [ $ch -eq '3' ];then
while :
do
rm *.xxx >/dev/null 2>&1
clear
echo -e "\e[1;31m"
echo -e "\e[1;34m Created By \e[1;32m" | lolcat
if [[ "$OSTYPE" == "linux-gnu" ]]; then
clear
toilet -f ivrit 'TTBOMB' | boxes -d cat -a hc -p h8 | lolcat
else
cowsay "TTBOMB" | lolcat
fi
echo -e "\e[4;34m This Bomber Was Created By Navin\e[0m" | lolcat
echo -e "\e[1;34m For Any Queries Contact Me!!!\e[0m"| lolcat
echo -e "\e[1;32m   Intagram:- navin_hariharan\e[0m"| lolcat
echo -e "\e[4;32m   Whatsapp: +917305574234 \e[0m"| lolcat
echo " "| lolcat
echo -e "\e[4;31m Please Read Instruction Carefully !!! \e[0m"| lolcat
echo " "| lolcat
echo "Press 1 To  Start SMS Timed-Tolarance-Bomber "| lolcat
echo "Press 2 To  Start Call Timed-Tolarance-Bomber "| lolcat
read tb
if [ $tb -eq 1 ];then
clear
echo -e "\e[1;32m"
if [[ "$OSTYPE" == "linux-gnu" ]]; then
python3 Time-Tolarance-Bomber.py
rm *.xxx >/dev/null 2>&1
exit 0
else
python Time-Tolarance-Bomber.py
rm *.xxx >/dev/null 2>&1
exit 0
fi
elif [ $tb -eq 2 ];then
clear
echo -e "\e[1;32m"
echo 'Call Bomb By Navin'> call.xxx
if [[ "$OSTYPE" == "linux-gnu" ]]; then
python3 Time-Tolarance-Bomber.py call
rm *.xxx >/dev/null 2>&1
exit 0
else
python Time-Tolarance-Bomber.py call
rm *.xxx >/dev/null 2>&1
exit 0
fi
else
clear
echo -e "\e[4;32m Invalid Input !!! \e[0m"| lolcat
echo "Press Enter To Go Home"| lolcat
read a3
fi
clear
done

elif [ $ch -eq '4' ];then
clear
if [[ "$OSTYPE" == "linux-gnu" ]]; then
toilet -f ivrit 'MAIL BOMBER' | boxes -d cat -a hc -p h8 | lolcat
else
cowsay "MAIL BOMBER" | lolcat
fi
python2 mail-bomb.py
exit 0



elif [ $ch -eq '5' ];then
clear
if [[ "$OSTYPE" == "linux-gnu" ]]; then
toilet -f ivrit 'CUSTOM SMS' | boxes -d cat -a hc -p h8 | lolcat
else
cowsay "CUSTOM SMS" | lolcat
fi
python3 sms.py
exit 0




elif [ $ch -eq '6' ];then
clear
if [[ "$OSTYPE" == "linux-gnu" ]]; then
toilet -f ivrit 'Mailer' | boxes -d cat -a hc -p h8 | lolcat
else
cowsay "Mailer" | lolcat
fi
python3 mail.py
exit 0



elif [ $ch -eq '7' ];then
clear
echo -e "\e[1;33m"| lolcat
echo  " "
if [[ "$OSTYPE" == "linux-gnu" ]]; then
clear
toilet -f ivrit 'Features' | boxes -d cat -a hc -p h8 | lolcat
else
cowsay "Features" | lolcat
fi
echo "  [+] Unlimited And Super-Fast Bombing"| lolcat
echo "  [+] Colourful Interface"| lolcat
echo "  [+] Call Bombing "| lolcat
echo "  [+] Custom SMS Sending"| lolcat
echo "  [+] Automated Future Updates"| lolcat
echo "  [+] Easy To Use And Embed in Code"| lolcat
echo ""
echo -e "\e[1;31m This Script is Only For Educational Purposes or To Prank.\e[0m"| lolcat
echo -e "\e[1;31m Do not Use This To Harm Others. \e[0m"| lolcat
echo -e "\e[1;31m I Am Not Responsible For The Misuse Of The Script. \e[0m"| lolcat
echo -e "\e[1;32m Make Sure To Update it If It Does not Work.\e[0m"| lolcat
echo  " "
echo -e "\e[4;31m That's All !!!\e[0m"| lolcat
echo -e "\e[4;34m This Bomber Was Created By Navin \e[0m" | lolcat
echo -e "\e[1;34m For Any Queries Contact Me!!!\e[0m"| lolcat
echo -e "\e[1;32m   Intagram:- navin_hariharan\e[0m"| lolcat
echo -e "\e[4;32m   Whatsapp: +917305574234 \e[0m"| lolcat
echo "Press Enter To Go Home"| lolcat
read a3
clear


elif [ $ch -eq '0' ];then
exit 0

else
clear
echo -e "\e[4;32m Invalid Input !!! \e[0m"| lolcat
echo "Press Enter To Go Home"| lolcat
read b4
fi
done



























