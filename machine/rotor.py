class Rotor:
    def __init__(self, pair):
        self.pair = pair
        """
        self.pair = [["A","E"], ["B","K"], ["C","M"], ["D","F"], ["E","L"], ["F","G"], ["G","D"],
        ["H","Q"], ["I","V"], ["J","Z"], ["K","N"], ["L","T"], ["M","O"] , ["N","W"], ["O","Y"],
        ["P","H"], ["Q","X"], ["R","U"], ["S","S"], ["T","P"], ["U","A"], ["V","I"],
        ["W","B"], ["X","R"], ["Y","C"], ["Z","J"]]
        """
        #self.state_start = "A"

    def rotate(self):
        #quita el primer elemento
        pos = self.pair[0]
        self.pair.remove(pos)
        #agrega el elemento al final
        self.pair.append(pos)

    #ingresa el estado inicial
    def set_state(self, state):
        for i in range(len(self.pair)):
            if self.pair[0][1] != state:
                self.rotate()
            else:
                break

    #De derecha a izquierda
    def right_to_left(self, pos_character):
        #obtiene la letra de la posicion en la columna derecha
        #pos es un entero
        #retorna la letra
        for i in range(len(self.pair)):
            if i == pos_character:             
                character = self.pair[i][1]
                break
        #obtiene la letra de la columna izquierda
        #pos es un caracter
        #retorna la posicion que es un entero    
        for i in range(len(self.pair)):
            if self.pair[i][0] == character:
                return i

    def left_to_right(self, pos_character):
        for i in range(len(self.pair)):
            if i == pos_character:             
                character = self.pair[i][0]
                break

        for i in range(len(self.pair)):
            if self.pair[i][1] == character:
                return i
  

"""
rotor = Rotor()
rotor.set_state("K")
print(rotor.pair)
print(rotor.left_to_right(11))
"""

    