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
#nmap -v -iR 9000 -Pn -p 80 | grep 'Discovered open port' > res.txt
zmap -p 80 77.221.153.0/24 -B 1000M -o all.txt
nmap -sV -p 80 -v -n  --script http-title  -iL habr.txt > res.txt

echo "Ending nmap"
python3 end.py
bash init.sh
