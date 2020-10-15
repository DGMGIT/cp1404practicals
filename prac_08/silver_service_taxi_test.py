
from prac_08.Silver_Service_Taxi import SilverServiceTaxi

prius = SilverServiceTaxi("Prius 1", 100, 2)
hummer = SilverServiceTaxi("Hummer", 100, 4)


prius.drive(18)
hummer.drive(18)

print("{}\nTotal fare ${:.2f}".format(prius, prius.get_fare()))
print("{}\nTotal fare ${:.2f}".format(hummer, hummer.get_fare()))

prius.start_fare()

prius.drive(100)

print("{}\nTotal fare ${:.2f}".format(prius, prius.get_fare()))