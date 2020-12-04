class CalculateDifferences():

    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2
        self.word1_length = len(self.word1)
        self.word2_length = len(self.word2)
        
        self.matrix = [[0 for i in range(self.word2_length + 1)] for j in range(self.word1_length + 1)]

        self.__initialize_matrix()

    def calculate(self):
        for i in range(1, self.word1_length + 1): 
            for j in range(1, self.word2_length + 1): 

                if self.word1[i - 1] == self.word2[j - 1]: 
                    self.matrix[i][j] = self.matrix[i - 1][j - 1] 
                else: 
                    self.matrix[i][j] = 1 + min(self.matrix[i][j-1],
                                                self.matrix[i-1][j],
                                                self.matrix[i-1][j-1])

    def print(self):
        i = self.word1_length
        j = self.word2_length

        word_formation = []
        word = ''

        word_formation_actions = []

        while(i >= 0 and j >= 0): 
            if self.word1[i - 1] == self.word2[j - 1]: 
                if len(word) != self.word2_length:
                    word += self.word1[i - 1]
                i -= 1
                j -= 1
            elif self.matrix[i][j] == self.matrix[i - 1][j - 1] + 1: 
                word_formation_actions.append(f"Mudar o caracter '{self.word1[i - 1]}' para '{self.word2[j - 1]}' na posição {i}")
                word += self.word2[j - 1]
                j -= 1
                i -= 1
            elif self.matrix[i][j] == self.matrix[i - 1][j] + 1:
                word_formation_actions.append(f"Remover o caracter '{self.word1[i - 1]}' na posição {i}") 
                i -= 1
            elif self.matrix[i][j] == self.matrix[i][j - 1] + 1: 
                word += self.word2[j - 1]
                word_formation_actions.append(f"Adicionar o caracter '{self.word2[j - 1]}'")
                j -= 1

            if i >= 0 and j >= 0:
                word_formation.append(word[::-1])

        print(word_formation_actions)
        print(word_formation)

    def __initialize_matrix(self):
        for i in range(self.word1_length + 1): 
            self.matrix[i][0] = i 
        for j in range(self.word2_length + 1): 
            self.matrix[0][j] = j 

def main():
    word1 = "sunday"
    word2 = "saturday"

    print(word1)
    print(word2)

    calculate = CalculateDifferences(word1, word2)
    calculate.calculate()
    calculate.print()

if __name__ == "__main__":
    main()