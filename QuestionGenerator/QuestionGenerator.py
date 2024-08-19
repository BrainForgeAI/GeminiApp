"""
Module focused exclusively on generating questions from a syllabus of varying difficulty and subject.
"""
import google.generativeai as genai
from google.generativeai.types.generation_types import GenerateContentResponse
from dotenv import load_dotenv
import os
import json
from .prompts import question_persona, question_guidelines
from .tools import generate_with_retry


load_dotenv()
genai.configure(api_key=os.environ["API_KEY"])


class QuestionGenerator:
    model = genai.GenerativeModel(model_name='gemini-1.5-flash', generation_config={"response_mime_type": "application/json"})
    
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
        
        
    def generate_response_questions(self, **kwargs) -> tuple[GenerateContentResponse, str, dict]:
        """
        Generates new question based on response to previous question.
        
        :param **kwargs:
            Additional info for question continuation.
        
        :return response:
            Entire response object.
        :return response.text:
            Text output of response.
        :return json.loads(response.text):
            Dictionary version of text output.
        """
        
        continuation_prompt = f'''
        {self.persona}
        
        Here's the syllabus:
        {self.syllabus}

        Here's what you've written so far (if it's blank, that means we're at the beginning of the question generation!):

        {self.questions_so_far}
        
        Additional info.
        (If "answer", that means the user provided an answer and you continue the question generation based on the correctness of the answer. If the answer is correct, permit the user to move on. If the answer is incorrect, reject the user).
        (If "multiple-choice", that means you should generate a multiple choice question with 4 possible options. Add these options as mcq_options = dict() to the JSON output).
        
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

        return response, response.text, json.loads(response.text)
