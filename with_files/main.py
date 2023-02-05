import csv
import json
import re


def is_valid_file(filename: str, ) -> bool:
    """Функция проверяет все ли в порядке с файлом"""
    pass


def read_from_csv(name: str, delimiter: str = ',', encoding: str = 'UTF-8',
                  newline: str = '', header: bool = None) -> list[list[str]]:
    """Функция читает все строки из CSV файла"""
    query: list[list] = []

    # Открывается файл для чтения
    with open(file=name, mode='r', encoding=encoding, newline=newline) as f:
        # рабивает по разделителю
        reader: csv = csv.reader(f, delimiter=delimiter)

        if header is not None:
            next(reader)  # пропускается заголовок

        # добавляет запросы в результирующий список
        for row in reader:
            query.append(row)

    return query


def get_domain_from_link(links: list[str],
                         pattern: str = "\/\/(.*?)\/") -> list[str]:
    """Извлекает из строки домены"""
    ans = []
    for link in links:
        ans.append(" ".join(re.findall(pattern, link)))

    return ans


def delat_krasivo(queries: list[list[str]]) -> dict[int: dict[str: [str, int, list]]]:
    """Создает словарь где ключами являются такие поля, как
        запрос, частота запроса, список доменов
    """
    res = {}
    for idx, item in enumerate(queries):
        query, frequency = item[:2]
        domains: list[str] = get_domain_from_link(item[2:])
        res[idx] = {
            'query': query,
            'frequency': int(frequency),
            'domains': domains
        }
    return res


if __name__ == '__main__':
    # n: int = 10  # аннотация типа
    # assistant: str = 'Alice'
    # numbers: list[int] = [1, 2, 4, 5, 6, 7]

    # TODO:
    #  1. Сколько раз домен попадает в ТОП 20
    #  2. Сколько раз домен попадает в ТОП 10
    #  3. Сколько трафика получает домен с поиска Яндекса
    data: list[list[str]] = read_from_csv('query.csv', delimiter=';', header=True)
    result: dict[int: dict[str: [str, int, list]]] = delat_krasivo(data)

    print(json.dumps(result, indent=4, ensure_ascii=False))  # выводит словарь в красивом виде
