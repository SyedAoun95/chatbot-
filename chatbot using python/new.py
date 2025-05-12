import random
import string

# Create a knowledge base (dictionary or list)
knowledge_base = {
    "What is your name?": "I'm a chatbot.",
    "What is the capital of Pakistan?": "Islamabad",
    "What is 2 + 2?": "4",
    "What is the largest planet in our solar system" :"jupitar"
    # Add more questions and answers here
}

# Function to find the best match for a given user input
def find_best_match(user_input, knowledge_base):
    best_match = None
    best_match_score = 0

    for question in knowledge_base.keys():
        # Calculate similarity using a suitable metric (e.g., Jaccard similarity, Levenshtein distance)
        similarity_score = calculate_similarity(user_input, question)

        if similarity_score > best_match_score:
            best_match = question
            best_match_score = similarity_score

    return best_match

# Function to calculate similarity between two strings (e.g., Jaccard similarity)
def calculate_similarity(string1, string2):
    # Implement your chosen similarity metric here
    # For example, using Jaccard similarity:
    set1 = set(string1.split())
    set2 = set(string2.split())
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    if len(union) == 0:
        return 0
    return len(intersection) / len(union)

# Chatbot response function
def chatbot_response(user_input):
    best_match = find_best_match(user_input, knowledge_base)

    if best_match:
        return knowledge_base[best_match]
    else:
        return "I couldn't find an answer to that. Please try asking something else."

# Main chat loop
def chat():
    print("Hello! I'm a chatbot. Ask me anything.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break

        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()