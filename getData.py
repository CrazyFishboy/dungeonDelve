import json


class Customization:

    def __init__(self):
        self.topWall = "@"
        self.leftWall = "@"
        self.bottomWall = "@"
        self.rightWall = "@"
        self.cornerWall = "@"
        self.floor = " "
        self.hallStart = "#"


    def getOrder(self):
        with open("./customization/loadOrder.json","r") as f:
            self.data = json.load(f)
            f.close()

        for item in self.data["directories"]:
            print(item)
            try:
                path = item["path"]
            except KeyError:
                print(f"path not found in {item}")
                continue
            try:
                characters = item["characters"]
            except KeyError:
                characters = "characters.json"
            self.updateCharacters("./customization/"+path+"/"+characters)

    def updateCharacters(self,characterPath):
        print(f"Path: {characterPath}")
        with open(characterPath,"r") as f:
            characters = json.load(f)
            f.close()
        try:
            self.topWall = characters["topWall"]
        except KeyError:
            pass
        try:
            self.leftWall = characters["leftWall"]
        except KeyError:
            pass
        try:
            self.bottomWall = characters["bottomWall"]
        except KeyError:
            pass
        try:
            self.rightWall = characters["rightWall"]
        except KeyError:
            pass
        try:
            self.cornerWall = characters["cornerWall"]
        except KeyError:
            pass
        try:
            self.floor = characters["floor"]
        except KeyError:
            pass
        try:
            self.hallStart = characters["hallStart"]
        except KeyError:
            pass
    
        
                
    
        


custom = Customization()
custom.getOrder()
print(custom.data)
print(custom.hallStart)
print(custom.topWall)
