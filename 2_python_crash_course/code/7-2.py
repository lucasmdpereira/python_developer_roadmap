# Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.


request = "How many people are in their dinner group? "

response = int(input(request))
if response > 8:
    print(f"Sorry, you have to wait a table for {response}")
else:       
    print(f"You table for {response} is ready")