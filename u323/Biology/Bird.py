class Bird:
    # Attributes
    weight = 22.5
    size= 18
    feather_color = "red"

    # Constructor - Setup every variable
    def __init__(self, weight, size, feather_color):
        self.weight = weight
        self.size = size
        self.feather_color = feather_color

    def __str__(self):
        return "weight: " + str(self.weight) + "size: " + str(self.size) + "feather_color: " + str(self.feather_color)

    def get_weight(self):
        return self.weight

    def get_size(self):
        return self.size

    def get_feather_color(self):
        return self.feather_color

    def set_weight(self, new_weight):
        self.weight = new_weight
    def set_size(self, new_size):
        self.size = new_size
    def set_feather_color(self, new_feather_color):
        self.feather_color = new_feather_color