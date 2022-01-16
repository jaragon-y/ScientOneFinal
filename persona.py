import json

class Persona:
    nombre = ''
    trabajos = []
    universidades = []
    colegios = []
    ubicaciones = []
    contactos = []
    links = []
    relacion = None
    familiares = []
    
    def add_trabajo(self,trabajo):
        self.trabajos.append(trabajo)

    def add_universidad(self,universidad):
        self.universidades.append(universidad)
    
    def add_colegio(self,colegio):
        self.colegios.append(colegio)

    def add_ubicacion(self,ubicacion):
        self.ubicaciones.append(ubicacion)

    def add_contacto(self,contacto):
        self.contactos.append(contacto)
    
    def add_link(self,link):
        self.links.append(link)

    def add_relacion(self,relacion):
        self.relacion = relacion

    def add_familiar(self,familiar):
        self.familiares.append(familiar)

    def toJSON(self):
        return {
            "nombre" : self.nombre,
            "trabajos" : self.trabajos,
            "universidades": self.universidades,
            "colegios": self.colegios,
            "ubicaciones": self.ubicaciones,
            "contactos": self.contactos,
            "links": self.links,
            "relacion": self.relacion,
            "familiares": self.familiares,
        }

