### Установка
На машине с установленным docker и docker-compose, находясь в папке с docker-compose.yml команда:

`docker-compose up`

### curl команды

* Создать товар:

`curl -H "Content-Type: application/json" -X POST -d "{\"title\":\"Asus\", \"desc\":\"Gaming SuperBook\", \"parameters\":{\"RAM\":\"24GB\",\"GPU\":\"2080TI\",\"CPU\":\"i999\", \"price\":120000}}" http://127.0.0.1:5000/item`

По ключу parameters есть возможность добавлять любое количество дополнительных характеристик.

* Найти по параметру:

`curl -H "Content-Type: application/json" -X GET -d "{\"param\":\"price\", \"value\": 100000, \"flag\": true}" http://127.0.0.1:5000/item/by_price`

Ищет в массиве значения parameters точное совпадение по ключу price и значением более 100000. flag: true отвечает за больше(price > 100000). Если изменить true на false, будет искать значения меньше 100000.

* Получить детали по id:

json вариант:
`curl -H "Content-Type: application/json" -X GET -d "{\"_id\":2}" http://127.0.0.1:5000/item/by_id`

url вариант:
`http://127.0.0.1:5000/item/2`

* По названию:

`curl -H "Content-Type: application/json" -X GET -d "{\"title\":\"sUS\"}" http://127.0.0.1:5000/item/by_title`

По частичному или точному совпадению по ключу title. Не чувствителен к регистру. 
