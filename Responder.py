from random import choice

class Responder:
    
    def __init__(self):
        self.defaultresponses = []
        self.responsemap = {
            'crash': 'Oh nee! Geen crash!?',
            'virus': 'Is het een RNA of DNA virus? ;-)',
        }
        self.fillResponses()

    def generateResponse(self, wordset):      
        for w in wordset:
            if w in self.responsemap:
                return self.responsemap[w]

        return choice(self.defaultresponses)

    def fillResponses(self):
        self.defaultresponses.append("Ahzo?")
        self.defaultresponses.append("Echt?")
        self.defaultresponses.append("Dat is ongeloofelijk!")
        self.defaultresponses.append("Amaj dat is interessant... Vertel me meer...")
