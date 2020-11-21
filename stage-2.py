n_of_coffee = int(input("Write how many cups of coffee you will need:\n"))
print(f"for {n_of_coffee} you will need:\n")
water = 200
milk = 50
beans = 15
water_total = water * n_of_coffee
milk_total = milk * n_of_coffee
beans_total = beans * n_of_coffee
print(f"{water_total} ml of water\n{milk_total} ml of milk\n{beans_total} g of coffee beans")
