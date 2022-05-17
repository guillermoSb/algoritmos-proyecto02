# Universidad del Valle de Guatemala
# Algoritmos y Estructuras de Datos
# Proyecto #2 - Motor de Recomendaciones

from RecommendationEngine import *
from View import *


def init():
    # Configure the Recommendation Engine
    engine = RecommendationEngine("neo4j+s://1693e124.databases.neo4j.io", "neo4j",
                                  "kwRfn1Ak-qqe7Jxybt8SwplT5--cP1cfEcIuo5tJlnM")
    View.greeting() # Show greeting message
    # Ask user to register or sign in
    opt = 0 # keep track of the option selected
    while opt != 3 and opt != 2 and opt != 1:
        try:
            opt = int(View.user_menu())
            if opt < 0 or opt > 3:
                print("El valor ingresado no está en el rango de opciones.")
            if opt == 3:
                return

        except ValueError:
            print("El valor ingresado no es un numero.")

    # Decide if the user needs to be registered or signed in
    if opt == 1:
        print("sign in")
    elif opt == 2:
        print("register")
    # Show the configuration menu for the user if the user is not configured yet

    # Show the options for the recommendation engine



if __name__ == '__main__':
    init()

