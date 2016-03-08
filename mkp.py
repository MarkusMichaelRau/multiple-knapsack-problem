if __name__ == '__main__':
  from parser import RcParser, ItemParser, KnapsackParser
  from chromosome import Chromosome
  from factory import ChromosomeFactory, PopulationFactory
  from crossover import OnePoint
  from item import ItemList
  from knapsack import KnapsackList
  from fitness import FitnessFunction
  from selection import RouletteSelection
  from population import Population
  from random import choice
  from mutation import Mutation

  rc = RcParser()
  items = ItemList(ItemParser(rc.get_rc_items()).items)
  knapsacks = KnapsackList(KnapsackParser(rc.get_rc_knapsacks()).knapsacks)
  n = rc.get_n()
  m = rc.get_m()
  a = Chromosome('000013120000001300000011')
  b = ChromosomeFactory(n, m).gen()
  print('p1 = ' + str(a))
  print('p2 = ' + str(b))
  print('number of knapsacks = {0}'.format(m))
  print('number of items = {0}'.format(n))
  
  p = 10
  print('population size = ' + str(p))
  population = PopulationFactory(p, n, m).gen()
  iterations = 100
  fittest_chromosome = None
  fittest_chromosomes = []
  for _ in range(iterations):
    pop_fsum = 0
    #calc population sum
    for i in range(p):
      fitness_function = FitnessFunction(population[i], items.get_all_on_items(population[i].solution, m))
      pop_fsum = pop_fsum + fitness_function.sum_all_fitness()
      population[i] = fitness_function.chromosome

    parents = []
    for i in range(2):#select 2 chromosomes for crossover
      parent = RouletteSelection(population).do_selection()
      parents.append(parent)

    point = choice(range(0, len(parents[0]), 2))

    children = OnePoint().exe(parents[0], parents[1], point)

    probability = 100
    mutated_children = []
    for i in range(2):
      mutated_children.append(Mutation(children[i], probability).exe())      #mutate offspring

    i = 0
    for chromosome in population: #replace current population with new one
      if str(chromosome) == str(parents[0]):
        population[i] = mutated_children[0]
        i = i + 1
      elif str(chromosome) == str(parents[1]):
        population[i] = mutated_children[1]
        i = i + 1
      else:
        i = i + 1

    #get list of fitness for each individual
    fsums = []
    for i in range(p):
      fitness_function = FitnessFunction(population[i], items.get_all_on_items(population[i].solution, m))
      fsums.append(fitness_function.sum_all_fitness())
      population[i] = fitness_function.chromosome

    #get fittest individual of current population
    #print('fsums = ' + str(fsums))
    max_fsum = max(fsums)
    #print('this max fsum ' + str(max_fsum)) 
    for i in range(p):
      if float(fsums[i]) == float(max_fsum):
        fittest_chromosome = population[i]

    fittest_chromosomes.append(fittest_chromosome)
    print('fittest solution from this population ' + str(fittest_chromosome) + ' where fsum = ' + str(max_fsum))
    print('population fsum = ' + str(pop_fsum))
    print(population)

  fittest_fsums = []
  for i in range(n):
    fitness_function = FitnessFunction(fittest_chromosomes[i], items.get_all_on_items(fittest_chromosomes[i].solution, m))
    fittest_fsums.append(fitness_function.sum_all_fitness())
    if i < p:
      population[i] = fitness_function.chromosome

  print('fittest fsums = ' + str(fittest_fsums))

  fittest_max_fsum = max(fittest_fsums)
  for i in range(n):
    if float(fittest_fsums[i]) == float(fittest_max_fsum):
      final_chromosome = fittest_chromosomes[i]

  print('fittest solutions from all populations \n \n' + str(Population(fittest_chromosomes)))
  #f_max_fsum = fitness_function.sum_all_fitness()
  #final_chromosome = fitness_function.chromosome
  print('final fittest solution = ' + str(final_chromosome) + ', where fsum = ' + str(fittest_max_fsum))
  
