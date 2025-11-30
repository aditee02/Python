class Cinema:
    def __init__(self, cinema_id, name, city_id):
        self.cinema_id = cinema_id
        self.name = name
        self.city_id = city_id

    def __repr__(self):
        return f"Cinema(cinema_id={self.cinema_id}, name='{self.name}', city_id={self.city_id})"
