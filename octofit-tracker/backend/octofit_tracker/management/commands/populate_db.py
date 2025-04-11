from pymongo import MongoClient
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Populate users
        users = [
            {"email": "john.doe@example.com", "name": "John Doe", "password": "password123"},
            {"email": "jane.smith@example.com", "name": "Jane Smith", "password": "password123"}
        ]
        db.users.insert_many(users)

        # Populate teams
        teams = [
            {"name": "Team Alpha", "members": ["john.doe@example.com", "jane.smith@example.com"]}
        ]
        db.teams.insert_many(teams)

        # Populate activities
        activities = [
            {"user": "john.doe@example.com", "activity_type": "Running", "duration": 30},
            {"user": "jane.smith@example.com", "activity_type": "Cycling", "duration": 45}
        ]
        db.activity.insert_many(activities)

        # Populate leaderboard
        leaderboard = [
            {"team": "Team Alpha", "score": 100}
        ]
        db.leaderboard.insert_many(leaderboard)

        # Populate workouts
        workouts = [
            {"name": "Morning Yoga", "description": "A relaxing yoga session to start the day."},
            {"name": "HIIT", "description": "High-intensity interval training for advanced users."}
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Database populated with test data using MongoDB native methods.'))
