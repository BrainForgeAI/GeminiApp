import pytest
from unittest.mock import patch, MagicMock
from ..QuestionGenerator import QuestionGenerator

@pytest.fixture
def question_generator():
    syllabus = "Topic 1: Introduction\nTopic 2: Advanced Concepts"
    return QuestionGenerator(syllabus=syllabus)

def test_initialization(question_generator):
    assert question_generator.syllabus == "Topic 1: Introduction\nTopic 2: Advanced Concepts"
    assert question_generator.questions_so_far == ""

def test_initialization_with_custom_persona_and_guidelines():
    custom_persona = "You are a history professor."
    custom_guidelines = "Focus on dates and important events."
    qg = QuestionGenerator("History syllabus", persona=custom_persona, guidelines=custom_guidelines)
    
    assert qg.persona == custom_persona
    assert qg.guidelines == custom_guidelines

@patch('google.generativeai.GenerativeModel')
def test_generate_response_questions(mock_model, question_generator):
    mock_response = MagicMock()
    mock_response.text = "What is the first topic in the syllabus?"
    mock_model.return_value.generate_content.return_value = mock_response

    response, text = question_generator.generate_response_questions()

    assert response == mock_response
    assert text == "What is the first topic in the syllabus?"
    assert question_generator.questions_so_far == "What is the first topic in the syllabus?"

@patch('google.generativeai.GenerativeModel')
def test_generate_response_questions_with_kwargs(mock_model, question_generator):
    mock_response = MagicMock()
    mock_response.text = "What are the advanced concepts mentioned in Topic 2?"
    mock_model.return_value.generate_content.return_value = mock_response

    response, text = question_generator.generate_response_questions(answer="correct", difficulty="harder")

    assert response == mock_response
    assert text == "What are the advanced concepts mentioned in Topic 2?"
    assert "answer: correct" in mock_model.return_value.generate_content.call_args[0][0]
    assert "difficulty: harder" in mock_model.return_value.generate_content.call_args[0][0]

@patch('google.generativeai.GenerativeModel')
def test_multiple_question_generation(mock_model, question_generator):
    mock_responses = [
        MagicMock(text="Question 1"),
        MagicMock(text="Question 2"),
        MagicMock(text="Question 3"),
    ]
    mock_model.return_value.generate_content.side_effect = mock_responses

    for i in range(3):
        response, text = question_generator.generate_response_questions()
        assert text == f"Question {i+1}"
    
    assert question_generator.questions_so_far == "Question 1Question 2Question 3"

def test_syllabus_in_prompt(question_generator):
    with patch.object(question_generator.model, 'generate_content') as mock_generate:
        question_generator.generate_response_questions()
        prompt = mock_generate.call_args[0][0]
        assert question_generator.syllabus in prompt

def test_persona_in_prompt(question_generator):
    with patch.object(question_generator.model, 'generate_content') as mock_generate:
        question_generator.generate_response_questions()
        prompt = mock_generate.call_args[0][0]
        assert question_generator.persona in prompt

def test_guidelines_in_prompt(question_generator):
    with patch.object(question_generator.model, 'generate_content') as mock_generate:
        question_generator.generate_response_questions()
        prompt = mock_generate.call_args[0][0]
        assert question_generator.guidelines in prompt