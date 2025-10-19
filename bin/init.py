# Inzializza ORM e Database

from init_database import engine, text

# Importa dipendenze

import json

# Inizializza delle funzioni per facilitare l'utilizzo dell'ORM

def execute_query(query: str) -> dict:
    results = engine.connect().execute(text(query)).mappings().all()

    results = [json.loads(str(row).replace("'", '"')) for row in results]

    return json.dumps(results, default=str).encode('utf8')