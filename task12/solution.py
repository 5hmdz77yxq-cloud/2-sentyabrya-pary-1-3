class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for row in data:
            values = row.split()
            record = dict(zip(self.FIELDS, values))
            self.lst_data.append(record)

    def select(self, a, b):
        if not self.lst_data:
            return []
        b = min(b, len(self.lst_data)-1)
        return self.lst_data[a:b+1]
