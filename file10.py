def main(data: str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    res = 0
    for i in data.split("\n"):
        i = len(i)
        if i > res:
            res = i
    return res


# Read data from file
f = open('txt_file/data10.txt', 'r')
print(main(f.read()))
f.close()
