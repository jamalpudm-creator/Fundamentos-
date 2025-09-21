# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento):

    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


descuento_porcentaje = 10

# Montos para sacar el descuento

monto1 = float(input("Ingrese el valor de la primera compra💵: "))
descuento1 = calcular_descuento(monto1, descuento_porcentaje)
monto_final1 = monto1 - descuento1

monto2 = float(input("Ingrese el valor de la segunda compra 💵: "))
descuento2 = calcular_descuento(monto2, descuento_porcentaje)
monto_final2 = monto2 - descuento2

print("\nCompra 1:")
print(f"  Valor total: 💲{monto1:.2f}")
print(f"  Descuento aplicado ({descuento_porcentaje}%): 💲{descuento1:.2f}")
print(f"  Valor final a pagar: 💲{monto_final1:.2f}")

print("\nCompra 2:")
print(f"  Valor total: 💲{monto2:.2f}")
print(f"  Descuento aplicado ({descuento_porcentaje}%): 💲{descuento2:.2f}")
print(f"  Valor final a pagar: 💲{monto_final2:.2f}")