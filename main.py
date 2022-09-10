import collections
import datetime
import pandas
import argparse
import logging
from pathlib import Path

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

def write_ru_years(num):
    
    year_string = 'лет'

    if str(num)[-2:-1] != '1':
        if str(num)[-1] == '1': 
            year_string = 'год'
        if str(num)[-1] == '2' or str(num)[-1] == '3' or str(num)[-1] == '4':
            year_string = 'года'
    return f'{num} {year_string}'


def main():

    year_of_opening = 1920

    logging.basicConfig(filename='logging.log', level=logging.DEBUG)

    parser = argparse.ArgumentParser(
        description='Запуск Сайта-магазина'
    )
    parser.add_argument('-d', '--dir', default='.', help='Папка с таблицой wine.xlsx (по умолчанию корневая)')
    args = parser.parse_args()

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    bottles_excel = pandas.read_excel(f'{Path().cwd().joinpath(args.dir).joinpath("wines.xlsx")}', keep_default_na=False).to_dict(orient='records')
    bottles_collection = collections.defaultdict(list)
    for bottle in bottles_excel:
        bottles_collection[bottle.get('Категория')].append(bottle)

    rendered_page = template.render(
        bottles_collection = bottles_collection,
        years_str = write_ru_years(datetime.date.today().year - year_of_opening)
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


    logging.info (f'Успешный запуск сайта ({str(datetime.datetime.now()).split(".")[0]})')
    logging.info ('Количество Вин: ' + str(len(bottles_excel)))
    logging.info ('Количество категорий: ' + str(len(bottles_collection)))
    category_str = ""
    for bottle in bottles_collection:
        logging.info ("  - "+bottle)
    logging.info ('-' * 40)
    #'''
        
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
