csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read(file):
    return [line.split(';') for line in file.split('\n')]


def _sort(seq):
    return sorted(seq, key=lambda x: int(x[1]))


def _filter(seq):
    return list(filter(lambda x: int(x[1]) < 10, seq))


def get_users_list():
    return _filter(_sort(_read(csv)))


if __name__ == '__main__':
    print(get_users_list())
