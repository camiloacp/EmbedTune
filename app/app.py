from autentication import sp
import pandas as pd

# Playlists populares de LATAM
playlists_latam = {
    'Top 50 México': '37i9dQZEVXbO3qyFxbkOE1',
    'Top 50 Argentina': '37i9dQZEVXbMMy2roB9myp',
    'Top 50 Colombia': '37i9dQZEVXbOa2GkKuHpJ6',
    'Top 50 Chile': '37i9dQZEVXbL0GavIqMTeb',
    'Top 50 Perú': '37i9dQZEVXbJfdy5b0KP7W',
}

generos = [
    'Reggaeton', 'Rock', 'Pop', 'Rap', 'Metal', 'Salsa', 'Cumbia', 
    'Norteña', 'Popular', 'Vallenato', 'House', 'Electronica', 'Indie'
]
playlist_encontradas = {}

for genero in generos:
    query = f'Top {genero}'
    results = sp.search(q=query, type='playlist', limit=5) 

    playlists = [p for p in results['playlists']['items'] if p is not None]

    print(f'\nResultados para la {query}:\n')
    for idx, playlist in enumerate(playlists, 1):
        print(f'{idx}.  {playlist['name']}')
        print(f'ID:     {playlist['id']}')
        print(f'Owner:  {playlist['owner']['display_name']}')
        print(f'Tracks: {playlist['tracks']['total']}')
        print(f'URL: {playlist['external_urls']['spotify']}')
        
        playlist_encontradas[playlist['name']] = playlist['id']

print(playlist_encontradas)
all_tracks = []

#for pais, playlist_id in playlists_encontradas

print("\nExtrayendo canciones...")