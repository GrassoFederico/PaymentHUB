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

### Configurazione

Copiare e incollare il file `config_example.py` in `config.py` andando a inserire nelle apposite variabili i dati corretti per accedere al server MySQL.

# Avvio

**Solamente quando tutte le dipendenze sono state installate** (vedi *Installazione*), è possibile avviare il programma con il comando

```python .\index.py```

All'interno della cartella del progetto.