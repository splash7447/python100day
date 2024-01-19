from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for quiz in question_data:
    question_text = quiz["question"]
    question_answer = quiz["correct_answer"]
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You're completed the quiz")
print(f"Your final score was {quiz.score}/{len(question_bank)}")