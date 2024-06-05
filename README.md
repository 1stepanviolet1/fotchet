# fotchet
Приложение для формирования отчётов по шахматам (для винды).<br />
Примеры входных/выходных данных присутствуют в папке ``data``.<br />
<br />

P.S. Далее подразумевается, что <i>Первая партия</i> - это та, в которой вы играли белыми<br />
<i>Вторая партия</i> - соответственно, чёрными

## Как использовать
1. Установите зависимости и собрать проект:
```powershell
.\install
```
2. Вам следует переместить ходы двух партий в виде ``.pgn`` файлов в папку ``data`` 
   (про другие варианты предоставления входных данных см. [Входные данные](https://github.com/1stepanviolet1/fotchet/tree/main?tab=readme-ov-file#входные-данные));
3. Загляните в файл ``.env``. Там вам следует заполнить поля под себя (см. [.env](https://github.com/1stepanviolet1/fotchet/tree/main?tab=readme-ov-file#env));
4. Из <b>кореневой папки</b> проекта запустите скрипт:
```powershell
.\fotchet
```
5. Далее проверьте результат в папке ``data``.

### Входные данные
Вы можете предоставить входные данные в различных вариантах:
- Получить ``.pgn`` файлы и перенести их в папку ``data`` (рекомендовано)
- Сами перенесите ходы в ``.txt`` файлы (<b>Обратите внимание</b> на примеры в папке ``data``)

### .env
Далее приведено объяснение, как использовать переменные в ``.env``:
- ``1_filename`` - файл, хранящий первую партию
- ``2_filename`` - файл, хранящий вторую партию
- ``output_filename`` - файл, в который будет записан отчёт (данному файлу не обязательно существовать в ``data``)
- ``platform`` - вариант платформы, на которой вы играли (``chess`` / ``lichess``)
- ``translate_en_into_ru`` - по желанию программа может перевести партию с английской нотации на русскую. Чтобы она это сделала, данное поле должно содержать не ``0`` и быть не пустым
- ``yourself`` - ваше <b>ФИО</b>
- ``opponent`` - только <b>Фамилия и Имя</b> вашего оппонента
- ``your_id`` - номер вашего студака
- ``tour`` - шахматный тур, в котором вы участвуете
- ``date`` - дата проведения партий

## Важная информация
1. В примерах указаны указаны следующие данные:
- ``data1.txt`` пример данных с ``lichess``
- ``data2.txt`` пример данных с ``chess``

Однако ваши данные должны быть в <b>едином формате</b>.

2. Для корректной работы скрипта выходной файл не должен использоваться другими программами (в том числе excel).
3. При некорректном заполнении полей ``.env`` или некорректном предоставлении входных данных скрипт может испытать внештатную ситуацию при работе, что влечёт за собой непредвиденные последствия.
4. Также стоит отметить, что если вы предоставляете входные данные в ``.txt`` файлах, то следите за тем, чтобы формат ваших данных совпадал с тем, которые предоставлены в примерах (в противном случае данные будут считаны неверно)

## Связь с разработчиками
- stepanviolet@gmail.com (рекомендовано)
- kosta-lap@yandex.ru (рекомендовано)
- [stepanviolet](https://vk.com/stepanviolet)
- [kostalap](https://vk.com/kostalap)
