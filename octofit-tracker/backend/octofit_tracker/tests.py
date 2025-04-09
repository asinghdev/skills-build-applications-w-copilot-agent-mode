from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25)
        self.assertEqual(user.name, "Test User")

class TeamModelTest(TestCase):
    def test_create_team(self):
        user1 = User.objects.create(email="user1@example.com", name="User1", age=30)
        user2 = User.objects.create(email="user2@example.com", name="User2", age=35)
        team = Team.objects.create(name="Team A")
        team.members.add(user1, user2)
        self.assertEqual(team.name, "Team A")
        self.assertEqual(len(team.members.all()), 2)

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=25)
        activity = Activity.objects.create(user=user, activity_type="Running", duration=30, date=date(2025, 4, 9))
        self.assertEqual(activity.activity_type, "Running")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user1 = User.objects.create(email="user1@example.com", name="User1", age=30)
        user2 = User.objects.create(email="user2@example.com", name="User2", age=35)
        team = Team.objects.create(name="Team A")
        team.members.add(user1, user2)
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Morning Run", description="A quick morning run", duration=20)
        self.assertEqual(workout.name, "Morning Run")
