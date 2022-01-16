from DTO.FechaDto import Fecha


def secureString(value=None):

    if value is not None:
        return value
    else:
        return ""


def secureList(value=None):

    if value is not None:
        return value
    else:
        return list()


def getFechas(dictionary=dict()):

    periodo = dictionary.get('timePeriod')
    if periodo == None:
        return Fecha(),Fecha()

    ini = periodo.get('startDate')
    fin = periodo.get('endDate')
    fechaIni = Fecha()
    fechaFin = Fecha()
    if ini is not None:
        fechaIni.setMes(secureString(ini.get('month')))
        fechaIni.setAnio(secureString(ini.get('year')))

    if fin is not None:
        fechaFin.setMes(secureString(fin.get('month')))
        fechaFin.setAnio(secureString(fin.get('year')))

    return fechaIni, fechaFin

