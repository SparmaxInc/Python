def binario_a_decimal(binario):
    decimal = 0
    potencia = 0

    while binario != 0:
        digito = binario % 10
        decimal += digito * (2 ** potencia)
        binario //= 10
        potencia += 1

    return decimal

# Pedir al usuario que ingrese un número binario
try:
    num_binario = int(input("Ingrese un número binario: "))
    decimal_resultado = binario_a_decimal(num_binario)
    print(f"El número decimal equivalente es: {decimal_resultado}")
except ValueError:
    print("¡Error! Ingrese un número binario válido (solo 0s y 1s).")
