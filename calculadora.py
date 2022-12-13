class Calculadora:
    
    def __init__(self, n1: int, n2: int) -> None:
        self.__n1 = n1
        self.__n2 = n2
        
    def sumar(self) -> int:
        return self.__n1 + self.__n2