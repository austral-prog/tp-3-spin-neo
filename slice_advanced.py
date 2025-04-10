def slice_advanced():
    Texto = input ("Ingrese un texto:")
    nstring = f"{Texto[4::2]}"
    print(nstring)

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_advanced_test.py` o `python tp3_slice_advanced_test.py`
