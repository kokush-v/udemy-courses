
from data import question_data
from question_model import Question
from  quiz_brain import QuizBrain

question_bank = [Question(text=q["text"], answer=q["answer"]) for q in question_data]
quiz = QuizBrain(question_bank)

while quiz.have_next_question():
    result = quiz.get_next_question()
    print(result)

print(f"\nYou complete quiz\nYour score is {quiz.correct_answers}/{quiz.question_number}")