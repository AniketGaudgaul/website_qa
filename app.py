from flask import Flask, request, jsonify
from utils.content_loader import load_web_content
from utils.text_processing import process_and_index
from utils.retriever_generator import retriever_generator
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# These should be initialized with the necessary API keys or configurations
llm = ChatOpenAI(model="gpt-3.5-turbo-0125",temperature=0.0)  # Initialize your language model here

@app.route('/answer', methods=['POST'])
def answer_question():
    try:
        # Extract URL and question from POST request
        data = request.json
        url = data['url']
        question = data['question']

        # Load the contents of the webpage
        docs = load_web_content(url)

        # Process and index the contents
        vectorstore = process_and_index(docs)

        # Setup retriever and generator
        answer = retriever_generator(vectorstore, question, llm)

        # Return the answer as JSON
        print(answer)
        return jsonify({'answer': answer})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)