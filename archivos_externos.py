import json

def leer(nombre_archivo):
    result=""
    with open(nombre_archivo, 'r') as f:
        result = f.read()
        f.close()
    return json.loads(result)


def editar(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as f:
        f.write(json.dumps(datos, indent=4))
        f.close()

def eliminar_datos(nombre_archivo):
    puntajes = leer(nombre_archivo)
    puntajes.clear()
    puntajes["puntajes"] = {}
    puntajes["numeros_usados"] = {}
    editar(nombre_archivo, puntajes)
    

def eliminar_puntajes(nombre_archivo):
    puntajes = leer(nombre_archivo)
    puntajes["puntajes"].clear()
    editar(nombre_archivo,puntajes)


def eliminar_numeros_usados(nombre_archivo):
    puntajes = leer(nombre_archivo)
    puntajes["numeros_usados"].clear()
    editar(nombre_archivo,puntajes)

def vaciar_diccionario(nombre_archivo,*clave):
    puntajes = leer(nombre_archivo)
    for i in clave:
        puntajes[i].clear()
        print("diccionario de {} completamente vacio".format(i))
    print(puntajes)

    


    
