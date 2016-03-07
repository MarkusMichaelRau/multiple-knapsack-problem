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
  
 
  
