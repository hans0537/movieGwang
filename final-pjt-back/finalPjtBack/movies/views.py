from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieSerializer
from .models import Movie,Genre

# Create your views here.

# @api_view([''])