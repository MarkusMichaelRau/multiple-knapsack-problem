

class FitnessFunction(object):

  def __init__(self, chromosome, knapsack_items_map):
    self.chromosome = chromosome
    self.knapsack_items_map = knapsack_items_map

  def sum_item_attribute(self, m, attribute):
    '''returns the sum of specified attribute of items in knapsacks m'''
    return sum([item.profit if attribute == 'profit' else item.weight for item in self.knapsack_items_map[m]])



