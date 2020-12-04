class CalculateDifferences():

    def __init__(self):
        pass

    def set_word_converted(self, word):
        self.word_converted = word

    def set_word(self,word):
        self.word = word

    def initialize(self):
        self.word_converted_length = len(self.word_converted)
        self.word_length = len(self.word)
        
        self.matrix = [[0 for i in range(self.word_length + 1)] for j in range(self.word_converted_length + 1)]

        self.__initialize_matrix()

    def calculate(self):
        for i in range(1, self.word_converted_length + 1): 
            for j in range(1, self.word_length + 1): 

                if self.word_converted[i - 1] == self.word[j - 1]: 
                    self.matrix[i][j] = self.matrix[i - 1][j - 1] 
                else: 
                    self.matrix[i][j] = 1 + min(self.matrix[i][j-1],
                                                self.matrix[i-1][j],
                                                self.matrix[i-1][j-1])

    def print(self):
        i = self.word_converted_length
        j = self.word_length

        word_formation = []
        word = ''

        word_formation_actions = []

        while(i >= 0 and j >= 0): 
            if self.word_converted[i - 1] == self.word[j - 1]  or (i == 0 and j == 0): 
                if len(word) != self.word_length:
                    word += self.word_converted[i - 1]
                i -= 1
                j -= 1
            elif self.matrix[i][j] == self.matrix[i - 1][j - 1] + 1: 
                word_formation_actions.append(f"Mudar o caracter '{self.word_converted[i - 1]}' para '{self.word[j - 1]}' na posição {i}")
                word += self.word[j - 1]
                j -= 1
                i -= 1
            elif self.matrix[i][j] == self.matrix[i - 1][j] + 1:
                word_formation_actions.append(f"Remover o caracter '{self.word_converted[i - 1]}' na posição {i}") 
                i -= 1
            elif self.matrix[i][j] == self.matrix[i][j - 1] + 1: 
                word += self.word[j - 1]
                word_formation_actions.append(f"Adicionar o caracter '{self.word[j - 1]}'")
                j -= 1

            if i >= 0 and j >= 0:
                word_formation.append(word[::-1])

        return word_formation_actions, list(dict.fromkeys(word_formation))

    def __initialize_matrix(self):
        for i in range(self.word_converted_length + 1): 
            self.matrix[i][0] = i 
        for j in range(self.word_length + 1): 
            self.matrix[0][j] = j 