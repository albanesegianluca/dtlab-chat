from enum import Enum

# Result è un'enumerazione. Serve a rendere più leggibile il codice. Ad esempio, 
# potrei far ritornare 2 quando un utente non viene trovato, ma questo sarebbe poco leggibile. 
# In python, le enumerazioni sono un particolare tipo di classe che ereditano da Enum.
class Result(Enum):
    OK = 1
    NOT_FOUND = 2 
    NOT_AUTHORIZED = 3
    DUPLICATED = 4
    EMPTY_MESSAGE = 5
    GENERIC_ERROR = 6
