# Universidad del Valle de Guatemala
# Algoritmos y Estructuras de Datos
# Proyecto #2 - Motor de Recomendaciones

from engine import RecommendationEngine


def init():
    print("Iniciando motor de recomendaciones")
    engine = RecommendationEngine("neo4j+s://1693e124.databases.neo4j.io", "neo4j",
                                  "kwRfn1Ak-qqe7Jxybt8SwplT5--cP1cfEcIuo5tJlnM")
    engine.print_greeting("guille")


if __name__ == '__main__':
    init()

