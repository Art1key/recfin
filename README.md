1) Данный репозиторий представляет собой django-проект с фронт-частью, выполненной с помощью HTML/CSS, и бек-частью, выполненной на  postgressql.
2) Чтобы запустить данный проект необходимо:
   1. Файл с БД с названием "restor" подгрузить в новую созданную БД с помощью функции backup
   2. Убедиться, что подгружены необходимые модели данных, таблицы заполнены значениями
   3. Создать в корневой папке диска папку с названием "recfin" (пусть должен содержать только латинские буквы)
   4. Поместить в эту папку файлы, находящиеся в репозитории
   5. Открыть командную строку или cmd
   6. Сделать следующие запросы:
      C:\Users\maxva>cd recfin
      C:\Users\maxva\recfin>manage.py runserver
   7. Сервер запущен
