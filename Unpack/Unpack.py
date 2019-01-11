class Unpack:
    def __init__(self, data):
        unpacked_data = self._unpack(data)
        if type(unpacked_data) == dict:
            self.__dict__.update(unpacked_data)
        elif type(unpacked_data) == list:
            self.__dict__.update({'items': unpacked_data})

    def __repr__(self):
        return "Unpack({contents})".format(contents=self.__dict__)

    def _create(self, data):
        if type(data) == dict:
            return Unpack(data)
        elif type(data) == list:
            if data != [] and type(data[0]) == dict:
                return list(map(lambda x: Unpack(x), data))

        return data

    def _unpack(self, data):
        if type(data) == dict:
            for key in data:
                data[key] = self._create(data[key])

        elif type(data) == list:
            data = self._create(data)

        return data
