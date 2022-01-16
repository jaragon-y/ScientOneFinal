class Profile():

    def __init__(self,descripcion, nombres, apellidos,
                 locacion, headline, educacion,skills,
                 experiencia):
        self._descripcion = descripcion
        self._nombres = nombres
        self._apellidos = apellidos
        self._locacion = locacion
        self._headline = headline
        self._educacion = educacion
        self._skills = skills
        self._experiencia = experiencia

    def toJSON(self):

        return {
            "descripcion" : self._descripcion,
            "nombres" : self._nombres,
            "apellidos" : self._apellidos,
            "locacion" : self._locacion,
            "headline" : self._headline,
            "educacion" : self._educacion,
            "skills" : self._skills,
            "experiencia" : self._experiencia,
        }

