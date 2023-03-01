from abc import ABC, abstractmethod


class AbstractTransport(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Transport(AbstractTransport):

    def __init__(self, title: str):
        self._title = title

    def start_engine(self):
        print(f'{self._title} engine started')

    def stop_engine(self):
        print(f'{self._title} engine stopped')

    def move(self):
        print(f'{self._title} started moving')

    def stop(self):
        print(f'{self._title} has stopped')


class Car(Transport):

    def __init__(self, title: str = 'Car'):
        super().__init__(title=title)


class Boat(Transport):

    def __init__(self, title: str = 'Boat'):
        super().__init__(title=title)


class ElectroScooter(Transport):

    def __init__(self, title: str = 'Electro-scooter'):
        super().__init__(title=title)


class Person:
    @staticmethod
    def use_transport(transport: Transport):
        transport.start_engine()
        transport.move()
        transport.stop()
        transport.stop_engine()


if __name__ == '__main__':
    boat = Boat()
    car = Car()
    kamikaze = ElectroScooter()

    person = Person()
    person.use_transport(boat)
    print('=' * 10)
    person.use_transport(car)
    print('=' * 10)
    person.use_transport(kamikaze)
