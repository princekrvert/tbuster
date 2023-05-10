#!/usr/bin/env python3
# made by prince kumar 
# date 14 jun 2022 
# import all the requirements 
import requests
import sys
import os 
import socket
import argparse
parser = argparse.ArgumentParser(description='Mass ip locater')
parser.add_argument("-u","--url",help='Enter the full url :')
parser.add_argument('-w',"--wordlist",help="Path to the wordlist: " )
args = parser.parse_args()
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
            print(f"\r\033[97;1m \r Checking.. {p_list}::",end="")
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
if (args.url):
    if(args.wordlist):
        # now check for the path exitance 
        if(os.path.exists(args.wordlist)):
            #now check the 
            if(isvalid(args.url)):
                makereq(args.wordlist,args.url)
            else:
                print("\033[31;1m Invalid url form , Please provide url with http and https:")
                sys.exit(1)
        else:
            print("033[31;1m Provided path does not exists ")
            choise = input("033[32;1m Want use default wordlist Y/N")
            if choise == "Y" or choise == "y":
                # then use the wordlist .....
                makereq("test.txt",args.url)
            else:
                sys.exit(1)
    else:
        #check if url is valid 
        if(isvalid(args.url)):
            makereq("test.txt",args.url)
        else:
            print("\033[31;1m Please provide a valid url:")
else:
    print("\033[35;1m Please provide a url")

