class QuizBrain:


    def __init__(self, q_list):
        self.quiz_list = q_list
        self.quiz_number = 0
        self.q_score = 0

    def ask_question(self):
        self.current_question = self.quiz_list[self.quiz_number]
        self.quiz_number += 1
        u_answer = input(f"Q.{self.quiz_number}: {self.current_question.text} true/false?: ").lower()
        self.check_answer(u_answer, self.current_question.answer.lower())

    def still_has_questions(self):
        return self.quiz_number < len(self.quiz_list)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.q_score +=1
            print(f"Your current score is {self.q_score} / {self.quiz_number}")
        else:
            print("You got it wrong!")
            print(f"Your current score is {self.q_score} / {self.quiz_number}")
