"""Quiz game application."""
class QuizGame:
    "Quiz game class"
    def __init__(self):
        """Game initialize"""
        self.score = 0
        self.correct_question_count = 0
        self.incorrect_question_count = 0
        self.current_question = None
        self.display_questions = []
        self.questions = [{
            "question" : "What is your Favourite programming language?",
            "answer" : "python"
        },
        {
            "question" : "Do you follow any author on AskPython?",
            "answer" : "yes"
        },{
            "question" : "What is the name of your favourite website for learning Python?",
            "answer" : "askpython"
        }]

    def start_game(self):
        """Start the quiz game."""
        self.next_question()

    def next_question(self):
        """Generate and display the next question."""
        try:
            #print(self.display_questions)
            if len(self.display_questions) == len(self.questions):
                self.end_game()
                return

            index = len(self.display_questions)
            self.current_question = index
            self.display_questions.append(index)
            question = self.questions[index]["question"]
            ans = input(f"Question {index + 1}:{question}")
            user_answer = ans.strip()
            if user_answer:
                self.check_answer(user_answer)
            else:
                print("Please type you answer")
                again_ans = input()
                user_again_answer = again_ans.strip()
                self.check_answer(user_again_answer)
        except (IndexError, KeyError) as e:
            print(e)


    def check_answer(self, ans):
        """Check whether the user's answer is correct."""
        correct_ans = self.questions[self.current_question]["answer"]
        if ans.lower() == correct_ans:
            print("correct")
            self.score += 100 / len(self.questions)
            self.correct_question_count += 1
            self.next_question()
        else:
            print("Incorrect")
            self.incorrect_question_count += 1
            self.next_question()

    def end_game(self):
        """End the game and display the final results."""
        print("Thankyou for Playing this small quiz game")
        print(f"You attempted {self.correct_question_count} questions correctly!")
        if self.incorrect_question_count > 0:
            print(f"and {self.incorrect_question_count} incorrectly!")
        print(f"Marks obtained: {round(self.score, 2)}")

def main():
    """Run the application."""
    print("Welcome to AskPython Quiz")
    ch = input("Are you ready to play the Quiz ? (yes/no) :")
    if ch.lower() == "yes":
        game = QuizGame()
        game.start_game()
    else:
        print("Okay, you can try sometime.")

if __name__ == "__main__":
    main()
