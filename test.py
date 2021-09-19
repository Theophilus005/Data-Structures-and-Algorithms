
#print("Hello world")

def sayHi():
    print("You run the sayhi function")

add = 5+7
print(add)

class linkedList:
    name = None

    def __init__(self):
        self.name = "Theophilus"

    def __repr__(self):
       return ("I returned my self %s" % self.name)

a = linkedList()
print(a.name)
print(a)

print("Its about to go up ")