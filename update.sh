#!/bin/sh

echo "\033[1;32m [+] Updating Please wait..."
sleep 1
echo "\033[1;32m [+] Removing Old files.."
sleep 1
sudo rm -rf ../subdomain-takeover
echo "\033[1;32m [+] Cloning New files"
sleep 2
cd .. && git clone https://github.com/yuvarajucet/subdomain-takeover.git

echo "\033[1;32m [+] Tool Updated success.."
cd subdomain-takeover
