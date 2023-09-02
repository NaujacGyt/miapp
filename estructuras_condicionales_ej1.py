
print("ingrese los dos numeros para la operacion")
num1 = int(input("Numero 1:"))
num2 = int(input("Numero 2:"))

opcion = input("Digite la letra correspondiente a la operacion que quiere realizar con los dos numeros\n\
S s=Suma\n\
R r=Resta\n\
M m=Multiplicacion\n\
D d=Division\n\
digite aqui:"
               )

opcion=opcion.lower()
res = 0
if (opcion == "s"):
    res = num1 + num2
elif opcion == "r":
    res = num1 - num2
elif opcion == "m":
    res = num1 * num2
elif opcion == "d":
    if num2 == 0:
     print("error no se puede dividir entre cero", "0")
     quit()
    elif(num2):
     res = num1 / num2
else:
    print("opcion erronea vuelva a ejecutar.") 
    quit()


if(opcion == "s"):
    opcion = "+"
elif(opcion == "r"):
    opcion = "-"
elif(opcion == "m"):
    opcion = "x"
elif(opcion == "d"):
    opcion = "/"    
signo =(opcion)
print(f"el resultado de tu operacion", num1, signo, num2, "esi gual a:", res )