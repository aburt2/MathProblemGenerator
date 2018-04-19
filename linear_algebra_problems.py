# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 10:41:04 2018

@author: aniyo
"""
import random
import numpy as np
import sympy
from sympy.solvers import solve
from sympy import Symbol

def show_problem(a1,b1,c1,a2,b2,c2,type):
    '''
    If type = 1 then prints a system of linear equations in the form
    a1x+b1y=c1
    a2x+b2y=c2

    If type = 2 then prints an equation in the form of
    (a1/a2)x + (b1/b2) = (c1/c2)

    If type = 3 then prints an equation in the form of
    (a1/a2)x + (b1/b2) = (c1/c2)x
    '''
    if type == '1':
        print('\nSolve the system of linear equations\n') 
        print(str(a1)+'x + '+str(b1)+'y = '+str(c1) + '\n'+ str(a2)+'x + '+str(b2)+'y = '+str(c2))
    elif  type == '2':
        print('\nSolve the algebraic equation\n') 
        print('('+str(a1)+'/'+str(a2)+')'+'x' + ' + ' + str(b1)+'/'+str(b2) + ' = ' + str(c1) + '/' + str(c2))
    elif type == '3':
        print('\nSolve the algebraic equation\n') 
        print('('+str(a1)+'/'+str(a2)+')'+'x' + ' + ' + str(b1)+'/'+str(b2) + ' = ' + '('+str(c1) + '/' + str(c2)+')'+'x')
    else:
        print('Incorrect Type please input either 1,2 or 3')
        type = input('Type of problem:')
        show_problem(a1,b1,c1,a2,b2,c2,type)

    
def interpret_solution(solution,type):
    '''
    Checks if the users answer is correct
    '''   
    if type == '1':
        while True:
            response1 = input('\nWhat is x? ')
            response2 = input('What is y? ')
            if len(solution) == 0:
                if response1 == 'no solution' or response1 == 'No solution' or response1 == 'No Solution' or response2 == 'no solution' or response2 == 'No solution' or response2 == 'No Solution':
                    print('\nCorrect')
                    return 1
                    break
                else:
                    print('\nThere is no solution to the system of linear equations.')
                    return 0
                    break
            else:
                try:
                    x = float(response1)
                    y = float(response2)
                    if abs(x-solution[0]) < abs(0.05*solution[0]) and abs(y-solution[1]) < abs(0.05*solution[1]):
                        print('\nCorrect'+'\n')
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
    elif type == '2' or type == '3':
            while True:
                response1 = input('\nWhat is x? ')
                if len(solution) == 0:
                    if response1 == 'no solution' or response1 == 'No solution' or response1 == 'No Solution':
                        print('\nCorrect')
                        return 1
                        break
                    else:
                        print('\nThere is no solution to this algebraic expression')
                        return 0
                        break
                else:
                    try:
                        x = float(response1)
                        if abs(x-solution[0]) < abs(0.05*solution[0]):
                            print('\nCorrect\n')
                            return 1
                            break
                        else:
                            print('\n'+'x is incorrect')
                            print('The correct answer is'+'\n')
                            print('x = '+str(solution[0]) + '\n')
                            return 0
                            break
                    except ValueError:
                        print('Please enter your answer as an integer or decimal')
    else:
        print('Invalid type entered. Please enter 1,2 or 3 for type of problem')
        type = input('Type of problem: ')
        interpret_solution(solution, type)
        
def random_math(type):
    '''
    Produces and solves multiple type of algebra problems
    If type = 1
        Produces 2 linear equations in the form a1x+b1y=c1 and a2x+b2y=c2 and 
        returns the a1,a2,b1,b2,c1,c2 and the solution of the linear equation 
    If type = 2
        Produces an equation in the form (a1/a2)x + (b1/b2) = (c1/c2) and solves for x, returns a1,b1,c1,a2,b2,c2 and the solution
    If type = 3
        Produces an equation in the form (a1/a2)x + (b1/b2) = (c1/c2)x and solves for x, returns a1,b1,c1,a2,b2,c2 and the solution
    '''
    variables = list(range(1,20))
    coefficients = random.sample(variables,6)
    a1 = coefficients[0]
    b1 = coefficients[1]
    c1 = coefficients[2]
    a2 = coefficients[3]
    b2 = coefficients[4]
    c2 = coefficients[5]
    if type == '1':
        A = np.array([[a1,b1],[a2,b2]])
        B = np.array([c1,c2])
        solution = np.linalg.solve(A,B)
    elif type == '2':
        x = Symbol('x')
        a = a1/a2
        b = b1/b2
        c = c1/c2
        solution = solve(a*x +b -c,x)
    elif type == '3':
        x = Symbol('x')
        a = a1/a2
        b = b1/b2
        c = c1/c2
        solution = solve(a*x +b -c*x,x)
    else:
        print('Invalid type please input 1 2 or 3')
        type = input('Type of problem: ')
        random_math(type)
    return a1,b1,c1,a2,b2,c2,solution
def generate_math_problems(problems,type):
    '''
    Generates a number of linear algebra problems. 
    The user must answer at 70% of those problems correctly
    '''
    correct_answers = 0
    attempted_problems = 0
    while attempted_problems < problems:
        a1,b1,c1,a2,b2,c2,solution = random_math(type) 
        show_problem(a1,b1,c1,a2,b2,c2,type)
        response = interpret_solution(solution,type)
        if response == 1:
            correct_answers += 1
            attempted_problems += 1
        else:
            attempted_problems += 1
    score = 100* correct_answers/attempted_problems
    if score < 70:
        print('Your score is '+str(score)+'%\n')
        print('Please attempt this again to obtain a score of at least 70'+'\n**************************\n')
        generate_math_problems(problems,type)
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

def getinput():
    while True:
        problems = input('Number of problems you want to attempt(max 20):')
        try:
            problems = int(problems)
            if problems <= 0:
                print('There must be more than 0 problems')
            elif problems > 20:
                print('There can only be at most 20 problems')
            else:
                break
        except ValueError:
            print('Please enter an integer')
    print('''There are three types of problems that can be attempted \n 
        1) System of Linear equations in the form a1x+b1y=c1 and a2x+b2y=c2 \n 
        2) Algebraic Equation in the form (a1/a2)x + (b1/b2) = (c1/c2) \n
        3) Algebraic Equation in the form (a1/a2)x + (b1/b2) = (c1/c2)x''')
    while True:
        type = input('\nEnter the type of problem you want to attempt(1,2 or 3): ')
        if type == '1' or type == '2' or type == '3':
            return problems,type
            break
        else:
            print('Please enter 1,2 or 3 for the type')

[problems,types] = getinput()
generate_math_problems(problems,types)     

    