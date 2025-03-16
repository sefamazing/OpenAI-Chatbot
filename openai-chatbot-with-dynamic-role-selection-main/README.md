# ChatBot with Dynamic Role Selection

## Overview

This project is a web-based ChatBot application built using Flask and OpenAI's GPT-3.5 Turbo. The application allows users to select their role dynamically and engage in conversations with the ChatBot. The role selection feature ensures that the ChatBot tailors its responses based on the user's chosen role.

## Features

- **Dynamic Role Selection:** Users can choose their role (e.g., University Guide, Sports Guide, Medical Guide) through a modal dialog before starting the chat.
- **Personalized Responses:** The ChatBot provides detailed and personalized responses based on the selected role.
- **Chat History:** The application saves chat history to a file for each session.
- **Responsive Design:** The front end is built with Bootstrap, making it responsive and user-friendly.

## Technologies Used

- **Backend:** Flask, OpenAI GPT-3.5 Turbo
- **Frontend:** HTML, CSS, Bootstrap, jQuery

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Flask
- OpenAI API Key

### Installation

### Installation

##  1. Install the required dependencies:

  pip install -r requirements.txt

### 2.Set up your OpenAI API key in app.py:

  openai.api_key = "your-openai-api-key"
  
### 3.Run the application:

  python app.py

### Usage
Open your web browser and navigate to http://127.0.0.1:5000/.
A modal will prompt you to select your role.
Enter your messages in the chat window and receive personalized responses from the ChatBot.
