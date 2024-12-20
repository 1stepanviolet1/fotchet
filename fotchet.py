from otchettable import OtchetTable
from parser import Parser


def make_otchettable( # recommended builder
    data1: dict[list[str]],
    data2: dict[list[str]],
    *, 
    student_id: str,
    fio: str,
    tour: str,
    date: str,
    your_name: str,
    opponent_name: str
) -> OtchetTable:
    table = OtchetTable()

    table.make_intro(
        student_id=student_id, 
        fio=fio
    )

    table.make_1_battle(data1,
        tour=tour,
        date=date,
        your_name=your_name, 
        opponent_name=opponent_name
    )

    table.make_2_battle(data2,
        tour=tour,
        date=date,
        your_name=your_name,
        opponent_name=opponent_name
    )

    return table


def main():
    import os
    import dotenv as _env

    _env.load_dotenv()
    config = _env.dotenv_values(".env")

    try:
        data1 = Parser(
            os.path.join('data', config.get("1_filename")), 
            platform=config.get("platform"),
            translate_en_into_ru=config.get("translate_en_into_ru")
        ).parse()

        data2 = Parser(
            os.path.join('data', config.get("2_filename")),
            platform=config.get("platform"),
            translate_en_into_ru=config.get("translate_en_into_ru")
        ).parse()

    except Exception:
        print("Error: у вас проблема с получением/парсингом входных данных")
        print()
        raise err

    table = make_otchettable(data1, data2,
        student_id=config.get("your_id"),
        fio=config.get("yourself"),
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
        print(f"Error: у вас возникла следующая ошибка, cвяжитесь с разработчиком.")
        print()
        raise err
