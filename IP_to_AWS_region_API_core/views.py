from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ipaddress import ip_address 
import requests
from rest_framework import permissions
from .models import IP_to_AWS_region_API
from .serializers import IP_to_AWS_region_API_Serializer
from .constants import aws_region_dict

class IP_to_AWS_region_APIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        ip = IP_to_AWS_region_API.objects
        serializer = IP_to_AWS_region_API_Serializer(ip, many=True)
        if not serializer.data:
            return Response({"error_description:": "No IPs have been uploaded to the database!"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            ip_address(serializer.data[-1]['ip'])
        except:
            return Response({"error_description:": "Invalid IP! Format must be in X.X.X.X! Furthermore IP must be public!"}, status=status.HTTP_400_BAD_REQUEST)
        
        ip = serializer.data[-1]['ip']
        geo_ip_data = requests.get("https://json.geoiplookup.io/" + ip, verify=False).json()
        aws_region_tuple = aws_region_dict[geo_ip_data["region"]] if geo_ip_data["region"] in aws_region_dict else ()    
        return Response(aws_region_tuple, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = {'ip': request.data.get('ip')}
        serializer = IP_to_AWS_region_API_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)