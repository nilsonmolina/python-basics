# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == 'spam':
#         # break  # 'breaks' you out of the for loop
#         continue  # halts progress of further code and 'continues' the for loop
#     print("Buy " + item)


meal = ["eggs", "bacon", "spam", "sausages"]
nasty_food_item = ''  # if the variable is undefined, an error will crash the program

for item in meal:
    if item == "spam":
        nasty_food_item = item
        break
else:  # else in the context of a for loop signifies that it will run if the for loop completes to entirety
    print("I'll have a plate of that, then, please")

if nasty_food_item:
    print("Can't I have anything without {} in it!".format(nasty_food_item))
