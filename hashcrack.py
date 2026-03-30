#!/usr/bin/env python3
import urllib.request
import urllib.parse
from re import search
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--path", help="Enter the path of your hashes.txt here", dest='path')
args = parser.parse_args()

# Colors
white = '\033[1;97m'
green = '\033[1;32m'
red = '\033[1;31m'
end = '\033[1;m'
info = '\033[1;33m[!]\033[1;m'
que =  '\033[1;34m[?]\033[1;m'
bad = '\033[1;31m[-]\033[1;m'
good = '\033[1;32m[+]\033[1;m'

def omega(hashvalue):
    data = urllib.parse.urlencode({"hash":hashvalue, "decrypt":"Decrypt"}).encode('utf-8')
    try:
        req = urllib.request.Request("http://md5decrypt.net/en/Sha256/", data=data)
        with urllib.request.urlopen(req) as response:
            find = response.read().decode('utf-8')
        match = search(r'<b>[^<]*</b><br/><br/>', find)
        if match:
            print(f"\n{good} {hashvalue} : {match.group().split('<b>')[1][:-14]}")
        else:
            if not args.path:
                print(f"{bad} Sorry this hash is not present in our database.")
    except:
        pass

def Lambda(hashvalue):
    url = f"http://md5decrypt.net/Api/api.php?hash={hashvalue}&hash_type=sha256&email=deanna_abshire@proxymail.eu&code=1152464b80a61728"
    try:
        with urllib.request.urlopen(url) as response:
            find = response.read().decode('utf-8')
        if len(find) > 0:
            print(f"\n{good} {hashvalue} : {find}")
        else:
            if not args.path:
                print(f"{bad} Sorry this hash is not present in our database.")
    except:
        pass

def beta(hashvalue):
    data = urllib.parse.urlencode({"auth":"8272hgt", "hash":hashvalue, "string":"","Submit":"Submit"}).encode('utf-8')
    try:
        req = urllib.request.Request("http://hashcrack.com/index.php", data=data)
        with urllib.request.urlopen(req) as response:
            find = response.read().decode('utf-8')
        match = search(r'<span class=hervorheb2>[^<]*</span></div></TD>', find)
        if match:
            print(f"\n{good} {hashvalue} : {match.group().split('hervorheb2>')[1][:-18]}")
        else:
            omega(hashvalue)
    except:
        omega(hashvalue)

print((56 * '\033[1;31m-'))
print(f"\t{white}     create {red}<3{end}{white} By HA-MRX")
print("""\033[1;97m
  _    _           _         _____                 _    
 | |  | |         | |       / ____|               | |   
 | |__| | __ _ ___| |__    | |      _ __ __ _  ___| | __
 |  __  |/ _` / __| '_ \   | |     | '__/ _` |/ __| |/ /
 | |  | | (_| \__ \ | | | | |____| | | (_| | (__|   < 
 |_|  |_|\__,_|___/_| |_|  \_____|_|  \__,_|\___|_|\_\   v.1""")
print((56 * '\033[1;31m-'))

def crack(hashvalue):
    if len(hashvalue) == 32:
        if not args.path:
            print(f"{info} Hash function : MD5")
        data = urllib.parse.urlencode({"hash":hashvalue,"submit":"Decrypt It!"}).encode('utf-8')
        try:
            req = urllib.request.Request("http://md5decryption.com", data=data)
            with urllib.request.urlopen(req) as response:
                find = response.read().decode('utf-8')
            match = search(r"Decrypted Text: </b>[^<]*</font>", find)
            if match:
                print(f"\n{good} {hashvalue} : {match.group().split('b>')[1][:-7]}")
            else:
                # Try another service
                url = "http://www.nitrxgen.net/md5db/" + hashvalue
                with urllib.request.urlopen(url) as response:
                    purl = response.read().decode('utf-8')
                if len(purl) > 0:
                    print(f"\n{good} {hashvalue} : {purl}")
                else:
                    if not args.path:
                        print(f"{bad} Sorry this hash is not present in our database.")
        except:
            if not args.path: print(f"{bad} Connection Error")
            
    elif len(hashvalue) == 40:
        if not args.path: print(f"{info} Hash function : SHA1")
        beta(hashvalue)
    elif len(hashvalue) == 64:
        if not args.path: print(f"{info} Hash function : SHA-256")
        Lambda(hashvalue)
    else:
        print(f"{bad} This hash is not supported.")

if args.path:
    try:
        with open(args.path, 'r') as f:
            for line in f:
                crack(line.strip())
    except FileNotFoundError:
        print(f"{bad} Wordlist not found!")
else:
    h = input(f'{que} Enter hash: ').lower().strip()
    crack(h)
