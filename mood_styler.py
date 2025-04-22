
import json
import os

def get_outfit(mood):
    if not os.path.exists('moods.json'):
        print("Error: moods.json not found.")
        return

    with open('moods.json', 'r') as file:
        try:
            moods = json.load(file)
        except json.JSONDecodeError:
            print("Error: Failed to parse moods.json.")
            return

    mood = mood.lower()
    if mood in moods:
        suggestion = moods[mood]
        print("\n--- Outfit Suggestion ---")
        print(f"Style: {suggestion['style']}")
        print(f"Colors: {', '.join(suggestion['colors'])}")
        print(f"Outfit: {suggestion['outfit']}")
    else:
        print("Sorry, mood not found. Try: happy, moody, or calm.")

if __name__ == "__main__":
    user_mood = input("What's your mood? (happy, moody, calm): ")
    get_outfit(user_mood)
