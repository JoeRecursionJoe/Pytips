class Pencil:
  def __init__(self, count):
    self._counter=count
  
  @property
  def counter(self):
    return self._counter
  
  @counter.setter
  def counter(self, count):
    self._counter = count

  @counter.getter
  def counter(self):
    return self._counter
  

HB = Pencil(100)
print (HB.counter)
HB.counter = 20
print (HB.counter)



# Output
# 100
# 20


# -----------------------------
class Accolade:
  def __init__(self, function):
    self.function = function
    
  
  def __call__ (self, name):
    # Adding Excellency before name
    name = "Excellency " + name
    self.function(name)
    # Saluting after the name
    print("Thanks " + name + " for gracing the occasion")

@Accolade
def simple_function(name):
  print (name)

simple_function('John McKinsey')

# Output
# Excellency John McKinsey
# Thanks Excellency John McKinsey for gracing the occasion

