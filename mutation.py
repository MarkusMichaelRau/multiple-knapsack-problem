from random import choice
from parser import RcParser
from chromosome import Chromosome
from random import randint

class Mutation(object):

  def __init__(self, chromosome, probability):
    self.chromosome = chromosome
    self.probabilty = probability
   
  def exe(self):
    for i in range(0, len(self.chromosome), 2):
      if choice(range(1, self.probabilty + 1)) == 1:
        if self.chromosome[i] == '1':
          return Chromosome(self.chromosome[:i] + '00' + self.chromosome[i + 2:])
        elif self.chromosome[i] == '0':
           return Chromosome(self.chromosome[:i] + '1' + str(randint(1, RcParser().get_m())) + self.chromosome[i + 2:]) 
    return self.chromosome

  
