class Card():
    def __init__(self, **kwargs):
        self.secret = False
        self.rank = kwargs["rank"]
        self.suit = kwargs["suit"]

    def __repr__(self):
        if self.secret:
            return 'xxx:xxx'
        else:
            return f'{self.suit}:{self.rank}'
