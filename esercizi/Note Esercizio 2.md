# Obiettivo
1. Raccogliere informazioni data di nascita, di morte, altezza e peso di tutti i file ".txt" presenti nella cartella /esercizi/Esercizio_2
2. Sistematizzare tutte le informazioni in un Dizionario di Python

tempo a disposizione 30 minuti 

## consiglio: 
```python
import os # libreria che permette di lavorare con il file sistem
os.chdir("./esercizi/Esercizio_2/") # cambia la directory sulla quale si lavora in quella degli esercizi
for item in os.listdir(os.getcwd()): # esegue un ciclo su tutte le schede presenti 
    if item[-3:] == "txt": # dato che nella cartella ci potrebbero essere altri file, esegue le operazioni solo su quelle che terminano per "txt"
        with open(item) as schede:
            print(schede.read())
```