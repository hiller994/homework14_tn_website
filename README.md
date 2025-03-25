## Автотесты по проекту "Информационный сайт АЗС Татнефть"
[Ссылка на сайт АЗС Татнефть](https://azs.tatneft.ru/)

![This is an image](media_conten/picture/main_page.jpg)
___

## Список кейсов по тестированию (UI-тесты)
1. Калькуляция бонусов в зависимости от трат пользователя (test_bonus_calc.py)
2. Открытие главной страницы и отображение основных элементов (test_open_main_page.py)
3. Открытие страницы промо и отображение акций (test_open_promo.py)
4. Отображение QR-кода для перехода в магазин приложений (test_open_qr.py)
5. Проверка поиска АЗС на карте (test_search_azs.py)

___

## Используемый стек: 
<a href="https://github.com/allure-framework">
<img src="media_conten/icon/icon_allure.png" height="40" width="40" /> 
</a>

<a href="https://www.jenkins.io/">
<img src="media_conten/icon/icon_jenkins.png" height="40" width="40" />
</a>

<a href="https://github.com/pytest-dev">
<img src="media_conten/icon/icon_pytest.png" height="40" width="40" />
</a>

<a href="https://www.python.org/downloads/">
<img src="media_conten/icon/icon_python.png" height="40" width="40" />
</a>

<a href="https://github.com/yashaka/selene">
<img src="media_conten/icon/icon_selene.png" width="40" height="40"/>
</a>

<a href="https://github.com/aerokube/selenoid">
<img src="media_conten/icon/icon_selenoid.png" width="40" height="40"/>
</a>

<a href="https://web.telegram.org/a/">
<img src="media_conten/icon/icon_tg.png" width="40" height="40"/>
</a>

___

## Запуск автотестов

### Удаленно

* Открыть проект в [Jenkins](https://jenkins.autotests.cloud/job/homework_14_website_tn/)
* Перейти в раздел `Build with Parameters`
* В поле `Выбор запуска тестов` выбрать `tests/azs_tn_website` для запуска всех тестов или выбрать конкретный
* В поле `Браузер по умолчанию` выбрать версию браузера (Доступно: 127.0, 128.0)
* В поле `Environment` выбрать среду запуска (Доступно: dev, stage, prod)
* В поле `Comment` указать текст, который нужно отобразать в телеграмм-боте в результатах теста
* Нажать `Build`
* Дождаться окончания прогона автотестов (статус можно отследить слева под боковым меню в блоке `Build`)
* После завершения появляется кнопка `Allure` (иконка), при нажатии открывается отчет

#### Пример отчета Allure:
![This is an image](media_conten/picture/example_allure.jpg)

#### Пример отчета в Телеграмм-бот:
![This is an image](media_conten/picture/example_tg_bot.jpg)

### Локально

* В проекте создать файл .env c данными
```
SELENOID_LOGIN="user1"
SELENOID_PASS="1234"
```
* Запустить команду для установки библиотек
```
Pip install –r requirements.txt
```
* Установить интерпритатор (через консоль или pycharm)
```
python -m venv .venv
source .venv/bin/activate
```
* Запуск теста
```
pytest tests/demoqa/test_registration_form.py --browser_version=128
```
* Вывод результатов в локальном allure
```
allure serve tests/azs_tn_website/allure-results
```




