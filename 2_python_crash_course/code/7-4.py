# Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

toppings = []

prompt = "Enter a pizza topping: "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        print(toppings)
        break
    else:
        toppings.append(topping)
        print(f"I'd add {topping}!")
    