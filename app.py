import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure the API key
API_KEY = os.getenv('API_KEY')
genai.configure(api_key=API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_email', methods=['POST'])
def generate_email():
    author = request.form['author']
    receiver = request.form['receiver']
    tone = request.form['tone']
    subject = request.form['subject']
    context = request.form['context']
    between_lines = request.form.get('between_lines', '')
    email_length = request.form['email_length']
    attachments = request.form.get('attachments', '')

    if not author or not receiver or not tone or not subject or not context or not email_length:
        return jsonify({'error': 'All fields except "Between the lines" and "Attachments" are required'})

    prompt = (f"Write a {tone} email from {author} to {receiver} with the subject '{subject}'. "
              f"Include a complete email body. Context: {context}. "
              f"The email should be {email_length}.")

    if between_lines:
        prompt += f" Implicitly convey: {between_lines}."
    if attachments:
        prompt += f" Attachments are about: {attachments}."
    else:
        prompt += " No attachments."

    model = genai.GenerativeModel('gemini-1.5-flash')

    try:
        response = model.generate_content(prompt)
        return jsonify({'email': response.text})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
