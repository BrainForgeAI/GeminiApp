import pytest
from flask import json
from server.app import app, gq

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data

def test_get_question_route(client, mocker):
    mock_response = {
        'prev_question': 'right',
        'prev_question_answer': 'a function maps one set of numbers to another, a relation equates two sets of numbers',
        'prev_question_actual_right_answer': 'A function is a special type of relation where each input has exactly one output. A relation is any set of ordered pairs, but a function must map each input to only one output.',
        'question_number': 2,
        'topic': 'Unit 01: Preparing for Calculus I',
        'difficulty': 'Medium',
        'question': 'Determine if the following relation is a function: {(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)}. Explain your reasoning.'
    }
    mocker.patch.object(gq, 'generate_response_questions', return_value=(None, None, mock_response))

    response = client.get('/get_question')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data == mock_response

def test_submit_answer_route(client, mocker):
    mock_response = {
        'prev_question': 'right',
        'prev_question_answer': 'Yes, it is a function because each input (x-value) corresponds to exactly one output (y-value).',
        'prev_question_actual_right_answer': 'Yes, it is a function because each input (x-value) corresponds to exactly one output (y-value).',
        'question_number': 3,
        'topic': 'Unit 01: Preparing for Calculus I',
        'difficulty': 'Hard',
        'question': 'Given the function f(x) = 2x^2 + 3x - 1, find f\'(x) using the definition of a derivative.'
    }
    mocker.patch.object(gq, 'generate_response_questions', return_value=(None, None, mock_response))

    response = client.post('/submit_answer', data={'answer': 'Yes, it is a function because each input (x-value) corresponds to exactly one output (y-value).'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data == mock_response

def test_submit_answer_route_completion(client, mocker):
    mock_response = {
        'question': 'IAMDONE',
        'completed': True
    }
    mocker.patch.object(gq, 'generate_response_questions', return_value=(None, None, mock_response))

    response = client.post('/submit_answer', data={'answer': 'Final answer'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data == {'question': 'Question generation completed.', 'completed': True}
