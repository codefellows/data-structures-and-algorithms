from code_challenges.stacks_and_queues.stacks_and_queues import Queue 

class Animal:
  """creates instance of animal with "name" and "species" properties
     used for verifying functionality of AnimalShelter subclass of Queue.
  """
  def __init__(self, name:str, species:str)-> object:
    self.name = name
    self.species = species


class AnimalShelter(Queue):
  """Creates an Instance of AnimalShelter as a sub-class of Queue
  """

  def __init__(self):
    self.dog = Queue()
    self.cat = Queue()
    self.cat_wait = 0
    self.dog_wait = 0

  def enqueue(self, animal: object):
    """adds an animal to AnimalShelter instance using the species attr. of animal object. Distinct from the enqueue method of SuperClass: Queue.
    input <-- object
    output --> mutates Queue in place. non-fruitful
    """
    #use property species to sort inputs into respective sub-queues
    if animal.species == 'dog':
      self.dog.enqueue(animal) 
    elif animal.species == 'cat':
      self.cat.enqueue(animal)
    else:
      return f'We\'re sorry, we cannot take {animal.species}s at this shelter'
    
  def dequeue(self, pref:str= 'cat')-> str:
    """Returns the name of first animal species equal to pref. defaults to cat
    input <-- str
    output --> str
    """

    if pref == 'dog':
      adopted = self.dog.dequeue()
      self.cat_wait += 1
      return adopted.name
    elif pref == 'cat': # explicitly checks default to allow exception if pref not available at shelter.
      adopted = self.cat.dequeue()
      self.dog_wait += 1
      return adopted.name
    else:
      #uses f-string for user facing error. backend Exception Handling could also be implemented. 
      return f'We\'re sorry, we have no {pref}s available for adoption'

