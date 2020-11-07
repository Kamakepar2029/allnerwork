sudo apt install nmap -y
echo "---------------------------- "
echo "Starting nmap"
echo "---------------------------- "
echo '1'>r.txt 
nmap -v -iR 102400 -Pn -p 80 | grep 'Discovered open port' > lastthing.txt
echo "Starting nmap"
bash init.sh
