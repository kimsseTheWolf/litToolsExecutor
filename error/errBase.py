
class CustomError(Exception):
    
    def __init__(self, ErrInfo) -> None:
        self.ErrInfo = ErrInfo
        super().__init__(ErrInfo)
        
    def __str__(self) -> str:
        return self.ErrInfo