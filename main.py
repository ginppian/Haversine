import math
from math import radians
from typing import NamedTuple
from decimal import Decimal

R = 6371 # Radio de la tierra

class Coordenada(NamedTuple):
    latitud: Decimal
    longitud: Decimal

def Haversine(coordenada_origen: Coordenada, coordenada_destino: Coordenada):
    #print(coordenada_origen)
    #print(coordenada_destino)

    lat_dist = radians(coordenada_destino.latitud - coordenada_origen.latitud)
    lon_dist = radians(coordenada_destino.longitud - coordenada_origen.longitud)

    lat1 = radians(coordenada_origen.latitud)
    lat2 = radians(coordenada_destino.latitud)

    a = math.sin(lat_dist / 2) * math.sin(lat_dist / 2) + math.cos(lat1) * math.cos(lat2) * math.sin(
        lon_dist / 2) * math.sin(lon_dist / 2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    d = R * c

    return  d

monterrey_catedral = Coordenada(25.665850, -100.309511)
cdmx_catedral = Coordenada(19.434748, -99.133104)
austin_capitolio = Coordenada(30.274925, -97.740383)

mty_to_mx = Haversine(monterrey_catedral, cdmx_catedral)
mty_to_aus = Haversine(monterrey_catedral, austin_capitolio)

print("Distancia de Monterrey a CDMX", "{0:.2f}".format(mty_to_mx), "Kms")
print("Distancia de Monterrey a Austin", "{0:.2f}".format(mty_to_aus), "Kms")
