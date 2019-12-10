import two_gpio

import time


epmOne = two_gpio

epmOne.epm(True)
time.sleep(5)

epmOne.epm(False)
time.sleep(5)

epmOne.epm('NTL')
time.sleep(5)
