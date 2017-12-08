# Imports
import sys
import os
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

# Connection
device = MonkeyRunner.waitForConnection()

print('\nTest - Rad sa modulima')
print("Test zapocet\n")

# Setuje/podesava path varijablu sa punim imenom .apk fajla
package = 'com.appparkingspot'
activity = '.ActivitySplash'
runComponent = package + '/' + activity

# Pokrece (Run) komponentu
device.startActivity(component=runComponent)

#ispisuje poruku o pokrenutoj aplikaciji
MonkeyRunner.alert("Aplikacija je pokrenuta")

# Pauzira izvrsenje programa na 3 sekunde da bi se aktivnost ucitala
MonkeyRunner.sleep(8)

y = MonkeyRunner.input("Unesite broj ponavljanja testa: ", "0")
print "Broj ponavljanja: ", y
#konvertujem String vrednost y =1 u int vrednost y = 1
y = int(y)

x = 1 
while (x <= y):
	print "Krug: ", x
	x = x + 1
	print('Klik na meni')
	device.touch(144, 180, "DOWN")
	MonkeyRunner.sleep(8)
	device.takeSnapshot()
	print('Klik na Event')
	device.touch(414, 636, "DOWN")
	MonkeyRunner.sleep(6)
	print('Klik na meni')
	device.touch(144, 180, "UP")
	MonkeyRunner.sleep(6)

#ispisuje poruku o zavrsenoj aplikaciji
MonkeyRunner.alert("Cestitamo uspesno ste zavrsili Monkey Runner Test!!!")
print("Test zavrsen")