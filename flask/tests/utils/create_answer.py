from models.answer import Answer

def create_answer(
        text=None,
        question=None,
        seals=None
):
    answer = Answer()
    answer.seals = seals
    answer.question = question
    answer.text = text

    return answer
