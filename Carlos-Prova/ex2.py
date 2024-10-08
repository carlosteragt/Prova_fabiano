def calcular_media_temperaturas(cidades_temperaturas):
    medias_cidades = []
    
    for cidade, temperaturas in cidades_temperaturas:
        media = sum(temperaturas) / len(temperaturas)
        medias_cidades.append((cidade, media))
    
    return medias_cidades

cidades_temperaturas = [
    ("São Paulo", [22.0, 23.0, 21.0, 24.0, 22.0, 23.0, 25.0]),
    ("Rio de Janeiro", [26.0, 27.5, 25.5, 28.0, 26.5, 29.0, 30.0]),
    ("Curitiba", [19.0, 18.5, 20.0, 21.0, 19.5, 20.5, 18.0])
]

resultado = calcular_media_temperaturas(cidades_temperaturas)
print(resultado)

