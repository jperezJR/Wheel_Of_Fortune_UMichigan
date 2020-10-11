VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer():

    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    
    def addMoney(self, amt):
        self.prizeMoney = amt
        
    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return '{} (${})'.format(self.name, self.prizeMoney)
        

# Write the WOFHumanPlayer class definition (part B) here

class WOFHumanPlayer(WOFPlayer):

    def getMove(self, category, obscuredPhrase, guessed):
        prompt = """
        {} has ${}\n
        \n
        Category: {}
        Phrase: {}
        Guessed: {}
        \n
        Guess a letter, phrase, or type 'exit' or 'pass':""".format(self.name, self.prizeMoney, category, obscuredPhrase, guessed)
        
        userinp = input(prompt)
        return userinp



