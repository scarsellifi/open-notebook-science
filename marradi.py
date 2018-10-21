import pandas as pd
import numpy as np

def dist_frequenza(matrice, colonna, save = False, tipo = "categoriale" , lista_ordinale = False):
    '''
    matrice: passare un dataframe di pandas
    colonna: indicare la colonna su cui effettuare la distribuzione di frequenza
    save: [False oppure nome del file] scegli se salvare o meno la tabella in excel
    tipo: 
        "categoriale": classi non ordinate
        "ordinale": classi ordinate
        "cardinale": valori numerici
    lista_ordinale: una lista di valori attraverso il cui ordinare il risultato del tipo ordinale
    '''

    frequenza = matrice[colonna].value_counts(dropna = False)
    percentuale = matrice[colonna].value_counts(normalize = True, dropna = False) * 100
    distribuzione = pd.concat([frequenza, percentuale], axis = 1)
    distribuzione.columns = ["Frequenze", "Percentuale"]
    if tipo == "categoriale":
        pass
    elif tipo == "ordinale": 
        try:
            distribuzione = distribuzione.reindex(lista_ordinale)
            distribuzione = distribuzione.fillna(0)
            distribuzione["Cumulata"] = distribuzione["Percentuale"].cumsum()
            
            #distribuzione["cumsum"] = distribuzione[colonna].cumsum()
        except:
            try:
                distribuzione = distribuzione.loc[lista_ordinale]
                distribuzione = distribuzione.fillna(0)
                distribuzione["Cumulata"] = distribuzione["Percentuale"].cumsum()
                
            except:
                print("errore, non corrispondenza con le categorie")
                

    elif tipo == "cardinale":
        distribuzione.sort_index(inplace = True)
        
    try:
        distribuzione["Cumulata"] = distribuzione["Percentuale"].cumsum()
        
    except:
        print("errore nella rimozione dell'incrocio Totale - Cumulata")    


    distribuzione.loc["Totale"] = distribuzione.apply(sum)
    
    distribuzione["Percentuale"] = distribuzione["Percentuale"].round(2)
    try:
      distribuzione["Cumulata"] = distribuzione["Cumulata"].round(2)
      distribuzione.loc["Totale", "Cumulata"] = ""
    except:
      pass
    
    if save == False:
        return distribuzione
    else:
        distribuzione.to_excel(str(save) + ".xlsx")
        return distribuzione

def estrai_valore(cella):
  try:
    return int(cella[0])
  except:
    return cella
    
    
def tabella_di_contingenza(dataframe, colonna_A, colonna_B, ordine_A = False, ordine_B = False, informativo = False):
    '''
    dataframe: inserire la tabella su cui si vuole fare la tabulazione incrociata
    colonna_A: inserire la stringa di testo che rappresenta l'intestazione della singola colonna
    colonna_B: inserire la stringa di testo che rappresenta l'intestazione della singola colonna
    ordine_A: inserire una lista di valori rappresentativi dell'ordine delle categorie della colonna A
    ordine_B: inserire una lista di valori rappresentativi dell'ordine delle categorie della colonna B
    iformativo: True, permette di avere in una stessa tabella frequenze, frequenze attese e scarti. 
    '''
    # qui aggiuntere tabella con scarti e percentuale.
    # qui andrebbero inserite anche le percentuali di riga
    crosstab = pd.crosstab(dataframe[colonna_A],dataframe[colonna_B], margins = True)
    if ordine_A != False:
        crosstab = crosstab.reindex(ordine_A, axis = 0)
    if ordine_B != False:
        crosstab = crosstab.reindex(ordine_B, axis = 1)
    if informativo == True:
        expected = pd.DataFrame(expected_freq(crosstab), index =  crosstab.index, columns = crosstab.columns)
        crosstab = crosstab.applymap(str) + " " + expected.applymap(lambda x: ("( {:.2f})".format(x) )) + " " + (crosstab - expected).applymap(lambda x: ("( {:.2f})".format(x) ))
    
    return crosstab

def plot_dist_frequenza(distribuzione, tipo = "categoriale", Y = "Percentuale", x_label="Valori", y_label="Percentuale"):
  distribuzione = distribuzione.iloc[:-1, :]
  
  print(distribuzione)
  if tipo == "categoriale":
    distribuzione.index = distribuzione.index.map(lambda x: str(x))
    g = sns.barplot(x = distribuzione.index, y=Y, data=distribuzione)
    x = 0
    for index, row in distribuzione.iterrows():
      stringa = "N.{},\n {}%".format(row.Frequenze, row.Percentuale)
      g.text(x,row.Frequenze, stringa, color='black', ha="center")
      x = x + 1
    g.set(xlabel=x_label, ylabel=y_label)
  
  elif tipo == "ordinale" or tipo == "cardinale":
    index = distribuzione.index
    distribuzione.reset_index(inplace = True)
    g = sns.barplot(x = index, y=Y, data=distribuzione, palette="Blues_d")
    for index, row in distribuzione.iterrows():
      stringa = "F.{},\n {}%".format(row.Frequenze, row.Percentuale)
      
      g.text(row.name,row.Frequenze, stringa, color='black', ha="center")
      g.set(xlabel=x_label, ylabel=y_label)
  return g


