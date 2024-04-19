def line():
    print("TO DO")
     import math
    a = float (input ("Ingrese el coeficiente A: ") )
    b = float (input ("Ingrese el coeficiente B: ") )
    x1 = float (input ("Ingrese el coeficiente X1: ") )
    x2 = float (input ("Ingrese el coeficiente X2: ") )

    y1 = a * x1 + b
    y2 = a * x2 + b
    print (f"""El coeficiente A de su ecuación de la recta es: {a}
El coficiente B de su ecuación de la recta es: {b}
El coeficiente X1 de su ecuación de la recta es : {x1}
El coeficiente X2 de su ecuación de la recta es : {x2}""")
    print (f"""\n Para la siguiente ecuación: 
    Y = {a}X + {b}""")
    print (f"""\n Dados los siguientes puntos:
    P1 ( {x1}, {y1} )
    P2 ( {x2}, {y2} )""")

    d= math.sqrt ((x2 - x1)**2 + (y2 - y1)**2)

    print(f"\n La distancia entre ellos es: {d}")
line()
