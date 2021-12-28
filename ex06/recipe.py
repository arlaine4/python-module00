from copy import deepcopy


cookbook = {'sandwich': {'ingredients': ['ham', 'bread', 'tomotoes'],
                         'meal': 'lunch',
                         'prep_time': 10},
            'cake': {'ingredients': ['flour', 'sugar', 'eggs'],
                     'meal': 'dessert',
                     'prep_time': 60},
            'salad': {'ingredients': ['avocado', 'arugula',
                      'tomatoes', 'spinach'],
                      'meal': 'lunch',
                      'prep_time': 15}
            }


def print_recipe(name):
    global cookbook
    if name in cookbook.keys():
        print(f"Recipe for {name}:")
        print(f"Ingredients list: {cookbook[name]['ingredients']}")
        print(f"To be eaten for {cookbook[name]['meal']}.")
        print(f"Takes {cookbook[name]['prep_time']} minutes of cooking.")
    else:
        print(f"Recipe '{name}' not found, please enter a valid one.")


def delete_recipe(name):
    global cookbook
    if name in cookbook.keys():
        cookbook.pop(name)
    else:
        print(f"Can't remove recipe '{name}', it doesn't exist.")


def add_recipe(name, ingredients, meal, prep_time):
    global cookbook
    new_dic = {name: {'ingredients': [f for f in ingredients],
                      'meal': meal,
                      'prep_time': prep_time}
               }
    cookbook.update(new_dic)


def print_cookbook():
    global cookbook
    for key in cookbook.keys():
        print()
        print_recipe(key)
    print()


def print_recipes_names():
    global cookbook
    print("Available recipes:")
    for key in cookbook.keys():
        print(key)


def print_input_menu():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")


def check_option(option):
    if option == 1:
        dynamic_recipe_add()
    elif option == 2:
        dynamic_recipe_delete()
    elif option == 3:
        dynamic_recipe_print()
    elif option == 4:
        print_cookbook()


def fill_infos(dic, data, stage, name):
    if stage == 0:
        dic[data] = {}
    elif stage == 1:
        dic[name]['ingredients'] = data.split(' ')
    elif stage == 2:
        dic[name]['meal'] = data
    elif stage == 3:
        dic[name]['prep_time'] = data
    return dic


def dynamic_recipe_print():
    recipe_name = ""
    while 1:
        print("Enter the name of the recipe you want to print:\n")
        recipe_name = str(input())
        print_recipe(recipe_name)


def dynamic_recipe_delete():
    global cookbook
    recipe_name = ""
    while 1:
        print("Enter the recipe name you want to delete:\n")
        recipe_name = str(input())
        if recipe_name in cookbook.keys():
            delete_recipe(recipe_name)
            break


def dynamic_recipe_add():
    infos = {}
    rec_name = ""
    stage = 0
    while stage != 4:
        if stage == 0:
            print("\nEnter the recipe name:")
            try:
                data = str(input())
                if ' ' in data:
                    data = data.replace(' ', '')
                if len(data) != 0:
                    rec_name = data
                    infos = fill_infos(infos, data, stage, rec_name)
                    stage = 1
                else:
                    print("You need to enter something as the recipe name.")
            except ValueError:
                print("You need to enter a string.\n")
        elif stage == 1:
            print("Enter a list of ingredients, separated by a space:\n")
            try:
                data = str(input())
                tmp = data.split(' ')
                if tmp.count('') != len(tmp) and len(data) != 0:
                    prev = deepcopy(infos)
                    infos = fill_infos(infos, data, stage, rec_name)
                    stage = 2
                else:
                    print('You need to enter something as the recipe name.')
            except ValueError:
                print("You need to enter string(s) separated by a space.\n")
        elif stage == 2:
            print("Enter the meal type:\n")
            try:
                data = str(input())
                if ' ' in data:
                    data = data.replace(' ', '')
                if len(data) != 0:
                    infos = fill_infos(infos, data, stage, rec_name)
                    stage = 3
                else:
                    print("You need to enter something as the meal type.")
            except ValueError:
                print("You need to enter a string.\n")
        elif stage == 3:
            print("Please enter the prep_time:\n")
            try:
                data = int(input())
                infos = fill_infos(infos, data, stage, rec_name)
                stage = 4
            except ValueError:
                print("You need to enter an int.\n")
    add_recipe(rec_name, infos[rec_name]['ingredients'],
               infos[rec_name]['meal'],
               infos[rec_name]['prep_time'])


if __name__ == "__main__":
    option = 0
    while option != 5:
        print_input_menu()
        try:
            option = int(input())
            if option > 5 or option < 0:
                print("\nThis option does not exist."
                      "\nTo exit, enter 5.\n")
        except ValueError:
            print("\nInvalid option.\n")
        check_option(option)
