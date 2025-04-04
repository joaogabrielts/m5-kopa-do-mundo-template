from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Team
from .serializers import TeamSerializer


class TeamDetailView(APIView):
    def get(self, request, team_id):
    
        team = get_object_or_404(Team, id=team_id)
        serializer = TeamSerializer(team)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, team_id):
        team = get_object_or_404(Team, id=team_id)
        serializer = TeamSerializer(team, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, team_id):
        team = get_object_or_404(Team, id=team_id)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
