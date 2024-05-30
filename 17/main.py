from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for q in question_data:
    question = Question(q['question'], q['correct_answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
points = 0

while quiz.still_has_questions():
    pts = quiz.next_question()
    if pts == 0:
        print("\tWell, that's a wrong answer.")
        break
    else:
        points += pts

print(f"You have scored: {points}")
