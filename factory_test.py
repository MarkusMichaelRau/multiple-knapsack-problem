import unittest
from factory import ChromosomeFactory, PopulationFactory
from chromosome import Chromosome
from population import Population

class ChromosomeFactoryTest(unittest.TestCase):

  def test_gen(self):
    n = 15 
    m = 3
    factory = ChromosomeFactory(n, m)
    c = factory.gen()
    expected_len = 30
    self.assertEqual(len(c), expected_len)
    self.assertEqual(type(c), Chromosome)

class PopulationFactoryTest(unittest.TestCase):

  def test_gen(self):
    n = 12
    m = 3
    p = 10

    factory = PopulationFactory(p, n, m)
    population = factory.gen()
    self.assertEqual(len(population), p)
    self.assertEqual(type(population), Population)

