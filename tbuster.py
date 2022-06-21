#!/usr/bin/env python3
# made by prince kumar 
# date 14 jun 2022 
# import all the requirements 
import requests
import sys
import os 
import socket
# make a nice banner for the tool 
def banner():
    print("""
         +-+-+-+-+-+-+-+
         |t|b|u|s|t|e|r|
         +-+-+-+-+-+-+-+""" )
    print("\033[31;1m         Made by prince ")
# make a help function 
def help():
    print("\033[35;1m Uses:")
    print("\033[32;1m tbuster <url> -w <wordlist> -o <nameofoutputfile> ")
    print("\033[32;1m  -help or --help to show the uses ")
    print("\033[32;1m tbuster <full url> <wordllist path> ")
# make a function to check the valid url 
def isvalid(url):
    if "http://" in url:
        return True
    elif "https://" in url:
         return True
    else:
        return False
# make a function to resulve the ip 
def getip(url):
    # first remove the https or http for the usr 
    hlist = url.split("//")
    try:
        ip = socket.gethostbyname(hlist[1])
        return ip
    except socket.gaierror:
        return "Not foumd"
# Make a function to make requests..
def makereq(path,url):
    with open(path,"r") as f:
        for line in f.readlines():
            #make url 
            p_list = line.strip()
            f_url = f"{url}/{p_list}"
            #print(f"\033[97;1m \r Checking.. {p_list}")
            req = requests.get(f_url)
            if req.status_code == 200:
                print(f" {f_url} Code:<{req.status_code}> ")
            elif req.status_code == 301:
                print(f" {f_url} Code:<{req.status_code}> ")
            elif req.status_code == 302:
                print(f" {f_url} Code:<{req.status_code}> ")
            else:
                pass
# handle the arguments of the user 
if len(sys.argv) < 2:
    help()
else:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        help()
    elif isvalid(sys.argv[1]):
        if "-w" in sys.argv :
            print("\033[0;1m [~] Checking wordlist path")
            if os.path.exists(sys.argv[3]):
                banner() 
                ip = getip(sys.argv[1])
                path = sys.argv[3]
                print(" ")
                print(f"[-] {sys.argv[1]} : {ip}")
                makereq(path,sys.argv[1])
        else:
            print("\033[35;1m [~] Using default passlist ")
            if os.path.exists("test.txt"):
                banner()
                ip = getip(sys.argv[1])
                print(f"\033[33;1m [~] Using default wordlist \033[36;1m ")
                print(f"[-] {sys.argv[1]} : {ip}")
                makereq("test.txt",sys.argv[1])
            else :
                print("\033[31;1m File not found")
    else:
        print("\033[31;1m [!] Invalid url format")
    

