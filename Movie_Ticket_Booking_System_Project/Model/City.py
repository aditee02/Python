class City:
    def __init__(self, city_id, name):
        self.city_id = city_id
        self.name = name

    def __repr__(self):
        return f"City(city_id={self.city_id}, name='{self.name}')"
