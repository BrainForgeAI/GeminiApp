import os
from flask import Flask, render_template, request, jsonify, Response

# Add the parent directory to the Python path.
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from QuestionGenerator.QuestionGenerator import QuestionGenerator
from QuestionGenerator.load_syllabus import load_syllabus


app = Flask(__name__)

qg = None
current_question = {}

@app.route('/load_syllabus', methods=['POST'])
def upload_syllabus() -> Response:
    """
    Loads syllabus with from file upload.
    
    :returns Response JSON object.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = file.filename
        file_path = os.path.join('uploads', filename)
        os.makedirs('uploads', exist_ok=True)
        file.save(file_path)
        
        try:
            global qg
            print("problem")
            _, syllabus = load_syllabus(gemini_model=QuestionGenerator.model, path_to_file=file_path)
            print('solution')
            qg = QuestionGenerator(syllabus=syllabus)
            return jsonify({'message': 'Syllabus loaded successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

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
    global current_question, qg
    if qg is None:
        return jsonify({'error': 'Syllabus not loaded'}), 400
    _, _, current_question = qg.generate_response_questions()
    
    return jsonify(current_question)

@app.route('/get_question_mcq', methods=['GET'])
def get_question_mcq() -> Response:
    """
    Get request for multiple choice question prompt.
    
    :return jsonify(current_question)
    """
    global current_question, qg
    if qg is None:
        return jsonify({'error': 'Syllabus not loaded'}), 400
    _, _, current_question = qg.generate_response_questions(multiple_choice=True)
    
    return jsonify(current_question)

@app.route('/submit_answer', methods=['POST'])
def submit_answer() -> Response:
    """
    Post request for question prompt.
    
    :return jsonify(current_question):
        JSON Response object.
    """
    global current_question, qg
    if qg is None:
        return jsonify({'error': 'Syllabus not loaded'}), 400
    answer = request.form['answer']
    _, _, current_question = qg.generate_response_questions(answer=answer)
    
    if "IAMDONE" in current_question['question']:
        return jsonify({'question': "Question generation completed.", 'completed': True})
    
    return jsonify(current_question)

if __name__ == '__main__':
    app.run(debug=True, port=5001)