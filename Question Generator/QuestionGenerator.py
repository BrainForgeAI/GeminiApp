"""
Module focused exclusively on generating questions from a syllabus of varying difficulty and subject.
"""
import google.generativeai as genai
from dotenv import load_dotenv
import os
from prompts import question_persona, question_guidelines


load_dotenv()
genai.configure(api_key=os.environ["API_KEY"])


class QuestionGenerator:
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    
    def __init__(self, persona: str = question_persona, guidelines: str=question_guidelines):
        
        """
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