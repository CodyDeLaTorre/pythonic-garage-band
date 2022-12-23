class Band:
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def __str__(self):
        return f"We are {self.name}"

    def __repr__(self):
        return f"Band instance. Name = {self.name}. Members = {self.members}"

    def play_solos(self):
        for member in self.members:
            return member.play_solo()


class Musician(Band):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"I am {self.name}"

    def __repr__(self):
        return f"Musician instance. Name = {self.name}"


class Guitarist(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = 'guitar'

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = 'bass'

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = 'drums'

    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "rattle boom crash"

