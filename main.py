from machine.enigma import Enigma

def encrypt(words, machine):
    result = []
    for i in words:
          result.append(machine.encrypt_letter(i))
    return "".join(result)

def main():
    #maquina enigma para encriptar
    enigma1 = Enigma("CAD")
    #maquina enigma para desencriptar
    enigma2 = Enigma("CAD")

    words = "CUALQUIERACUALQUIERACUALQUIERACUALQUIRACUALQUIERACUALQUIERACUALQUIERACUALQUIERA"
    print("Encriptado: ")
    result = encrypt(words, enigma1)
    print(result)
    print("Desencriptado: ")
    result2 = encrypt(result, enigma2)
    print(result2)

    #

if __name__ == "__main__":
    main()