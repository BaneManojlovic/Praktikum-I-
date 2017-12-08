# Imports
import sys
import os
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

# Constants
duration = 1
steps    = 30

# Connection
device = MonkeyRunner.waitForConnection()

print("Test04 zapocet\n")

# Setuje/podesava path varijablu sa punim imenom .apk fajla
package = 'com.appparkingspot'
activity = '.ActivitySplash'
runComponent = package + '/' + activity

# Pokrece (Run) komponentu
device.startActivity(component=runComponent)

# Pauzira izvrsenje programa na 3 sekunde da bi se aktivnost ucitala
MonkeyRunner.sleep(8)

# Pitam korisnika koliko ponavljanja zeli da ima.
#x = input("Koliko ponavljanja zelite? ");
#print x 
#print type(x)
#for x in range(1, x):
x = 1
while (x <= 2):
	print "Krug: ", x
	x = x + 1
	print('Klik na meni')
	device.touch(144, 180, "DOWN")
	MonkeyRunner.sleep(8)
	#print('Klik na Event')
	#device.touch(414, 636, "DOWN")
	#MonkeyRunner.sleep(6)
	#print('Klik na meni')
	#device.touch(144, 180, "UP")
	#MonkeyRunner.sleep(6)
	print('Klik na My spaces')
	device.touch(432, 810, "UP")
	MonkeyRunner.sleep(8)
	print('Skrolovanje')
	device.drag((360, 2352), (360, 696), 1.0, 10)
	device.drag((360, 696), (360, 2352), 1.0, 10)
	device.drag((360, 2352), (360, 696), 1.0, 10)
	device.drag((360, 696), (360, 2352), 1.0, 10)
	device.drag((360, 2352), (360, 696), 1.0, 10)
	device.drag((360, 696), (360, 2352), 1.0, 10)
	MonkeyRunner.sleep(8)

		

print('\nKraj testa')