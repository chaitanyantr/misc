import epm_class
import time

epmOne = epm_class

epmOne.gpio_clean()

tic = time.time()
epmOne.epm(True)
time.sleep(5)
epmOne.epm(False)

