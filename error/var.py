
import error.errBase as errBase

class UnsignableVariableError(Exception):
    
    def __init__(self) -> None:
        super().__init__(self)
        
    def __str__(self) -> str:
        return "Unassignable variable: constant"
    
class VarAlreadyExistError(errBase.CustomError):
    
    def __init__(self, ErrInfo = "Variable already exists!") -> None:
        super().__init__(ErrInfo)
        
class VarNotExistError(errBase.CustomError):
    
    def __init__(self, ErrInfo = "Variable does not exists!") -> None:
        super().__init__(ErrInfo)