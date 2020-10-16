class retailItem:

    def __init__(self, name, description_of_item, number_of_item, prise):
        self.name = name
        self.prise = prise
        self.number_of_item = number_of_item
        self.description_of_item = description_of_item

    def set_name(self, name):
        self.name = name

    def set_prise(self, prise):
        self.prise = prise

    def set_number_of_item(self, number_of_item):
        self.number_of_item = number_of_item

    def set_description_of_item(self, description_of_item):
        self.description_of_item = description_of_item

    def get_prise(self):
        return self.prise

    def get_number_of_item(self):
        return self.number_of_item

    def get_description_of_item(self):
        return self.description_of_item

    def get_name(self):
        return self.name
