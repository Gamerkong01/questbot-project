# QuestBot Day 2 Complete Solution
# Mission: Add task management powers to your bot!

# Initialize empty task list
tasks = []

# Day 1 greeting functionality
print("Greetings, Recruit! I'm QuestBot, your AI sidekick!")
name = input("What's your Recruit name? ")
vibe = input("Pick a vibe (epic, chill, heroic): ")
print(f"Salute, {name}! QuestBot is ready in {vibe} mode!")

# Task collection loop
print("\nTime to log your missions!")
while True:
    task = input("Log a mission (or 'done' to finish): ")
    if task.lower() == "done":
        break
    tasks.append(task)
    print(f"Added: {task}")

# Display mission log with style
print(f"\n{'='*40}")
print(f"{name}'s Epic Mission Log:")
print(f"{'='*40}")

if tasks:
    for i, task in enumerate(tasks, 1):
        print(f"Mission {i}: {task}")
    
    # Bonus motivational message based on task count
    if len(tasks) == 1:
        print(f"\n🎯 {name}, you've got focus! One mission, maximum impact!")
    elif len(tasks) <= 3:
        print(f"\n💪 {name}, perfect balance! {len(tasks)} missions ready to conquer!")
    else:
        print(f"\n🔥 {name}, you're ambitious! {len(tasks)} missions - you're unstoppable!")
else:
    print("No missions logged. Ready when you are, Recruit!")