

import json


from Librarues.JSON.Model.Human import Human
from Librarues.JSON.Model.Town import Town
# SQL - MySQL, PostgreSQL..
# NoSQL - MongoDB, MariaDB
# Key:Value - JSON, XML

# WEB - REST(JSON), SOAP(XML)

class App():


    @staticmethod
    def run():

        town = App.uploadData()

        print("Привет странник!", "Ты попал в город "+town.name)
        print("Здесь проживает "+str(len(town.citizen))+" людей")
        print("А точнее: ")
        for abc in town.citizen:
            print(abc.name, abc. account)







    @staticmethod
    def uploadData():

        file = open("town.json", 'r')
        data = json.load(file)

        town = Town(data["name"])

        for cit in data["citizen"]:
            human = Human(cit["name"], cit["account"])
            town.addCitizen(human)

        return town

    @staticmethod
    def saveTown(town, path):
        file = open(path, 'w')
        dict_town = {}
        dict_town["name"] = town.name
        dict_town["citizen"] = []

        for citizen in town.citizen:
            dict_town["citizen"].append(citizen.__dict__)

        json.dump(dict_town, file)
        file.close()





App.run()






