import time
import sys

def type_text(text, delay=10):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

lyrics = [ 
    "SÓ DEPOIS QUE EU FIZ FAMA ★ ★",
    "\nCANTANDO CHEI DE SAL 🧂"
]


for line in lyrics:
    type_text(line, delay=0.05)
    time.sleep(1.70)

lyricsmefalou = [
    "\nME FALOOOUUU",
    "\nME FALA!!!!!"
]
time.sleep(1)
for line in lyricsmefalou:
    type_text(line, delay=0.05)
    time.sleep(0.2)

    

lyrics2 = [
    "\nEU SOU MAIS TOP QUE O CHRIS BROWN "
]

time.sleep(1)
for line in lyrics2:
    type_text(line, delay=0.05)
    time.sleep(1.2)

time.sleep(0.7)
lyrics3 = [
    "\nELA GOSTA É DE LEITE  QUENTE 🥛",
    "\nELA TOMA NA XOTA, TOMA NO (UUUuuunnnnn)",
    "\nMELHOR QUE OS PROTETOR DA SUNDOWN 🧴🧴",
    "\nELA QUER LEITE DE PIRUUUUUUUUU 🦃🦃",
    "\nELA QUER O MEU SEMEEENNNNNNNN"
]

time.sleep(0.5)
for line in lyrics3:
    type_text(line, delay=0.05)
    time.sleep(1.70)