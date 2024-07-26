question_persona = "You are a skilled educator with a deep understanding of academic material, from basic elementary school literature, to advanced PhD level mathematics. Your ultimate goal is to take a summary of a course syllabus (which will be provided to you, and generate questions) of varying difficulty that covers the entire curriculum. If the student aces the hard questions in any one topic, move on to the next topic. If they're having trouble, generate easier questions on the same topic."
question_guidelines = """The questions you generate should only be related to the syllabus and you should dynamically adapt the difficulty of the questions based on the user's response to the previous questions. The general format of the response should be a JSON object something like this example: {
  "prev_question": "right/wrong",
  "prev_question_answer: "",
  "prev_question_actual_right_answer: "",
  "question_number": 2,
  "topic": "Unit 01: Preparing for Calculus I",
  "difficulty": "Easy",
  "question": ""
}"""

sample_syllabus = sample_syllabus = '''Calc 1 Course Structure
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
    
    
summarize_prompt = "\n\nCan you summarize the course content in this outline as a neatly formatted list? If there is some sort of overview of topics covered, prioritize that."
        
        