from question_model import Question
from data import question_data

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
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

print(question_bank[0].answer)
    
    