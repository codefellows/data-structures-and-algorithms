import pytest
from code_challenges.fifo_animal_shelter.fifo_animal_shelter import AnimalShelter, Animal 

#define  Animal Objects as Animals for use in testing AnimalShelter Queue
ferran = Animal('Ferran', 'cat')
raya = Animal('Raya','cat')
jora = Animal('Jora', 'dog')
athena = Animal('Athena', 'dog')



def test_shelter_enqueue_cat():
  shelter = AnimalShelter()
  shelter.enqueue(ferran)
  actual_1 = shelter.cat.front.value.name
  actual_2 = shelter.cat.rear.value.name
  expected = 'Ferran'
  assert actual_1 == expected
  assert actual_2 == expected

def test_shelter_enqueue_dog():
  shelter = AnimalShelter()
  shelter.enqueue(jora)
  actual_1 = shelter.dog.front.value.name 
  actual_2 = shelter.dog.rear.value.name
  expected = 'Jora'
  assert actual_1 == expected
  assert actual_2 == expected

def test_shelter_enqueue_multi_cat():
  shelter = AnimalShelter()
  shelter.enqueue(ferran)
  shelter.enqueue(raya)
  actual_1 = shelter.cat.front.value.name
  expected_1 = 'Ferran'
  assert actual_1 == expected_1
  actual_2 = shelter.cat.rear.value.name
  expected_2 = 'Raya'
  assert actual_2 == expected_2

def test_shelter_enqueue_multi_dog():
  shelter = AnimalShelter()
  shelter.enqueue(jora)
  shelter.enqueue(athena)
  actual_1 = shelter.dog.front.value.name
  expected_1 = 'Jora'
  assert actual_1 == expected_1
  actual_2 = shelter.dog.rear.value.name
  expected_2 = 'Athena'
  assert actual_2 == expected_2

def test_dequeue_pref_cat():
  shelter = AnimalShelter()
  shelter.enqueue(ferran)
  shelter.enqueue(jora)
  actual = shelter.dequeue('cat')
  expected = 'Ferran'
  assert actual == expected

def test_dequeue_pref_dog():
  shelter = AnimalShelter()
  shelter.enqueue(ferran)
  shelter.enqueue(jora)
  actual = shelter.dequeue('dog')
  expected = 'Jora'
  assert actual == expected

def test_dog_wait_after_dequeue_cat():
  shelter = AnimalShelter()
  shelter.enqueue(ferran)
  shelter.enqueue(jora)
  shelter.dequeue('cat')
  actual = shelter.dog_wait 
  expected = 1
  assert actual == expected


def test_cat_wait_after_dequeue_dog():
  shelter = AnimalShelter()
  shelter.enqueue(ferran)
  shelter.enqueue(jora)
  shelter.dequeue('dog')
  actual = shelter.cat_wait 
  expected = 1
  assert actual == expected

def test_multi_dequeue_cat():
  shelter = AnimalShelter()
  shelter.enqueue(ferran)
  shelter.enqueue(jora)
  shelter.enqueue(raya)
  shelter.enqueue(athena)
  
  shelter.dequeue('cat')
  shelter.dequeue('cat')
  actual = shelter.cat.front
  expected = None
  assert actual == expected
  

def test_dog_wait_after_multi_dequeue_cat():
  shelter = AnimalShelter()
  shelter.enqueue(ferran)
  shelter.enqueue(jora)
  shelter.enqueue(raya)
  shelter.enqueue(athena)
  
  shelter.dequeue('cat')
  shelter.dequeue('cat')
  actual = shelter.dog_wait
  expected = 2
  assert actual == expected

def test_multi_dequeue_dog():
  shelter = AnimalShelter()
  shelter.enqueue(ferran)
  shelter.enqueue(jora)
  shelter.enqueue(raya)
  shelter.enqueue(athena)
  
  shelter.dequeue('dog')
  shelter.dequeue('dog')
  actual = shelter.dog.front
  expected = None
  assert actual == expected

def test_cat_wait_after_multi_dequeue_dog():
  shelter = AnimalShelter()
  shelter.enqueue(ferran)
  shelter.enqueue(jora)
  shelter.enqueue(raya)
  shelter.enqueue(athena)
  
  shelter.dequeue('dog')
  shelter.dequeue('dog')
  actual = shelter.cat_wait
  expected = 2
  assert actual == expected

def test_dequeue_no_pref_wait_even():
  #program currently defaults to cat 
  shelter = AnimalShelter()
  shelter.enqueue(jora)
  shelter.enqueue(ferran)
  shelter.enqueue(raya)
  shelter.enqueue(athena)
  actual = shelter.dequeue()
  expected = 'Ferran'
  assert actual == expected

def test_dequeue_no_pref_cat_wait():
  shelter = AnimalShelter()
  shelter.enqueue(jora)
  shelter.enqueue(ferran)
  shelter.enqueue(raya)
  shelter.enqueue(athena)

  shelter.dequeue()
  actual = shelter.cat_wait
  expected = 0
  assert actual == expected

def test_dequeue_no_pref_dog_wait():
  shelter = AnimalShelter()
  shelter.enqueue(jora)
  shelter.enqueue(ferran)
  shelter.enqueue(raya)
  shelter.enqueue(athena)

  shelter.dequeue()
  actual = shelter.dog_wait
  expected = 1
  assert actual == expected


