"""
Module focused exclusively on generating questions from a syllabus of varying difficulty and subject.
"""
import google.generativeai as genai
from dotenv import load_dotenv
import os
from prompts import question_persona, question_guidelines
from tools import generate_with_retry


load_dotenv()
genai.configure(api_key=os.environ["API_KEY"])


class QuestionGenerator:
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    
    def __init__(self, syllabus: str, persona: str = question_persona,
                 guidelines: str=question_guidelines):
        
        """
        :param syllabus:
            The syllabus or course outline from which all questions will be generated.
        :param persona (optional):
            Each prompt includes a persona statement, which helps the language model understand its 
            role and generate more relevant and accurate content. For example: You are an
            award-winning science fiction author with a penchant for expansive, intricately woven
            stories. Your ultimate goal is to write the next award winning sci-fi novel.
        :param guidelines (optional):
            Guidelines that modify or constrain the model's behaviour.
        """
        
        self.persona = persona
        self.guidelines = guidelines
        
        self.syllabus = syllabus
        self.questions_so_far = ""
        
        
    def generate_response_questions(self, **kwargs) -> str:
        """
        Generates new question based on response to previous question.
        
        :param **kwargs:
            Additional info for question continuation.
        
        :return response:
            Entire response object.
        :return response.text:
            Text output of response.
        """
        
        continuation_prompt = f'''
        {self.persona}
        
        Here's the syllabus:
        {self.syllabus}

        Here's what you've written so far (if it's blank, that means we're at the beginning of the question generation!):

        {self.questions_so_far}
        
        Additional info. (If "answer", that means the user provided an answer and you continue the question generation based on the correctness of the answer. If the answer is correct, permit the user to move on. If the answer is incorrect, reject the user).
        
        {', '.join([f'{key}: {value}' for key, value in kwargs.items()])}

        =====

        First, silently review what you've written so far.
        
        Your task is to continue where you left off and write the next question.
        You are not expected to finish the whole syllabus right now. However, once the syllabus
        is COMPLETELY finished, write IAMDONE. Remember, if the answer to the previous question was wrong, generate an easier question on the same topic. If it was right, generate a harder question. Once you fell we've successfull convered this topic, move on to the next topic in the syllabus.

        As a reminder, your guidelines are:
        {self.guidelines}'''
     
        response = generate_with_retry(model=self.model, prompt=continuation_prompt)
        self.questions_so_far += response.text

        return response, response.text
    
    
if __name__ == '__main__':
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
    7. Compute linear approximations to implicit functions using “implicit differentiation”;
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
    iterations = 0
    answer = ""
    while True:
        if iterations == 0:
            _, question = gq.generate_response_questions()
        else:
            _, question = gq.generate_response_questions(answer=answer)
            
        print(question)
        answer = str(input("Whats your answer: "))
        iterations += 1
        
        if "IAMDONE" in question:
            print("Question generation completed.")
            break
    