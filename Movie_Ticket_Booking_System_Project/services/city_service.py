class CityService:
    def __init__(self, city_dao):
        self.city_dao = city_dao

    def add_city(self, city_name):
        return self.city_dao.create_city(city_name)

    def list_cities(self):
        return self.city_dao.get_all_cities()

    def get_city(self, city_id):
        return self.city_dao.get_city_by_id(city_id)
