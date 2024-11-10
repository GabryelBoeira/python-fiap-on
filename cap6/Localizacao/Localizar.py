from pygeocoder import Geocoder

api_key = ''

endereco = "Av. Paulista, 1000, Sao Paulo, SP"
print("Coordenadas: ", Geocoder(api_key).geocode(endereco).coordinates)
