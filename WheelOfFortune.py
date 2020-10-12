import random

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
        self.prizeMoney += amt
        
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
        {} has ${}
        
        Category: {}
        Phrase: {}
        Guessed: {}
        
        Guess a letter, phrase, or type 'exit' or 'pass':""".format(self.name, self.prizeMoney, category, obscuredPhrase, guessed)
        
        userinp = input(prompt)
        return userinp



# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):

    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty

    def smartCoinFlip(self):
        rand_num = random.randint(1, 10)

        if rand_num > self.difficulty:
            return True
        elif rand_num <= self.difficulty:
            return False

    def getPossibleLetters(self, guessed):
        poss_letter = []
        for letter in LETTERS:
            if letter not in guessed:
                poss_letter.append(letter)
            if self.prizeMoney < VOWEL_COST:
                    for p_letter in poss_letter:
                        if p_letter in VOWELS:
                            poss_letter.remove(p_letter)
        return poss_letter



    def getMove(self, category, obscuredPhrase, guessed):

        move = self.getPossibleLetters(guessed)
        if not move:
            return 'pass'
        
        else:
            if self.smartCoinFlip() == True:
                for freq_letter in self.SORTED_FREQUENCIES[::-1]:
                    if freq_letter in move:
                        return freq_letter
            else:
                return random.choice(move)
            



        


    

