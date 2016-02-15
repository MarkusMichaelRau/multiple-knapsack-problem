from chromosome import Chromosome
from random import randint
from population import Population

class ChromosomeFactory(object):

  def __init__(self, n, m):
    self.n = n #number of items
    self.m = m #number of knapsacks
    self.item_vals = ['1', '0']
    self.knapsack_vals = [str(knapsack) for knapsack in range(0, m + 1)]

