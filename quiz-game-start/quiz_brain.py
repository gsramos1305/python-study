class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_guess = input(f"Q.{self.question_number} - {current_question.text} (True/False): ")
        self.check_answer(user_guess, current_question.answer)

    def check_answer(self, user_guess, correct_answer):
        if user_guess.capitalize() == correct_answer:
            self.score += 1
            print("---Right---")
        else:
            print("---Wrong---")
            print(f"Correct answer: {correct_answer}")

        print(f"Current Score: {self.score}/{self.question_number}")
        print('\n' * 3)
