
class View:

    @staticmethod
    def greeting():
        print("****************************************************")
        print("Bienvenid@ al sistema de recomendación para carros.")
        print("****************************************************")

    @staticmethod
    def user_menu() -> str:
        print("Usuario")
        print("-------------------")
        print("1. Iniciar Sesion")
        print("2. Registrarse")
        print("3. Cerrar el programa")
        return input("")