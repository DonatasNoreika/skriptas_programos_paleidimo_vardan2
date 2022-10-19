import os
import time

programos_pavadinimas = 'superprograma.exe'

os.startfile(programos_pavadinimas)
time.sleep(2)
os.system(f"TASKKILL /F /IM {programos_pavadinimas}")
