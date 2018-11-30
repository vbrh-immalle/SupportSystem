from InputReader import InputReader
from Responder import Responder

class SupportSystem:
    def __init__(self):
        self.reader = InputReader()
        self.responder = Responder()
    
    def start(self):
        finished = False

        self.printWelcome()

        while not finished:
            wordset = self.reader.getInput()

            if 'bye' in wordset:
                finished = True
            else:
                response = self.responder.generateResponse(wordset)
                print(response)

        self.printGoodbye()

    def printWelcome(self):
        print("Welkom bij het immalle helpsysteem...")
        print()
        print("Vertel ons uw probleem...")
        print("Type 'bye' om te stoppen.")

    def printGoodbye(self):
        print("Tot ziens!")