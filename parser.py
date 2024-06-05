import re
class Parser:
    def __init__(self, filename: str, *, platform: str) -> None:
        self._sep: str
        self._isPgn: False
        match platform:
            case 'chess':
                self._sep = ' '
            case 'lichess':
                self._sep = '\n'
            case _:
                raise ValueError(f'This type of input data is not provided: {platform}')

        if filename[-4:] == ".pgn":
            self._isPgn = True
            self._sep = ' '

        with open(filename, 'r', encoding='utf-8') as fp:
            self.data = fp.read()

    def change_local(self):
        table = {
            "N": "К",
            "B": "C",
            "R": "Л",
            "K": "Кр",
            "Q": "Ф"
        }

        result = list(self.data)
        for literal in result:
            if literal in table:
                result[result.index(literal)] = table[literal]

        self.data = "".join(result)

    def parse_pgn(self):
        moves = []

        lines = self.data.split('\n')
        moves_re = re.compile(r'(\d+\.\s+\S+\s+\S+)')

        for line in lines:
            moves_match = moves_re.findall(line)
            if moves_match:
                for move in moves_match:
                    moves.append(move.strip())

        self.data = " ".join(moves)

    def parse(self) -> dict[list[str]]:
        self.change_local()

        if self._isPgn:
            self.parse_pgn()

        return self.parse_data(self.data, sep=self._sep)

    @staticmethod
    def parse_data(data: str, *, sep: str) -> dict[list[str]]:
        data = data.split(sep)
        res = {
            'white': [],
            'black': []
        }

        for i, v in enumerate(data):
            match i % 3:
                case 0:
                    continue
                case 1:
                    res['white'].append(v)
                case 2:
                    res['black'].append(v)

        return res

# type: ignore
