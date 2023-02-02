# Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.


sandwich_orders = ["sandwich1", "sandwich2", "sandwich3", "sandwich4", "sandwich5", "sandwich6"]
sandwich_orders.reverse()
finished_sandwiches = []

print()
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"{sandwich} finished")
    
    finished_sandwiches.append(sandwich)

print(f"\n{finished_sandwiches}")