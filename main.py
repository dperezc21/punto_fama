import archivos_externos as archivos
lista_numeros = ["0","1","2","3","4","5","6","7","8","9"]
lista_numeros_usados = []
lista_puntajes = archivos.leer('puntajes_obtenidos.json')



def tratar_adivinar_numero(lista_numeros_usados, lista_puntajes):
    pass

def numeros_usados(numero):
    if numero in lista_numeros_usados:
        return None
    else:
        lista_numeros_usados.append(numero)


def punto_fama(numero_adivinar:str, numero:str, puntaje:dict):
    for i in range(len(numero_adivinar)):
        if numero_adivinar[i] == numero[i]:
            puntaje["punto"] += 1
        elif numero[i] in numero_adivinar:
            puntaje["fama"] += 1
        
    return puntaje

        
if __name__ == '__main__':
    
    numero_adivinar = "1234"

    while True:
        numero = input("ingrese un numero: ")
        if len(numero) == len(numero_adivinar):
            break
        print("el numero debe ser de {} cifra".format(len(numero_adivinar)))
    

    puntaje = {"punto":0, "fama":0}
    resultado = punto_fama(numero_adivinar, numero, puntaje)

    if puntaje["punto"]==len(numero_adivinar):
        print("PUNTO Y FAMA, el numero es {}".format(numero_adivinar))
    else:
        lista_puntajes["puntajes"][numero] = puntaje
        archivos.escribir('puntajes_obtenidos.json', lista_puntajes)
        for clave in resultado:
            print(clave,":",puntaje[clave])


