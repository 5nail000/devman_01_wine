# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте архив с кодом ([ссылка для скачивания](https://codeload.github.com/5nail000/devman_01_wine/zip/refs/heads/master)) и распакуйте его.
- Для удобства реккомендуется установить виртуальное окружение ([ссылка на руководство](https://fixmypc.ru/post/sozdanie-virtualnogo-okruzheniia-v-python-3-s-venv-i-virtualenv/?ysclid=l7udz3aqdd57938214#efd7))
- Установите необходимые библиотеки
```
python3 -m pip install -r requirements.txt
```
- Запустите сайт командой:
```
python3 main.py
```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).
- После успешной установки и запуска, по указанному выше адресу должна отобразиться главная страница сайта.

## Данные

- Перечень продукции загружается из таблицы с названием '**wines.xlsx**', сформированному по такому образцу:

Категория | Название | Сорт | Цена | Картинка | Акция
--- | --- | --- | --- | --- | ---
Белые вина | Белая леди | Дамский пальчик | 399 | belaya_ledi.png | Выгодное предложение
Напитки | Коньяк | классический | 350 | konyak_klassicheskyi.png |
Белые вина | Ркацители | Ркацители | 499 | rkaciteli.png |
Красные вина | Черный лекарь | Качич | 399 | chernyi_lekar.png |

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
