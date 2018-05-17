# Obiettivo
1. Raccogliere informazioni data di nascita, di morte, altezza e peso di tutti i file ".txt" presenti nella cartella /esercizi/Esercizio_2
2. Sistematizzare tutte le informazioni in Dizionari di Python
3. aggiungere i dizionari con tutte le informazioni ad una lista

tempo a disposizione 30 minuti 

## consiglio: 
```python
import os # libreria che permette di lavorare con il file sistem
import numpy as np # importo la libreria numpy che permette di utilizzare il tipo di dato "missing
dir_di_lavoro = "./esercizi/Esercizio_2/" # directory dove sono presenti i file

#creo una lista vuota dove contenere tutti i file di testo
lista_schede = []

for item in os.listdir(dir_di_lavoro): # esegue un ciclo su tutte le schede presenti 
    if item[-3:] == "txt": # dato che nella cartella ci potrebbero essere altri file, esegue le operazioni solo su quelle che terminano per "txt"
        with open(os.path.join(dir_di_lavoro, item)) as schede:
            scheda = schede.read()
            lista_schede.append(scheda)
```
