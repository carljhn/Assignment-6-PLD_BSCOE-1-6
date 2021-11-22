#Addition Quiz
# Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer
#The program will ask the user 10 addition operation
#Display the result summary of the 10 operations (ex 9/10)

import random
num1=random.randint(0, 99)
num2=random.randint(0, 99)
ans=int(input(f"Question 1. {num1}+{num2}="))
total=num1+num2
score=0
if ans==total:
    print("correct!")
    score+=1
else:
    print("Incorrect, the right answer is", total)

num1=random.randint(0, 99)
num2=random.randint(0, 99)
ans=int(input(f"Question 2. {num1}+{num2}="))
total=num1+num2
score+=0
if ans==total:
    print("Correct!")
    score+=1
else:
    print("Incorrect, the right answer is", total)

num1=random.randint(0, 99)
num2=random.randint(0, 99)
ans=int(input(f"Question 3. {num1}+{num2}="))
total=num1+num2
score+=0
if ans==total:
    print("Correct!")
    score+=1
else:
    print("Incorrect, the right answer is", total)

num1=random.randint(0, 99)
num2=random.randint(0, 99)
ans=int(input(f"Question 4. {num1}+{num2}="))
total=num1+num2
score+=0
if ans==total:
    print("Correct!")
    score+=1
else:
    print("Incorrect, the right answer is", total)

num1=random.randint(0, 99)
num2=random.randint(0, 99)
ans=int(input(f"Question 5. {num1}+{num2}="))
total=num1+num2
score+=0
if ans==total:
    print("Correct!")
    score+=1
else:
    print("Incorrect, the right answer is", total)

num1=random.randint(0, 99)
num2=random.randint(0, 99)
ans=int(input(f"Question 6. {num1}+{num2}="))
total=num1+num2
score+=0
if ans==total:
    print("Correct!")
    score+=1
else:
    print("Incorrect, the right answer is", total)

num1=random.randint(0, 99)
num2=random.randint(0, 99)
ans=int(input(f"Question 7. {num1}+{num2}="))
total=num1+num2
score+=0
if ans==total:
    print("Correct!")
    score+=1
else:
    print("Incorrect, the right answer is", total)

num1=random.randint(0, 99)
num2=random.randint(0, 99)
ans=int(input(f"Question 8. {num1}+{num2}="))
total=num1+num2
score+=0
if ans==total:
    print("Correct!")
    score+=1
else:
    print("Incorrect, the right answer is", total)