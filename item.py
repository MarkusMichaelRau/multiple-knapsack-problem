class Item(object):

  def __init__(self, index, profit, weight):
    self.index = index
    self.profit = profit
    self.weight = weight

    def __str__(self):
    return 'i = {0}, p = {1}, w = {2}'.format(self.index, self.profit, self.weight)
