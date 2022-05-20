class InferenceEngineZookeeper():
    def __init__(self) -> None:
        self.outcome = ["MAMMAL", "BIRD", "CARNIVORE",
            "UNGULADO", "LEOPARD", "TIGER", "GIRAFFE", "ZEBRA",
            "OSTRICH", "PENGUIN", "ALBATROSS", "WOLF", "DUCK"]
        self.kb = []

        kb_file = open('db/knowledge_base.txt', 'r')
        for line in kb_file:
            if line[len(line)-1] == '\n':
                line = line.replace('\n', '')
                self.kb.append(line.split('-'))
        kb_file.close()

    def nof_animals_on_db(self):
        return len(self.outcome)

    def calculate_probability(self):
        size_zoo = self.nof_animals_on_db()
        return int(1/size_zoo)*100

    def search_backward_chaining(self, assumption, attr):
        size_zoo = self.nof_animals_on_db()
        for i in range(size_zoo):
            if assumption == self.kb[i][1]:
                if self.kb[i][0] == attr:
                    return True
        return False

    def reject_outcome_without_attr(self, attr):
        to_remove = []
        tot_to_remove = 0
        for i in range(self.nof_animals_on_db()):
            oc = self.outcome[i]
            if not self.search_backward_chaining(oc, attr):
                to_remove.append(oc)
                tot_to_remove = tot_to_remove + 1
        for i in range(tot_to_remove):
            self.outcome.remove(to_remove[i])

    def reject_outcome_with_attr(self, attr):
        to_remove = []
        tot_to_remove = 0
        for i in range(self.nof_animals_on_db()):
            oc = self.outcome[i]
            if self.search_backward_chaining(oc, attr):
                to_remove.append(oc)
                tot_to_remove = tot_to_remove + 1
        for i in range(tot_to_remove):
            self.outcome.remove(to_remove[i])

    def get_user_input(self, question, attr):
        answer = input('\n\n~ ' + question + '\n> ')
        answer = answer.lower()

        if answer == 'yes':
            self.reject_outcome_without_attr(attr)
        elif answer == 'no':
            self.reject_outcome_with_attr(attr)

