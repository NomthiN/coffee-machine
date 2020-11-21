cur_water = int(input("Write how many ml of water the coffee machine has:"))
cur_milk = int(input("Write how many ml of milk coffee machine has:"))
cur_beans = int(input("Write how many grams of coffee beans the coffee machine has:"))
cups = int(input("Write how many cups of coffee you will need:"))

water_amount = cur_water // 200
milk_amount = cur_milk // 50
beans_amount = cur_beans // 15
pos_cups = min(water_amount, milk_amount, beans_amount)

if cups > pos_cups:
    print(f"No, I can make only {pos_cups} of coffee")
elif cups == pos_cups:
    print("Yes, I can make that amount of coffee")
else:
    print(f"Yes, I can make that amount of coffe (and even {pos_cups - cups} more than that")