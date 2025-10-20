# Inzializza ORM e Database

from init_database import engine, text

# Inizializza delle funzioni per facilitare l'utilizzo dell'ORM

def execute_query(query: str, args: dict = {}) -> dict:
    try:
        conn = engine.connect()

        results = conn.execute(text(query), args).mappings().all()

        results = [str(row).replace("'", '"') for row in results]
        
        conn.close()

        return ("[" + ','.join(results) + "]").encode('utf8')
    except Exception as e:
        print(str(e))
        
        conn.close()

        return dict()
    
def execute_statement(query: str, args: list = []) -> bool:
    try:
        conn = engine.connect()

        result = conn.execute(text(query), args)
 
        conn.commit()

        conn.close()

        return result
    except Exception as e:
        print(str(e))

        conn.close()

        return False