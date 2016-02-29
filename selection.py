from random import uniform
from fitness import FitnessFunction
from parser import RcParser
from knapsack import KnapsackList
from parser import KnapsackParser, ItemParser
from item import ItemList


class RouletteSelection(object):

  def __init__(self, population):
    self.population = population

  def do_selection(self):
    '''performs roulette selection'''
    fsum = 0
    pop_fsum = []
    for i in range(len(self.population)):
      rc = RcParser()
      fitness_function = FitnessFunction(self.population[i], ItemList(ItemParser(rc.get_rc_items()).items).get_all_on_items(self.population[i].solution, RcParser().get_m()))
      fitness = fitness_function.sum_all_fitness()
      fsum = fsum + fitness 
      pop_fsum.append(fitness)
    
    bound = uniform(0, fsum)
    curr_fsum = 0
    for i in range(len(self.population)):
      curr_fsum = curr_fsum + pop_fsum[i]
      if curr_fsum >= bound:
        return self.population[i]
    
