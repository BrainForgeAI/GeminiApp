from flask import Flask, render_template, request, jsonify, Response
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from QuestionGenerator import QuestionGenerator
from load_syllabus import load_syllabus

app = Flask(__name__)

# Will raise Exception as currently implemented since file isn't being passed in.
_, syllabus = load_syllabus(gemini_model=QuestionGenerator.model)
qg = QuestionGenerator(syllabus=syllabus)
current_question = {}

@app.route('/')
def index() -> str:
    """
    Renders index.html.
    """
    return render_template('index.html')

@app.route('/get_question', methods=['GET'])
def get_question() -> Response:
    """
    Get request for question prompt.
    
    :return jsonify(current_question):
        JSON Response object.
    """
    global current_question
    _, _, current_question = qg.generate_response_questions()
    
    return jsonify(current_question)

@app.route('/submit_answer', methods=['POST'])
def submit_answer() -> Response:
    """
    Post request for question prompt.
    
    :return jsonify(current_question):
        JSON Response object.
    """
    global current_question
    answer = request.form['answer']
    _, _, current_question = qg.generate_response_questions(answer=answer)
    
    if "IAMDONE" in current_question['question']:
        return jsonify({'question': "Question generation completed.", 'completed': True})
    
    return jsonify(current_question)

if __name__ == '__main__':
    app.run(debug=True, port=5001)