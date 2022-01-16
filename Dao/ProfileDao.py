from linkedin_api import Linkedin


def getProfile(cuenta, contrasenia,persona):

    api = Linkedin(cuenta, contrasenia)

    #api = Linkedin('theterx118@gmail.com', '2102jaay')
    #test-test-a3049122b
    #alonsoaguinaga
    #marcomartinezlinares

    profile = api.get_profile(persona)

    return profile
