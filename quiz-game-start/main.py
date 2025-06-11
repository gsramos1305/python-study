from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


# score = 0
# for n in question_data:
#     print(n['text'])
#     print(n['answer'])
#     guess = input("\nFalse or True: ").capitalize()
#     if guess == n['answer']:
#         score += 1
#     print('\n' * 5)
#     print(f"score: {score}")


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("---Quiz Completed---")
print(f"Final Score: {quiz.score}/{quiz.question_number}")
    