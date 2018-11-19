from random import randint

class Responder:
    
    def __init__(self):
        self.responses = []
        self.fillResponses()

    def generateResponse(self):
        random_index = randint(0, len(self.responses) - 1)
        return self.responses[random_index]

    def fillResponses(self):
        self.responses.append("Ahzo?")
        self.responses.append("Echt?")
        self.responses.append("Dat is ongeloofelijk!")
        self.responses.append("Amaj dat is interessant... Vertel me meer...")