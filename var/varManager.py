
import varPool as pool
import error.var as varErr

class VarManager:
    
    def __init__(self) -> None:
        self.__pools:list = []
        self.__currentScope = 0
        # Create a default global scope pool
        gScope = pool.VarPool()
        self.__pools.append(gScope)
        pass
    
    def removeScope(self):
        if len(self.__pools) == 1:
            return
        self.__pools.pop()
        self.__currentScope -= 1
        
    def addScope(self):
        newScope = pool.VarPool()
        self.__pools.append(newScope)
        self.__currentScope += 1
        
    def getValue(self, name):
        for scopePool in reversed(self.__pools):
            result = scopePool.getValue(name)
            if result[0] == True:
                return result[1]
        raise varErr.VarNotExistError
    
    def createVar(self, name, value):
        self.__pools[self.__currentScope].createNewVar(name, value)
        
    def removeVar(self, name):
        self.__pools[self.__currentScope].removeVariable(name)
        
    def modifyVar(self, name, newValue):
        for scopePool in reversed(self.__pools):
            result = scopePool.getValue(name)
            if result[0] == True:
                scopePool.modifyVariable(name, newValue)
                return
        raise varErr.VarNotExistError