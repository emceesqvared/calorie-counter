import pprint

foodDatabase = {
    'Unit' : {},
    'Cup' : {},
    'Oz' : {},
    'T' : {}
}

foodList = {}


def addUnitItem(item, calories):
    item = item.capitalize()
    foodDatabase['Unit'][item] = calories


def addCupItem(item, calories):
    item = item.capitalize()
    foodDatabase['Cup'][item] = calories


def addOzItem(item, calories):
    item = item.capitalize()
    foodDatabase['Oz'][item] = calories
    
    
def addTItem(item, calories):
    item = item.capitalize()
    foodDatabase['T'][item] = calories


def searchFood(x):
    t = []
    x.capitalize
    for unit, food in foodDatabase.items():
        for name in food:
                t.append(name)
    if x in t:
        return True
    else:
        return False



def getFoodInfo(x):
    x = x.capitalize()
    if searchFood(x):
        for unit, food in foodDatabase.items():
            for name in food:
                if x == name:
                    print(name + ':', food[name], 'calories')
                    print(name + ' is measured in {}s.'.format(unit.lower()))
    else:
        print('This food does not exist in the database.')



def addToFoodList(d, x, quantity=1):
    x = x.capitalize()
    if searchFood(x):
        for unit, food in foodDatabase.items():
            for name in food:
                if x == name:
                    if quantity > 1:
                        d[name] = food[name] * quantity
                    else:
                        d[name] = food[name]
    else:
        print('This food does not exist in the database.')




def addTotalCalories(d):
    calories = d.values()
    total = sum(calories)
    print('You have consumed {} calories today.'.format(total))



addUnitItem('Banana', 100)
addUnitItem('Brazil nut', 27)
addCupItem('Greek yogurt', 215)
addOzItem('Ground beef', 50)
addOzItem('Ham', 50)
addOzItem('Chicken', 33)
addTItem('Honey', 60)
addCupItem('Salad', 6.5)
addTItem('Butter', 100)
addTItem('Balsamic vinegar', 15)
addTItem('Olive oil', 120)
addCupItem('Raspberries', 65)
addUnitItem('Marco\'s pizza', 310)
addCupItem('Rice', 200)
addUnitItem('Bell pepper', 50)
addUnitItem('Carrot', 25)
addUnitItem('Meatball', 50)
addCupItem('Broccoli', 30)
addUnitItem('Protein powder', 160)
addTItem('Nutritional yeast', 20)
addUnitItem('Egg', 70)
addUnitItem('Corn', 100)
addUnitItem('Fruit smoothie', 530)
addCupItem('Popcorn', 30)
