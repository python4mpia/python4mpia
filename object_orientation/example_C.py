class Star(object):
    def __init__(self, name, RA, dec, Jmag, Hmag, Kmag, SpT):
        self.__name = name
        self.__RA = RA
        self.__dec = dec
        self.__Jmag = Jmag
        self.__Hmag = Hmag
        self.__Kmag = Kmag
        self.__SpT = SpT
        self.__Av = 0.0

    # The following functions return values for internal variables
    def getName(self):
        return self.__name
    
    def get_RA(self, segFlag=False):
        if segFlag:
            hours = int(self.__RA/15)
            minutes = int((self.__RA-hours*15)*60/15)
            seconds = (self.__RA-hours*15.0-minutes/60.0*15.0)*3600/15
            return (hours, minutes, seconds)
        else:
            return self.__RA

    def getRA(self):
        return self.__RA

    def getdec(self):
        return self.__dec

    def getJmag(self):
        return self.__Jmag

    def getHmag(self):
        return self.__Hmag

    def getKmag(self):
        return self.__Kmag

    def getSpT(self):
        return self.__SpT

    def getAv(self):
        return self.__Av

    # The following functions set/modify values for internal variables
    def setName(self, name):
        self.__name = name

    def setRA(self, RA):
        self.__RA = RA

    def setdec(self, dec):
        self.__dec = dec

    def setJmag(self, Jmag):
        self.__Jmag = Jmag

    def setHmag(self, Hmag):
        self.__Hmag = Hmag

    def setKmag(self, Kmag):
        self.__Kmag = Kmag

    def setSpT(self, SpT):
        self.__SpT = SpT
    
    # The following functions perform internal calculations
    def computeReddening(self):
        self.__Av = calcReddening(self.__Jmag, self.__Hmag, self.__Kmag, self.__SpT)

    def __repr__( self ):
        return '%s: %f' % (self.__name, self.__RA)

    def __lt__(self, other):
        if isinstance(other, float):
            return self.__RA < other
        else:
            return self.__RA < other.__RA


star_list = []

starA = Star('TWHya', 165.46625, -34.7047, 8.2, 7.6, 7.3, 'K7V')
star_list.append(starA)

starB = Star('AlphaBoo', 213.91529, 19.1824, -2.25, -2.81, -2.91, 'K1III')
star_list.append(starB)

starC = Star('TTauri', 65.495, 19.535, 7.24, 6.24, 5.32, 'G5V')
star_list.append(starC)


