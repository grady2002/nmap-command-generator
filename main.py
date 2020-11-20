import os
from os import system, name
import time
import nmap

scanner = nmap.PortScanner()
ver = scanner.nmap_version()

def clear () :
    if os.name == 'nt' :
        os.system("cls")
    else : 
        os.system("clear")

def textColor () :
    if os.name == 'nt' : 
        os.system("color 6")
        os.system("title Port Scanner")
    else : 
        pass

textColor()

start = clear()

print(" 1 - english\n 2 - french")
language = int(input("\n choose language ? "))

def scan1 (host) :
    print(" \n[+] command : sudo nmap",host)

def scan2 (host) :
    print(" \n[+] command : sudo nmap -sS",host)

def scan3 (host) :
    print(" \n[+] command : sudo nmap -T4 -sV -sP",host)

def scan4(host) : 
    print(" \n[+] command : sudo nmap -T4 -O",host)

def scan5(host) :
    print(" \n[+] command : sudo nmap -T4 -A", host)

def scan6(host) :
    print(" \n[+] command : sudo nmap -T4 -sV -O", host)

def scan7(host) :
    print(" \n[+] command : sudo nmap -T4 -sV -A", host)

def scan8(host) : 
    print(" \n[+] command : sudo nmap -T4 -O -A",host)

if language == 1 : 
    clear()
    print(" NMAP scan command generation tool by Grady\n")
    print(" Instagram - grady.css\n")
    print(" 1 - simple port scan\n 2 - syn stealth scan")
    print(" 3 - advanced service scan\n 4 - os detection")
    print(" 5 - traceroute\n 6 - advanced service scan + os detection")
    print(" 7 - advanced service scan + traceroute")
    print(" 8 - traceroute + os detection\n 9 - print version\n")
    option = int(input("\n scan option ? "))

elif language == 2:
    clear()
    print(" Outil de génération de commandes NMAP par Grady\n")
    print(" Instagram - grady.css\n")
    print(" 1 - scan simple des ports\n 2 - scan furtif syn")
    print(" 3 - scan de service avancé\n 4 - détection du système d'exploitation")
    print(" 5 - traceroute\n 6 - scan de service avancé + détection du système d'exploitation")
    print(" 7 - scan de service avancé + traceroute")
    print(" 8 - traceroute + détection du système d'exploitation\n 9 - version imprimée\n")
    option = int(input("\n option d'analyse ? "))    

host = input(" \nhost ? ")

if option == 1 : 
    scan1(host)

elif option == 2 :
    scan2(host)

elif option == 3 : 
    scan3(host)

elif option == 4 : 
    scan4(host)

elif option == 5 : 
    scan5(host)

elif option == 6 :
    scan6(host)

elif option == 7 :
    scan7(host)

elif option == 8 :
    scan8(host)

elif option == 9 :
    print("\n",ver)

elif option > 9 and language == 1 :
    print(" \ninvalid choice")
elif option > 9 and language == 2 :
    print(" \nchoix invalide")