def main(data: str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    res = [0, 0]
    for i in data:
        if i.isdigit():
            res[0] += 1
        else:
            res[1] += 1
    return res


# Read data from file

f = open('txt_file/data05.txt', 'r')
print(main(f.read()))
f.close()