class ConvertidoraRomano:
    def __init__(self):
        self.__numero = 0
        self.__resultado = ""
        self.__romanos = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        self.__decimales = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

    def rangoNumero(self, numero):
        if 1 <= numero <= 3999:
            self.__numero = numero
        else:
            raise ValueError("Número fuera del rango.")

    def Resultado(self):
        return self.__resultado

    def Convertir(self):
        numero = self.__numero
        self.__resultado = ""
        i = len(self.__romanos) - 1

        while numero > 0:
            while numero >= self.__decimales[i]:
                self.__resultado += self.__romanos[i]
                numero -= self.__decimales[i]
            i -= 1 

        return self.__resultado


