Дипломный проект: реальный кейс компании «Ростелеком Информационные Технологии»

Сайт «Ростелеком Информационные Технологии» - https://b2c.passport.rt.ru
Бриф - https://drive.google.com/drive/folders/1I4RNs4X8wQjeAk-jgNePKDwkw65XsrWc?usp=sharing

Задачи: 
 - протестировать требования на основе брифа
 - разработать тест-кейсы (не менее 15);
 - провести автоматизированное тестирование продукта (по одному автотесту на каждый тест-кейс);
 - описать обнаруженные дефекты.

Во время выполнения проекта 
 ~ были написанны:
   - Чек-лист, тест-кейсы, баг-репорт - https://drive.google.com/drive/folders/1I4RNs4X8wQjeAk-jgNePKDwkw65XsrWc?usp=sharing
   - Автотесты - https://github.com/Elgr97/Rostelecom/tree/master

 ~ были применены:
   - Техники тест-дизайна (тестирование состояний и переходов; анализ граничных значений; разбиение на классы эквивалентности)
   - Библиотеки PyCharm (requests; python-dotenv; pytest; selenium; faker)

Доп.ресурсы:
 - https://temp-mail.org - для создания временной эл.почты
 - https://drive.google.com - для создания гугл-таблицы и хранения доп.материалов

Описание проекта:
Проект содержит 
 ~ папку pages, в которой находятся файлы:
    - registration_email.py - GET-запросы к виртуальному почтовому ящику для получения валидного email и кода для регистрации на сайте и восстановления пароля;
    - config.py - основной URL тестируемого сайта;
    - auth.py - функции-обертки для локаторов, распределенные по классам в зависимости от тематики тестов;
    - base.py - функции для применения к локаторам явных ожиданий, получения главной страницы сайта и пути текущей страницы;
    - locators.py - XPath- и CSS-локаторы web-элементов сайта;
    - settings.py - данные, используемые в процессе теста.
 
 ~ папку tests, в которой находятся файлы с тестами:
    - test_auth_page_positive - позитивные тесты страницы авторизации;
    - test_auth_page_negative - негативные тесты страницы авторизации;
    - test_new_password_positive - позитивные тесты страницы восстановления пароля;
    - test_new_password_negative - негативные тесты страницы восстановления пароля;
    - test_registr_positive - позитивные тесты страницы регистрации;
    - test_registr_negative - негативные тесты страницы регистрации.
 
 ~ файл conftest.py, который содержит фикстуру для работы с браузером;
 
 ~ файл pytest.ini, который содержит маркеры для параметризации.





   
