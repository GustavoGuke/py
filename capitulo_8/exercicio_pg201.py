print('Exercicio 8.6')
print('Nomes de Cidade, função deve aceitar nome de uma cidade e pais.')


def city_country(city, country):
    formated = city + ', ' + country
    return formated


city = city_country('Aruja', 'Brasil')
print(city)
print('...')
print('\n\n')
# ==============================================================================
print('Devolver um dicionario')


def make_album(artista, album):
    make = {'artista': artista, 'album': album}
    return make


albuns = make_album('Michael Jackson', 'Vagalume')
print(albuns)
