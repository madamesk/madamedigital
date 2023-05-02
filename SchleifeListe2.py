for i in 3, -9 , 0:
    erg = i * i
    print(i, "*", i, "=",  erg)
    if i * i > 0:
        print("Die Zahl ist positiv")
    else:
        if i * i < 0:
            print("Die Zahl ist negativ")
        else: 
            print("Die Zahl ist gleich 0")