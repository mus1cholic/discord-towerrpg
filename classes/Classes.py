class Classes:
    #this class contains information only about the classes, not about the user
    #who chose this class.
    #variables
    name = None
    idnum = None

    def __init__(self, name, idnum):
        self.name = name
        self.idnum = idnum

    def getId(self):
        return idnum