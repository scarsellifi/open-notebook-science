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
            distribuzione["Cumulata"] = distribuzione["Percentuale"].cumsum()
            
            #distribuzione["cumsum"] = distribuzione[colonna].cumsum()
        except:
            try:
                distribuzione = distribuzione.loc[lista_ordinale]
                distribuzione["Cumulata"] = distribuzione["Percentuale"].cumsum()
                
            except:
                print("errore, non corrispondenza con le categorie")
                

    elif tipo == "cardinale":
        distribuzione.sort_index(inplace = True)
        distribuzione["Cumulata"] = distribuzione["Percentuale"].cumsum()
        distribuzione["Cumulata"].loc[-1] = np.nan
    
    distribuzione.loc["Totale"] = distribuzione.apply(sum)
    distribuzione["Percentuale"] = distribuzione["Percentuale"].round(2)

    
    if save == False:
        return distribuzione
    else:
        distribuzione.to_excel(str(save) + ".xlsx")
        return distribuzione
    
    
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
