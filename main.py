from classes import savingsPlan

def maxMin(vList, vValue):
    for i in range(len(vList)):
        vehicle = vList[i]

        if vValue > vehicle.getPayValue():
            print(f"""
            La cuota de este vehiculo es menor a la proporcionada
            Codigo: {vehicle.getCode()}
            Modelo: {vehicle.getModel()}
            Version: {vehicle.getVersion()}
            """)

def search(vList, vCode):
    i = 0
    ret = None
    while i < len(vList):
        if vList[i].getCode() == vCode:
            ret = i
            break
    return ret

if __name__ == "__main__":
    planList = []
    with open("planes.csv") as archive:
        for line in archive:
            data = line.strip().split(";")
            planList.append(savingsPlan(int(data[0]), data[1], data[2], int(data[3]), int(data[4]), int(data[5])))

    while True:
        option = input("""
        ¿Que decea hacer?
        A:  Actualizar el valor del vehículo de cada plan.
        B:  Mostrar código del plan, modelo y versión del vehículo cuyo valor de la cuota sea inferior al valor dado.
        C:  Mostrar el monto que se debe haber pagado para licitar el vehículo.
        D:  Modificar la cantidad cuotas que debe tener pagas para licitar.
        E:  Salir.
        """)
        option.lower()

        if option == "a":
            for i in range(len(planList)):
                print(f"""
                Codigo: {planList[i].getCode()}
                Modelo: {planList[i].getModel()}
                Version: {planList[i].getVersion()}
                """)
                planList[i].setValue(int(input("Ingrese el nuevo valor: ")))
        elif option == "b":
            maxMin(planList, int(input("Ingrese un valor de cuota: ")))
        elif option == "c":
            for i in planList:
                amount = i.getPayRequired() * i.getPayValue()
                print(f"Para licitar el vehiculo: {i.getCode()} se necesita: ${int(amount)}")
        elif option == "d":
            while True:
                while True:
                    code = input("Ingrese el codigo: ")
                    if code.isdigit():
                        code = int(code)
                        break
                    else: print("El codigo ingresado es invalido")
                i = search(planList, code)
                if i != None:
                    newReqPay = int(input("Ingrese la cantidad de cuotas deseadas: "))
                    planList[i].setPayRequired(newReqPay)
                    break
                else: print("El codigo no corresponde a ningun plan existente")
            
        elif option == "e":
            print("Espero haber sido util. By Lucifer")
            break
        else:
            print("La opcion no es valida.")