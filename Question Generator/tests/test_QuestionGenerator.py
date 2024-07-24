import pytest
from unittest.mock import patch, MagicMock
from QuestionGenerator import QuestionGenerator
from google.generativeai.types.generation_types import GenerateContentResponse
import json

# Mock the environment and API key configuration
@pytest.fixture(autouse=True)
def mock_env_and_genai(monkeypatch):
    monkeypatch.setenv("API_KEY", "mock_api_key")
    monkeypatch.setattr("google.generativeai.configure", lambda api_key: None)

# Sample data for testing
sample_syllabus = "Sample syllabus content"
sample_persona = "Sample persona"
sample_guidelines = "Sample guidelines"

@pytest.fixture
def question_generator():
    return QuestionGenerator(syllabus=sample_syllabus, persona=sample_persona, guidelines=sample_guidelines)

def test_question_generator_initialization(question_generator):
    assert question_generator.syllabus == sample_syllabus
    assert question_generator.persona == sample_persona
    assert question_generator.guidelines == sample_guidelines
    assert question_generator.questions_so_far == ""

@patch('question_generator.generate_with_retry')
def test_generate_response_questions(mock_generate_with_retry, question_generator):
    # Mock the response from generate_with_retry
    mock_response = MagicMock(spec=GenerateContentResponse)
    mock_response.text = json.dumps({
        "question": "Sample question",
        "difficulty": "Medium",
        "topic": "Sample topic"
    })
    mock_generate_with_retry.return_value = mock_response

    # Call the method
    response, text, json_data = question_generator.generate_response_questions(answer="Sample answer")

    # Assertions
    assert isinstance(response, GenerateContentResponse)
    assert text == mock_response.text
    assert json_data == json.loads(mock_response.text)
    assert question_generator.questions_so_far == mock_response.text

    # Check if generate_with_retry was called with correct arguments
    mock_generate_with_retry.assert_called_once()
    call_args = mock_generate_with_retry.call_args[1]
    assert 'model' in call_args
    assert 'prompt' in call_args
    assert sample_syllabus in call_args['prompt']
    assert sample_persona in call_args['prompt']
    assert sample_guidelines in call_args['prompt']
    assert "answer: Sample answer" in call_args['prompt']

def test_generate_response_questions_with_multiple_kwargs(question_generator):
    with patch('question_generator.generate_with_retry') as mock_generate_with_retry:
        mock_response = MagicMock(spec=GenerateContentResponse)
        mock_response.text = json.dumps({"question": "Sample question"})
        mock_generate_with_retry.return_value = mock_response

        question_generator.generate_response_questions(answer="Sample answer", difficulty="Hard", topic="Advanced Math")

        call_args = mock_generate_with_retry.call_args[1]['prompt']
        assert "answer: Sample answer" in call_args
        assert "difficulty: Hard" in call_args
        assert "topic: Advanced Math" in call_args

@patch('question_generator.generate_with_retry')
def test_questions_so_far_accumulation(mock_generate_with_retry, question_generator):
    mock_response1 = MagicMock(spec=GenerateContentResponse)
    mock_response1.text = json.dumps({"question": "Question 1"})
    mock_response2 = MagicMock(spec=GenerateContentResponse)
    mock_response2.text = json.dumps({"question": "Question 2"})
    
    mock_generate_with_retry.side_effect = [mock_response1, mock_response2]

    question_generator.generate_response_questions()
    question_generator.generate_response_questions()

    assert question_generator.questions_so_far == mock_response1.text + mock_response2.text

if __name__ == "__main__":
    pytest.main()