# top_place
### Выставка компетенций
## По проблемам и вопросам запуска писать на https://t.me/lordsanchez
### Как развернуть проект у себя на сервере:
+ Клонировать репозиторий:
```
git clone https://github.com/FFFSanchez/top_place.git
```
+ Cоздать и активировать виртуальное окружение, установить зависимости:
```
python3 -m venv env
source venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```
+ Выполнить миграции и создать суперюзера:
```
python manage.py migrate
python manage.py createsuperuser
```
```
python manage.py runserver
```
### Описание проекта:
#### Ссылка: http://atrifonov.pythonanywhere.com/0/
Дамы и Господа! Представляю вашему вниманию!
Не придумал какую-то конкретную цель, поэтому просто сделал сайт, где использовал все полученные знания и конечно-же кучу всего догугливал, пробовал, кумекал кукарекал, НО! Все работает как я задумал! это прекрасно.
За основу взял какой то шаблон из интернета и полностью переработал его.


Итак:


Главная страница.
Могу создавать опросы (от 2 до 4 вариантов ответа), голосвать может онли зареганный юзер и только 1 раз, после голосования он видит результаты текущего опроса. По нажатии кнопки Следующий опрос рандомится следующий опрос, из выборки исключаются уже пройденные опросы. Результаты всех опросов также отображены на главной странице и доступны по прохождении всех существующих опросов.
Много пришлось поломать голову над таблицами моделями и связями, чтобы опросы дружили с вариантами ответом, считались голоса, выводились правильно каждому юзеру.


Страница статей.
Тут в целом функционал вам всем известен - статьи, картинки, комментарии, пагинация, сортировка по Темам.


Страница Портфолио.
Статические страницы + можно добавлять проекты, ссылки на них и описание.


Страница Связь со мной.
Вот тут интересно, прикрутил smtp сервер gmail(оказалось phytonanywhere работает только с гуглом). Письма приходят на мой почтовый ящик, могу указать любой. Валидация формы работает вроде бы, сообщения об успешной или неуспешной отправке отображаются.


Страница с регистрацией.
Тут как в нашем проекте - логин, регистрация, смена/ресет пароля.


Еще использовал переменные окружения .env чтобы не писать пароли в явном виде в settings.py.
Использовал библиотеку django-environ.
Также есть кастомная 404 ))


Прошу проходить, регаться, голосовать, отправлять письма, писать комменты, тыкать везде, ломать сайт полностью)
