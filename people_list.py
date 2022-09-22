
"""
Esta aplicación nos permite crear y agregar usuarios a un archivo que definamos en una url ubicada en nuestro home, 
por otro parte podemos consultarla en su totalidad, o por genero, edad o nombre
"""

"Definir una url dentro de tu home"
url= "colocar url de tu home" 

"Función para crear y agregar personas con su edad y genero"
def add(name, age, gender):
    with open (url, "a") as document:
        file=f" {name}, {age}, {gender} \n"
        document.write(file)
        print("-"*40)
        print("Se ha agregado una persona exitosamente")
        print("-"*40)

"Función para consultar la totalidad de las personas en la lista"
def list():
    with open(url, "r") as document:
        print("-"*30)
        print("Lista Actualizada")
        print(document.read())
        print("-"*30)

"Función para consultar por genero las personas de la lista"
def list_gender(letter_gen):
    with open(url, "r") as documents:
        documents.seek(0,0)
        for document in documents:
            document=document.strip("\n")
            name,age,gender=document.split(",")
            if letter_gen==gender:
                print(document)

"Función para consultar por edad las personas de la lista"
def list_age(number_age):
    with open(url, "r") as documents:
        documents.seek(0,0)
        for document in documents:
            document=document.strip("\n")
            name,age,gender=document.split(",")
            if number_age==age:
                print(document)

if __name__=="__main__":
    while True:
        selection=int(input("Seleccione la acción que desea hacer (1-Agregar personas, 2-Listar personas, 3-Buscar por genero, 4-Buscar por edad, 5-Cerrar registro) "))

        if selection==1:
            name=input("Ingrese el nombre de la persona: ").strip().capitalize()
            age=input("Ingrese la edad de la persona: ").strip()
            gender=input("Ingrese el genero de la persona (F-Femenino, M-Masculino)" ).strip().upper()
            add(name, age, gender)
            

        elif selection==2:
            list()
            
            
        elif selection==3:
            letter_gen=input("Selecciona el genero que deseas clasificar (F-Femenino, M-Masculino) ").strip().upper()
            list_gender(letter_gen)

        elif selection==4:
            number_age=int(input("Ingresa el valor por la edad que deseas buscar: ").strip())
            list_age(number_age)
                        

        elif selection==5:
            break

        else:
            print("Escoge una opción valida")
       





