from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

def get_bot_response(user_input):
    input_text = user_input.lower()

    # 25 conditions
    if "hi" in input_text or "hello" in input_text:
        return "Hello! I am ProBot. I can answer questions about technology, programming, web development, AI, and general info. Try asking me something!"
    elif "how are you" in input_text:
        return "I'm a bot, so I don't have feelings, but I'm always ready to help you!"
    elif "your name" in input_text:
        return "I am ProBot, your professional chatbot assistant."
    elif "programming languages" in input_text:
        return "I can provide information on languages like Python, C, C++, Java, HTML, CSS, and JavaScript."
    elif "web development" in input_text:
        return "Web development involves HTML, CSS, JavaScript for frontend, and Python, PHP, or Node.js for backend."
    elif "ai" in input_text:
        return "AI stands for Artificial Intelligence. It includes machine learning, deep learning, and natural language processing."
    elif "python" in input_text:
        return "Python is a versatile programming language used for web development, AI, automation, and more."
    elif "c programming" in input_text:
        return "C is a powerful language for system programming, embedded systems, and performance-critical applications."
    elif "c++" in input_text:
        return "C++ is an extension of C with object-oriented features, widely used in game development and system software."
    elif "java" in input_text:
        return "Java is platform-independent, mainly used for enterprise applications and Android development."
    elif "html" in input_text:
        return "HTML is the standard markup language for creating web pages."
    elif "css" in input_text:
        return "CSS is used to style HTML content, controlling layout, colors, fonts, and animations."
    elif "javascript" in input_text:
        return "JavaScript adds interactivity to websites and is essential for modern frontend development."
    elif "project ideas" in input_text:
        return "You can create web apps, AI-based tools, chatbots, games, or mobile apps as projects."
    elif "internship" in input_text:
        return "Internships are a great way to gain practical experience. Focus on web development, AI, or software development."
    elif "ui/ux" in input_text:
        return "UI/UX design focuses on user interface and experience to make apps intuitive and visually appealing."
    elif "career" in input_text:
        return "Career options include software development, AI/ML, web development, data science, and product design."
    elif "tips" in input_text:
        return "Practice coding, work on projects, read documentation, and stay updated with the latest tech trends."
    elif "tools" in input_text:
        return "Useful tools include VS Code, Figma, Photoshop, GitHub, and browser developer tools."
    elif "learning" in input_text:
        return "You can learn from online courses, tutorials, YouTube, and by practicing projects."
    elif "help" in input_text:
        return "I can answer questions about tech, programming, web development, AI, and more."
    elif "thank you" in input_text or "thanks" in input_text:
        return "You're welcome! Happy to help."
    elif "bye" in input_text or "goodbye" in input_text:
        return "Goodbye! Have a great day."
    elif "date" in input_text:
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}."
    elif "time" in input_text:
        return f"Current time is {datetime.now().strftime('%H:%M:%S')}."
    else:
        return "I'm not sure about that. Please ask me about programming, web development, AI, or tech."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json["message"]
    response = get_bot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
