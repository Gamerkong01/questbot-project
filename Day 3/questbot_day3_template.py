# QuestBot Day 3 Starter Template
# Mission: Add task deletion and motivational quotes!

# TODO: Import the random module for quotes
# Hint: import random

# TODO: Create a list of motivational quotes
# Hint: quotes = ["Quote 1", "Quote 2", "Quote 3"]


tasks = []

# Day 1 & 2 code - greeting and task collection
name = input("What's your Recruit name? ")
vibe = input("Pick a vibe (epic, chill, heroic): ")
print(f"Salute, {name}! QuestBot is ready in {vibe} mode!")

while True:
    task = input("Log a mission (or 'done' to finish): ")
    if task == "done":
        break
    tasks.append(task)

# Display mission log
print(f"\n{name}'s Epic Mission Log:")
for i, task in enumerate(tasks, 1):
    print(f"Mission {i}: {task}")

# TODO: Add task deletion feature
# Hint: Ask user for task number to delete
# Check if it's a valid number and within range
# Use tasks.pop(index) to remove the task


# TODO: Display updated mission log after deletion


# TODO: Show a random motivational quote
# Hint: Use random.choice(quotes) to pick a random quote


# Bonus Challenge: Add your own creative features!