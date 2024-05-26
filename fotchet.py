from otchettable import OtchetTable
from parser import Parser # type: ignore
import os

import dotenv as _env

_env.load_dotenv()
config = _env.dotenv_values(".env")

sep: str
match config.get("input_var"):
    case 'chess':
        sep = ' '
    case 'lichess':
        sep = '\n'
    case _:
        raise ValueError(f'This type of input data is not provided: {config.get("input_var")}')

try:
    data1 = Parser(os.path.join('data', config.get("1_filename"))).parse(sep=sep)
    data2 = Parser(os.path.join('data', config.get("2_filename"))).parse(sep=sep)
except FileNotFoundError:
    print("Error: у вас проблема с получением/парсингом входных данных")
    exit(1)

def main():
    table = OtchetTable()

    table.make_intro(
        student_id=config.get("your_id"),
        fio=config.get("yourself")
    )

    table.make_1_battle(data1,
        tour=config.get("tour"),
        date=config.get("date"),
        your_name=' '.join(config.get("yourself").split()[:2]),
        opponent_name=config.get("opponent")
    )

    table.make_2_battle(data2,
        tour=config.get("tour"),
        date=config.get("date"),
        your_name=' '.join(config.get("yourself").split()[:2]),
        opponent_name=config.get("opponent")
    )

    table.save(
        os.path.join('data', config.get("output_filename"))
    )

    table.close()

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"Error: у вас возникла следующая ошибка:\n{err}\nСвяжитесь с разработчиком.")
