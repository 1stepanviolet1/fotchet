from otchettable import OtchetTable
import os

import dotenv as _env

_env.load_dotenv()
config = _env.dotenv_values(".env")


table = OtchetTable()
table.make_intro(
    student_id=config.get("your_id"),
    fio=config.get("yourself")
)

table.save(
    os.path.join('data', config.get("output_filename"))
)

table.close()
