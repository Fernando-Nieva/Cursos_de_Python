CONSTANTE="soy una constante";
my_string_variable="VARIABLE N9"
my_bool_variable=True

nombre_tutor="Codi";
print(nombre_tutor);
print(CONSTANTE);
print(my_string_variable,my_bool_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Fernando", "Nieva", 'Mr.Phoenix', 32
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)

