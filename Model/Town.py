

class Town():


    def __init__(self, name):
        self.name = name
        self.citizen = []

    def addCitizen(self, human):
        self.citizen.append(human)

