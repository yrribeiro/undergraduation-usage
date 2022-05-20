class QuestionMed:
    def __init__(self) -> None:
        self.questions = [
            ['Do you feel body aches?', 'bodyache'],
            ['Do you cough oftenly?', 'cough'],
            ['Do you have high blood pressure?', 'highBloodPressure'],
            ['Do you have fatigue?', 'fatigue'],
            ['Do you have sore throat?', 'soreThroat'],
            ['Have you noticed headaches?', 'headache'],
            ['Do you cough oftenly?', 'cough'],
        ]

    def select_question(self):
        question = self.questions[0]
        del self.questions[0]

        return question