from models.question import Question

def create_question(
        text=None
):
    question = Question()
    question.text = text

    return question
