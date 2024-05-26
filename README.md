# fotchet
Приложение для формирования отчётов по шахматам (для винды).<br />
Примеры входных/выходных данных присутствуют в папке ``data``.<br />
<br />
<b>Обращаю ваше внимание</b> на то, что для корректной работы скрипта файл не должен использоваться другими программами (в том числе excel)<br />
<br />
P.S. Далее подразумевается, что <i>Первая партия</i> - это та, в которой вы играли белыми<br />
<i>Вторая партия</i> - соответственно, чёрными

## Как использовать
1. Установите зависимости:
```powershell
pip install -r requirements.txt
```
2. Вам следует переместить ходы двух партий по разным файлам и поместить их в папку ``data``.
3. Загляните в файл ``.env``. Там вам следует заполнить поля под себя (см. [.env](https://github.com/1stepanviolet1/fotchet/tree/main?tab=readme-ov-file#env)).
4. Из <b>кореневой папки</b> проекта запустите скрипт:
```powershell
.\fotchet
```
5. Далее проверьте результат в папке ``data``.

### .env
Далее приведено объяснение, как использовать переменные в ``.env``:
- ``1_filename`` - файл, хранящий первую партию
- ``2_filename`` - файл, хранящий вторую партию
- ``output_filename`` - файл, в который будет записан отчёт (данному файлу не обязательно существовать в ``data``)
- ``input_var`` - вариант платформы, на которой вы играли (``chess`` / ``lichess``)
- ``yourself`` - ваше <b>ФИО</b>
- ``opponent`` - только <b>Фамилия и Имя</b> вашего оппонента
- ``your_id`` - номер вашего студака
- ``tour`` - шахматный тур, в котором вы участвуете
- ``date`` - дата проведения партий

<b>Обращаю ваше внимание</b> на то, что при некорректном заполнении полей ``.env`` скрипт может испытать внештатную ситуацию при работе, что влечёт за собой непредвиденные последствия.

## Связь с разработчиком
- [VK](https://vk.com/stepanviolet)
- stepanviolet@gmail.com
