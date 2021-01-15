from fifo_animal_shelter.fifo_animal_shelter import AnimalShelter, InvalidOperationError, Node

def test_dog():
    a = AnimalShelter()
    a.enqueue("dog")
    actual = a.first.value
    expected = "dog"
    assert actual == expected

def test_dequeue():
    a = AnimalShelter()
    a.enqueue("dog")
    actual = a.dequeue('dog')
    expected = "dog"
    assert actual == expected

def test_not_dog_or_cat():
    a = AnimalShelter()
    a.enqueue("Lizard")
    a.enqueue("dog")
    a.enqueue("cat")
    actual = a.dequeue('lizard')
    expected = "null"
    assert actual == expected