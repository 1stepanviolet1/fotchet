cimport cython
from cython cimport final


import re


@final
cdef class Parser:
    cdef str _sep
    cdef object _isPgn 
    cdef str _translate_en_into_ru

    cdef readonly str data

    def __cinit__(Parser self):
        self._isPgn = False

    def __init__(Parser self, str filename, *, str platform, str translate_en_into_ru = ''):
        if platform == 'chess': 
            self._sep = ' '
        elif platform == 'lichess': 
            self._sep = '\n'
        else: 
            raise ValueError(f'This type of input data is not provided: {platform}')
        
        if translate_en_into_ru == '': self._translate_en_into_ru = "0"
        else: self._translate_en_into_ru = translate_en_into_ru

        self._isPgn = filename[-4:] == ".pgn"

        with open(filename, 'r', encoding='utf-8') as fp:
            self.data = fp.read()

    cdef change_local(Parser self):
        cdef dict table = {
            "N": "К",
            "B": "C",
            "R": "Л",
            "K": "Кр",
            "Q": "Ф"
        }

        cdef list result = list(self.data)

        cdef str literal
        for literal in result:
            if literal in table:
                result[result.index(literal)] = table[literal]

        self.data = "".join(result)

    cdef preprocess_data_from_pgn(Parser self):
        self._sep = ' '
        cdef list moves = []
        cdef list lines = self.data.split('\n')
        
        moves_re = re.compile(r'(\d+\.\s+\S+\s+\S+)')

        cdef str line
        for line in lines:
            moves_match = moves_re.findall(line)

            if not moves_match:
                continue

            for move in moves_match:
                moves.append(move.strip())

        self.data = " ".join(moves)

    cpdef dict parse(Parser self) except *:
        if self._translate_en_into_ru != "0":
            self.change_local()

        if self._isPgn:
            self.preprocess_data_from_pgn()

        return self.parse_data(self.data, self._sep)

    cpdef dict parse_data(Parser self, str data, str sep) except *:
        cdef list _data = data.split(sep)
        cdef dict res = {
            'white': [],
            'black': []
        }

        cdef size_t i
        cdef str v
        for i, v in enumerate(_data):
            if not (i % 3):
                continue
            elif i % 3 == 1:
                res['white'].append(v)
            elif i % 3 == 2:
                res['black'].append(v)
            else:
                raise ArithmeticError("Остаток от деления на 3, отличный от 0, 1, 2 :)")

        return res

# type: ignore
