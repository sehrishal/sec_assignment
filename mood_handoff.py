class Runner:
    @staticmethod
    def run(agent, message):
        return agent.handle(message)

class MoodAnalyzerAgent:
    def handle(self, message):
        message = message.lower()
        if "sad" in message or "upset" in message:
            return "sad"
        elif "stressed" in message or "overwhelmed" in message:
            return "stressed"
        elif "happy" in message or "great" in message:
            return "happy"
        elif "angry" in message:
            return "angry"
        else:
            return "neutral"

class ActivitySuggesterAgent:
    def handle(self, mood):
        if mood == "sad":
            return "Try watching a comforting movie or talking to a friend."
        elif mood == "stressed":
            return "Take a short walk or try a breathing exercise."
        else:
            return "You're doing fine! No activity needed."

# Main execution
if __name__ == "__main__":
    user_input = input("👤 How are you feeling today? ")

    # Run Mood Analyzer
    mood = Runner.run(MoodAnalyzerAgent(), user_input)
    print(f"🧠 Detected Mood: {mood}")

    # Handoff to Activity Suggester if needed
    if mood in ["sad", "stressed"]:
        suggestion = Runner.run(ActivitySuggesterAgent(), mood)
        print(f"🎯 Suggested Activity: {suggestion}")
    else:
        print("✅ No special suggestion needed.")
 