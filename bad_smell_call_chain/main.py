class Person:
    def __init__(self, room_number: int, population: int):
        self._population = population
        self._room = room_number

    def get_person_room(self):
        return self._room

    def get_city_population(self):
        return self._population


if __name__ == '__main__':
    person = Person(444, 1002222)
    print(person.get_person_room())
    print(person.get_city_population())
