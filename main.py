import collections
import datetime
import pandas
import pprint

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


pp = pprint.PrettyPrinter(indent=4)

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

bottles_excel = pandas.read_excel('wine3.xlsx', keep_default_na=False).to_dict(orient='records')
bottles_collection = collections.defaultdict(list)
for bottle in bottles_excel:
    bottles_collection[bottle.get('Категория')].append(bottle)

rendered_page = template.render(
    bottles = bottles_collection,
    years_str = write_ru_years(datetime.date.today().year - 1920)
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

print ('Количество Вин: ' + str(len(bottles_excel)))
print ('Количество категорий: ' + str(len(bottles_collection)))
category_str = ""
for bottle in bottles_collection:
    print ("  - "+bottle)
    
server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()