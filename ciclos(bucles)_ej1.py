palabra = input("Ingrese Una palabra o una Frase:") #pedimos al usuario que digite una palabra o una frase

def esPalindromo(palabra):
    palabra = palabra.lower()      #convertimos la palabra o frase a minusculas
    palabra = palabra.replace(" ", "") #reemplazamos los espacios por nada (no espacios)  a la frase o palabra que se ingrese para que queden las letras juntas
    palabra = palabra.replace("á", "a") #reemplazamos las palabras tildadas por no tildadas
    palabra = palabra.replace("é", "e") #reemplazamos las palabras tildadas por no tildadas
    palabra = palabra.replace("í", "i") #reemplazamos las palabras tildadas por no tildadas
    palabra = palabra.replace("ó", "o") #reemplazamos las palabras tildadas por no tildadas
    palabra = palabra.replace("ú", "u") #reemplazamos las palabras tildadas por no tildadas
    
    a = 0  #definimos el valor de (a) al primer digito teniendo en cuenta que al contar las letras se interpreta la primera como 0
    b = len(palabra) - 1 #luego realizamos el conteo de la cantidad de letras y le restamos 1 para tener el numero exacto de la ultima posicion

    for i in range(0, len(palabra)): #empezamos a realizar el bucle y la validacion de las letras
        if palabra[a] == palabra[b]: # desde la posicion 0 con la posicion final hacia el centro de la frase o palabra
            a += 1   #realizamos suma a la variable (a) mas 1
            b -= 1   #realizamos resta a la variable (b) menos 1 para posteriormente ser verificados nuevamente
        else:
            return False # si en algun momento la validacion nos da que no es igual nos va a retornar como falso
    return True   #en caso de que la validacion hasta la ultima posicion nos da iguales nos permitira el paso al la siguiente ejecucion

if esPalindromo(palabra): #realizamos validacion al resultado anterior y si nos da true mostrara un mensaje positivo de lo contrario enviara un mensaje de error
    print("Es una palabra o frase palíndroma")
else:
    print("No es una palabra o frase palíndroma")    