
def pretend_to_read(file):
    return f"File content {file}..."

class Something:
    def __init__(self, data=None):
        self.data = data

    @classmethod
    def data_from_txtfile(cls, file):
        data = pretend_to_read(file)
        return cls(data=data)

    @classmethod
    def data_from_excelfile(cls, file):
        data = pretend_to_read(file)
        return cls(data=data)

    @classmethod
    def data_from_csvfile(cls, file):
        data = pretend_to_read(file)
        return cls(data=data)


something = Something.data_from_excelfile("xls")
print(something.data)

something = Something.data_from_txtfile("txt")
print(something.data)
