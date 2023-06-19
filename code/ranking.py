import sqlite3, traceback 

def create(nombre_bd:str) -> bool:
    '''
    Se conecta con el archivo de la base de datos y crea la tabla "ranking" solamente si esta no existe. Le agrega los campos:
    
    - id: Como clave principal de tipo entero (integer) y auto-incremental.
    - nombre: Como texto (text) que representará el nombre del jugador.
    - score: Como número real (real) que representará el puntaje del jugador.
    
    En caso de error, lo muestra en pantalla. 
    '''
    with sqlite3.connect(nombre_bd) as conexion:
        try:
            sentencia = '''
            CREATE TABLE IF NOT EXISTS ranking
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                score INTEGER
            )
            '''
            
            conexion.execute(sentencia)
            
        except:
            traceback.print_exc()
        
def update(nombre_bd:str, usuario:str, score:int) -> None:
    '''
    Se conecta a la base de datos y actualiza el "score" del jugador por su puntuacion maxima. Si el jugador no se encuentra en la tabla, lo agrega.
    
    En caso de error, lo muestra en pantalla.
    '''
    with sqlite3.connect(nombre_bd) as conexion:
        try:
            #? Se ejecuta cundo se ingresa un nombre 
            if usuario:
                #? Verifica si ya existe en la tabla
                cursor = conexion.execute('SELECT score FROM ranking WHERE nombre = ?', (usuario,))
                fila = cursor.fetchone() #? Devuelve una tupla con un elemento  
                
                if fila: #? Si el nombre existe, compara el score actual con el nuevo
                    score_actual = fila[0]
                    if score > score_actual:
                        sentencia = 'UPDATE ranking SET score = ? WHERE nombre = ?'
                        conexion.execute(sentencia, (score, usuario))
                else: #? Si no existe, lo agrega al ranking
                    sentencia = 'INSERT INTO ranking(nombre, score) VALUES (?, ?)'
                    conexion.execute(sentencia, (usuario, score))
                conexion.commit()
                
        except:
            traceback.print_exc()
            
def select(nombre_bd:str) -> list:
    '''
    Se conecta a la base de datos y devuelve una lista con las filas de la tabla "ranking" ordenadas por score de mayor a menor.
    
    Retorna una lista vacia ocurre un error o si no hay datos en la tabla.
    '''
    
    try:
        with sqlite3.connect(nombre_bd) as conexion:
            cursor = conexion.execute('SELECT * FROM ranking ORDER BY score DESC')
            filas = cursor.fetchall()
            return filas
    except:
        traceback.print_exc()
        return []