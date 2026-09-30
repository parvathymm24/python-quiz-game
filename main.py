# -----PYTHON QUIZ GAME-----
from questions import question_SET, opt,correct_ans
from utils import seperator_line , see_score
from database import create_database, save_score

create_database()

print("WELCOME TO THE PYTHON QUIZ GAME ! ! !")

player_name=input("ENTER YOUR NAME: ")
total_questions=len(question_SET)

guesses= []
score = 0
total_questions = 0
for x in question_SET:
    seperator_line()
    print(x)
    for y in opt[total_questions]:
        print(y)
    guess=input("ENTER A,B,C OR D : ")
    guesses.append(guess)
    if guess == correct_ans[total_questions]:
        print("CORRECT!")
        score += 1
    else:
        print("INCORRECT! ")
        print(f"{correct_ans[total_questions]}is the correct answer")

    total_questions += 1

seperator_line()
print("                    RESULT OF THE QUIZ               " )
seperator_line()

print("\nANSWERS:", end="")
for answer in correct_ans :
    print(answer, end="")
print()

print("GUESSES:", end="")
for guess in guesses:
    print(guess, end="")
print()    

see_score(score,total_questions)

print("\n--------------THANK YOU FOR ATTENDING THE QUIZ--------------")

save_score(player_name,score,total_questions)
