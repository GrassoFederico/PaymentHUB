# Installazione

### MySQL

È necessario installare MySQL 8 per poter utilizzare il software.

Se non si dispone di MySQL è possibile scaricarlo [qui](https://dev.mysql.com/downloads/file/?id=544662).

Una volta installato MySQL è **fondamentale** creare il database.

Eseguire nella CLI di MySQL i seguenti comandi

```
CREATE DATABASE IF NOT EXISTS payments_hub;
```

Installare successivamente il modulo MySQL per Python

```
pip install mysqlclient
```

### Python

L'applicazione è interamente scritta in Python, linguaggio di programmazione scaricabile da [questo link](https://www.python.org/downloads/release/python-3135/).

Sono anche presenti:

- SQLAlchemy: sistema per l'ORM in Python.
- CheeryPy: piccolo Web Framework dove vengono costruite le pagine web per l'applicativo.

### SQLAlchemy (ORM)

È necessario installare SQLAlchemy per poter utilizzare il software.

Se non si dispone di SQLAlchemy è possibile scaricarlo [qui](https://docs.sqlalchemy.org/en/20/intro.html#installation)

### CherryPy (Web Framework)

È necessario installare CherryPy per poter utilizzare il software.

Se non si dispone di CherryPy è possibile scaricarlo [qui](https://cherrypy.dev/)

**Importante:** installare la seguente dipendenza per permettere al sistema di funzionare correttamente:

```
pip install routes
```

### Configurazione

Copiare e incollare il file `config_example.py` in `config.py` andando a inserire nelle apposite variabili i dati corretti per accedere al server MySQL.

# Avvio

**Solamente quando tutte le dipendenze sono state installate** (vedi *Installazione*), è possibile avviare il programma con il comando

```
python .\bin\app.py
```

All'interno della cartella del progetto.

### Guida all'uso

L'applicativo si presenta come semplice CRUD: si occupa solo di fare operazioni sui dati attraverso delle chiamate, nello specifico:

- `INSERT`: per ciascuna entità è presente un tasto aggiungi. Ciò permette attraverso una modale di inserire un nuovo record.
- `SELECT`: usato per stampare i record delle diverse entità nelle datatables ed elencare le tabelle disponibili
- `UPDATE`: usato per modificare i dati già esistenti. *N.B:* è sufficiente variare il dato all'interno della input senza salvare, infatti l'operazione avviene in tempo reale tramite chiamate ajax.
- `DELETE`: il tasto cancella a fianco di ciascun record ne permette la cancellazione.

*Attenzione:* ci si può spostare da una tabella all'altra cliccando sopra il nome della tabella desiderata nell'elenco a sinistra.

Per usare l'applicativo è importante accedere all'indirizzo http://127.0.0.1:8080

**Assicurarsi** che la porta 8080 (per il servizio HTTP) e la 3306 (per il servizio MySQL) siano libere per evitare problemi di esecuzione.