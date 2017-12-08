from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

# Connection
device = MonkeyRunner.waitForConnection()
#device.wake()  #pobudjuje uredjaj i sam od sebe upali i rotaciju telefona
MonkeyRunner.sleep(8)

print('\nTest - Testiranje pres() metode')

# Setuje/podesava path varijablu sa punim imenom .apk fajla
package = 'io.selendroid.testapp'
activity = '.HomeScreenActivity'
runComponent = package + '/' + activity
# Pokrece (Run) komponentu
device.startActivity(component=runComponent)
MonkeyRunner.sleep(8)


# Klik na dugme MENU u aplikaciji
device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)  #otvara one tri crtice (hamburger meni)

print('klik na dugme')
device.press('visibleButtonTest')

MonkeyRunner.sleep(3)

print('kraj testa')