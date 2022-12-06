def Suma(a,b):
    try:
        r = a + b
    except TypeError:
        print("error: tipo de dato no valido")
    else: 
        return r

def Resta(a,b):
    try:
        r = a - b
    except TypeError:
        print("error: tipo de dato no valido")
    else: 
        return r

def Multiplicacion(a,b):
    try:
        r = a * b
    except TypeError:
        print("error: tipo de dato no valido")
    else: 
        return r

def Division(a,b):
    try:
        r = a / b
    except TypeError:
        print("error: tipo de dato no valido")
    except ZeroDivisionError:
        print("error: tipo de dato no valido")
    else: 
        return r