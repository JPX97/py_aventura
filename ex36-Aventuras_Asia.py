from sys import exit

vacunas = False

def dead(why):
    print(why, "Te esperaba más inteligente.")
    exit(0)

def intro():
    print("Madrid. Son las 9am de la mañana, te duele la cabeza…\n"
    "Recuerdas que tienes las vacunas a las 10am, ¿qué haces?\n"
    "¿Correr o dormir (y perderte las vacunas)?\n")


    while True:
        choice = input("> ")

        if choice == "correr":
            print("Sales corriendo y coges el autobús de milagro.\n"
            "Tras un buen rápido en transporte público llegas al centro para vacunarte\n"
            "Ahora estás inmunizado de la rabia y el cólera.\n"
            "¡Bendita ciencia!\n")

            global vacunas
            vacunas = True

            london()

        elif choice == "dormir":
            print("Se está demasiado bien durmiendo… Además, no creo que necesite vacunas, ¿verdad?\n"
            "Duermes hasta las 3pm\n")

            london()

        else:
            print("No entiendo lo que quieres hacer")


def london():
    print("… Tras un primer vuelo bastante rápido estás en un aeropuerto en Londres esperando a coger el vuelo de escala destino a Mumbai.\n"
    "Tienes ganas de ir al baño, ¿qué haces con el pasaporte y tu billete?\n"
    "\t 1. Lo llevas encima\n"
	"\t 2. Se lo dejas a alguien para que te lo vigile\n")


    while True:
        choice = input("> ")

        if choice == "1":
            print("Eres precavido.\n"
            "Vas al baño con normalidad…\n"
            "Te subes al avión y te duermes rápidamente.\n")
            inicio_mumbai()

        elif choice == "2":
            print("Vuelves y ¡tu pasaporte no está!\n"
            "¿Qué ha pasado con él?\n"
            "Tu imprudencia ha hecho que no te puedas subir al avión.\n")

            dead("Tu viaje acaba aquí.")

        else:
            print("No entiendo lo que quieres hacer")

def inicio_mumbai():
    print("""\
    //////////////////////////////////////////////////
    //////////////////////////////////////////////////
    //////////////////////////////////////////////////
    //////////////////////////////////////////////////
    //////////////////////////////////////////////////
    .......................----.......................
                         -/::::/-
                        -/.+ss+./-
                        -/.+ss+./-
                         -/::::/-
    ----------------------:////:----------------------
    hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
    hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
    hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
    hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
    hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
    """)

    print("Llegas a Mumbai sin mucho problema\n"
    "Hace mucho calor y todo es un poco caótico…\n"
    "Te instalas en el hotel y vais a cenar…\n"
    "Una vez llegas al restaurante pides de comer y el camarero te pregunta ¿spicy?\n")

    while True:
        choice = input("> ")

        if choice == "sí" or choice == "si":
            print("Parece que este picante era mucho más picante de lo que esperabas")
            bebida()
        elif choice == "no":
            print("El camarero ha ignorado tu petición y la comida está muy picante.")
            bebida()

        else:
            print("No entiendo lo que quieres hacer")

def bebida():
    print("Te arde la boca y el camarero te pregunta si quieres algo de pedir, ¿qué bebes?\n"
    "¿Agua o Lassi?\n")

    while True:
        choice = input("> ")

        if choice == "Agua" or choice == "agua":
            print("Aunque el agua tiene mala pinta, te la bebes de un trago.")
            agua()
        elif choice == "Lassi" or choice == "agua":
            print("Está delicioso!\n"
            "El picor baja, te empiezas a encontrar mejor\n")
            perros()

        else:
            print("No entiendo lo que quieres hacer")
def agua():
    global vacunas

    if vacunas == True:
        print("En este momento te acuerdas que te vacunaste del cólera y te ves tranquilo\n")
        perros()
    else:
        print("Empiezas a tener sudores fríos y te duele mucho el estómago.\n"
        "Parece que tienes el Cólera\n"
        "Te empiezas a preguntar, ¿por qué no me habré vacunado?\n")

        dead("Tu viaje acaba aquí.")

def perros():
    print("Después de una rica (y picante) cena, volvéis andando al hotel.\n"
    "Todo parece muy tranquilo pero…\n"
    "¡De repende aparece una jauría de perros rabiosos?\n"
    "¿Qué haces? ¿Correr o no hacer nada?\n")

    choice = input("> ")

    if choice == "correr":
        print("Sales corriendo y ellos detrás tuya…\n"
        "Son más rápidos que tu y acaban mordiéndote un par…\n")
        mordida()
    else:
        print("No haces nada y ellos se van por donde vinieron, la calma te ha ayudado esta vez\n"
        "¡Bien hecho!\n")
        building()

def mordida():
    global vacunas

    if vacunas == True:
        print("Te han jodido la pierna, pero gracias a que tienes la vacuna de la rabia, te da tiempo a llegar al hospital")
        building()

    else:
        print("Te han jodido la pierna y lo peor es que parecía que tenían la rabia…\n"
        "Corres al hospital pero te estás empezando a quedar inconsciente...\n"
        "Te empiezas a preguntar, ¿por qué no me habré vacunado?\n")

        dead("No llegas al hospital, estás muerto.")

intro()

def building():
    print("Todavía en desarrollo, espero que os guste ;)")
