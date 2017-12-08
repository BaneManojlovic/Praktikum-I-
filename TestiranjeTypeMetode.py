# Imports
import sys
import os
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

# Connection
device = MonkeyRunner.waitForConnection()
device.wake()
MonkeyRunner.sleep(8)

print('\nTest - Testiranje Type Metode')
print("Test zapocet\n")
MonkeyRunner.sleep(8)

# Setuje/podesava path varijablu sa punim imenom .apk fajla
package = 'com.appparkingspot'
activity = '.ActivitySplash'
runComponent = package + '/' + activity

# Pokrece (Run) komponentu
device.startActivity(component=runComponent)

#ispisuje poruku o pokrenutoj aplikaciji
MonkeyRunner.alert("Aplikacija je pokrenuta")

# Pauzira izvrsenje programa na 3 sekunde da bi se aktivnost ucitala
MonkeyRunner.sleep(5)

x = 1 
while (x <= 1):
	print "Krug: ", x
	x = x + 1
	# kliknuo sam na Email addres
	device.touch(354, 1092, "DOWN_AND_UP")
	device.type("bane1manojlovic@gmail.com")
	MonkeyRunner.sleep(3)
	# klik na password field
	device.touch(336, 1320, "DOWN_AND_UP")
	device.type("BakiMaki1")
	MonkeyRunner.sleep(3)
	# klik na done da spusti tastaturu
	device.touch(1284, 2364, "DOWN_AND_UP")
	MonkeyRunner.sleep(3)
	# klik na Log in dugme
	device.touch(414, 1614, "DOWN_AND_UP")
	MonkeyRunner.sleep(8)
	print('Klik na meni')
	device.touch(144, 180, "DOWN")
	MonkeyRunner.sleep(8)
	#klik na settings
	device.touch(414, 1896, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)
	#klik na LogOut
	device.touch(702, 2268, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)

print('Kraj testa!')
