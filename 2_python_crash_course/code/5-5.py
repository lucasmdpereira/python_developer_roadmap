# Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

alien_color = 'red'

# If the alien is green, print a message that the player earned 5 points.
# If the alien is yellow, print a message that the player earned 10 points.
# If the alien is red, print a message that the player earned 15 points.

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15

print(f"You win {points} points!")