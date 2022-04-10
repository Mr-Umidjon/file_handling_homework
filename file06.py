def main(data: str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    res = []
    for i in data.split("\n"):
        res.append(len(i))
    return res


# Read data from file

f = open('txt_file/data06.txt', 'r')
print(main(f.read()))
f.close()
