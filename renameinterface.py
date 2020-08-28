import os, sys

interface = input("Entrez le nom de l'interface que vous souhaitez modifier en wlan0 : ")
print("Changement de " + interface + " pour wlan0mon...")
os.system("ifconfig " + interface + " down")
newinterface = input("Quel sera le nouveau nom de l'interface ? : ")
os.system("ip link set " + interface + " name " + newinterface)
os.system("ifconfig " + newinterface + " up")
print("Changement de l'interface terminé !")

#interface = os.system("ifconfig | cut -d ':' -f1")
#print(interface)
