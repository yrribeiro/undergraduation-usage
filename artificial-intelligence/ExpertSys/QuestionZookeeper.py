class QuestionZookeeper:
    def __init__(self) -> None:
        self.questions = [
            ['Does it have fur?', 'hasFur'],
            ['Does it produce milk?', 'produceMilk'],
            ['Does it has feather?', 'hasFeathers'],
            ['Does it flies?', 'flies'],
            ['Does it produce egg?', 'produceEggs'],
            ['Is it a mammal?', 'isMammal'],
            ['Does it eat meat?', 'isCarnivore'],
            ['Does it have sharp teeth?', 'hasSharpTeeth'],
            ['Does it have claws?', 'hasClaws'],
            ['Does it have frontal eyes?', 'hasFrontalEyes'],
            ['Does it have a hull?', 'hasHull'],
            ['Does it ruminate?', 'ruminate'],
            ['Does it have even number of fingers?', 'hasEvenFingers'],
            ['Is it a carnivore?', 'isCarnivore'],
            ['Does it have a toasted yellow color?', 'colorToastedYellow'],
            ['Does it have dark spots?', 'hasDarkSpots'],
            ['Does it have black lines?', 'hasBlackLines'],
            ['Is it an ungulado?', 'isUngulado'],
            ['Does it have long legs?', 'hasLongLegs'],
            ['Does it have long neck?', 'hasLongNeck'],
            ['Is it white?', 'colorWhite'],
            ['Is it a bird?', 'isBird'],
            ['Is it black and white?', 'colorBlackWhite'],
            ['Does it swims?', 'swims'],
        ]

    def select_question(self):
        question = self.questions[0]
        del self.questions[0]

        return question