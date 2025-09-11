# Day 1: Summon Your QuestBot 🤖⚡

Welcome back, Recruits! Ready to start building your AI sidekick? Today we're breathing life into QuestBot - your personal AI assistant that'll grow smarter over the next 3 days.

**What we're building today:** A friendly AI that greets you by name and adapts its personality to your vibe.

**Time needed:** ~30 minutes  
**XP Reward:** 100 XP + Code Summoner badge 🎖️

## 🎯 Mission Overview
By the end of today, your QuestBot will:
- Greet users with a custom message
- Ask for their name and remember it
- Adapt its personality based on user preference
- Feel like a real conversation!

## 📁 Download the Files

**Prefer to code along?** Grab the starter files:
- **questbot_day1_template.py** - Empty template with TODO comments and hints
- **questbot_day1_solution.py** - Complete working code (check this if you get stuck)
- **setup_guide.md** - Detailed installation instructions

**Choose your adventure:**
- 📖 **Follow the tutorial** → Read and code step-by-step below
- 📝 **Use the template** → Download the template and fill in the TODOs  
- ✅ **Check solutions** → Compare your code with the working version

*Files will be available in the comments or on my GitHub*

---

## Quest 1: Unlock the Code Vault (20 XP - 5 min)

First things first - let's make sure your setup is ready to roll!

