"""
Usage::

    from unpack import Unpack
"""
class Unpack:
    """
    * Unpack a dictionary into a class with the dictionary's keys as members.
    * Unpack a list into a class with `.items` as a member that contains the list's members

    .. testsetup:: *

        from unpack import Unpack

    .. doctest::

        >>> v = Unpack({"a": "one", "b": "two"})

        >>> v.a
        'one'
    """
    def __init__(self, data):
        unpackedData = self._unpack(data)
        if isinstance(unpackedData, dict):
            self.__dict__.update(unpackedData)
        elif isinstance(unpackedData, list):
            self.__dict__.update({'items': unpackedData})

    def __repr__(self):
        return "Unpack({contents})".format(contents=self.__dict__)

    def _create(self, data):
        if isinstance(data, dict):
            return Unpack(data)

        if isinstance(data, list):
            if data != [] and isinstance(data[0], dict):
                return list(map(lambda x: Unpack(x), data))

        return data

    def _unpack(self, data):
        if isinstance(data, dict):
            for key in data:
                data[key] = self._create(data[key])

        elif isinstance(data, list):
            data = self._create(data)

        return data
