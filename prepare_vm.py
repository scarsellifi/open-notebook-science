import pandas as pd
import os

#effettuo l'importazione della libreria statistica Pandas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import subprocess
import sys

subprocess.call([sys.executable, "-m", "pip", "install", "git+https://github.com/mwaskom/seaborn.git"])

subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade", "-q", "gspread"])

from marradi import dist_frequenza, plot_dist_frequenza, estrai_valore, tabella_di_contingenza
from tools import download_gspread

print("""librerie importate: \n
os - libreria per gestire il sistema operativo \n
numpy as np - libreria per gestire matrici di dati \n
pandas as pd - libreria per gestire matrici a 2d ed effettuare analisi dati \n
seabortn as sns - libreria per la visualizzazione dei dati \n
from marradi import dist_frequenza, plot_dist_frequenza, estrai_valore, tabella_di_contingenza \n
from tools import download_gspread \n 
""" )