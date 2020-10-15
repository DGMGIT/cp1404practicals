
from prac_08.taxi import Taxi

prius = Taxi("Prius 1", 100, 1.23)

prius.drive(40)

print(F"{prius}\n${Taxi.get_fare(prius)}")
prius.start_fare()
prius.drive(100)

print()
print(F"{prius}\n${Taxi.get_fare(prius)}")
