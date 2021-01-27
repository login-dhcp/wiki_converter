import csv
import sys

NAMES = {
    'プロデューサー': 'P',
    'はづき': 'Hazuki',
    '社長': 'Shacho',
    '真乃': 'Mano',
    '灯織': 'Hiori',
    'めぐる': 'Meguru',
    '恋鐘': 'Kogane',
    '摩美々': 'Mamimi',
    '咲耶': 'Sakyua',
    '結華': 'Yuika',
    '霧子': 'Kiriko',
    '果穂': 'Kaho',
    '智代子': 'Chiyoko',
    '樹里': 'Rinze',
    '凛世': 'Natsuha',
    '川夏葉': 'Juri',
    '甘奈': 'Amana',
    '甜花': 'Tenka',
    '千雪': 'Chiyuki',
    'あさひ': 'Asahi',
    '優子': 'Fuyuko',
    '愛依': 'Mei',
    '透': 'Toru',
    '円香': 'Madoka',
    '小糸': 'Koito',
    '雛菜': 'Hinana',
}


# need to have blank row at the top of csv
def name_to_iconPath(name, ext='webp'):
    if name in NAMES.keys():
        return f'{NAMES[name]}Icon.{ext}'
    else:
        return ''


def csvline_to_wikiline_if_data(csvline):
    filename, id, name, text, trans = csvline[:5]

    wikiline = ''
    wikiline += "{{틀:커뮤 대사 | "
    wikiline += f"id = {id} | "
    wikiline += f"name = {name} | "
    wikiline += f"icon = {name_to_iconPath(name)} | "
    wikiline += f"text = {text} | "
    wikiline += f"trans = {trans}"
    wikiline += "}}"

    return wikiline


def csvline_to_wikiline(csvline):
    assert len(csvline) >= 5
    wikiline = ''
    status = ''

    filename, id, name, text, trans = csvline[:5]

    if filename != '':
        if filename.startswith('#FILENAME'):
            status = 'meta'
        elif filename.startswith('#EOF'):
            status = 'meta'
        else:
            raise ValueError
    else:
        if id == 'id':
            status = 'meta'
            wikiline = 'row_info:'
        elif id == 'info':
            status = 'meta'
            wikiline = 'file_info:'
        elif id == '译者':
            status = 'meta'
            wikiline = '译者:'
        elif id == 'select':
            status = 'data'
            wikiline = csvline_to_wikiline_if_data(csvline)
        else:
            try:
                _ = int(id)
                status = 'data'
                wikiline = csvline_to_wikiline_if_data(csvline)

            except ValueError as e:
                wikiline = ''
                status = 'error'
                # print(e, id)

    if status == 'meta':
        wikiline += ','.join(csvline)
        # wikiline += f'{csvline:s}'

    wikiline += '\n'

    return wikiline, status


def csv_to_wikitext(path):
    metas = []
    wikitext = '{{틀:커뮤 테이블 | text=\n'

    with open(path, 'r', encoding='utf-8') as f:
        rdr = csv.reader(f)
        for line in rdr:
            wikiline, status = csvline_to_wikiline(line)

            if status == 'data':
                wikitext += f"{wikiline}"
            elif status == 'meta':
                metas.append(wikiline)
            elif status == 'error':
                pass
            else:
                raise ValueError

    wikitext += '}}\n'

    wikitext += '<!--metadata\n'
    for meta in metas:
        wikitext += f'{meta}'
    wikitext += '-->\n'

    return wikitext


if __name__ == '__main__':
    path = input("csv 파일 경로를 입력해주세요: ") 
    wikitext = csv_to_wikitext(path=path)
    print(wikitext)

    path_save = path[:-4] + '.txt' # assert path ends with .csv
    with open(path_save, 'w', encoding='utf-8') as f:
        f.write(wikitext)

    print(f'output file saved at {path_save}')
    input("Press enter to close..")