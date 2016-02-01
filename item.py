class Item(object):

  def __init__(self, index, profit, weight):
    self.index = index
    self.profit = profit
    self.weight = weight

    def __str__(self):
    return 'i = {0}, p = {1}, w = {2}'.format(self.index, self.profit, self.weight)

class ItemList(object):

  def __init__(self, items):
    self.items = items

  def __str__(self):
    return '\n'.join([str(item) for item in self.items])

  def __len__(self):
    return len(self.items)

  def __getitem__(self, key):
    '''given a key returns the associated item'''
    return self.items[key]

