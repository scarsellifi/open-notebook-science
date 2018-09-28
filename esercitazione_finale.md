# Esercitazione finale

## Creazione della squadra di lavoro
Si consiglia di creare una squadra di 5 persone dalle competenze eterogenee di cui almeno un:

* esperto tematico rispettivamente al tema scelto
* una persona con una buona base statistica
* una persona con buone capacità di lavoro sui dati

## Individuazione del progetto

si consiglia di rispondere alle seguenti domande:

* scopo della ricerca
* dati disponibili



## Indicazioni generali Documentare ogni passaggio tramite celle markdown

### Passaggi:

1. Selezionare il/i dataset: spiegare il perchè della scelta ed il risultato atteso

1. Salvarle e caricare il/i dataset sulla piattaforma

1. Trasformare il/i dataset in uno più DataFrame di Pandas

1. Effettuare le elaborazioni

1. Descrivere i risultati con tabelle e grafici

### Eurostat
per l'esercitazione finale è possibile utilizzare qualsiasi dataset. Si consiglia di usare i
dati [Eurostat](http://ec.europa.eu/eurostat/data/database?p_p_id=NavTreeportletprod_WAR_NavTreeportletprod_INSTANCE_nPqeVbPXRmWQ&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_pos=1&p_p_col_count=2=) con la nostra liberia di importazione [tsv_to_pandas](https://github.com/datalifelab/tsv_to_pandas)


## Per i progetti che vogliono seguire al 100% la filosofia open-notebook-science:
1. creare un utente github [](https://github.com)
1. creare un repository github
1. aprire terminale linux
1. navigare nella cartella
``` bash
cd /path/to/your/repo
```

1. usare il seguente codice

``` bash
git init
git add -A
git commit -m "commit iniziale"
git remote add origin https://github.com/<nome-utente>/<nome-progetto>.git
git push -u origin master
```

1.ogni volta che si voglia salvare un **commit**
``` bash
git add -A
git commit -m "descrizione del commit"
git push origin master
```

## Per i progetti che vogliono inizalmente rimanere privati
[](https://bitbucket.org/)

1. creare un utente bitbucket (https://bitbucket.org/)
1. creare un repository bit-bitbucket
1. aprire terminale linux
1. navigare nella cartella

``` bash
cd /path/to/your/repo
```

1. usare il seguente codice
``` bash
git init
git add -A
git commit -m "commit iniziale"
git remote add origin https://<nome-utente>@bitbucket.org/<nome-utente>/<nome-progetto>.git
git push -u origin master
```

1.ogni volta che si voglia salvare un **commit**
``` bash
git add -A
git commit -m "descrizione del commit"
git push origin master
```
