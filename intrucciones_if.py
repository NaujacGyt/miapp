variable_digitada=input("digite su edad: ")
variable_edad = int(variable_digitada)
if(variable_edad < 0):
    print("la edad es incorrecta, no puede ser negativa")
elif(variable_edad == 0):
    print("la edad es incorrecta y debe ser mayor a cero")    
elif(variable_edad > 0 and variable_edad < 18):
    print("es niño o joven no mayor de edad")    
else:
    print("es mayor de edad")