# Imports
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

# Constants
duration = 1
steps    = 30

# Connection
device = MonkeyRunner.waitForConnection()
print("Test zapocet")

package = 'com.appparkingspot'
activity = '.ActivitySplash'
runComponent = package + '/' + activity
print('Launching app')
print(runComponent)

device.startActivity(component = runComponent )

MonkeyRunner.sleep(6)
# Deploy your app, add your intent, if needed


# Touch or drag
device.touch(144, 198, "DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(466, 1684, "DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(346, 1083, "DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(1110, 2203, "DOWN_AND_UP")
MonkeyRunner.sleep(3)
device.touch(144, 198, "DOWN_AND_UP")
print('Kraj testa!')