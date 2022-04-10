def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data, 'r')
    res = []
    for i in f.read():
        if i.isdigit():
            res.append(int(i))
    return res

# Read data from file