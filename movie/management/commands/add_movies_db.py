from django.core.management.base import BaseCommand
from movie.models import Movie
import os
import json

class Command(BaseCommand):
    help = 'Load movies from movie_descriptions.json into the Movie model'

    def handle(self, *args, **kwargs):
        json_file_path = 'movie/management/commands/movies.json'

        with open('movie/management/commands/movies.json', 'r', encoding='utf-8') as file:
         movies = json.load(file)

        for i in range(100):
            movie = movies[i]
            exist = Movie.objects.filter(title=movie['title']).first()
            if not exist:
                # Toma el primer campo no vacío entre 'fullplot', 'plot' o usa 'Sin descripción'
                desc = (movie.get('fullplot') or '').strip() or (movie.get('plot') or '').strip() or 'Sin descripción'
                Movie.objects.create(
                    title=movie['title'],
                    image='movie/images/default.JPG',  # Corrige la extensión a .JPG
                    genre=movie['genre'],
                    year=movie['year'],
                    description=desc,
                )