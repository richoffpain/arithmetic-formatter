def arithmetic_arranger(problemas, mostrar_resultado=False):
    if len(problemas) > 5:
        return "Error: Too many problems."

    acomodar_eje = {"arriba": [], "abajo": [], "barra": [], "resultado": []}
    # Por cada problema existente, desempaqueta cada uno y asignale sus valores a estos variables
    for cada_operacion in problemas:
        modelado = cada_operacion.split()
        cifra1, operator, cifra2 = modelado

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        if not cifra1.isdigit() or not cifra2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(cifra1) > 4 or len(cifra2) > 4:
            return "Error: Numbers cannot be more than four digits."
        # definir la cifra con el mayor numero de digitos y en base a esto añadirle 2 mas para luego usar como el tamaño de la anchura que tiene que ocupar los guiones bajos
        anchura = max(len(cifra1), len(cifra2)) + 2
        acomodar_eje["arriba"].append(cifra1.rjust(anchura))
        acomodar_eje["abajo"].append(operator + cifra2.rjust(anchura - 1))
        acomodar_eje["barra"].append("-" * anchura)

        if mostrar_resultado:
            resultado = str(eval(cada_operacion)).rjust(anchura)
            acomodar_eje["resultado"].append(resultado)

    formato_aritmetico = (
        "    ".join(acomodar_eje["arriba"]) + "\n" +
        "    ".join(acomodar_eje["abajo"]) + "\n" +
        "    ".join(acomodar_eje["barra"])
    )

    if mostrar_resultado:
        formato_aritmetico += "\n" + "    ".join(acomodar_eje["resultado"])

    return formato_aritmetico


def main():
    mostrar_resultado = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
    print(mostrar_resultado)


if __name__ == '__main__':
    main()