class Unit:

    def __init__(self, game_field, x_coord, y_coord):
        self._game_field = game_field
        self._x_coord = x_coord
        self._y_coord = y_coord

    def move(self, direction, state='crawl', base_speed=1):
        speed = self._speed_calculation(state, base_speed)

        if direction == 'UP':
            self._y_coord += speed
        elif direction == 'DOWN':
            self._y_coord -= speed
        elif direction == 'LEFT':
            self._x_coord -= speed
        elif direction == 'RIGHT':
            self._x_coord += speed

        self._game_field.set_unit(x=self._x_coord, y=self._y_coord)

    @staticmethod
    def _speed_calculation(state, base_speed):
        if state == 'fly':
            return base_speed * 1.2
        if state == 'crawl':
            return base_speed * 0.5
