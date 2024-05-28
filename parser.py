

class Parser:
    def __init__(self, filename: str, *, platform: str) -> None:
        self._sep: str
        match platform:
            case 'chess':
                self._sep = ' '
            case 'lichess':
                self._sep = '\n'
            case _:
                raise ValueError(f'This type of input data is not provided: {platform}')

        with open(filename, 'r', encoding='utf-8') as fp:
            self.data = fp.read()
    
    def parse(self) -> dict[list[str]]:
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
