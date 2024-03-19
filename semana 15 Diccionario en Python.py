# Crear el diccionario informacion_personal
informacion_personal = {
    "nombre": "Dina",
    "edad": 42,
    "ciudad": "Orellana",
    "profesion": "Ingeniero"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Orellana"

# Agregar una nueva clave-valor que represente la "profesion" de la persona
informacion_personal["profesion"] = "Ingeniero"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0996175985"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario resultante
print(informacion_personal)

