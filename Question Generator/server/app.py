from flask import Flask, render_template, request, jsonify
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from QuestionGenerator import QuestionGenerator
from prompts import sample_syllabus

app = Flask(__name__)


gq = QuestionGenerator(syllabus=sample_syllabus)
current_question = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_question', methods=['GET'])
def get_question():
    global current_question
    _, _, current_question = gq.generate_response_questions()
    
    return jsonify(current_question)

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    global current_question
    answer = request.form['answer']
    _, _, current_question = gq.generate_response_questions(answer=answer)
    
    if "IAMDONE" in current_question['question']:
        return jsonify({'question': "Question generation completed.", 'completed': True})
    
    return jsonify(current_question)

if __name__ == '__main__':
    app.run(debug=True, port=5001)