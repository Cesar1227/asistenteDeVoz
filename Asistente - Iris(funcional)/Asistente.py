import pyttsx3 as voz


asistente=voz.init()
velocidad = asistente.getProperty('rate')
asistente.setProperty('rate', velocidad-20)
asistente.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')


class talk():
	"""docstring for talk"""
	salir='finaliza el programa'
	name='iris'
	
	def __init__(self):
		super(talk,self).__init__()

	def hablar(self,texto):
		asistente.say(texto)
		asistente.runAndWait()