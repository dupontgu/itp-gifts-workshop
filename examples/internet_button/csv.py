class CsvReader:
    def __init__(self, file):
        with open(file) as f:
            lines = f.readlines()
            self.headers = [l.strip() for l in lines[0].split(',')]
            self.rows = lines[1:]

    def __getitem__(self, index):
        row = [i.strip() for i in self.rows[index].split(',')]
        output = {}
        for (i, h) in enumerate(self.headers):
            output[h] = row[i]
        return output