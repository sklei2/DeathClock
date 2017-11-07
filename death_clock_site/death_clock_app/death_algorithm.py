from .models import *

american_average = 78.74


def run_algorithm(data):
    offset_values = mine_data(data)

    return american_average


def mine_data(data):
    questions = []
    answer_life_effect = []
    for item in data:
        questions.append(item.Key)
        answer = Answer.objects.filter(question=Question.get(question=item.Key))[int(item.Value)]
        offset = answer.impact
        offset_type = answer.impact_type
        answer_life_effect.append((offset, offset_type))
    return answer_life_effect
