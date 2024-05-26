

class Parser:
    def __init__(self, filename="data.txt") -> None:
        with open(filename, 'r', encoding='utf-8') as fp:
            self.data = fp.read()
    
    def parse(self, *, var: int) -> list[str]:
        match var:
            case 1: return self.parse_1var(self.data)
            case 2: return self.parse_2var(self.data)
            case _: raise ValueError(f"var must be 1 or 2, not {var}")
    
    @staticmethod
    def parse_1var(data: str) -> list[str]:
        ...
    
    @staticmethod
    def parse_2var(data: str) -> dict[list[str]]:
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
