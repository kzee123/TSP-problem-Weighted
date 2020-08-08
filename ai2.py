import random
from random import randint
from math import floor

given_cities=[
    [0,    66,    21,  300,  500,   26,   77,   69,  125,  650 ],
    [66,    0,    35,  115,   36,   65,   85,   90,   44,  54  ],
    [21,   35,     0,  450,  448,  846,  910,   47,   11,  145 ],
    [300, 115,   450,    0,   65,  478,  432,  214,  356,  251 ],
    [500,  36,   448,   65,    0,  258,  143,  325,  125,  39  ],
    [ 26,  65,   846,  478,  258,    0,  369,  256,  345, 110  ],
    [ 77,  85,   910,  432,  143,  369,    0,   45,  120, 289  ],
    [ 69,  90,    47,  214,  325,  256,   45,    0,  325, 981  ],
    [125,  44,    11,  356,  125,  345,  120,  325,    0, 326  ],
    [650,  54,   145,  251,   39,  110,  289,  981,  326,   0  ],
]

total_population=40
total_cities = len(given_cities)
city = [0,1,2,3,4,5,6,7,8,9]
population , child = [0]*total_population ,[]
shortest_path=[99999*99999,0]


def make_population():
    for i in range(total_population):
        population[i]= random.sample( deepcopy(city), len(given_cities) )


fitness_values = [0]*total_population 

total_fitness = 0


def find_total_fitness(pp,fitness):
    global total_fitness,shortest_path
    count=0
    for i in pp:
        tmp= find_distance(i)
        if tmp<shortest_path[0]:
            shortest_path[0]=tmp
            shortest_path[1]=[x+1 for x in i ]        
        fitness[count]=450/float(tmp)
        total_fitness+=tmp
        count+=1
    total_fitness=450/float(total_fitness)



def crossover(list1, list2):
    r =random.randrange(0,total_cities-1)
    c1 = []
    c2 = []

    x = 0
    while x < r:
        c1[x] = list1[x]
        x+=1
    while x < len(list1):
        c1[x] = list2[x]
        x+=1

    child.append(c1)
    child.append(c2)
