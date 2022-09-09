import collections
import datetime
import pandas
import pprint
import argparse

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():

    pp = pprint.PrettyPrinter(indent=4)

    parser = argparse.ArgumentParser(
        description='Описание что делает программа'
    )
    parser.add_argument('-d', '--dir', help='Папка с таблицой wine.xlsx (по умолчанию корневая)', type=str)
    args = parser.parse_args()

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')


    def write_ru_years(num):
        
        string = 'лет'

        if str(num)[-2:-1] != '1':
            if str(num)[-1] == '1': string = 'год'
            if str(num)[-1] == '2': string = 'года'
            if str(num)[-1] == '3': string = 'года'
            if str(num)[-1] == '4': string = 'года'

        return str(num) + ' ' + string

    if args.dir: wine_folder = args.dir
    else : wine_folder = '.'

    bottles_excel = pandas.read_excel(f'{wine_folder}/wines.xlsx', keep_default_na=False).to_dict(orient='records')
    bottles_collection = collections.defaultdict(list)
    for bottle in bottles_excel:
        bottles_collection[bottle.get('Категория')].append(bottle)

    rendered_page = template.render(
        bottles = bottles_collection,
        years_str = write_ru_years(datetime.date.today().year - 1920)
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    # Prints info For testing
    '''
    print ('Количество Вин: ' + str(len(bottles_excel)))
    print ('Количество категорий: ' + str(len(bottles_collection)))
    category_str = ""
    for bottle in bottles_collection:
        print ("  - "+bottle)
    #'''
        
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()