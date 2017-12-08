# Imports
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

# Constants
duration = 1
steps    = 19

# Connection
device = MonkeyRunner.waitForConnection()

print("Test02 zapocet")

# Setuje/podesava path varijablu sa punim imenom .apk fajla
package = 'com.appparkingspot'
activity = '.ActivitySplash'
runComponent = package + '/' + activity

# Pokrece (Run) komponentu
device.startActivity(component=runComponent)

# Pauzira izvrsenje programa na 3 sekunde da bi se aktivnost ucitala
MonkeyRunner.sleep(6)

for x in range(0, 3):
	# Deploy your app, add your intent, if needed
	# Touch or drag
	device.touch(144, 180, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)
	device.touch(414, 636, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)
	device.touch(144, 180, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)
	device.touch(432, 810, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)
	device.touch(144, 180, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)
	device.touch(408, 996, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)
	device.touch(144, 180, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)	
	device.touch(432, 1176, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)
	device.touch(144, 192, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)
	device.touch(702, 1362, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)
	device.touch(144, 180, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)
	device.touch(534, 1554, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)
	device.touch(144, 180, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)
	device.touch(444, 1716, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)
	device.touch(144, 180, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)
	device.touch(402, 1896, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)
	device.touch(144, 180, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)
	device.touch(420, 2076, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)
	device.touch(144, 180, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)

print('Test02 zavrsen!')