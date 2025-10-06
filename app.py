from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message'].lower()  # convert to lowercase for easier matching

    # Initialize bot message
    bot_message = "I’m still learning 😅. Can you ask something else?"

    # 1-5: Greetings
    if "hello" in user_message or "hi" in user_message:
        bot_message = "Hello! Type your question: travel tips, favorite cities, simple math, or just say hi! 🛫💬 "
    elif "hey" in user_message:
        bot_message = "Hey there! Looking for a new adventure? 🌍"
    elif "good morning" in user_message:
        bot_message = "Good morning! Ready to explore the world today? ☀️"
    elif "good night" in user_message:
        bot_message = "Good night! Dreaming about travels? 🌙"
    elif "how are you" in user_message:
        bot_message = "I’m a bot, but I’m vibing! How about you? 😊"

    # 6-10: Farewell
    elif "bye" in user_message or "goodbye" in user_message:
        bot_message = "Goodbye! Catch you later 👋"
    elif "see you" in user_message:
        bot_message = "See you soon! Keep dreaming of adventures 🌏"
    elif "thanks" in user_message or "thank you" in user_message:
        bot_message = "You’re welcome! 💛"
    elif "ok" in user_message or "okay" in user_message:
        bot_message = "Cool! 😎"
    elif "what’s up" in user_message or "sup" in user_message:
        bot_message = "Just helping travelers like you! 🚀"

    # 11-20: Travel destinations info
    elif "paris" in user_message:
        bot_message = "Paris is the city of love! 🗼 Don’t miss the Eiffel Tower and Louvre Museum."
    elif "new york" in user_message:
        bot_message = "New York, New York! 🏙️ Check out Times Square and Central Park."
    elif "tokyo" in user_message:
        bot_message = "Tokyo is buzzing with energy! 🗾 Visit Shibuya Crossing and Senso-ji Temple."
    elif "london" in user_message:
        bot_message = "London is historic and charming! 🇬🇧 Don’t miss the Big Ben and London Eye."
    elif "sydney" in user_message:
        bot_message = "Sydney has stunning beaches and the Opera House! 🌊🎭"
    elif "delhi" in user_message:
        bot_message = "Delhi is full of culture and history! 🇮🇳 Try India Gate and Red Fort."
    elif "paris attractions" in user_message:
        bot_message = "Top Paris attractions: Eiffel Tower, Louvre, Notre-Dame, Montmartre."
    elif "budget travel" in user_message:
        bot_message = "Budget travel tips: Use hostels, local transport, eat street food, travel off-season."
    elif "best season to travel" in user_message:
        bot_message = "It depends on the place! Generally, spring and autumn are great worldwide. 🍃🍂"
    elif "beach destination" in user_message:
        bot_message = "Some top beach destinations: Maldives, Bali, Phuket, Miami. 🏖️"

    # 21-30: Basic math and small talk
    elif "add" in user_message or "+" in user_message:
        try:
            numbers = [int(s) for s in user_message.split() if s.isdigit()]
            bot_message = f"The sum is {sum(numbers)}"
        except:
            bot_message = "I couldn’t figure out the numbers 😅"
    elif "subtract" in user_message or "-" in user_message:
        try:
            numbers = [int(s) for s in user_message.split() if s.isdigit()]
            if len(numbers) >= 2:
                bot_message = f"The result is {numbers[0] - numbers[1]}"
            else:
                bot_message = "I need two numbers to subtract! 🤔"
        except:
            bot_message = "I couldn’t calculate that 😅"
    elif "multiply" in user_message or "*" in user_message:
        try:
            numbers = [int(s) for s in user_message.split() if s.isdigit()]
            result = 1
            for n in numbers:
                result *= n
            bot_message = f"The product is {result}"
        except:
            bot_message = "Oops! Something went wrong with numbers 😅"
    elif "divide" in user_message or "/" in user_message:
        try:
            numbers = [int(s) for s in user_message.split() if s.isdigit()]
            if len(numbers) >= 2 and numbers[1] != 0:
                bot_message = f"The division result is {numbers[0]/numbers[1]}"
            else:
                bot_message = "Cannot divide by zero or missing numbers! ⚠️"
        except:
            bot_message = "Math error 😅"
    elif "joke" in user_message:
        bot_message = "Why don’t scientists trust atoms? Because they make up everything! 😆"
    elif "weather" in user_message:
        bot_message = "I can't check real-time weather yet, but sunny vibes for today! ☀️"
    elif "your name" in user_message:
        bot_message = "I’m TravelBot! Ready to explore the world with you 🌍"
    elif "help" in user_message:
        bot_message = "Ask me about travel destinations, basic math, or just chat with me! ✨"
    elif "time" in user_message:
        from datetime import datetime
        bot_message = f"Current time is {datetime.now().strftime('%H:%M:%S')}"
    elif "date" in user_message:
        from datetime import datetime
        bot_message = f"Today’s date is {datetime.now().strftime('%Y-%m-%d')}"
    elif "favorite place" in user_message:
        bot_message = "I think Paris would be dreamy! 😍"
    elif "tips for travel" in user_message:
        bot_message = "Always carry a map, pack light, and enjoy local food! 🥘"

    return jsonify({'reply': bot_message})


if __name__ == '__main__':
    app.run(debug=True)
