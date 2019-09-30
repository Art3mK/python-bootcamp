class Card():
    def __init__(self, **kwargs):
        self.rank = kwargs["rank"]
        self.suit = kwargs["suit"]

    def __repr__(self):
        return f'{self.suit}:{self.rank}'

    def value(self, **kwargs):
        kwargs.setdefault('ace11', False)
        if self.rank in ["jack","queen","king"]:
            return 10
        elif self.rank == "ace":
            if kwargs["ace11"]:
                return 11
            else:
                return 1
        else:
            return self.rank
