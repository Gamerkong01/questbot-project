# QuestBot Day 3 Complete Solution
# Mission: Add task deletion and motivational quotes!

import random

# Motivational quotes database
quotes = [
    "Keep slaying, Recruit!",
    "You're unstoppable!",
    "Forge your future!",
    "Every mission brings you closer to mastery!",
    "The 4IR revolution starts with YOU!",
    "Code today, conquer tomorrow!",
    "Your potential is limitless!",
    "Small steps, EPIC results!",
    "You're not just learning, you're leveling up!",
    "Champions are made in the coding trenches!"
]

# Initialize task list
tasks = []

# Day 1 & 2 functionality - Greeting and task collection
print("Greetings, Recruit! I'm QuestBot, your AI sidekick!")
name = input("What's your Recruit name? ")
vibe = input("Pick a vibe (epic, chill, heroic): ")
print(f"Salute, {name}! QuestBot is ready in {vibe} mode!")

# Task collection
print("\nTime to log your missions!")
while True:
    task = input("Log a mission (or 'done' to finish): ")
    if task.lower() == "done":
        break
    tasks.append(task)
    print(f"✅ Added: {task}")

# Display initial mission log
print(f"\n{'='*50}")
print(f"{name}'s Epic Mission Log:")
print(f"{'='*50}")

if tasks:
    for i, task in enumerate(tasks, 1):
        print(f"Mission {i}: {task}")
else:
    print("No missions logged yet!")

# Task deletion feature
if tasks:
    print(f"\n🗑️ Want to remove a completed mission?")
    delete = input("Enter mission number to delete (or 'no' to keep all): ")
    
    if delete.isdigit():
        task_num = int(delete)
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"🎉 Vanquished: '{removed_task}'")
            
            # Display updated log
            if tasks:
                print(f"\nUpdated Mission Log:")
                print(f"{'='*30}")
                for i, task in enumerate(tasks, 1):
                    print(f"Mission {i}: {task}")
            else:
                print("\n🏆 All missions complete! You're a true champion!")
        else:
            print("❌ Invalid mission number. No changes made.")
    else:
        print("📝 Mission log unchanged. All tasks remain active!")

# Display motivational quote
print(f"\n{'='*50}")
print("🌟 QuestBot's Daily Wisdom:")
print(f"'{random.choice(quotes)}'")
print(f"{'='*50}")

# Final status based on remaining tasks
if tasks:
    print(f"\n🚀 {name}, you have {len(tasks)} missions remaining. Go forth and conquer!")
else:
    print(f"\n🏅 {name}, your mission log is clear! Time for new adventures!")

print("\nThank you for using QuestBot! Keep building, keep growing! 💪")