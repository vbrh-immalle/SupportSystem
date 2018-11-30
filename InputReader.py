class InputReader:
    def getInput(self):
        user_input = input(" > ")
        splitted_input = user_input.split()
        wordset = set()
        for w in splitted_input:
            wordset.add(w)
        return wordset
