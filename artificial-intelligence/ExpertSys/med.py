from InferenceEngineMed import InferenceEngineMed
from QuestionMed import QuestionMed

inference_engine = InferenceEngineMed()
questionnaire = QuestionMed()


while len(inference_engine.outcome) > 1:
    question = questionnaire.select_question()
    inference_engine.get_user_input(question[0], question[1])

    cnf = inference_engine.calculate_probability()
    if cnf == -1:
        print("{!} Error! There's no mapped disease with those symptoms. {!}")
        break

    outcome = inference_engine.outcome
    print(f'- Outcome: {outcome}\n--- confidence: {cnf}')

    if cnf == 100:
        print(f'YOUR DIAGNOSIS IS {outcome[0]}')
