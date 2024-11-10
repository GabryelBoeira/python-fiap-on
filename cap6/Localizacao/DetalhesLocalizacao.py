from pygeocoder import Geocoder

api_key = ''

endereco = "Av. Paulista, 1000"
geocode = Geocoder(api_key).geocode(endereco)

print("Coordenadas: ", geocode)
print("Coordenadas: ", geocode.coordinates)
print("CEP: ", geocode.postal_code)
print("Logradouro: ", geocode.route)
print("numero: ", geocode.street_number )
print("Cidade: ", geocode.province)
print("Estado: ", geocode.state)
print("Pais: ", geocode.country)





