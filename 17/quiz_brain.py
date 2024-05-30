class QuizBrain:

    def __init__(self, question_list, question_number=0):
        self.question_list = question_list
        self.question_number = question_number
        self.size = len(question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        user_in = input(f"Q.{self.question_number}: {current_question.text} (True / False): ").lower()
        if user_in == current_question.answer.lower():
            return 1
        else:
            return 0

    def still_has_questions(self):
        return self.question_number < self.size
