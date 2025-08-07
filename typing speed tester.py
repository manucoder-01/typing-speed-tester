import time 
import random 
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful programming language.",
    "Typing fast helps improve productivity.",
    "Practice makes a person perfect.",
    "Always write clean and readable code."

] 
test_sentence= random.choice(sentences)
print("✍️ Type the following sentence:\n")
print(test_sentence)

start_time =time.time()
user_input = input("\n⌨️ Now type here:\n")
end_time= time.time()

time_taken = end_time -start_time
print(f"\n⏱️ You took {round(time_taken, 2)} seconds.")

word_count = len(test_sentence.split())
wpm = (word_count/ time_taken)*60
print(f"⚡ Your Typing Speed: {round(wpm, 2)} words per minute (WPM)")

correct_chars =0
for i in range(min(len(test_sentence),len(user_input))):
    if test_sentence[i]==user_input[i]:
        correct_chars+1

accuracy = (correct_chars / len(test_sentence))*100
print(f"🎯 Accuracy: {round(accuracy, 2)}%")

with open("typing_result.txt","a",encoding="utf-8") as file:
    file.write(f"TIME:{round(time_taken,2)}s|⚡ Speed: {round(wpm, 2)} WPM | 🎯 Accuracy: {round(accuracy, 2)}%\n  ")