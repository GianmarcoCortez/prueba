while True:
    print("Menú de recomendaciones")
    print("   1. Literatura")
    print("   2. Cine")
    print("   3. Música")
    print("   4. Videojuegos")
    print("   5. Salir")
    OP=int(input("Elija una opción (1-5): "))
    if OP==1:
        print("Lecturas recomendables:")
        print(" + Esperándolo a Tito y otros cuentos de fúbol (Eduardo Sacheri)")
        print(" + El juego de Ender (Orson Scott Card)")
        print(" + El sueño de los héroes (Adolfo Bioy Casares)")
    elif OP==2:
        print("Películas recomendables:")
        print(" + Matrix (1999)")
        print(" + El último samuray (2003)")
        print(" + Cars (2006)")
    elif OP==3:
        print("Discos recomendables:")
        print(" + Despedazado por mil partes (La Renga, 1996)")
        print(" + Búfalo (La Mississippi, 2008)")
        print(" + Gaia (Mägo de Oz, 2003)")
    elif OP==4:
        print("Videojuegos clásicos recomendables")
        print(" + Día del tentáculo (LucasArts, 1993)")
        print(" + Terminal Velocity (Terminal Reality/3D Realms, 1995)")
        print(" + Death Rally (Remedy/Apogee, 1996)")
    elif OP==5:
        print("Gracias, vuelva pronto")
        break
    else:
        print("Opción no válida")
        break