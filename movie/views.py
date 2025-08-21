from django.shortcuts import render
from django.http import HttpResponse
from .models import Signup
from .models import Movie
import matplotlib.pyplot as plt
import matplotlib
import urllib, base64
import io
matplotlib.use('Agg')

def statistics_view(request):
    # --- Movies per year ---
    all_movies = Movie.objects.all()
    movie_counts_by_year = {}
    for movie in all_movies:
        year = movie.year if movie.year else "None"
        movie_counts_by_year[year] = movie_counts_by_year.get(year, 0) + 1

    bar_positions_year = range(len(movie_counts_by_year))
    plt.bar(bar_positions_year, movie_counts_by_year.values(), align='center')
    plt.title('Movies per year')
    plt.xlabel('Year')
    plt.ylabel('Number of movies')
    plt.xticks(bar_positions_year, movie_counts_by_year.keys(), rotation=90)
    plt.tight_layout()
    buffer_year = io.BytesIO()
    plt.savefig(buffer_year, format='png')
    buffer_year.seek(0)
    graphic_year = base64.b64encode(buffer_year.getvalue()).decode('utf-8')
    buffer_year.close()
    plt.close()

    # --- Movies per genre ---
    genre_counts = {}
    for movie in all_movies:
        if movie.genre:
            first_genre = movie.genre.split(',')[0].strip()
            genre_counts[first_genre] = genre_counts.get(first_genre, 0) + 1

    bar_positions_genre = range(len(genre_counts))
    plt.bar(bar_positions_genre, genre_counts.values(), align='center')
    plt.title('Movies per genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of movies')
    plt.xticks(bar_positions_genre, genre_counts.keys(), rotation=45)
    plt.tight_layout()
    buffer_genre = io.BytesIO()
    plt.savefig(buffer_genre, format='png')
    buffer_genre.seek(0)
    graphic_genre = base64.b64encode(buffer_genre.getvalue()).decode('utf-8')
    buffer_genre.close()
    plt.close()

    return render(request, 'statistics.html', {
        'graphic_year': graphic_year,
        'graphic_genre': graphic_genre,
    })

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Welcome to Home Page</h1>")
    #return render(request, 'home.html', {'name': 'Anyela Jimenez'})
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else: 
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies})

def about(request):
    return HttpResponse("<h1>Welcome to about page</h1>")


from django.shortcuts import render, redirect
from .models import Signup

def signup(request):
    email = None
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            Signup.objects.get_or_create(email=email)
            return render(request, 'signup.html', {'email': email})
    return render(request, 'signup.html')