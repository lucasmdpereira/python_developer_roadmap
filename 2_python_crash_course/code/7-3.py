# Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

request = "Give me a number: "

response = int(input(request))

is_divisible_by_10 = print("The number is divisible by 10") if (response % 10 == 0) else print("The number is not divisible by 10")

