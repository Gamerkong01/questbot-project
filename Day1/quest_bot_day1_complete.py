# QuestBot Day 1 Complete Solution
# Mission: Create your first AI greeting bot!

# Basic greeting
print("Greetings, Recruit! I'm QuestBot, your AI sidekick!")

# Get user information
name = input("What's your Recruit name? ")
vibe = input("Pick a vibe (epic, chill, heroic): ")

# Create personalized greeting
print(f"Salute, {name}! QuestBot is ready in {vibe} mode!")

# Bonus: Add vibe-specific responses
if vibe.lower() == "epic":
    print("🚀 Prepare for LEGENDARY adventures!")
elif vibe.lower() == "chill":
    print("😎 Cool vibes activated. Let's take it easy.")
elif vibe.lower() == "heroic":
    print("⚔️ For honor and glory! Your quest awaits!")
else:
    print("✨ Whatever your style, we've got this!")