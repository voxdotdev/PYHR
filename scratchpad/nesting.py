item_0 = {'color': 'green', 'rarity': 5}
item_1 = {'color': 'yellow', 'rarity': 10}
item_2 = {'color': 'red', 'rarity': 15}

items = [item_0, item_1, item_2]

for item in items:
    print(item)


# More realistic example: 

# Make an empty list for storing items 

items = []

# Make 30 green items

for item_number in range(30):
    new_item = {'color': 'green', 'value': 5, 'rarity': 'common'}
    items.append(new_item)


# Show the first 5 items 

for item in items[:5]:
    print(item)
print("...")

# Show how many itmes have been created 
print(f"Total number of items: {len(items)}")

'''
OUTPUT
{'color': 'green', 'value': 5, 'rarity': 'common'}
{'color': 'green', 'value': 5, 'rarity': 'common'}
{'color': 'green', 'value': 5, 'rarity': 'common'}
{'color': 'green', 'value': 5, 'rarity': 'common'}
{'color': 'green', 'value': 5, 'rarity': 'common'}

'''

# This method allows you to access the items individually.

for item in items[:3]:
    if item['color'] == 'green':
        item['color'] = 'yellow'
        item['rarity'] = 'uncommon'
        item['value'] = '10'


for item in items[:10]: 
    print(item)

print("...")

'''
OUTPUT
{'color': 'yellow', 'value': '10', 'rarity': 'uncommon'}
{'color': 'yellow', 'value': '10', 'rarity': 'uncommon'}
{'color': 'yellow', 'value': '10', 'rarity': 'uncommon'}
{'color': 'green', 'value': 5, 'rarity': 'common'}
{'color': 'green', 'value': 5, 'rarity': 'common'}

This can then be expanded with an elif block that turns yellow items into red, rare items worth 15 each. 

    elif item['color'] == 'yellow':
        item['color'] = 'red'
        item['rarity'] = 'rare'
        item['value'] = '15'
'''

# Alternatively, store a list in a dictionary. 

item = {
    'value': '10',
    'category': ['weapon', 'axe'],
}

# Summarize the list. 
print(f"You've found a item worth {item['value']} gold!")

for type in item['category']:
    print("Type: \t" + type.title())

'''
OUTPUT
You've found a item worth 10 gold!
Type:   Weapon
Type:   Axe

'''