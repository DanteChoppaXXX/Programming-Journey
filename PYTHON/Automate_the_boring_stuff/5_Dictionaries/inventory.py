#!../bin/python3
import time

# stuffs = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v
    print(f"Total number of items: {item_total}")

def addToInventory(inventory, addedItems):
    item_counts = {}
    for i in addedItems:
        if i in item_counts:
            item_counts[i] +=1
        else:
            item_counts[i] = 1
    

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)