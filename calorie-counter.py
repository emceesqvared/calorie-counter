import pprint

foodDatabase = {
    'Unit' : {},
    'Cup' : {},
    'Oz' : {},
    'T' : {}
}

foodList = {}



def main():
    while True:
        res = input('Add a food, (V)iew calories, or type (D)one: ')
        res = res.capitalize()
        if res == 'D' or res == 'Done':
            pprint.pprint(foodList)
            addTotalCalories(foodList)
            break
        elif res == 'V' or res == 'View':
            pprint.pprint(foodList)
            addTotalCalories(foodList)
        elif searchFood(res):
            getFoodInfo(res)
            quantity = input('How much? ')
            while True:
                try:
                    quantity = float(quantity)
                    addToFoodList(foodList, res, quantity)
                    break
                except ValueError:
                    quantity = input('Please enter a number: ')
        else:
            print('This food does not exist in the database.')
            ans = input('Would you like to add it to the food list? (Y) or (N): ')
            while True:
                if ans.upper() == 'Y':
                    calories = input('How many calories? ')
                    while True:
                        try:                            
                            calories = float(calories)
                            foodList[res] = calories
                            break
                        except ValueError:
                            calories = input('Please enter a number: ')
                    break
                elif ans.upper() == 'N':
                    break
                else:
                    ans = input('Please enter (Y) or (N): ')







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
                    print(name + ': measured in {}s.'.format(unit))
                    print(food[name], 'calories per {}.'.format(unit))
    else:
        print('This food does not exist in the database.')



def addToFoodList(foodList, x, quantity=1):
    x = x.capitalize()
    for unit, food in foodDatabase.items():
        for name in food:
            if x == name:
                if quantity > 1:
                    foodList[name] = food[name] * quantity
                else:
                    foodList[name] = food[name]




def addTotalCalories(foodList):
    calories = foodList.values()
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
addCupItem('Blueberries', 85)
addTItem('Sugar', 45)
addTItem('Powdered sugar', 30)
addTItem('Brown sugar', 45)
addUnitItem('Strawberries', 5)
addCupItem('Pineapple', 80)


if __name__ == '__main__':
    main()
