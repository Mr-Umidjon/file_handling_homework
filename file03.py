def main(data: str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    res = []
    for i in data:
        if i.isdigit():
            res.append(i)
    return res

# Read data from file
