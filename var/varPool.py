
import varUnit
import error.var as varErr
# Single scope of variable storing pool

class VarPool:
    
    def __init__(self) -> None:
        self.__scopePool:list = []
        pass
    
    # Find a var's location in the list. If not exist then return -1
    def __findElement(self, eleName):
        for i in range(len(self.__scopePool)):
            if self.__scopePool[i].getName() == eleName:
                return i
        
        return -1
    
    def createNewVar(self, name, value):
        if self.__findElement(name) != -1:
            # Means the target element already existed! Raise an error
            raise varErr.VarAlreadyExistError
        newVar = varUnit(name, value)
        self.__scopePool.append(newVar)
        pass
        
    def modifyVariable(self, name, newValue):
        varLoc = self.__findElement(name)
        if varLoc == -1:
            return False
        self.__scopePool[varLoc].setValue(newValue)
        return True
    
    def removeVariable(self, name):
        varLoc = self.__findElement(name)
        if varLoc == -1:
            return False
        self.__scopePool.remove(self.__scopePool[varLoc])
        return True
    
    def getValue(self, name):
        varLoc = self.__findElement(name)
        if varLoc == -1:
            return (False, None)
        result = self.__scopePool[varLoc].getValue()
        return (True, result)
