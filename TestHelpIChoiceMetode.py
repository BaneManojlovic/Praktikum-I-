import sys
import os
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

# Connection
device = MonkeyRunner.waitForConnection()
#device.wake()  #pobudjuje uredjaj i sam od sebe upali i rotaciju telefona
MonkeyRunner.sleep(8)

print('\nTest - Testiranje Type Metode')

# Setuje/podesava path varijablu sa punim imenom .apk fajla
package = 'io.selendroid.testapp'
activity = '.HomeScreenActivity'
runComponent = package + '/' + activity
# Pokrece (Run) komponentu
device.startActivity(component=runComponent)

#ispisuje poruku o pokrenutoj aplikaciji
#MonkeyRunner.help('io.selendroid.testapp') #Ne znam sta je uradila ova komanda???

#komanda za izbor nke od zeljenih opcija napisanih u vidu liste
y = MonkeyRunner.choice("Izaberite koliko ponavljanja zelite", [1, 2, 3, 4, 5])

# Pauzira izvrsenje programa na 3 sekunde da bi se aktivnost ucitala
MonkeyRunner.sleep(5)

x = 1 
while (x <= y):
	print "Krug: ", x
	x = x + 1
	#klik na EN Button
	device.touch(362, 136, "DOWN_AND_UP")
	#klik na No, no
	device.touch(352, 450, "DOWN_AND_UP")
	#klik na folder
	device.touch(370, 220, "DOWN_AND_UP")
	#klik na polje za Username
	device.touch(230, 172, "DOWN_AND_UP")
	MonkeyRunner.sleep(3)
	#ovde stavi type() metodu
	device.type("bane")
	MonkeyRunner.sleep(3)
	#klik na E-mail polje
	device.touch(104, 302, "DOWN_AND_UP")
	#ovde stavi drugu type() metodu
	device.type("bane1manojlovic@gmail.com")
	#klik na Password polje
	device.touch(70, 448, "DOWN_AND_UP")
	#ovde stavi narednu type() metodu
	device.type("MojaLozinka")
	#povukao sam ekran na gore
	device.drag((232, 400), (242, 110), 1.0, 10)
	MonkeyRunner.sleep(3)
	#klik nA IZBOR JEZIKA
	device.touch(436, 428, "DOWN_AND_UP")
	MonkeyRunner.sleep(3)
	#stikliram Python
	device.touch(420, 482, "DOWN_AND_UP")
	MonkeyRunner.sleep(3)
	#povlacim ekran na gore
	device.drag((250, 370), (250, 90), 1.0, 10)
	MonkeyRunner.sleep(3)
	#stikliram "I accept adds"
	device.touch(24, 388, "DOWN_AND_UP")
	MonkeyRunner.sleep(3)
	#klik na Register User dugme (prvo)
	device.touch(220, 466, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)
	#klik na Register User dugme (drugo)
	device.touch(230, 360, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)

print('Kraj testa!')
