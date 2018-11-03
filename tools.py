def download_gspread(file_name, sheet_name = "Foglio1", key = False, format = "wide", virgola_italiano = False, gc = gc):
  '''questa funzione, dato il nome del file di google spreadsheet
  e dello specifico foglio di calcolo (opzionale) di google
  restituisce un dataframe di pandas
  file_name: str 
  sheet_name: str
  key: boolean
  format: ["wide", "long", None]
  '''
  
  def str_to_float(cell):
    '''trasforma in decimale 
    tutti i valori stringa contententi 
    valori numerici, anche quelli che hanno punti per migliaia e milioni e virgole
    come decimali'''
    
    try:
      if virgola_italiano == True:
        cell = "".join(cell.split("."))
      else:
        pass
      cell = cell.replace(",", ".")
      cell = cell.strip()
      cell = float(cell)
    except:
      cell = cell
    return cell
  
  #questo comando scarica il foglio 1 del foglio di calcolo
  if key == False:
    if sheet_name == "Foglio1":
      worksheet = gc.open(file_name).sheet1
    else:
      worksheet = gc.open(file_name).worksheet(sheet_name)
  elif key == True:
    if sheet_name == "Foglio1":
      worksheet = gc.open_by_key(file_name).sheet1
    else:
      worksheet = gc.open_by_key(file_name).worksheet(sheet_name)
    
  # prendo tutte le righe del foglio
  rows = worksheet.get_all_values()

  # Converto in DataFrame di Pandas ed effettuo la pulizia dei dati con la funzione
  # str_to_float
  
  dati = pd.DataFrame.from_records(rows)
  if format == "wide":
    dati.columns = dati.loc[0]
    dati = dati.drop(0, axis = 0)  
  else:
    pass
  #converte. dove necessario stringhe verso decimali
  dati = dati.applymap(str_to_float)
  dati = dati.apply(lambda x: pd.to_numeric(x, errors='ignore'))
  return dati
