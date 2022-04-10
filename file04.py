def main(data: str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    res = []
    for i in data:
        if not i.isdigit():
            res.append(i)
    return res


# Read data from file
f = open('txt_file/data04.txt', 'r')
print(main(f.read()))
