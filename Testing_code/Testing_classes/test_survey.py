import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions"""
    question = "What language did you first learn"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored properly"""
    language_survey.store_response("English")
    assert "English" in language_survey.reponses

def test_multiple_responses(language_survey):
    """Test that survey class can hold multiple responses"""
    responses = ["English", "Arabic","Italian"] 
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.reponses
