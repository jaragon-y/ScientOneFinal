class Fecha():

    def __init__(self, mes="", anio=""):
        self._mes = mes
        self._anio = anio

    def __iter__(self):
        yield ('mes', self._mes)
        yield ('anio', self._anio)

    def setMes(self,mes):
        self._mes = mes

    def getMes(self):
        return self._mes

    def setAnio(self,anio):
        self._anio = anio

    def getAnio(self):
        return self._anio

    def to_string(self):
        return str(self._mes) + " /" + str(self._anio)

    def toJSON(self):

        return {
            "mes" : self._mes,
            "anio" : self._anio
        }
