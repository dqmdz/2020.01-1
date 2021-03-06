# Creamos una clase de prueba
class Persona:
    def __init__(self,nombre):
        self.nombre = nombre
​
    def __str__(self):
        return self.nombre
​
# Creamos la lista con los objetos
nombres = ["Héctor","Mario","Marta"]
personas = []
​
for n in nombres:
    p = Persona(n)
    personas.append(p)
​
# Escribimos la lista en el fichero con pickle
import pickle
f = open('personas.pck','wb')
pickle.dump(personas, f)
f.close()
​
# Leemos la lista del fichero con pickle
f = open('personas.pck','rb')
personas = pickle.load(f)
f.close()
​
for p in personas:
    print(p)