### Option A: Local Setup
1. **Install Python 3** from [python.org](https://python.org) if you haven't already
2. **Test it:** Open your terminal/command prompt and type:
```bash
python --version
# or try
python3 --version
```
3. **Create your workspace:** Make a new folder called `questbot-project`
4. **Choose your editor:** VS Code, PyCharm, or even Notepad works!

### Option B: Online Setup (Zero Install!)
1. Go to [replit.com](https://replit.com) and create a free account
2. Click "Create Repl" → Choose "Python"  
3. Name it "QuestBot-Assistant"
4. You're ready to code!

✅ **Checkpoint:** You can run Python and see the version number

---

## Quest 2: Forge QuestBot's Voice (30 XP - 10 min)

Time to give your bot its first words! Create a new file called `questbot.py` and let's start simple:

```python
# QuestBot Day 1 - First Contact
print("Greetings, Recruit! I'm QuestBot, your AI sidekick!")
```

**Run it:**
- **Local:** `python questbot.py` in your terminal
- **Replit:** Hit that green "Run" button

You should see QuestBot's first message! 🎉

### Level Up: Add Some Personality
Let's make it more interesting:

```python
print("🤖 SYSTEM INITIALIZING...")
print("✨ QuestBot v1.0 ONLINE")
print("")
print("Greetings, Recruit! I'm QuestBot, your AI sidekick!")
print("Ready to embark on your coding quest? 🚀")
```

✅ **Checkpoint:** Your bot has a personality and greets users

---

## Quest 3: Personalize the Mission (50 XP - 15 min)

Here's where the magic happens - making it feel like a real conversation!

### Step 1: Get to Know Your User
```python
print("🤖 SYSTEM INITIALIZING...")
print("✨ QuestBot v1.0 ONLINE")
print("")
print("Greetings, Recruit! I'm QuestBot, your AI sidekick!")

# Get user's name
name = input("What's your Recruit name? ")
print(f"Excellent! Nice to meet you, {name}!")
```

### Step 2: Adapt to Their Vibe
```python
# Ask for their preferred vibe
print(f"\\nAlright {name}, let's set the mood...")
vibe = input("Pick a vibe (epic, chill, heroic): ")

# Respond with personalized greeting
print(f"\\nSalute, {name}! QuestBot is ready in {vibe} mode! 🎯")
```

### Step 3: Complete Day 1 Code
Here's your full `questbot.py` for today:

```python
# QuestBot Day 1 - First Contact
print("🤖 SYSTEM INITIALIZING...")
print("✨ QuestBot v1.0 ONLINE")
print("")
print("Greetings, Recruit! I'm QuestBot, your AI sidekick!")

# Get user's name
name = input("\\nWhat's your Recruit name? ")
print(f"Excellent! Nice to meet you, {name}!")

# Ask for their preferred vibe
print(f"\\nAlright {name}, let's set the mood...")
vibe = input("Pick a vibe (epic, chill, heroic): ")

# Personalized response
print(f"\\nSalute, {name}! QuestBot is ready in {vibe} mode! 🎯")
print("Your AI sidekick is now online and ready for action!")
```

✅ **Checkpoint:** QuestBot knows your name and adapts to your chosen vibe

---

## 🏆 Bonus Challenge: Dynamic Responses (10 XP)

Want to earn extra XP? Make QuestBot respond differently based on the vibe:

```python
# Add this after getting the vibe, before the final greeting
if vibe.lower() == "epic":
    print("🚀 Prepare for LEGENDARY adventures!")
elif vibe.lower() == "chill":
    print("😎 Cool vibes activated. Let's take it easy.")
elif vibe.lower() == "heroic":
    print("⚔️ Honor and glory await! Ready for battle!")
else:
    print(f"🎭 {vibe} mode activated! Let's make it happen!")

print(f"\\nSalute, {name}! QuestBot is ready and reporting for duty! 🎯")
```

---

## 🎮 Test Your QuestBot

Run your code and try different inputs:
1. **Test 1:** Use your real name + "epic" vibe
2. **Test 2:** Try a fun nickname + "chill" vibe  
3. **Test 3:** Enter something random for vibe and see what happens

**Example interaction:**
```
🤖 SYSTEM INITIALIZING...
✨ QuestBot v1.0 ONLINE

Greetings, Recruit! I'm QuestBot, your AI sidekick!

What's your Recruit name? Alex
Excellent! Nice to meet you, Alex!

Alright Alex, let's set the mood...
Pick a vibe (epic, chill, heroic): epic
🚀 Prepare for LEGENDARY adventures!

Salute, Alex! QuestBot is ready and reporting for duty! 🎯
```

---

## 📸 Quest Log: Share Your Victory!

Got your QuestBot talking? Awesome! Share a screenshot of your personalized greeting on social media with **#4IRQuestSaga** - I'd love to see what names and vibes you chose!

**🎖️ Badge Unlocked: Code Summoner**  
*"Summoned your first AI companion from lines of code"*

---

## What's Next?

Tomorrow in **Day 2**, we'll teach QuestBot to:
- 📝 Remember and manage your tasks
- ♻️ Handle multiple commands in a loop
- 🎯 Display your mission log with style

**Your homework:** Play around with your QuestBot! Try different names, vibes, and see what happens. The more comfortable you get with input/output, the easier Day 2 will be.

---

**Total XP Earned Today:** 100 XP  
**Running Total:** 100/300 XP  
**Progress:** 33% complete 📊

**Solution** will be posted tomorrow!
See you tomorrow for Day 2: Task Mastery! 🚀

---
*Having trouble? Drop a comment below or find me on social @creator_x - happy to help debug! 👨‍💻*

---

## Day 2: Build Task Mastery (100 XP)
**🎯 Objective**: Teach QuestBot to manage tasks like a true sidekick  
**⏱️ Time**: 45 minutes  
**🧠 Skills Learned**: Lists, loops, user input validation

### Quest Tasks:

#### 1. Create the Task Codex (30 XP - 10 minutes)
**Build on Day 1:**
1. Open `day2_starter.py`
2. Add your Day 1 greeting code at the top
3. **Create a task storage system:**
   ```python
   tasks = []  # Empty list to store missions
   ```
4. **Collect one task:**
   ```python
   task = input("Log a mission (e.g., Study AI): ")
   tasks.append(task)
   print("Mission Log:", tasks)
   ```

**🎮 Test It**: Add a task and see it in your mission log

#### 2. Loop the Quest Cycle (40 XP - 20 minutes)
**Add continuous task entry:**
1. **Replace single task input with a loop:**
   ```python
   while True:
       task = input("Log a mission (or 'done' to finish): ")
       if task.lower() == "done":
           break
       tasks.append(task)
       print(f"✅ Added: {task}")
   ```

**🎮 Test It**: 
- Add 3-4 tasks
- Type "done" to finish
- See all your tasks collected

#### 3. Display with Epic Flair (30 XP - 15 minutes)
**Make your output professional:**
```python
print(f"\n{name}'s Epic Mission Log:")
print("="*40)
for i, task in enumerate(tasks, 1):
    print(f"Mission {i}: {task}")
```

**🏆 Bonus Challenge (10 XP)**: 
Add motivational messages based on task count:
```python
if len(tasks) == 1:
    print(f"🎯 {name}, laser focus! One mission, maximum impact!")
elif len(tasks) <= 3:
    print(f"💪 Perfect balance! {len(tasks)} missions ready to conquer!")
```

**📸 Quest Log**: Share your Mission Log screenshot  
**🎖️ Reward**: *Task Master* badge unlocked!

**✅ Day 2 Checkpoint**: QuestBot collects multiple tasks and displays them professionally

---

## Day 3: Unleash QuestBot's Power (100 XP)
**🎯 Objective**: Add task deletion and motivational quotes for a complete AI assistant  
**⏱️ Time**: 60 minutes  
**🧠 Skills Learned**: Random selection, data manipulation, error handling

### Quest Tasks:

#### 1. Master Task Control (40 XP - 20 minutes)
**Add task deletion feature:**
1. Open `day3_starter.py`
2. **Import random module:**
   ```python
   import random
   ```
3. **Create motivational quotes:**
   ```python
   quotes = [
       "Keep slaying, Recruit!",
       "You're unstoppable!",
       "Forge your future!",
       "Every mission brings you closer to mastery!"
   ]
   ```
4. **Add deletion logic after displaying tasks:**
   ```python
   delete = input("\nDelete a completed mission? Enter number (or 'no'): ")
   if delete.isdigit() and 1 <= int(delete) <= len(tasks):
       removed = tasks.pop(int(delete) - 1)
       print(f"🎉 Vanquished: {removed}")
   ```

**🎮 Test It**: Add tasks, then delete one by its number

#### 2. Add AI Wisdom (30 XP - 15 minutes)
**Display random motivational quotes:**
```python
print(f"\n🌟 QuestBot's Daily Wisdom:")
print(f"'{random.choice(quotes)}'")
```

**🎮 Test It**: Run multiple times to see different quotes

#### 3. Portfolio Polish (30 XP - 25 minutes)
**Final touches:**
1. **Add error handling for invalid deletion:**
   ```python
   if delete.isdigit():
       task_num = int(delete)
       if 1 <= task_num <= len(tasks):
           # deletion code
       else:
           print("❌ Invalid mission number")
   ```
2. **Create a README.md file:**
   ```markdown
   # QuestBot - AI Task Assistant
   
   Built during the 4IR Quest 3-Day Challenge
   
   ## Features
   - Personalized greetings
   - Task management
   - Motivational quotes
   - Task deletion
   
   ## Skills Learned
   - Python basics
   - User input handling
   - List manipulation
   - Loops and conditionals
   ```

**🏆 Bonus Challenges (10 XP each)**:
- Add task editing functionality
- Create task categories (work, personal, learning)
- Add task priority levels
- Save tasks to a file

**📸 Quest Log**: Share your complete QuestBot in action!  
**🎖️ Reward**: *Quest Champion* badge unlocked!

**✅ Final Checkpoint**: You've built a complete AI assistant!

---
