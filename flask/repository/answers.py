from models.answer import Answer

def create_answers_with_form_and_question(form, question):
    answers = []
    for (key, value) in form.items():
        if value and key.startswith('answerText'):
            answer = Answer()
            answer.question = question
            answer.text = value
            answers.append(answer)
    return answers
