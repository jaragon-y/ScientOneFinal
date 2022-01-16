from Dao import ProfileDao
from DTO import ProfileDto, ExperienciaDto, EducacionDto, FechaDto
from Util import funciones


def getProfile(cuenta, contrasenia, persona):

    rawProfile = ProfileDao.getProfile(cuenta, contrasenia, persona)

    educacion = getEducacion(rawProfile)
    skills = getSkills(rawProfile)
    experiencia = getExperiencia(rawProfile)

    profile = ProfileDto.Profile(funciones.secureString(rawProfile.get('summary')),
                         funciones.secureString(rawProfile.get('firstName')),
                         funciones.secureString(rawProfile.get('lastName')),
                         funciones.secureString(rawProfile.get('locationName')),
                         funciones.secureString(rawProfile.get('headline')),
                         educacion,
                         skills,
                         experiencia)

    return profile.toJSON()

def getEducacion(rawProfile=None):

    education = list()

    if rawProfile is None:
        return education

    for ed in rawProfile.get('education'):
        fechaIni, fechaFin = funciones.getFechas(ed)
        educacion = EducacionDto.Educacion(funciones.secureString(ed.get('schoolName')),
                                 funciones.secureString(ed.get('fieldOfStudy')),
                                 fechaIni,
                                 fechaFin)
        education.append(educacion.toJSON())

    return education

    pre_exp = list()
    experiencia = list()
    skills = list()


def getSkills(rawProfile=None):

    skills = list()

    if rawProfile is None:
        return skills

    for s in rawProfile.get('skills'):
        skills.append(s.get('name'))

    return skills


def getExperiencia(rawProfile=None):

    experiencia = list()

    if rawProfile is None:
        return experiencia

    for e in rawProfile.get('experience'):
        company = e.get('company')
        fechaIni, fechaFin = funciones.getFechas(e)

        if company is not None:
            company = company.get('industries')
        else:
            company = list()

        e = ExperienciaDto.Experiencia(funciones.secureString(e.get('locationName')),
                                       funciones.secureString(e.get('companyName')),
                                       funciones.secureString(e.get('title')),
                                       fechaIni,
                                       fechaFin,
                                       company)
        experiencia.append(e.toJSON())

    return experiencia
