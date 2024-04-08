from abstract.abs_strategy import AbsStrategy


class Fedex(AbsStrategy):
    def get_fee(self):
        return 100