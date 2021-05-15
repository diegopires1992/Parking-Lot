from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SpaceSerializers,VehiclesSerializers
from .models import Space,Vehicles
from levels.models import Level
from django.shortcuts import get_object_or_404
from datetime import datetime,timezone
from .services import PaymentAmountServices
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from pricings.models import Price


class VehiclesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        serializer = VehiclesSerializers(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        price = Price.objects.all().last()

        if not price:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        vehiclesdata = serializer.data

        level_in_use = Level.objects.order_by('fill_priority')
        vacancy = []
        try:
            for level in level_in_use:
                if vehiclesdata['vehicle_type'] == 'car' and level.available_spaces.available_car_spaces > 0:
                    level.available_spaces.available_car_spaces -= 1
                    level.available_spaces.save()
                    space = Space.objects.create(variety=vehiclesdata['vehicle_type'], level_name=level.name,level_id=level)
                    vacancy.append(space)
                    break
                if vehiclesdata['vehicle_type'] == 'motorcycle' and level.available_spaces.available_motorcycle_spaces > 0:
                    level.available_spaces.available_motorcycle_spaces -= 1
                    level.available_spaces.save()
                    space = Space.objects.create(variety=vehiclesdata['vehicle_type'], level_name=level.name, level_id=level)
                    vacancy.append(space)
                    break
        
            vehicles = Vehicles.objects.get_or_create(**vehiclesdata,space=vacancy[0])
        
            serializer = VehiclesSerializers(vehicles[0])

            return Response(serializer.data)

        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self,request,vehicle_id):
        vehicles = get_object_or_404(Vehicles, id=vehicle_id)
        if vehicles.vehicle_type == 'car':
           vehicles_space  = vehicles.space.level_id.available_spaces
           vehicles_space.available_car_spaces = vehicles_space.available_car_spaces + 1
           vehicles_space.save()

        if vehicles.vehicle_type == 'motorcycle':
           vehicles_space  = vehicles.space.level_id.available_spaces
           vehicles_space.available_motorcycle_spaces = vehicles_space.available_motorcycle_spaces + 1
           vehicles_space.save()

        vehicles.paid_at = datetime.now(timezone.utc)        
        vehicles.amount_paid = PaymentAmountServices(vehicles.paid_at,vehicles.arrived_at).amount_paid()
        vehicles.space = None
        vehicles.save()

        serializer = VehiclesSerializers(vehicles)
        return Response(serializer.data , status=status.HTTP_200_OK)


