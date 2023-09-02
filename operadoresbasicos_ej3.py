from math import sqrt #para importar la funcion sqrt

cateto_a = float(input("ingrese el valor de cateto a:"))
cateto_b = float(input("ingrese el valor del cateto b:"))

hipotenusa = sqrt(cateto_a ** 2 + cateto_b ** 2)

print("le valor de la hipotenusa es:", hipotenusa)