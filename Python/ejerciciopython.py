def eje9():
    fecha = int(input("Ingrese alguna fecha en formato numérico"))
    n1 = int(input("Ingresar fecha en formato númerico (DDMMAAAA): "))
    m = n1 % 1000000
    meses = int(m//10000)  
    dias = int(n1//1000000)
    años = n1 % 10000
    print("La fecha es : ", "Dia : ", dias, "Mes :", meses ,"Año : ", años)
    print(dias,meses,años)
#eje9()

def eje10():
    EP = int(input("Ingrese su nota de Exámenes Parciales"))
    TP = int(input("Ingrese su nota de Trabajos Prácticos"))
    EI = int(input("Ingrese su nota del Exámen Integrador"))

    REP = EP*0.3
    RTP = TP*0.2
    REI = EI*0.5
    NotaFinal = REP+RTP+REI

#eje9()
    if(NotaFinal>10):
        print("El resultado es incorrecto, ingrese las notas exactas")

    else:
        print("Su Nota Final es: ", NotaFinal)
    
#eje10()

def eje11():
    AutosVendidos = int(input("Ingrese la cantidad de autos vendidos"))
    i=0
    Precios=[]
    while i < AutosVendidos:
        Precios.append(float(input(f"Ingrese el precio del auto n°{i + 1}: ")))
        Adicional = Precios[i] * 0.05
        print("megustanlosquesosapestosos")
    Comision=(AutosVendidos * 200)

    SalarioTotal = 5500 + Comision + Adicional
    print("Su salario total es de: ", SalarioTotal)

eje11()