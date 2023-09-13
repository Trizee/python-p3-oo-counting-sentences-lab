#!/usr/bin/env python3

class MyString:
  
  def __init__(self,value = ''):
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self,value):
    if isinstance(value, str):
      self._value = value
    else:
      print('The value must be a string.')

  def is_sentence(self):
    if self.value.endswith('.'):
      return True
    else:
      return False

  def is_question(self):
    if self.value.endswith('?'):
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self.value.endswith('!'):
      return True
    else: 
      return False

  def count_sentences(self):
    # value = self.value
    # for punc in ['!', '?']:
    #   value = value.replace(punc, '.')
    # sentences = [self.value.split()]
    x = 0

    for sen in self.value.split():
      if sen.endswith('.'):
        x = x + 1
      elif sen.endswith('!'):
        x = x + 1
      elif sen.endswith('?'):
        x = x + 1

    return x


q = MyString('This, well, is a sentence. This is too!! And so is this, I think? Woo...')
q.count_sentences()