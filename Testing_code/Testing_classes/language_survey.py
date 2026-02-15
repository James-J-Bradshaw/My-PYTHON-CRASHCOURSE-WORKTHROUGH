from survey import AnonymousSurvey
question = "what language did you first learn"
language_survey =AnonymousSurvey(question)
#   show the question, and store responses to the question
language_survey.show_question()
print("press 'q' at any time to quit")
while True:
    response = input("Language: ")
    if response == "q":
        break
    language_survey.store_response(response)

#   show survey results
print("\n Thank you for everyone who participated, these are the results \n")
language_survey.show_results()