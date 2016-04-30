# Animal is-a object
class Animal(object):
	pass
	
# Dog is-a Animal
class Dog(Animal):
	
	def __init__(self, name):
		# Dog has-a init that assigns a name attribute
		self.name = name
		self.bark_amount = 1
	
	def trick(self):
		print "%s says: " % self.name,
		print "Woof! " * self.bark_amount
		

# Cat is-a Animal
class Cat(Animal):
	
	def __init__(self, name):
		# Cat has-a init that assigns a name attribute
		self.name = name
		self.meow_amount = 2
		
	def trick(self):
		print "%s says: " % self.name,
		print "Meow! " * self.meow_amount

# Person is-a object
class Person(object):
	
	def __init__(self, name):
		# Persons has-a init that assigns a name attribute
		self.name = name
		
		# Person has-a pet of some kind
		self.pet = None
	
	def pet_trick(self):
		self.pet.trick()

# Employee is-a person
class Employee(Person):
	
	def __init__(self, name, salary):
		# make sure there's a person object of the same name?
		super(Employee, self).__init__(name)
		# Employee has-a salary attribute
		self.salary = salary

# Fish is-a object
class Fish(object):
	pass
	
# Salmon is-a Fish
class Salmon(Fish):
	pass

# Halibut is-a Fish
class Halibut(Fish):
	pass
	

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary's pet is Satan
mary.pet = satan

# frank is-a Employee and has-a salary of 120000
frank = Employee("Frank", 120000)

# frank's pet is Rover
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()

fluffy = Cat("Mr. Fluffy")

mary.pet = fluffy

rover.bark_amount = 3

mary.pet_trick()
frank.pet_trick()
