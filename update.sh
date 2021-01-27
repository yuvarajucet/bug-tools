#!/bin/sh

echo "\033[1;32m [+] Updating Please wait..."
echo "\033[1;32m [+] Removing Old files.."
sudo rm -rf *
echo "\033[1;32m [+] Cloning New files"
sleep 2
git clone https://github.com/yuvarajucet/subdomain-takeover.git
sudo "\033[1;32m [+] Tool Updated success.."
