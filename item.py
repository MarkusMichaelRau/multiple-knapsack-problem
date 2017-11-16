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

  def get_all_on_items(self, chromosome, m):
    '''returns on items with their associated knapsacks as dict of lists'''
    all_on_items = {}
    on_items = []
    for knapsack in range(1, m + 1):
       for gene in range(1, len(chromosome), 2):
         if chromosome[gene] == str(knapsack):
           index = 0 if gene == 1 else ((gene - 1) / 2)
           on_items.append(self.items[int(index)])
       all_on_items[knapsack] = on_items
       on_items = []
    return all_on_items

