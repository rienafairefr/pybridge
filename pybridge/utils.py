from datetime import date


def string_concat(*arg):
    #return u''.join([str(el) for el in list(arg)])

    list1 = []
    for el in list(arg):
        if type(el) == str:
            list1.append(el)
        else:
            if type(el) == list:
                list1.append(string_concat('[', ','.join(map(string_concat, el)), ']'))
            else:
                list1.append(str(el))
    return u''.join(list1)


class Bunch:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

    def __str__(self):
        return self.__dict__.__str__()

    def __repr__(self):
        return object.__repr__(self) + self.__dict__.__repr__()


class DateMonth(date):
    def __new__(typ,year,month):
        obj = date.__new__(typ,year=year,month=month,day=1)
        return obj


def copy_dict(source_dict, diffs):
    """Returns a copy of source_dict, updated with the new key-value
       pairs in diffs."""
    result=dict(source_dict) # Shallow copy, see addendum below
    result.update(diffs)
    return result