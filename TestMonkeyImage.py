from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

# Connection
device = MonkeyRunner.waitForConnection()
#device.wake()  #pobudjuje uredjaj i sam od sebe upali i rotaciju telefona
MonkeyRunner.sleep(8)

print('\nTest - Testiranje MonkeyImage modula')

# Setuje/podesava path varijablu sa punim imenom .apk fajla
package = 'io.selendroid.testapp'
activity = '.HomeScreenActivity'
runComponent = package + '/' + activity
# Pokrece (Run) komponentu
device.startActivity(component=runComponent)
MonkeyRunner.sleep(8)

# Uzima/slika  screenshot 1
slika1 = device.takeSnapshot()
# Memorise screenshot u preciziran fajl
slika1.writeToFile('C:\Users\manojlovic\Desktop\slika1.png','png')
print "Slika napravljena i snimljena"
MonkeyRunner.sleep(5)

#konvertuje sliku u niz bajtova, tj bajt koordinata
#m = MonkeyImage.convertToBytes(slika1)
#print m   #kada ovo odkomentarisem, dobicu ispis tih bajt koordinata

slika1 = MonkeyImage.getRawPixel(10, 10)
print slika1


# Pauzira izvrsenje programa na 3 sekunde da bi se aktivnost ucitala
MonkeyRunner.sleep(5)

x = 1 
while (x <= 1):
	print "Krug: ", x
	x = x + 1
	#klik na EN Button
	device.touch(362, 136, "DOWN_AND_UP")
	#klik na No, no
	device.touch(352, 450, "DOWN_AND_UP")
	MonkeyRunner.sleep(5)
	#uzimam screenshot 2
	slika2 = device.takeSnapshot()
	slika2.writeToFile('C:\Users\manojlovic\Desktop\slika2.png','png')
	MonkeyRunner.sleep(5)

print('Kraj testa!')