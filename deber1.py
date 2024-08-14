def calcularpropina(total_cuenta, porcentaje_propina):
    propina = total_cuenta * (porcentaje_propina / 100)
    total_pagar = total_cuenta + propina
    return propina, total_pagar
def main():
    total_cuenta = float(input("Ingresa el total : "))
    porcentaje_propina = float(input("Ingresa el porcentaje de propina: "))
    numero_personas = int(input("Ingresa el número de personas que compartida: "))

    propina, total_pagar = calcularpropina(total_cuenta, porcentaje_propina)

    if numero_personas > 0:
        monto_por_persona = total_pagar / numero_personas
    else:
        monto_por_persona = 0
        print("El número de personas debe ser mayor que cero.")
    
    print(f"Debes dejar una propina de: ${propina:.2f}")
    print(f"El total a pagar es: ${total_pagar:.2f}")

    if numero_personas > 0:
        print(f"Cada persona debe pagar: ${monto_por_persona:.2f}")
main()