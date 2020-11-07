sudo apt install nmap -y
echo "---------------------------- "
echo "Starting nmap"
echo "---------------------------- "
echo '1'>>r.txt 
nmap -v -iR 10000 -Pn -p 80 | grep 'Discovered open port' > 10.11.2020.txt
echo "Starting nmap"
bash init.sh
