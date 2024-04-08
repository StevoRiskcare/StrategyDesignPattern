class Shipper(object):
    def __init__(self, _carrier):
        self.carrier = _carrier

    def get_cost(self):
        return self.carrier.get_fee()