import random


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.correct_answers = 0
        self.question_list = question_list

    def have_next_question(self):
        return not self.question_number == len(self.question_list)

    def get_next_question(self):
        random_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number} {random_question.text} (True / False): ")
        result = "No, that's wrong"
        if answer == random_question.answer:
            self.correct_answers += 1
            result = "Yes, that's correct"
        return result + f" ({self.correct_answers}/{self.question_number})"
