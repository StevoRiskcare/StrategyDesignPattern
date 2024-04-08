from abstract.abs_strategy import AbsStrategy


class RoyalMail(AbsStrategy):
    def get_fee(self):
        return 10