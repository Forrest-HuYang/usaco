#function = -x**2 + 2*x - 1
# x = [0，3]
import random
import easygui
import math

def representation(interval,precision,no_selected):
    original_list = []
    largest = int(interval*(10**precision))
    select_interval = int(largest//no_selected)
    for i in range(1,largest + 1):
        str_temp = ''
        if i % select_interval == 0:
            m = bin(i).split('b')[1]
            original_list.append(m)
        
    return original_list 


def select(list_num,no_selected,lower_bound):
    score = []
    total = 0
    dice = []
    index = []
    final_choice = []
    xval = []
    for i in range(no_selected):
        x = int(list_num[i],2)/1000000 + lower_bound
        xscore = get_x(x)
        xval.append(x)
        score.append(xscore)
        total += xscore
    print(max(score))
    print(max(xval))
    if min(score) < 0:
        minimum = min(score)
        for j in range(no_selected):
            score[j] -= minimum
        total -= minimum * no_selected
    score[0] = score[0]/total

    for k in range(1,no_selected):
        score[k] = score[k-1] + score[k]/total
    
    score.insert(0,0)

    for l in range(no_selected):
        dice.append(random.random())

    for m in range(no_selected):
        index.append(get_nos(no_selected,score,dice[m]))

    for n in range(no_selected):
        final_choice.append(list_num[index[n]])
    
    return final_choice

    
def get_nos(no_selected,score,dice_no):
    for m in range(no_selected):
        if score[m] <= dice_no < score[m+1]:
            return m

        
def crossover(choices,percentage_cross,no_selected):
    for i in range(0,no_selected,2):
        new = cross_individual(choices[i],choices[i+1],percentage_cross)
        choices[i],choices[i+1] = new[0],new[1]
    return choices


def cross_individual(crossA,crossB,percentage_cross):
    length = min(len(crossA),len(crossB))
    length = round(length * percentage_cross,0)
    a = len(crossA)
    b = len(crossB)
    m = int(a-length)
    n = int(b-length)
    atemp = crossA[m:a]
    btemp = crossB[n:b]
    crossA = crossA[0:m]
    crossB = crossA[0:n]
    crossA += btemp
    crossB += atemp
    return [crossA,crossB]


def mutate(choices,percentage_mutate,no_selected):
    list_nos = []
    no_mutate = int(round(no_selected * percentage_mutate,0))
    for i in range(no_mutate):
        place = random.randint(0,no_selected-1)
        while place in list_nos:
            place = random.randint(0,no_selected-1)
        list_nos.append(place)


    for i in range(no_mutate):
        choices[i] = mutate_individual(choices[i])

    return choices


def mutate_individual(original):
    position_mutate = []
    place = random.randint(0,len(original)-1)
    while place in position_mutate:
        place = random.randint(0,len(original)-1)
    position_mutate.append(place)
    if original[place] == '1':
        original = original[0:place] + '0' + original[place+1:len(original)]
    else:
        original = original[0:place] + '1' + original[place+1:len(original)]

    return original

    
def main(no_selected,percentage_cross,percentage_mutate,precision,no_repetition,lower_bound,upper_bound,interval):
    list_no = representation(interval,precision,no_selected)
    for i in range(no_repetition):
        list_no = run(no_selected,percentage_cross,percentage_mutate,precision,no_repetition,interval,list_no,lower_bound)

    fals = []
    m = 0
    for j in range(no_selected):
        x = int(list_no[j],2)/1000000
        fals.append(x)
        m += x


def run(no_selected,percentage_cross,percentage_mutate,precision,no_repetition,interval,list_no,lower_bound):
    m = select(list_no,no_selected,lower_bound)
    n = crossover(m,percentage_cross,no_selected)
    o = mutate(n,percentage_mutate,no_selected)
    return o

def imput():
    easygui.msgbox('We are going to use the genetic algorithm to help you determine the greatest or smallest possible value of a function in a given range.',title = 'Genetic Algorithm',ok_button='Continue')
    easygui.msgbox('You can select the kinds of functions that you want to calculate and the various parameters that would be put into the algotithm.',title = 'Genetic Algorithm',ok_button='Continue')
    function_choice = easygui.choicebox(msg= 'Which kind of function do you want to do?',title='Genetic Algorithm',choices = ['Linear Function','Quadratic Function','Sinusoid Function'])
    if function_choice == 'Linear Function':
        return linear_init()
        
    elif function_choice == 'Quadratic Function':
        return quadratic_init()

    elif function_choice == 'Sinusoid Function':
        return sinusoid_init()

def linear_init():
    a = int(easygui.enterbox(msg= 'What is the value of a in the function f(x)=ax+b? ',title='Genetic Algorithm -- Linear'))
    b = int(easygui.enterbox(msg= 'What is the value of b in the function f(x)=ax+b? ',title='Genetic Algorithm -- Linear'))
    return ['linear',a,b]

def quadratic_init():
    a = int(easygui.enterbox(msg= 'What is the value of a in the function f(x)=ax^2+bx+c? ',title='Genetic Algorithm -- Quadratic'))
    b = int(easygui.enterbox(msg= 'What is the value of b in the function f(x)=ax^2+bx+c? ',title='Genetic Algorithm -- Quadratic'))
    c = int(easygui.enterbox(msg= 'What is the value of c in the function f(x)=ax^2+bx+c? ',title='Genetic Algorithm -- Quadratic'))
    return ['quadratic',a,b,c]

def sinusoid_init():
    a = int(easygui.enterbox(msg= 'What is the value of a in the function f(x)=asin(bx+c)? ',title='Genetic Algorithm -- Sinusoid'))
    b = int(easygui.enterbox(msg= 'What is the value of b in the function f(x)=asin(bx+c)? ',title='Genetic Algorithm -- Sinusoid'))
    c = int(easygui.enterbox(msg= 'What is the value of c in the function f(x)=asin(bx+c)? ',title='Genetic Algorithm -- Sinusoid'))
    return ['sinusoid',a,b,c]

m = imput()

def get_x(x):
    ftype = m[0]
    if ftype == 'linear':
        return m[1]*x + m[2]
    elif ftype == 'quadratic':
        return m[1]*(x**2) + m[2]*x + m[3]
    else:
        return m[1]*math.sin(m[2]*x + m[3]) 

def parameters():
    a = int(easygui.enterbox(msg= 'What is the number of individuals you wish to select? ',title='Genetic Algorithm -- Parameters'))
    b = float(easygui.enterbox(msg= 'What is the crossover rate you wish to have? ',title='Genetic Algorithm -- Parameters'))
    c = float(easygui.enterbox(msg= 'What is the mutation rate you wish to have? ',title='Genetic Algorithm -- Parameters'))
    d = int(easygui.enterbox(msg= 'What is the degree of precision you wish to have(digits after the decimal place)? ',title='Genetic Algorithm -- Parameters'))
    e = int(easygui.enterbox(msg= 'What is number of generations you wish to run? ',title='Genetic Algorithm -- Parameters'))
    f = float(easygui.enterbox(msg= 'What is the lower boundary of your function? ',title='Genetic Algorithm -- Parameters'))
    g = float(easygui.enterbox(msg= 'What is the upper boundary of your function? ',title='Genetic Algorithm -- Parameters'))
    h = g-f
    main(a,b,c,d,e,f,g,h)
    

parameters()