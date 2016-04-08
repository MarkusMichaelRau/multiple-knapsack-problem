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

