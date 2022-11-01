def string_index(string: str, character: str, case=False) -> dict:
    """
    Function that takes a string and a given character and returns
    the number of times a character appears in a string and it's 
    indices.
    """
    
    if not case:
        string = string.lower()
        
    count = string.count(character)
    indices = [i for i, l in enumerate(string) if l == character]
            
    string_positions = {'character': character,
                        'indices': indices,
                        'count': count}
    
    return string_positions
