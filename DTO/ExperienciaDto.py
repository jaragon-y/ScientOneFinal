from DTO import FechaDto


class Experiencia:

    def __init__(self, location, nombreempresa, cargo,
                 fechaini=FechaDto.Fecha(), fechafin=FechaDto.Fecha(),
                 industria=list()):
        self._locacion = location
        self._nombreempresa = nombreempresa
        self._cargo = cargo
        self._fechaini = fechaini
        self._fechafin = fechafin
        self._industria = industria

    def getLocation(self):
        return self._locacion

    def getNombreEmpresa(self):
        return self._nombreempresa

    def getCargo(self):
        return self._cargo

    def getFechaIni(self):
        return self._fechaini

    def getFechaFin(self):
        return self._fechafin

    def getIndustria(self):
        return self._industria

    def print(self):
        print(" -Empresa : " + self._nombreempresa)
        print(" -Ubicacion : " + self._locacion)
        print(" -Cargo : " + self._cargo)
        print(" -Fecha Inicio : " + self._fechaini.to_string())
        print(" -Fecha Fin : " + self._fechafin.to_string())
        for i in self._industria:
            print("   -Industrias relacionadas : " + i)

    def toJSON(self):

        return {
            "location" : self._locacion,
            "nombreempresa" : self._nombreempresa,
            "cargo": self._cargo,
            "fechaini": self._fechaini.toJSON(),
            "fechafin": self._fechafin.toJSON(),
            "industria": self._industria
        }
