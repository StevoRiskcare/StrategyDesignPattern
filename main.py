from carriers.fedex import Fedex
from shipper.shipper import Shipper

carrier = Fedex()
ship = Shipper(carrier)
shipping_cost = ship.get_cost()
print(shipping_cost)