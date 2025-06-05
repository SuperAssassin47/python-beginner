from pprint import pprint
import ex26

pprint(ex26.__dict__)

print("AGE IS ", ex26.age)
print("AGE IS ALSO ", ex26.__dict__['age'])

print(f'Zaffod Beeblebrox was {ex26.age} years old')

ex26.__dict__['age'] = 1000
print(f"He is now {ex26.age} years old")

ex26.age = 50
print(f"Oops, now he is {ex26.__dict__['age']} years old")
