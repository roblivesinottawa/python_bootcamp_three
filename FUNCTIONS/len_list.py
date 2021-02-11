def lengthen_list(n, _list=None):
    if _list == None:
        _list = [1,2,3]
        _list.append(n)
        return _list

l = lengthen_list(4)
print(l)