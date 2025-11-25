def IsGoodType(Value, Type) -> bool:
    """
    Return True if the value has the right type.
    Type being the type you want the value to be.
    """
    return type(Value) == Type
    
def IsEqual(Value1, Value2) -> bool:
    """
    Return True if the first value is equal to the second.
    """
    return Value1 == Value2

def IsGreater(Value1, Value2) -> bool:
    """
    Return True if the first value is strictly greater than the second.
    """
    return Value1 > Value2

def FirstElementEqual(List, Value) -> None:
    """
    Return True if the first element of the List is equal to the Value.
    """
    return List[0] == Value

def IsBetween(Min, Value, Max) -> bool:
    """
    Return True if the Value is between the Min and Max.
    """
    return Min <= Value and Max >= Value
