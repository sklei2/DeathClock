from .models import *

american_average = 78.74

# Get list of questions in list, look up in db to see what linked effects are, put effects into categories, calculate individual categories, average categories

def run_algorithm(data):
    # Dictionaries of offsets and multipliers for each cause of death
    causesOfDeathOffset = {}
    causesOfDeathMultiplier = {}

    # Init each dictionary
    for cause in CauseOfDeath.objects.all():
        causesOfDeathOffset[cause.name] = 0
        causesOfDeathMultiplier[cause.name] = 1

    # For each question
    for q in data:
        question = Question.objects.filter(question=str(q))[0]
        # Get all symptoms, for each symptom
        for map in QuestionSymptomMapper.objects.filter(question=question.id):
            symptom = Symptom.objects.filter(id=map.symptom.id)[0]
            # Sum or multiply into appropriate dictionary
            if symptom.multiplier:
                causesOfDeathMultiplier[symptom.cause.name] *= symptom.impact
            else:
                causesOfDeathOffset[symptom.cause.name] += symptom.impact

    # Apply each multiplier
    for cause in CauseOfDeath.objects.all():
        causesOfDeathOffset[cause.name] *= causesOfDeathMultiplier[cause.name]

    # Average values
    sum = 0
    for cause in CauseOfDeath.objects.all():
        sum += causesOfDeathOffset[cause.name]

    subVal = sum / len(CauseOfDeath.objects.all())
    print(subVal)
    print(american_average + subVal)

    return american_average + subVal
