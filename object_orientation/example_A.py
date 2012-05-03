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

    # The following functions perform internal calculations
    def computeReddening(self):
        self.__Av = calcReddening(self.__Jmag, self.__Hmag, self.__Kmag, self.__SpT)

star_list = []

starA = Star('TWHya', 165.46625, -34.7047, 8.2, 7.6, 7.3, 'K7V')
star_list.append(starA)

starB = Star('AlphaBoo', 213.91529, 19.1824, -2.25, -2.81, -2.91, 'K1III')
star_list.append(starB)

starC = Star('TTauri', 65.495, 19.535, 7.24, 6.24, 5.32, 'G5V')
star_list.append(starC)


