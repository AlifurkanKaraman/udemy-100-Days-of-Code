question_data = [
    {"category": "Science: Computers",
     "type": "boolean",
     "difficulty": "easy",
     "question": "Linus Torvalds created Linux and Git.",
     "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The programming language &quot;Python&quot; is based off a modified version of &quot;JavaScript&quot;.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The logo for Snapchat is a Bell.", "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Ada Lovelace is often considered the first computer programmer.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
                                       "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
                                       "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "In most programming languages, the operator ++ is equivalent to the statement &quot;+= 1&quot;.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Time on Computers is measured via the EPOX System.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
                                      "question": "The Windows 7 operating system has six main editions.",
                                      "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The Windows ME operating system was released in the year 2000.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
                                       "question": "Linux was first created as an alternative to Windows XP.",
                                       "correct_answer": "False", "incorrect_answers": ["True"]}
]

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

class QuizBrain:

    def __init__(self, q_list):
        self.questions_list = q_list
        self.question_number = 0
        self.score = 0

    # True if we have questions, False otherwise.
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")