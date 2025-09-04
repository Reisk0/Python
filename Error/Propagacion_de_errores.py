#codigo hijo, que esta mal

def funcionerror(): 
    try:
        a = 10/10
    except: 
        print("Algo malo paso")
#El codigo papa lleva el try para evitar saturar el codigo hijo
    try: 
        print("Antes del error")
        funcionerror()
        print("Despus del error")
    except: 
        print("Algo paso")