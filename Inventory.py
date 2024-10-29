import random

class Inventory:
    def __init__(self):
        self.items = []
        
    def pick(self, newItem):
        self.items.append(newItem)

    def drop(self, itemToDrop):
        self.items.remove(itemToDrop)

    def pull(self):
        return self.items[random.randint(0, len(self.items)-1)]

    def search(self):
        for item in self.items:
            print(item)

inventory = Inventory()
inventory.pick("Sword")

inventory.drop("Sword")

inventory.pick("Apple")
inventory.pick("Pear")
print(inventory.pull())

inventory.search()