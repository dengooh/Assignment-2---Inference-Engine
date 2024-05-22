import sys


class ParseFile:
    def __init__(self):
        self.filename = sys.argv[1]
        self.method = sys.argv[2]

    def getMethod(self):
        return self.method

    def TellData(self):
        with open(self.filename, "r") as file:

            first_line = file.readline().strip()
            
            if first_line == "TELL":
                kb_line = file.readline().strip()
                kb_data = kb_line.split(";")
                kb_data_line = list(filter(None, kb_data))
                
            else:
                return None
            
        return kb_data_line
    
    def QueryData(self):
        with open(self.filename, "r") as file:
            
            next(file)
            next(file)
            next(file)
            
            query_file = file.readline().strip()
                
        return query_file