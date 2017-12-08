# Imports
import sys
import os
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage


# Connection
device = MonkeyRunner.waitForConnection()

print('\nTest - Testiranje tutorijala')
print("Test05 zapocet\n")

# Setuje/podesava path varijablu sa punim imenom .apk fajla
package = 'com.appparkingspot'
activity = '.ActivitySplash'
runComponent = package + '/' + activity

# Pokrece (Run) komponentu
device.startActivity(component=runComponent)

# Pauzira izvrsenje programa na 3 sekunde da bi se aktivnost ucitala
MonkeyRunner.sleep(8)

x = 1
while (x <= 5):
	print "Krug: ", x
	x = x + 1
	print('Klik na meni')
	device.touch(144, 180, "DOWN")
	MonkeyRunner.sleep(8)
	print('Klik na tutorijal')
	device.touch(420, 2262, "DOWN_AND_UP")
	MonkeyRunner.sleep(8)
	print('Swipe s desna na levo tri puta')
	device.touch(198, 2340, "DOWN_AND_UP")
	MonkeyRunner.sleep(3)
	device.drag((1302, 1674), (144, 1668), 0.1, 10)
	MonkeyRunner.sleep(1)
	device.drag((1302, 1674), (144, 1668), 0.1, 10)
	MonkeyRunner.sleep(1)
	device.drag((1302, 1674), (144, 1668), 0.1, 10)
	MonkeyRunner.sleep(1)
	print('Swipe s leva na desno tri puta')
	device.drag((144, 1668), (1302, 1674), 0.1, 10)
	MonkeyRunner.sleep(1)
	device.drag((144, 1668), (1302, 1674), 0.1, 10)
	MonkeyRunner.sleep(1)
	device.drag((144, 1668), (1302, 1674), 0.1, 10)
	MonkeyRunner.sleep(1)
	print('Swipe s desna na levo tri puta')
	device.touch(1236, 2340, "DOWN_AND_UP")
	MonkeyRunner.sleep(3)
	device.drag((1302, 1674), (144, 1668), 0.1, 10)
	MonkeyRunner.sleep(1)
	device.drag((1302, 1674), (144, 1668), 0.1, 10)
	MonkeyRunner.sleep(1)
	device.drag((1302, 1674), (144, 1668), 0.1, 10)
	MonkeyRunner.sleep(3)
	print('klik na dugme')
	device.touch(702, 2316, "DOWN_AND_UP")
	MonkeyRunner.sleep(8)
	device.touch(144, 180, "DOWN")
	MonkeyRunner.sleep(3)

print('Kraj testa!')