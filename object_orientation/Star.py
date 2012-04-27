class StarObject(object):
    def __init__(self, name, RA, dec, Jmag, Hmag, Kmag, SpT):
        self.name = name
        self.RA = RA
        self.dec = dec
        self.Jmag = Jmag
        self.Hmag = Hmag
        self.Kmag = Kmag
        self.SpT = SpT
        self.Av = 0.0

    # The following functions return values for internal variables
    def getName(self):
        return self.name
    
    def getRA(self):
        return self.RA

    def getdec(self):
        return self.dec

    def getJmag(self):
        return self.Jmag

    def getHmag(self):
        return self.Hmag

    def getKmag(self):
        return self.Kmag

    def getSpT(self):
        return self.SpT

    def getAv(self):
        return self.Av

    # The following functions set/modify values for internal variables
    def setName(self, name):
        self.name = name

    def setRA(self, RA):
        self.RA = RA

    def setdec(self, dec):
        self.dec = dec

    def setJmag(self, Jmag):
        self.Jmag = Jmag

    def setHmag(self, Hmag):
        self.Hmag = Hmag

    def setKmag(self, Kmag):
        self.Kmag = Kmag

    def setSpT(self, SpT):
        self.SpT = SpT
    
    # The following functions perform internal calculations
    def computeReddening(self):
        self.Av = calcReddening(self.Jmag, self.Hmag, self.Kmag, self.SpT)
        return self.Av

    def __repr__( self ):
        return '%s: %f' % (self.name, self.RA)

    def __lt__(self, other):
        if isinstance(other, float):
            return self.RA < other
        else:
            return self.RA < other.RA

    def __gt__(self, other):
        if isinstance(other, float):
            return self.RA > other
        else:
            return self.RA > other.RA

    def __le__(self, other):
        if isinstance(other, float):
            return self.RA <= other
        else:
            return self.RA <= other.RA

    def __ge__(self, other):
        if isinstance(other, float):
            return self.RA >= other
        else:
            return self.RA >= other.RA

    def __eq__(self, other):
        if isinstance(other, float):
            return self.RA == other
        else:
            return self.RA == other.RA
