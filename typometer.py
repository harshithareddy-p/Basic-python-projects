import time
import random

# sample text to type
texts = [
    "Python is a powerful programming language.",
    "Typing speed is measured in words per minute.",
    "Practice makes a person perfect in coding.",
    "Artificial Intelligence is the future of technology.",
    "Engineering is not just about study, it is about creating."
]

print("================ TYPE-O-METER ================")
print("Let your thoughts flow through your fingertips. Type. Learn. Evolve.")
print("You will be given a sentence to type.")
print("Press Enter when you are ready...\n")

input("👉 Press Enter to start...")

# Choose a random text
test_text = random.choice(texts)
print("\nType this:\n")
print(test_text)
print("\n")

# Start timer
start_time = time.time()

# Take input from user
typed_text = input("Start typing here: ")

# End timer
end_time = time.time()

# Calculate time taken
time_taken = end_time - start_time
time_taken = round(time_taken, 2)

# Calculate words per minute (WPM)
words = len(typed_text.split())
if time_taken > 0:
    wpm = round((words / time_taken) * 60)
else:
    wpm = 0

# Calculate accuracy
correct_chars = 0
for i, c in enumerate(typed_text):
    if i < len(test_text) and c == test_text[i]:
        correct_chars += 1

accuracy = (correct_chars / len(test_text)) * 100
accuracy = round(accuracy, 2)

# Show results
print("\n================ Results ================")
print(f"Time Taken ⏱️ : {time_taken} seconds")
print(f"Words Typed 🧾 : {words}")
print(f"Typing Speed ⚡ : {wpm} WPM")
print(f"Accuracy ⭐ : {accuracy}%")

# Flow
if wpm >= 15:
    print("Flow 🎧 : FAST")
elif wpm >= 10:
    print("Flow 🎧 : MEDIUM")
else:
    print("Flow 🎧 : SLOW")

# Feedback statements
if accuracy > 90:
    print("🔥 Incredible! You're typing like a pro!")
elif accuracy > 80:
    print("🌟 Solid work! You're nearly at professional level!")
elif accuracy > 70:
    print("🚀 Nice effort — consistency will take you higher!")
else:
    print("🎯 Missed some hits, but your effort counts. Keep training!")
