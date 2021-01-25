import os,sys
import requests
from argparse import ArgumentParser

fingers = ["Sorry, this page is no longer available.",
            "If this is your website and you've just created it, try refreshing in a minute",
            "The specified bucket does not exist",
            "Repository not found",
            "Trying to access your account?",
            "404 Not Found",
            "Domain uses DO name serves with no records in DO.",
            "404: This page could not be found.",
            "The thing you were looking for is no longer here, or never was",
            "There isn't a Github Pages site here.",
            "404 Blog is not found",
            "We could not find what you're looking for.",
            "No settings were found for this company:",
            "Uh oh. That page doesn't exist.",
            "is not a registered InCloud YouTrack",
            "No Site For Domain",
            "It looks like you may have taken a wrong turn somewhere. Don't worry...it happens to all of us.",
            "Tunnel *.ngrok.io not found",
            "404 error unknown site!",
            "This public report page has not been activated by the user",
            "Project doesnt exist... yet!",
            "This job board website is either expired or its domain name is invalid.",
            "page not found",
            "project not found",
            "Non-hub domain, The URL you've accessed does not provide a hub.",
            "This UserVoice subdomain is currently available!",
            "Do you want to register *.wordpress.com?",
            "Hello! Sorry, but the website you&rsquo;re looking for doesn&rsquo;t exist.",
            "The requested URL was not found on this server.",
            "Please renew your subscription",
            "Whatever you were looking for doesn't currently exist at this address",
            "Sorry, this shop is currently unavailable.",
            "Unrecognized domain",
            "No such app",
            "Fastly error: unknown domain:"]


parser = ArgumentParser(description="Subdomain Takeover Tool", epilog="Usage : python3 subtake.py -f file.txt")
parser.add_argument('-f','--file',dest="subfile",metavar='',help="Subdomains file",required=True)
args = parser.parse_args()

#colors....
red = "\033[1;31m"
green = "\033[1;32;0m"
reset = "\033[0m"

def check_bug(url):
    try:
        r = requests.post(url,timeout=5).text
        for finger in fingers:
            if finger in r:
                print(f"\033[1;32m[ Vulnerable ] \033[0m {url}")
        print(f"\033[1;31m[ Not Vulnerable ] \033[0m {url}")
    except KeyboardInterrupt:
        print("\n \033[1;31m[-] \033[1;0mYou pressed CTRL + C")
        exit(1)
    except requests.exceptions.SSLError:
        print(f"\n \033[1;31m[ SSL ERROR ] \033[1;0m{url}")

def check(file):

    f = open(file,"r")
    sites = f.readlines()
    for line in sites:
        site = line.strip()
        check_bug(site)

def banner():
    print("-------------------------------------------------------------------------------------------------------")
    #print("\n")
    print(" ######  ##     ## ########  ########    ###    ##    ## ########  #######  ##     ## ######## ######## ")
    print("##    ## ##     ## ##     ##    ##      ## ##   ##   ##  ##       ##     ## ##     ## ##       ##     ## ")
    print("##       ##     ## ##     ##    ##     ##   ##  ##  ##   ##       ##     ## ##     ## ##       ##     ## ")
    print(" ######  ##     ## ########     ##    ##     ## #####    ######   ##     ## ##     ## ######   ########")
    print("      ## ##     ## ##     ##    ##    ######### ##  ##   ##       ##     ##  ##   ##  ##       ##   ## ")
    print("##    ## ##     ## ##     ##    ##    ##     ## ##   ##  ##       ##     ##   ## ##   ##       ##    ## ")
    print(" ######   #######  ########     ##    ##     ## ##    ## ########  #######     ###    ######## ##     ##")
    #print("\n")
    print("----------------------------------------------------------------@Mr_3rr0r_501--------------------------")
 

if __name__ == "__main__":
    banner()
    print("\n\033[1;32m[+] Subdomain takeover started....\n \033[1;0m")
    check(args.subfile)