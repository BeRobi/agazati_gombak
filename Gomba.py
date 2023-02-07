class Gomba:
    def __init__(self, sor):
        self.nev = sor[0]
        self.nemz = sor[1]
        self.evszak = sor[2]

    def __str__(self):
        return f"{self.nev}, {self.nemz}, {self.evszak}"
