import random
import math
import sys

def importData(name):
    global NUMOFPROCESSORS, NUMOFTASKS, TASKS
    with open("data/"+name) as file:
        NUMOFPROCESSORS = int(file.readline())
        NUMOFTASKS = int(file.readline())
        TASKS = [int(x) for x in file.read().splitlines()]

def rating(individual):
    processors = [0] * NUMOFPROCESSORS
    for i in range(len(individual)):
        processors[individual[i] - 1] += TASKS[i]

    return max(processors)

def pConversion(p):
    new = []
    for i in range(len(p)):
        new.append([i+1])

    for i in range(len(p)):
        new[i].append(p[i])

    return new

def breed(chromosome1, chromosome2):
    length = len(chromosome1)
    pivot = random.randint(1, length-2)
    return chromosome1[0:pivot]+chromosome2[pivot::], chromosome2[0:pivot]+chromosome1[pivot::]

def mutation(individual):
    length = len(individual)
    pivot = random.randint(0, length - 1)
    randomChange = random.randint(1, NUMOFPROCESSORS)
    while individual[pivot] == randomChange:
        randomChange = random.randint(1, NUMOFPROCESSORS)
    individual[pivot] = randomChange

    return individual

def insert(element, list, index):
    global processesOrder
    list.append(element)
    i = len(list)-1

    processesOrder = processesOrder[1:] + processesOrder[:1]

    while i > 0 and list[i - 1] > list[i]:
        list[i], list[i - 1] = list[i - 1], list[i]
        processesOrder[i], processesOrder[i - 1] = processesOrder[i - 1], processesOrder[i]
        i -= 1

    chromosome[index-1] = processesOrder[i]
    return list

def greedyAlgorithm(m, n, p):
    global chromosome, processesOrder
    chromosome = [0] * n
    processesOrder = []
    for i in range(m):
        processesOrder.append(i+1)

    processes = [0] * m

    for i in range(n):
        element = processes[0]+p[i][1]
        index = p[i][0]
        processes = insert(element, processes[1:], index)

def firstGeneration(p, numOfIndividualsPerGen):
    population = []

    for i in range(numOfIndividualsPerGen):
        random.shuffle(p)
        greedyAlgorithm(NUMOFPROCESSORS, NUMOFTASKS, p)
        population.append(chromosome)
    return population

def selection(population, numOfGenerations):
    i = 0
    first = 0
    number = 0

    while i < numOfGenerations:
        print(f"Run {i}:", end=" ")
        number = len(population)

        # Calculate fitness 
        ratings = []
        for j in range(number):
            ratings.append([rating(population[j]), population[j]])
        ratings = sorted(ratings, key=lambda x: x[0])
        print(ratings[0][0])

        # Remember first score
        if i == 0:
            first = ratings[0][0]

        # Create new population
        population = []

        percentage = math.ceil(number * 0.9)
        # Wybór najlepszych do przeniesienia do nowego pokolenia, aby liczba osobników się nie zmieniła
        left = number - percentage
        for j in range(left):
            population.append(ratings[j][1])

        # Choose the best 80% of opulation for crossings
        for j in range(0, percentage, 2):
            newIndividual1, newIndividual2 = breed(ratings[j][1], ratings[j + 1][1])
            population = population + [newIndividual1, newIndividual2]
        ratings = ratings[percentage:]

        # Mutate random 40% of generation
        if i / numOfGenerations in [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
            percentage = math.ceil(0.9 * number)
        else:
            percentage = math.ceil(0.8 * number)

        for j in range(percentage):
            randomNumber = random.randint(math.ceil(number * 0.1), number - 1)
            population[randomNumber] = mutation(population[randomNumber])
        
        i += 1

    ratings = []
    for j in range(number):
        ratings.append([rating(population[j]), population[j]])
    ratings = sorted(ratings, key=lambda x: x[0])
    print(f"\n\nFirst best result:{first}")
    print(f"\n\nLast best result:{ratings[0][0]}")
    print(f"\n\nImprovement:{round(((first - ratings[0][0])/first) * 100, 2)}")

if __name__ == "__main__":
    print("Podaj nazwe pliku do pobrania")
    name = input()
    importData(name)

    pConverted = pConversion(TASKS)

    numOfIndividualsPerGen = 4000
    numOfGenerations = int(round(1000_000 / NUMOFTASKS, (-1 * len(str(int(1000_000 / NUMOFTASKS)))) + 1)) * (1000 / numOfIndividualsPerGen)

    populationZero = firstGeneration(pConverted, numOfIndividualsPerGen)
    selection(populationZero, numOfGenerations)

