inventory = {'rope': 1, 'torch': 6, 'gold coins': 86, 'arrows': 12, 'bow': 1}

def displayInventory(inventory, item):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        #item_total = item_total + v.get(item, 0)
        print(str(inventory.get('rope', 0)) + ' rope')
        print(str(inventory.get('torch', 0)) + ' torches')
        print(str(inventory.get('gold coins', 0)) + ' gold coins')
        print(str(inventory.get('arrows', 0)) + ' arrows')
        print(str(inventory.get('bow', 0)) + ' bow')
    return item_total

print('Total inventory items: ' + str(item_total))
