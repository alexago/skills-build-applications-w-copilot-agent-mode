from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from pymongo import MongoClient
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

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
            {"_id": ObjectId(), "username": "john_doe", "email": "john@example.com", "password": "password123"},
            {"_id": ObjectId(), "username": "jane_doe", "email": "jane@example.com", "password": "password123"},
        ]
        db.users.insert_many(users)

        # Populate teams
        teams = [
            {"_id": ObjectId(), "name": "Team Alpha", "members": [users[0]["_id"], users[1]["_id"]]},
        ]
        db.teams.insert_many(teams)

        # Populate activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "Running", "duration": "00:30:00"},
        ]
        db.activity.insert_many(activities)

        # Populate leaderboard
        leaderboard = [
            {"_id": ObjectId(), "user": users[0]["_id"], "score": 100},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Populate workouts
        workouts = [
            {"_id": ObjectId(), "name": "Pushups", "description": "Do 20 pushups"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
