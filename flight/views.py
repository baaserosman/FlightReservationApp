from .models import Flight, Reservation
from .serializers import FlightSerializer, ReservationSerializer
from rest_framework import viewsets
from .permissions import IsStufforReadOnly


class FlightView(viewsets.ModelViewSet):  # GET, POST, UPDATE, DELETE, PATCH
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStufforReadOnly,)
    
    
class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
