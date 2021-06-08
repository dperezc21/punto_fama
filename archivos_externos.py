import json

def leer(nombre_archivo):
    result=""
    with open(nombre_archivo, 'r') as f:
        result = f.read()
        f.close()
    return json.loads(result)


def escribir(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as f:
        f.write(json.dumps(datos, indent=4))
        f.close()


    
