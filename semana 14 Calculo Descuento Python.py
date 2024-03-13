# En el archivo calculo_descuento.py

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento en función del monto total de la compra y el porcentaje de descuento.

    Args:
        monto_total (float): El monto total de la compra.
        porcentaje_descuento (float, optional): El porcentaje de descuento a aplicar.
            Por defecto es 10%.

    Returns:
        float: El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Llamadas a la función
monto_compra_1 = 100
descuento_1 = calcular_descuento(monto_compra_1)
monto_final_1 = monto_compra_1 - descuento_1

monto_compra_2 = 200
porcentaje_descuento_2 = 15
descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
monto_final_2 = monto_compra_2 - descuento_2

# Muestra de resultados
print("Para una compra de $", monto_compra_1)
print("Descuento aplicado: $", descuento_1)
print("Monto final a pagar: $", monto_final_1)

print("\nPara una compra de $", monto_compra_2, "con un descuento del", porcentaje_descuento_2, "%")
print("Descuento aplicado: $", descuento_2)
print("Monto final a pagar: $", monto_final_2)

