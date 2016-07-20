import requests
import hashlib


class PachuMarvel(object):
	""" Ingresa tu llaves publica primero y luego privada, si no se Ingresa
		el programa utilizara unas por default """

	def __init__(self, public_key = '07fc4e914e525403435cf8f9921a87c2', private_key = '2c789ef81330386c206d729211769a7d42590d0a'):
		self.public_key = public_key
		self.private_key = private_key
		ts = '1'
		self.ha = hashlib.md5((ts+self.private_key+self.public_key).encode()).hexdigest()
		self.url = 'http://gateway.marvel.com/v1/public/'

		#aqui ponemos vacios los datos del superH
		self.nombre = ''
		self.descripcion = ''
		self.img = ''
		self.personaje = None
		self.id = ''
		#Datos del comic por id
		self.comicId = ''
		self.tituloComicId = ''
		self.descripcionComicId = ''
		self.imgComicId = ''

	def get_personaje(self, nombre='hulk'):
		""" Escribe el nombre del personaje corretamente"""
		try:
			self.personaje = requests.get(
				self.url+'characters',
    				params={
    					'apikey': self.public_key,
    					'ts': '1',
    					'hash': self.ha,
    					'name': nombre
    				}).json()
			self.nombre = nombre
			self.descripcion = self.personaje['data']['results'][0]['description']
			extensionPersonje = self.personaje['data']['results'][0]['thumbnail']['extension']
			imgPersonaje = self.personaje['data']['results'][0]['thumbnail']['path']
			self.img = imgPersonaje+'.'+extensionPersonje
			print('echo')
		except:
			print('Escribe bien')

	def get_response(self):
		""" Este metodo solo puede ser llamado despues de get_personaje"""
		try:
			print(self.personaje)
		except:
			print('Algo paso ........|.')

	def get_id(self):
		""" Este metodo setea el id del personaje """
		try:
			self.id = self.personaje['data']['results'][0]['id']
			print(self.id)
		except:
			print('llama primero get_personaje')

	def get_comic_id(self, numId = "41531"):
		"""Regresa datos del comic por el Id"""
		try:
			self.comicId = requests.get(
			self.url+'comics',
			params={
				'apikey': self.public_key,
				'ts': '1',
				'hash': self.ha,
				'id': numID,
			}).json()

			self.tituloComicId = self.comicId['data']['results'][0]['title']
			self.descripcionComicId = self.comicId['data']['results'][0]['description']
			extensionComic = self.comicId['data']['results'][0]['thumbnail']['extension']
			imagenComic = self.comicId['data']['results'][0]['thumbnail']['path']
			self.imgComicId = imgComicId+extensionComic
			print('take me to the place a love!!!')
		except:
			print(':( ID no valido')
