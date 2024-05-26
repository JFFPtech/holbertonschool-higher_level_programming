document.addEventListener('DOMContentLoaded', function () {
    const listMovies = document.getElementById('list_movies');
    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
