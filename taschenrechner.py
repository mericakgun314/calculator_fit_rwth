import math
import time
import numpy as np 
import matplotlib.pyplot as plt



print("\nWillkommen zum Pyhton-Taschenrechner!")
running = True
while running:
    # Auswahl
    print("\nAuswahl von Funktionen:")
    print("1) Addition")
    print("2) Subtraktion")
    print("3) Division")
    print("4) Multiplikation")
    print("5) Mittelwert, Summe, Maximum, Minimum einer Liste an Zahlen")
    print("6) Umfang, Fläche eines Kreises")
    print("7) Die Länge der Hypotenuse eines rechtwinkligen Dreiecks")
    print("8) Polynom & Simulation")
    print("9) P-Q Formel")
    print("Um das Programm zu beenden, geben Sie '0' ein.\n")

    # Benutzereingabe
    auswahl = int(input("Bitte geben Sie die Nummer der gewünschten Funktion ein: "))
    print("\n")

    
    if auswahl == 0:
        running = False
        print("Auf Wiedersehen!")
        time.sleep(1)

    # Addition
    elif auswahl == 1:
        print("'Addition(a + b)' gewählt")
        a1 = float(input("a: "))
        b1 = float(input("b: "))
        print(a1, "+", b1, "=", a1 + b1)

    # Substraktion    
    elif auswahl == 2:
        print("'Substraktion(a - b)' gewählt")
        a2 = float(input("a: "))    
        b2 = float(input("b: "))
        print(a2, "-", b2, "=", (a2 - b2))

    # Division
    elif auswahl == 3:
        print("'Division(a / b)' gewählt")
        a3 = float(input("a: "))
        b3 = float(input("b: "))
        print(a3, "/", b3, "=",(a3 / b3))

    # Multiplikation  
    elif auswahl == 4:
        print("'Multiplikation(a * b)' gewählt")
        a4 = float(input("a: "))
        b4 = float(input("b: "))
        print(a4, "*", b4, "=", (a4 * b4))    

    # Mittelwert, Summe, Maximum, Minimum
    elif auswahl == 5:
        print("'Mittelwert, Summe, Maximum, Minimum einer Liste an Zahlen' gewählt")
        eingabe = input("Geben Sie die gewünschten Zahlen ein(Bsp: 2,5,7,4...): ") 
        split_string = eingabe.split(",") # aufgeteilte Liste

        # Umwandlung von Strings in Floats
        split_float = []
        for i in split_string:
            split_float.append(float(i))

        # Mittelwert
        mittel = float(sum(split_float)) / float(len(split_float))    
        print("Mittelwert:", mittel)

        # Summe
        print("Summe:", sum(split_float))

        # Maximum
        print("Maximum:", sorted(split_float, reverse=True)[0])

        # Minimum
        print("Minimum:", sorted(split_float)[0])

    # Umfang, Fläche
    elif auswahl == 6:
        print("'Umfang, Fläche eines Kreises' gewählt")
        durchmesser = float(input("Geben Sie den Durchmesser des Kreises ein: "))
        
        # Umfang
        print("Umfang: ", math.pi * durchmesser, "Meter")

        # Fläche 
        print("Fläche: ", math.pi * (durchmesser / 2)**2, "Quadratmeter")

    # Hypotenuse
    elif auswahl == 7:
        print("'Die Länge der Hypotenuse eines rechtwinkligen Dreiecks' gewählt")
        a7 = float(input("Erste Kante: "))
        b7 = float(input("Zweite Kante: "))
        print("Hypotenuse:", math.sqrt((a7**2) + (b7**2)))

    # Polynom
    elif auswahl == 8:
        print("'Polynom' gewählt")    
        print("y = Ax^5 + Bx^4 + Cx^3 + Dx^2 + Ex^1 + F")
        input_str_8 = input("Geben Sie die gewünschten Konstanten ein( Bsp: A,B,C,D,E,F ): ")
        spl_string_8 = input_str_8.split(",")
        k = []
        for i in spl_string_8:
            k.append(float(i))

        x = np.linspace(-50, 50, 500)
        y = k[0] * x**5 + k[1] * x**4 + k[2] * x**3 + k[3] * x**2 + k[4] * x + k[5]

        plt.plot(x, y)
        plt.title("y = " + str(k[0]) + "x^5 + " + str(k[1]) + "x^4 + " + str(k[2]) + "x^3 + " + str(k[3]) + "x^2 + " + str(k[4]) + "x^1 + " + str(k[5]))
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()     
    
    # PQ
    elif auswahl == 9:
        print("'P-Q Formel' gewählt")
        print("y = Ax^2 + Bx^1 + C")
        input_str_9 = input("Geben Sie die gewünschten Konstanten ein( Bsp: A,B,C ): ")
        spl_string_9 = input_str_9.split(",")
        k = []
        for i in spl_string_9:
            k.append(float(i))
        
        if k[0] > 1 or k[0] < -1:
            k[1] = k[1] / k[0]
            k[2] = k[2] / k[0]
        
        p, q = k[1], k[2]
        print(k)
        
        im = (p/2)**2 - q
        print(im)
        if im < 0:
            print("\nx1 =", -(p / 2), "+", np.sqrt(im * -1), "* i")  
            print("x2 =", -(p / 2), "-", np.sqrt(im * -1), "* i")
        else:
            print("x1 =", -(p / 2) + np.sqrt((p/2)**2 - q))    
            print("x2 =", -(p / 2) - np.sqrt((p/2)**2 - q))
    
    time.sleep(1)    
