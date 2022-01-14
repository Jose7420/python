# ejercicio 1


import re
nombre = "Juan"
apellido = "Perez"
balance = 53.44
print(("Hola %s %s. Tu saldo es %.2f ") % (nombre, apellido, balance))

# ejercicio 2
a_float = float("3.14")

b_string = str(a_float)

c_int = int(a_float)

d_bool = bool(a_float)

print(type(a_float))
print(type(b_string))
print(type(c_int))
print(type(d_bool))

# ejercicio 3
a = 1234567
b = "Hola como estas"
c = 15.2

print(len(str(a)))
print(len(b))
print(len(str(c)))


# ejercicio 4

b = "Hola esto es una prueba"


print(b.lower())
print(b.strip())
print(b.upper())
print(b.find("o"))
print(b.index("l"))
print(b.startswith("H"))

# ejercicio 5
frase = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor». Fuente: «Capítulo primero. Que trata de la condición y ejercicio del famoso hidalgo don Quijote de la Mancha."
bus = re.findall("a", frase)
print(len(bus))
