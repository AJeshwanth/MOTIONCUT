import time
answer_count=0
class Comp_Quiz:
    # playquiz is a method which takes questions and options as well as correct option as parameters
    # Displaying question 
    def playquiz(question, A, B, C, D, ans):
        print(question)
        print(A)
        print(B)
        print(C)
        print(D)
        # Taking Answer Option
        user_ans=input("Enter your Answer Option: ")
        # Displaying wheter the given option is right or wrong
        if user_ans==ans:
            global answer_count
            answer_count+=1
            print("Yeah! Its a Correct Answer")
        else:
            print("Oh! Wrong Answer")
            print("The correct answer is Option: ", ans)
class cust_Quiz:
    # In this class we take questions as input as well as correct option and return this to the custom_quiz method
    def question():
        q=input("Enter your Question: ")
        A=input("Enter option A:")
        B=input("Enter option B:")
        C=input("Enter option C:")
        D=input("Enter option D:")
        ans=input("Enter the Answer Option: ")
        return q, A,B,C,D,ans
    # This playquiz works same as the method in comp_quiz class just for displaing Options names and Question Numbers used in this class
    def playquiz(qno, question, A, B, C, D, ans):
        print(qno,":", question)
        print("A)",A)
        print("B)",B)
        print("C)",C)
        print("D)",D)
        user_ans=input("Enter your Answer Option: ")
        if user_ans==ans:
            global answer_count
            answer_count+=1
            print("Yeah! Its a Correct Answer")
        else:
            print("Oh! Wrong Answer")
            print("The correct answer is Option:", ans)
    
def quiz():
    # this method calls playquiz method in comp_quiz class and passes questions, options and answers
    q1, A1, B1, C1, D1, ans1=["1: What is the capital city of Austrailia?", "A)Sydney", "B)Melbourne", "C)Canberra", "D)Brisbane", "C"]
    q2, A2, B2, C2, D2, ans2=["2: What is the currency of Japan?", "A)Yuan", "B)Yen", "C)Won", "D)Ringgit", "B"]
    q3, A3, B3, C3, D3, ans3=["3: In which year did the Titanic sink?", "A)1910", "B)1925", "C)1912", "D)1930", "C"]
    Comp_Quiz.playquiz(q1, A1, B1, C1, D1, ans1)
    time.sleep(1)
    Comp_Quiz.playquiz(q2, A2, B2, C2, D2, ans2)
    time.sleep(1)
    Comp_Quiz.playquiz(q3, A3, B3, C3, D3, ans3)
    time.sleep(1)
def custom_quiz():
    # this method calls playquiz method in cutom_quiz class if user wants to play and passes the questions, options and answers
    q1,A1,B1,C1,D1, ans1=cust_Quiz.question()
    q2,A2,B2,C2,D2, ans2=cust_Quiz.question()
    q3,A3,B3,C3,D3, ans3=cust_Quiz.question()
    play=input("Want to play your quiz(Y/N)")
    # Takes input as Y/N
    if(play == "Y" or play== "y"):
        cust_Quiz.playquiz(1, q1, A1, B1, C1, D1, ans1)
        time.sleep(1)
        cust_Quiz.playquiz(2, q2, A2, B2, C2, D2, ans2)
        time.sleep(1)
        cust_Quiz.playquiz(3, q3, A3, B3, C3, D3, ans3)
        time.sleep(1)
# Displaying Options
print("1:Play Computer Generated QUIZ!!")
print("2:Custom QUIZ!!")
# Taking input as 1 or 2
select =int(input())
if select == 1:
    quiz()
else:
    custom_quiz()
# Displaying the Number of Correct answers out of 3
print(f"You have Scored: {answer_count}/3")