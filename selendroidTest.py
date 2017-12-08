
import sys
import os
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage


# Connection
device = MonkeyRunner.waitForConnection()


print "Instaliram apk ..."
device.installPackage('C:\Users\manojlovic\Desktop\Test03\selendroid-test-app-0.17.0.apk')

MonkeyRunner.sleep(8)
print "launching myapp..."
device.startActivity(component='io.selendroid.testapp/io.selendroid.testapp.MainActivity')
MonkeyRunner.sleep(3)

device.press('KEYCODE_MENU', MonkeyDevice.DOWN_AND_UP)

