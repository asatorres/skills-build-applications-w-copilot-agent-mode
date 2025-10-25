
from django.core.management.base import BaseCommand
from pymongo import MongoClient, ASCENDING

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
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        # Eliminar datos existentes
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Insertar datos de ejemplo
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)

        # Índice único en email de usuarios
        db.users.create_index([("email", ASCENDING)], unique=True)

        self.stdout.write(self.style.SUCCESS('La base de datos octofit_db ha sido poblada con datos de prueba.'))
