class Cargo:
    def __init__(self, cargo_weight):
        self.cargo_weight = cargo_weight

    def __str__(self):
        return f"{self.cargo_weight}"