# Obiettivo
creare una funzione che raccolga tutte le informazioni relative ad una scheda 

tempo a disposizione 30 minuti 

## consiglio: 
```python
def estrai_data(scheda):
    '''
    doc string
    scheda: passiamo alla funzione la stringa di testo contenente le informazioni
    '''

    try:
        Data_Nascita = scheda.split("Nascita: ")[1].split(",")[0]
    except:
        Data_Nascita = np.nan
    try:
        Descrizione =  scheda.split(" Wikipedia")[0]
    except:
        Descrizione = np.nan
    try:
        Decesso = scheda.split("Decesso: ")[1].split(",")[0]
    except:
        Decesso = np.nan
    try:
        Altezza = scheda.split("Altezza: ")[1].split(" m")[0]
    except:
        Altezza = np.nan
    try:
        Figli = scheda.split("Figli: ")[1].split("\n")[0].split(", ")
    except:
        Figli = np.nan
    try:
        Coniuge = scheda.split("Coniuge: ")[1].split("\n")[0].split(", ")
    except:
        Coniuge = np.nan
    try:
        Peso = scheda.split("Peso: ")[1].split(" kg")[0]
    except:
        Peso = np.nan
        
    
    dizionario = {
    "Data_nascita": Data_Nascita,
    "Decesso": Decesso,
    "Alezza": Altezza,
    "Descrizione": Descrizione,
    "Figli": Figli,
    "Coniuge": Coniuge,
    "Peso": Peso
    }
    
    return dizionario
```
