# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 10:41:04 2018

@author: aniyo
"""
import random
import numpy as np

def show_problem(a1,b1,c1,a2,b2,c2):
    '''
    Prints a linear equation in the form
    a1x+b1y=c1
    a2x+b2y=c2
    '''
    print(str(a1)+'x + '+str(b1)+'y = '+str(c1) + '\n'+ str(a2)+'x + '+str(b2)+'y = '+str(c2))
    
def interpret_solution(solution):
    '''
    Checks if the users input for x and y are correct
    '''
    print('Solve the system of linear equations')    
    while True:
        response1 = input('What is x? ')
        response2 = input('What is y? ')
        try:
            x = float(response1)
            y = float(response2)
            if abs(x-solution[0]) < 10**-2 and abs(y-solution[1]) <10**-2:
                print('Correct'+'\n')
                return 1
                break
            else:
                print('\n'+'Either x or y is incorrect')
                print('The correct answer is'+'\n')
                print('x = '+str(solution[0]) + '\n'+ 'y = ' + str(solution[1])+str('\n'))
                return 0
                break
        except ValueError:
            print('Please enter your answer as an integer or decimal')
                
        

def random_math():
    '''
    Produces 2 linear equations in the form a1x+b1y=c1 nd a2x+b2y=c2 and 
    returns the a1,a2,b1,b2,c1,c2 and the solution of the linear equation 
    '''
    variables = list(range(0,20))
    coefficients = random.sample(variables,6)
    a1 = coefficients[0]
    b1 = coefficients[1]
    c1 = coefficients[2]
    a2 = coefficients[3]
    b2 = coefficients[4]
    c2 = coefficients[5]
    A = np.array([[a1,b1],[a2,b2]])
    B = np.array([c1,c2])
    solution = np.linalg.solve(A,B)
    return a1,b1,c1,a2,b2,c2,solution
    
def generate_math_problems(problems):
    '''
    Generates a number of linear algebra problems. 
    The user must answer at 70% of those problems correctly
    '''
    correct_answers = 0
    attempted_problems = 0
    while attempted_problems < problems:
        a1,b1,c1,a2,b2,c2,solution = random_math() 
        show_problem(a1,b1,c1,a2,b2,c2)
        response = interpret_solution(solution)
        if response == 1:
            correct_answers += 1
            attempted_problems += 1
        else:
            attempted_problems += 1
    score = 100* correct_answers/attempted_problems
    if score < 70:
        print('Your score is '+str(score)+'\n')
        print('Please attempt this again to obtain a score of at least 70'+'\n**************************\n')
        generate_math_problems(problems)
    else:
        print('Your score is '+str(score))
        response3 = input('Would you like to attempt another ' +str(problems)+' problems?'+'\n'+'Yes or No: ')
        if response3 == 'No' or response3 == 'no' or response3 == 'Yes' or response3 == 'yes':
            if response3 == 'No' or response3 == 'no': 
                print('Thank you for practicing')
            if response3 == 'Yes' or response3 == 'yes':
                generate_math_problems()
        else:
            print('Please responde with Yes or No')

while True:
    problems = input('Number of problems you want to attempt:')
    try:
        problems = int(problems)
        break
    except ValueError:
        print('Please enter an integer')
generate_math_problems(problems)     

    