sudo apt install nmap -y
sudo apt install zmap -y
sudo apt install python3-pip -y
pip3 install setuptools
pip3 install telebot pytelegrambotapi
python3 start.py
echo "---------------------------- "
echo "Starting nmap"
echo "---------------------------- "
echo '1'>>r.txt 
nmap -v -iR 500000 -p 80 -oG - > res.txt
echo "Ending nmap"

python3 end.py
bash init.sh
