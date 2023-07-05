import requests
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the pre-trained model and tokenizer
model_name = "tiiuae/falcon-40b"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Retrieve the text from the GitHub repository
repo_url = "https://raw.githubusercontent.com/amandewatnitrr/gradle-tutorial/main/README.md"
response = requests.get(repo_url)
text = response.text

# Define a function to generate a summary from the text
def generate_summary(text):
    # Encode the text
    input_ids = tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)
    # Generate a summary
    summary_ids = model.generate(input_ids, max_length=100, num_return_sequences=1, early_stopping=True)
    # Decode and return the generated summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Generate a summary of the text
summary = generate_summary(text)
print("Summary:", summary)

# Test the chatbot
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    else:
        response = generate_summary(user_input)
        print("Chatbot:", response)
