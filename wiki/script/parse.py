from bs4 import BeautifulSoup
import lxml
import unittest


def parse(path_to_file):
    return [parse_count_amg(path_to_file), parse_count_header(path_to_file), parse_link_count(path_to_file),
            parse_ul_ol_count(path_to_file)]


def parse_count_amg(path_to_file: str) -> int:
    """Считаем количество удовлетворяющих условию тегов img"""
    size_list = []
    count = 0
    soup = BeautifulSoup(open(path_to_file, encoding='utf-8'), 'lxml')
    body = soup.find('div', attrs={'id': 'bodyContent'})
    all_img = body.find_all('img')
    for img in all_img:
        try:
            size_list.append(int(img['width']))

        except KeyError:
            pass

    for i in size_list:
        if i >= 200:
            count += 1
        else:
            continue

    return count


def parse_count_header(path_to_file: str) -> int:
    h_list = {}  # Словарь дли списков с заголовками. Для каждого уровня заголовков (h1, h2 ...) свой список
    soup = BeautifulSoup(open(path_to_file, encoding='utf-8'), 'lxml')
    body = soup.find('div', attrs={'id': 'bodyContent'})

    """Распределяем заголовки по спискам"""
    default_i = 1
    for i in range(1, 7):
        all_h = body.find_all(f'h{i}')

        if default_i == i:
            h_list[i] = all_h
            default_i += 1

    def check_list(ls: []) -> int:

        """Проверяем содержимое заголовков и считаем количество подходящих по условию"""
        count = 0
        for i in ls:
            text = i.get_text(strip=True)
            if text[0] == 'E' or text[0] == 'C' or text[0] == 'T':
                count += 1
        return count

    """Чекаем все списки. Суммируем количество подходящих по условию заголовков"""
    result = 0
    for i in h_list.keys():
        result += check_list(h_list[i])

    return result


def parse_link_count(path_to_file: str) -> int:
    result_count = []
    soup = BeautifulSoup(open(path_to_file, encoding='utf-8'), 'lxml')
    body = soup.find('div', attrs={'id': 'bodyContent'})
    all_a = body.find_all('a')

    result = 0
    for a in all_a:
        count = 1
        for link in a.find_next_siblings():
            if link.name != 'a':
                break
            count += 1
        result = max(result, count)

    return result


def parse_ul_ol_count(path_to_file: str) -> int:
    soup = BeautifulSoup(open(path_to_file, encoding='utf-8'), 'lxml')
    body = soup.find('div', attrs={'id': 'bodyContent'})
    all_ul = body.find_all('ul')
    all_ol = body.find_all('ol')
    # print(all_ul)

    count_ul, count_ol = 0, 0
    for ul in all_ul:
        if not (ul.find_parent(['ol', 'ul'])):
            count_ul += 1
    for ol in all_ol:
        if not (ol.find_parent(['ol', 'ul'])):
            count_ol += 1
    result = count_ol + count_ul
    print(result)
    return result



class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            (r'C:\Users\Denis\Desktop\Скрипты\wiki\Stone_Age.html', [13, 10, 12, 40]),
            (r'C:\Users\Denis\Desktop\Скрипты\wiki\Brain.html', [19, 5, 25, 11]),
            (r'C:\Users\Denis\Desktop\Скрипты\wiki\Artificial_intelligence.html', [8, 19, 13, 198]),
            (r'C:\Users\Denis\Desktop\Скрипты\wiki\Python_(programming_language).html', [2, 5, 17, 41]),
            (r'C:\Users\Denis\Desktop\Скрипты\wiki\Spectrogram.html', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    # unittest.main()
     parse_ul_ol_count(r'C:\Users\Denis\Desktop\Скрипты\wiki\Artificial_intelligence.html')
