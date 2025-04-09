from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamListCreateView(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityListCreateView(ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardListCreateView(ListCreateAPIView):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutListCreateView(ListCreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/api/users/',
        'teams': '/api/teams/',
        'activity': '/api/activity/',
        'leaderboard': '/api/leaderboard/',
        'workouts': '/api/workouts/',
    })
