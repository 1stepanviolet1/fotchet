

class Parser:
    def __init__(self, filename: str) -> None:
        with open(filename, 'r', encoding='utf-8') as fp:
            self.data = fp.read()
    
    def parse(self, *, sep: str) -> dict[list[str]]:
        return self.parse_data(self.data, sep=sep)
    
    @staticmethod
    def parse_data(data: str, *, sep: str) -> dict[list[str]]:
        data = data.split('\n')
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
