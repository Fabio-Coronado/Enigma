from machine.rotors import Rotors

class Enigma:
    def __init__(self, states):
        #lista de rotores
        self.rotors = Rotors()
        #cambiar orden de rotores
        self.rotors.sort([2, 1, 0])
        #contador de rotaciones
        self.counters = [0] * len(self.rotors)
        self.abc_num = {
            "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8,"J": 9, 
            "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19,
            "U": 20, "V": 21, "W": 22, "X": 23 , "Y": 24 ,"Z": 25
        }
        self.num_abc = {
            0: "A",  1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J", 
            10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R", 18: "S", 19: "T",
            20: "U", 21: "V", 22: "W", 23: "X" , 24: "Y", 25: "Z"
        }

        self.reflector = {
            "A":"Y", "B":"R","C":"U", "D":"H","E":"Q", "F":"S","G":"L", "I":"P", "J":"X", "K":"N", "M": "O", "T": "Z", "V":"W",
            "Y":"A", "R":"B","U":"C", "H":"D","Q":"E", "S":"F","L":"G", "P":"I", "X":"J", "N":"K", "O": "M", "Z": "T", "W":"V",
        }

        #El estado se ingresa: "NMA" para tres rotores
        self.states = states
        self._process_states()
    
    def encrypt_letter(self, letter):
        value = letter
        
        for i in reversed(range(len(self.rotors))):
            
            if i == len(self.rotors) - 1:
                rotor = self.rotors[i]             
                #rotar al presionar
                rotor.rotate()
                self.counters[i] += 1
                value = self.num_abc[rotor.right_to_left(self.abc_num[value])]
               
            else:
                rotor = self.rotors[i]
                #si el rotor anterior llega a 26 rotarlo
                if self.counters[i + 1] == 26:
                    
                    rotor.rotate()                    
                    self.counters[i] += 1
                    # resetear conteno de rotaciones
                    self.counters[i + 1] = 0 
                value = self.num_abc[rotor.right_to_left(self.abc_num[value])]

        value = self.reflector[value]

        #Recorrido inverso
        for i in (range(len(self.rotors))):
            if i == 0:
                rotor = self.rotors[i]             
                value = self.num_abc[rotor.left_to_right(self.abc_num[value])]
            else:
                rotor = self.rotors[i]
                #si el rotor anterior llega a 26 rotarlo
                value = self.num_abc[rotor.left_to_right(self.abc_num[value])]
        
        return value

    def _process_states(self):
        for i in reversed(range(len(self.states))):
            self.rotors[i].set_state(self.states[i])


