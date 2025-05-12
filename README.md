Simple Chatbot in Python

A basic rule-based chatbot implemented in Python using string similarity (Jaccard similarity) to understand user queries and respond accordingly from a predefined knowledge base.

Features

Rule-based question-answer chatbot
Uses Jaccard similarity to match user queries with known questions
Easily extendable knowledge base
CLI-based chat interface
Educational and beginner-friendly Python project Getting Started
Prerequisites: Python 3.x installed on your system

Installation:

Clone the repository: git clone

Run the chatbot: python chatbot.py

(Replace chatbot.py with your actual Python filename if different)

How It Works

The chatbot contains a predefined knowledge base (a dictionary of questions and answers). When a user types a question, it compares the input to each known question using the Jaccard similarity metric. The most similar question is selected and its corresponding answer is returned. If no suitable match is found, the chatbot provides a default fallback response.

Sample Knowledge Base

The knowledge base includes questions such as:

What is your name?
What is the capital of Pakistan?
What is 2 + 2?
What is the largest planet in our solar system?
You can expand this dictionary to handle more queries and responses.

Integrate advanced NLP using libraries like spaCy or NLTK
Add a graphical user interface using Tkinter or a web framework
Enhance intent recognition using machine learning models
License

This project is open-source and available under the MIT License.

Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.
