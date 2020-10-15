class CellPhone:

    def __init__(self, manufact, model, price):
        self.manufact = manufact
        self.model = model
        self.retail_price = price

    def set_manufact(self, manufact):
        self.manufact = manufact

    def set_model(self, model):
        self.model = model

    def set_retail_price(self, price):
        self.retail_price = price

    def get_manufact(self):
        return self.manufact

    def get_model(self):
        return self.model

    def get_retail_price(self):
        return self.retail_price
