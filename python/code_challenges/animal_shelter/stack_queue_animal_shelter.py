class AnimalShelter:

    def __init__(self, front=None, rear = None):
        self.front = front
        self.rear = rear

    pets = []

    def enqueue(self, input_pet):
        """Arguments: input_pet
        Adds a new node with that input_pet to the rear of the queue with an O(1) Time performance."""

        if self.front is None:
            self.front = input_pet
            #If there are no items in the list the first is the front.
            self.pets.append(input_pet.value)
        if self.rear:
            self.rear.next = input_pet
            self.pets.append(input_pet.value)


        self.rear = input_pet
            #This runs in either case
            #If we are putting something into the list line 22 is setting something to the front and to the rear. Look at the spacing. This happens in both cases and runs outside of the second if statement.
            # Not every if needs an else in python.

        # Why is it that we do not need to set the next of the front to the first rear for this to work? Based on the way this is currently it seems like the front would be detached from the rest of the queue
        # The last line is setting whatever we put into the stack as the rear. Thus is there is only one item going in it will be both the front and the rear.


    def dequeue(self, pref=None):
        """Arguments: none
        Returns: the value from node from the front of the queue
        Removes the node from the front of the queue
        Should raise exception when called on empty queue"""
        if self.front.value == pref:
            prev_front = self.front
            self.front = self.front.next
            return prev_front
    #     if pref in self.pets:
    #         self.re_enqueue(pref)
            # Attempt to put the oldest animal in the back of the queue until you get to the animal that is wanted.
        if pref in self.pets:
            if self.peek() == pref:
                #This may still need self.peek.value
                return self.front.value
            else:
                animal = self.dequeue()
                self.enqueue(animal)
                #This takes whatever is currently in the front (and not pref) and puts it in the back.

                # prev_front = self.front
                # self.front = self.front.next
                # self.enqueue(prev_front)

        if pref not in self.pets:
            return None
        if pref is None:
            prev_front = self.front
            self.front = self.front.next
            return prev_front
            #Stretch goal to return the oldest animal if no preference given.

    # def re_enqueue(self, pref):
    #     reverse = self.front
    #     self.front = self.front.next
    #     self.enqueue(reverse)
    #     self.dequeue(pref)
    #     #This should dequeue the front value and enqueue it to the back of the list.

# btw - the solution you were going for is very efficient in terms of space, but inefficient for time. There's another common solution that is worse on space but way better on time. In case you want another challenge :D


    def peek(self):
        """Arguments: none
        Returns: Value of the node located at the top of the stack or the front of the queue
        Should raise exception when called on empty stack"""
        if self.front:

            return self.front.value

    #This is an example that only works with the test stuff in the dunder main
    def adopt(pref):
        animal = shelter.dequeue()
        if animal.type ==pref:
            return animal
        else:
            first_animal = animal
            #This looks for the first cat INSTANCE or that node in particular.
            while True:
                shelter.enqueue(animal)
                animal = shelter.dequeue()
                if animal.type == pref:
                    return animal
                    # Would want to keep enqueing until first animal is front again.
                elif animal == first_animal:
                    shelter.enqueue(first_animal)
                    break

            return None



# Remember dunder strs? This will make it so that if you return the object, it will come in with the str aka pass that test bug where you return the object!
class Dog:
    def __init__(self, value=None, next=None):
        self.value = "dog"
        self.next = next

    def __str__(self):
        return f"{self.value}"


class Cat:
    def __init__(self, value=None, next=None):
        self.value = "cat"
        self.next = next

    def __str__(self):
        return f"{self.value}"

class Kitten:
    def __init__(self):
        self.type = "cat"

class Pupper:
    def __init__(self):
        self.type = "dog"

if __name__ == "__main__":
    # For testing the adopt bonus feature
    shelter = AnimalShelter()
    shelter.enqueue(Kitten())
    shelter.enqueue(Kitten())
    shelter.enqueue(Pupper())
    print(shelter)

    adopted = adopt("Cat")
    print(adopted)

