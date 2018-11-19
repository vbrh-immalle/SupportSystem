from random import choice

class Responder:
    
    def __init__(self):
        self.responses = []
        self.fillResponses()

    def generateResponse(self):
        return choice(self.responses)

    def fillResponses(self):
        self.responses.append("Ahzo?")
        self.responses.append("Echt?")
        self.responses.append("Dat is ongeloofelijk!")
        self.responses.append("Amaj dat is interessant... Vertel me meer...")