# Obiettivo
1. Raccogliere informazioni data di nascita, di morte, altezza e peso di tutti i file ".txt" presenti nella cartella /esercizi/Esercizio_2
2. Sistematizzare le informazioni in un Dizionario di Python. Prendere solo:
  * data di nascita
  * decesso
  * altezza
  * peso
  se un dato è mancante assegnare il valore np.nan (equivalente ai missing) o None (equivalente a valore nullo)
3. Dal Dizionario di Python creare un dataframe di Pandas

tempo a disposizione 30 minuti 

## consiglio: 
```python
import os # libreria che permette di lavorare con il file sistem
import numpy as np # importo la libreria numpy che permette di utilizzare il tipo di dato "missing
dir_di_lavoro = "./corso-open-notebook-science/esercizi/Esercizio_2/" # directory dove sono presenti i file
for item in os.listdir(dir_di_lavoro): # esegue un ciclo su tutte le schede presenti 
    if item[-3:] == "txt": # dato che nella cartella ci potrebbero essere altri file, esegue le operazioni solo su quelle che terminano per "txt"
        with open(os.path.join(dir_di_lavoro, item)) as schede:
            print(schede.read())
```
