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
    if "http://" or "https://" in url :
        return True
# make a function to resulve the ip 
def getip(url):
    # first remove the https or http for the usr 
    hlist = url.split("//")
    ip = socket.gethostbyname(hlist[1])
    return ip
# handle the arguments of the user 
if sys.argv[1] == "-h" or sys.argv[1] == "--help":
    help()
elif isvalid(sys.argv[1]):
    if "-w" in sys.argv :
        print("\033[0;1m [~] Checking wordlist path")
        if os.path.exists(sys.argv[3]):
            banner()  
    else:
        print("\033[35;1m [~] Using default passlist ")
        if os.path.exists("test.txt"):
            banner()
            ip = getip(sys.argv[1])
            print(f"[-] {sys.argv[1]} : {ip}")
        else :
            print("\033[31;1m File not found")
else:
    print("\033[31;1m [!] Invalid url format")
    

