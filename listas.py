lenguajes = ["Python", "Csharp", "PHP", "GO", "JAVA", "Javascript"]
#print(lenguajes)
#print(lenguajes[2])
#lenguajes[2]="C++"
#print(lenguajes[-1])
#print(lenguajes[1:3])
#print(lenguajes[:3])
#print(lenguajes[1:])
#lenguajes.insert(3, "Cobol")
#lenguajes.insert(0,"Pascal")

#lenguajes.remove("PHP")

#print("PHP" in lenguajes)
#print(lenguajes)
#lenguajes.append("c")
#print(len(lenguajes))

"""tupla = ("C++", True, 25)
print(tupla[1])
print(tupla.count(True))
print(tupla.index("C++"))"""


lenguajes2 = ["Python", "Csharp", "PHP", "GO", "JAVA", "Javascript"]
personas =[ [1,"Carlos",25], [2, "Tomas", 15], [3, "Mauricio", 36]  ]

personas[1] [1] = "Pedro" #para reemplazar un elemento de la lista

#print(personas[1]) #para implrimir un elemento de la lista
#print(personas[1][1]) #para implrimir un elemento de un elemento de la lista


array_datos = [[]]
array_datos[0].append(1)
array_datos[0].append("Satiago")
array_datos[0].append(17)

array_datos.append([])
array_datos[1].append(2)
array_datos[1].append("Tomas")
array_datos[1].append(35)

print(array_datos)