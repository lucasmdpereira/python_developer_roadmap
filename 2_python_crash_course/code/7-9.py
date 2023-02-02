# No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["sandwich1", "sandwich2", "pastrami", "sandwich4", "pastrami", "pastrami"]
sandwich_orders.reverse()
finished_sandwiches = []


print(f"\nWe are out of pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    
    if sandwich == "pastrami":
        print(f"Sorry, we are out of pastrami")
    else:
        print(f"{sandwich} finished")
        finished_sandwiches.append(sandwich)

print(f"\n{finished_sandwiches}")