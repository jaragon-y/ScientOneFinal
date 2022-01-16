from DTO import FechaDto


class Educacion():

    def __init__(self, nombre, campo, fechaini=FechaDto.Fecha(), fechafin=FechaDto.Fecha):
        self._nombre = nombre
        self._campo = campo
        self._fechaini = fechaini
        self._fechafin = fechafin

    def setFechaIni(self, fechaIni):
        self._fechaini = fechaIni

    def setFechaFin(self, fechaFin):
        self._fechafin = fechaFin

    def toJSON(self):

        return {
            "nombre" : self._nombre,
            "campo": self._campo,
            "fechaini": self._fechaini.toJSON(),
            "fechafin": self._fechafin.toJSON(),
        }
