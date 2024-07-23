from flask import Flask, render_template, request, jsonify
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from QuestionGenerator import QuestionGenerator

app = Flask(__name__)

sample_syllabus = '''Calc 1 Course Structure
    This course is divided into 12 units of study:
    • Unit 01: Preparing for Calculus I
    • Unit 02: Preparing for Calculus II
    • Unit 03: Limits and Continuity
    • Unit 04: The Derivative I
    • Unit 05: The Derivative II
    • Unit 06: More About Derivatives I
    • Unit 07: More About Derivatives II
    • Unit 08: Applications of the Derivative I
    • Unit 09: Applications of the Derivative II
    • Unit 10: The Integral I
    • Unit 11: The Integral II
    • Unit 12: The Integral III
    Learning Outcomes
    Course Learning Outcomes
    This course is designed for students interested in the application of mathematics in the
    biological sciences. Some of the topics covered include: the role of mathematics in
    biology decisions; elementary functions, sequences and series, difference equations,
    differential calculus and integral calculus.
    By the end of this course, you should be able to:
    1. Determine the domain, range and the inverse of a function and form a composite
    function;
    2. Describe the differences between sequences and series, and use formulas
    resulting from finite and infinite series to solve problems involving payments,
    deposits, dosage of drugs, and population size;
    3. Compute basic limits of functions and discuss the importance of limits to the
    process of differentiation. Determine where and whether functions are
    continuous, and identify and classify points of discontinuity;
    4. Explain the derivative in terms of the idea of a tangent line to the graph of a
    function and how a derivative can be used to describe the rate of change of one
    quantity with respect to another;
    5. Differentiate a wide class of single-variable functions, including polynomials,
    trigonometric, exponential, logarithmic, sums, products, quotients, compositions;
    6. Apply the chain rule to find derivatives of different functions including functions
    raised to a power, exponential, and logarithmic functions;
    7. Compute linear approximations to implicit functions using "implicit differentiation";
    Page 4 of 22
    8. Use derivatives to solve applied problems involving rate-of-change, maximum
    and minimum values; critical numbers; local extrema and concavity and
    optimization;
    9. Use integrals to solve problems involving area.
    10.Find a definite integral using the limit of Riemann sums.
    11.Evaluate definite integrals using the Fundamental Theorem of Calculus.
    12.Find indefinite and definite integral using substitution.
    '''

gq = QuestionGenerator(syllabus=sample_syllabus)
current_question = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_question', methods=['GET'])
def get_question():
    global current_question
    _, current_question = gq.generate_response_questions()
    return jsonify({'question': current_question})

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    global current_question
    answer = request.form['answer']
    _, current_question = gq.generate_response_questions(answer=answer)
    
    if "IAMDONE" in current_question:
        return jsonify({'question': "Question generation completed.", 'completed': True})
    
    return jsonify({'question': current_question, 'completed': False})

if __name__ == '__main__':
    app.run(debug=True)