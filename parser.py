from os.path import abspath
from yaml import load

class RcParser(object):
  def __init__(self):
   with open(abspath('rc.yaml'), 'r') as ymlf:
     self.rc = load(ymlf.read())
  
  def __str__(self):
    return str(self.rc) 

  def get_rc_items(self):
    '''returns a list of a list of items'''
    return self.rc['items']
  
  def get_rc_knapsacks(self):
    '''returns a list of knapsacks'''
    return self.rc['knapsacks']

  def get_n(self):
    '''returns n, the number of items'''
    return self.rc['n']

  def get_m(self):
    '''returns m, the number of knapsacks'''
    return self.rc['m']

