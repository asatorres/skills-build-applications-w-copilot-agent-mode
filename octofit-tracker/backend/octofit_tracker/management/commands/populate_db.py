

from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

# Datos de ejemplo
USERS = [
    {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
    {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
    {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
    {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
    {"name": "Spider-Man", "email": "spiderman@marvel.com", "team": "Marvel"},
    {"name": "Captain Marvel", "email": "captainmarvel@marvel.com", "team": "Marvel"},
]

TEAMS = [
    {"name": "Marvel", "description": "Equipo Marvel"},
    {"name": "DC", "description": "Equipo DC"},
]

ACTIVITIES = [
    {"user_email": "superman@dc.com", "activity": "Vuelo", "duration": 60},
    {"user_email": "batman@dc.com", "activity": "Entrenamiento", "duration": 45},
    {"user_email": "ironman@marvel.com", "activity": "Vuelo en armadura", "duration": 50},
    {"user_email": "spiderman@marvel.com", "activity": "Balanceo", "duration": 30},
]

LEADERBOARD = [
    {"user_email": "superman@dc.com", "score": 1000},
    {"user_email": "ironman@marvel.com", "score": 950},
    {"user_email": "batman@dc.com", "score": 900},
]

WORKOUTS = [
    {"name": "Entrenamiento de fuerza", "description": "Rutina de fuerza para superhéroes"},
    {"name": "Cardio extremo", "description": "Cardio para resistencia sobrehumana"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Eliminar datos existentes usando los modelos de Django
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Insertar datos de ejemplo usando los modelos de Django
        for team in TEAMS:
            Team.objects.create(**team)
        for user in USERS:
            User.objects.create(**user)
        for activity in ACTIVITIES:
            Activity.objects.create(**activity)
        for entry in LEADERBOARD:
            Leaderboard.objects.create(**entry)
        for workout in WORKOUTS:
            Workout.objects.create(**workout)

        self.stdout.write(self.style.SUCCESS('La base de datos octofit_db ha sido poblada con datos de prueba usando los modelos de Django.'))

        self.stdout.write(self.style.SUCCESS('La base de datos octofit_db ha sido poblada con datos de prueba.'))
