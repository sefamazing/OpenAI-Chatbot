from flask import Flask, render_template, request, session
import openai
import os
import time

# OpenAI API key
openai.api_key = "Your OpenAI API Key"

# Flask app initialization
app = Flask(__name__)
app.secret_key = '667d58645c41e6f432264ae5df989978'  # Secret key for session management

# Initialize variables for chat history
explicit_input = ""
chatgpt_output = 'Chat log: \n'
cwd = os.getcwd()
i = 1

# Find an available chat history file
while os.path.exists(os.path.join(cwd, f'chat_history{i}.txt')):
    i += 1

history_file = os.path.join(cwd, f'chat_history{i}.txt')

# Create a new chat history file
with open(history_file, 'w') as f:
    f.write('\n')

# Initialize chat history
chat_history = ''

# Read additional information from a file
def read_additional_info(file_path='data.txt'):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:  # For Turkish characters 
            additional_info = file.read()
    else:
        additional_info = ""
    return additional_info            

# Function to complete chat input using OpenAI's GPT-3.5 Turbo
def chatcompletion(user_input, impersonated_role, explicit_input, chat_history, additional_info):
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301", 
        temperature=0.7,  
        presence_penalty=0.6, 
        frequency_penalty=0.5, 
        max_tokens=2000,
        messages=[
            {"role": "system", "content": f"{impersonated_role}. Here is some additional info you can use: {additional_info}. Conversation history: {chat_history}"},
            {"role": "user", "content": f"{user_input}. {explicit_input}"},
        ]
    )

    for item in output['choices']:
        chatgpt_output = item['message']['content']

    return chatgpt_output

# Function to handle user chat input
def chat(user_input):
    global chat_history, chatgpt_output
    current_day = time.strftime("%d/%m", time.localtime())
    current_time = time.strftime("%H:%M:%S", time.localtime())
    additional_info = read_additional_info()
    chat_history += f'\nUser: {user_input}\n'
    role = session.get('role', 'Guide')
    impersonated_role = f"""
        From now on, you are going to act as ChatBot. Your role is {role}.
        You are a true impersonation of ChatBot and you reply to all requests with "I" pronoun. You give very detailed information.
    """
    chatgpt_output = chatcompletion(user_input, impersonated_role, explicit_input, chat_history, additional_info)
    chat_history += f' ChatBot: {chatgpt_output}\n'

    # Save the chat history to the file
    with open(history_file, 'a') as f:
        f.write(f'User: {user_input}\nChatBot: {chatgpt_output}\n')

    return chatgpt_output

# Function to get a response from the chatbot
def get_response(userText):
    return chat(userText)

# Define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
# Function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(get_response(userText))

# Route for setting user role
@app.route("/set_role", methods=['POST'])
def set_role():
    role = request.form['role']
    session['role'] = role  # Store role in session
    return 'Role set successfully'

# Run the Flask app
if __name__ == "__main__":
    app.run()
