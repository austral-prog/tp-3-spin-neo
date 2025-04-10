def slice_simple():
    texto = "Awesome"
    Awe= f"{texto[:3].lower()}"
    eso= f"{texto[2:5].lower()}"
    Full= f"{texto[:] .lower()}"
    print(Awe)
    print(eso)
    print(Full)
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.
 
# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
