from InferenceEngineZookeeper import InferenceEngineZookeeper
from QuestionZookeeper import QuestionZookeeper

inference_engine = InferenceEngineZookeeper()
questionnaire = QuestionZookeeper()


while len(inference_engine.outcome) > 1:
	question = questionnaire.select_question()
	inference_engine.get_user_input(question[0], question[1])

	cnf = inference_engine.calculate_probability()
	outcome = inference_engine.outcome
	print(f'- Outcome: {outcome}\n--- confidence: {cnf}')

	if cnf == 100:
		print(f'YOUR ANIMAL IS A/AN {outcome[0]}')