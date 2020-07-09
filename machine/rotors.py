from machine.rotor import Rotor
#Lista de rotores
class Rotors:
    def __init__(self):
        self.rotor0 = Rotor([["A","E"], ["B","K"], ["C","M"], ["D","F"], ["E","L"], ["F","G"], ["G","D"],
        ["H","Q"], ["I","V"], ["J","Z"], ["K","N"], ["L","T"], ["M","O"] , ["N","W"], ["O","Y"],
        ["P","H"], ["Q","X"], ["R","U"], ["S","S"], ["T","P"], ["U","A"], ["V","I"],
        ["W","B"], ["X","R"], ["Y","C"], ["Z","J"]])

        self.rotor1 = Rotor([["A","A"], ["B","J"], ["C","D"], ["D","K"], ["E","S"], ["F","I"], ["G","R"],
        ["H","U"], ["I","X"], ["J","B"], ["K","L"], ["L","H"], ["M","W"] , ["N","T"], ["O","M"],
        ["P","C"], ["Q","Q"], ["R","G"], ["S","Z"], ["T","N"], ["U","P"], ["V","Y"],
        ["W","F"], ["X","V"], ["Y","O"], ["Z","E"]])

        self.rotor2 = Rotor([["A","B"], ["B","D"], ["C","F"], ["D","H"], ["E","J"], ["F","L"], ["G","C"],
        ["H","P"], ["I","R"], ["J","T"], ["K","X"], ["L","V"], ["M","Z"] , ["N","N"], ["O","Y"],
        ["P","E"], ["Q","I"], ["R","W"], ["S","G"], ["T","A"], ["U","K"], ["V","M"],
        ["W","U"], ["X","S"], ["Y","Q"], ["Z","O"]])

        #por defecto 0-1-2
        self.rotors = [self.rotor0, self.rotor1, self.rotor2]

    def __call__(self):
        return self.rotors

    def __len__(self):
        return len(self.rotors)

    def __getitem__(self, key):
        return self.rotors[key]

    #lista de posiciones 
    def sort(self, list_rotors):
        #[2, 1, 0]
        for i in range(len(list_rotors)):
            #print(i)
            #guardo el rotor de la posicion i
            aux = self.rotors[i]
            #obtener el rotor de la lista
            self.rotors[i] = self.rotors[list_rotors[i]]
            self.rotors[list_rotors[i]] = aux


        
