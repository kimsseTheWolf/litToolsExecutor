import error.var as varError

class VarUnit:
    
    def __init__(self, name, value) -> None:
        self.__name = name
        self.__value = value
        self.__isConstant = False
        pass
    
    def __init__(self, name, value, isConstant):
        self.__name = name
        self.__value = value
        self.__isConstant = isConstant
        pass
    
    def getName(self):
        return self.__name
    
    def getValue(self):
        return self.__value
    
    def setValue(self, value):
        if not self.__isConstant:
            self.__value = value
            return
        else:
            raise varError.UnsignableVariableError
