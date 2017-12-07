from .models import *

american_average = 78.74

# Get list of questions in list, look up in db to see what linked effects are, put effects into categories, calculate individual categories, average categories

def run_algorithm(data, user_profile):
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
            if (("-F" in symptom.name and user_profile.sex == "F")
                or ("-M" in symptom.name and user_profile.sex == "M")
                or ("-M" not in symptom.name and "-F" not in symptom.name)):

                if symptom.multiplier:
                    causesOfDeathMultiplier[symptom.cause.name] *= symptom.impact
                else:
                    causesOfDeathOffset[symptom.cause.name] += symptom.impact

    # Calculate stuff
    ratio = 1
    for cause in CauseOfDeath.objects.all():
        causesOfDeathOffset[cause.name] *= causesOfDeathMultiplier[cause.name]
        ratio *= (american_average + causesOfDeathOffset[cause.name]) / american_average

    # returns years of life from dob - death.
    return american_average * ratio
