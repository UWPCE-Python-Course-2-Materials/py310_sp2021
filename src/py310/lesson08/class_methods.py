
def pretend_to_read(file):
    return f"doing an open {file}..."

class Something:
    def __init__(self, data=None):
        self.data = data

    @classmethod
    def data_from_txtfile(cls, file):
        # code here specific to txt
        data = pretend_to_read(f"{file}.txt")
        return cls(data=data)

    @classmethod
    def data_from_excelfile(cls, file):
        # code here specific to excel
        data = pretend_to_read(f"{file}.xlsx")
        return cls(data=data)

    @classmethod
    def data_from_csvfile(cls, file):
        # code here specific to csv
        data = pretend_to_read(f"{file}.csv")
        return cls(data=data)


something = Something.data_from_excelfile("hrdata")
print(something.data)

something = Something.data_from_txtfile("hrdata")
print(something.data)
