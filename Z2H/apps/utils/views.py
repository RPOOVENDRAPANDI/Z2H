from django.conf import settings
from django.shortcuts import render
from datetime import datetime
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import permissions, authentication
from .models import State, District
from .serializers import StateSerializer, DistrictSerializer
from rest_framework.response import Response
from rest_framework import status
import os

# Create your views here.

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'production')

class StateView(ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class DistrictView(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    lookup_field = 'uid'
    lookup_url_kwarg = 'uid'
    lookup_value_regex = '[0-9a-f-]{36}'

    def get_queryset(self):
        return District.objects.filter(state__uid=self.kwargs['state_uid'])

class UploadImageView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_proper_file_name(self, file_name):
        file_name_extension = "." + file_name.split(".")[-1]
        file_name_without_extension = file_name.replace(file_name_extension, "")
        file_name_date = file_name_without_extension.replace(".", "") + "_" + str(datetime.now()).replace("-", "_").replace(" ", "_").replace(":", "_").replace(".","_") + file_name_extension
        file_name_proper = file_name_date.replace(" ", "_").replace("-", "_").replace("'", "").replace("#", "_No_").replace("&", "_").replace("(", "_").replace(")", "_")
        return file_name_proper
    
    def handle_product_image_upload(self, request, upload_type):
        data = dict()
        file_uploaded_urls = list()
        try:
            file_name_list = request.FILES.getlist('file_name')

            for file in file_name_list:
                file_name = file.name
                file_uplaod_path = os.path.join(settings.STATICFILES_DIRS[0], "product_image")
                proper_file_name = self.get_proper_file_name(file_name)
                file_to_upload = os.path.join(file_uplaod_path, proper_file_name)

                if not os.path.exists(file_uplaod_path):
                    os.makedirs(file_uplaod_path)

                with open(file_to_upload, "wb") as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                
                destination.close()

                if ENVIRONMENT == 'local':
                    file_uploaded_url = f"{os.environ['APP_URL']}/static/{upload_type}/{proper_file_name}"
                elif ENVIRONMENT == 'production':
                    file_uploaded_url = f"{os.environ['APP_URL']}/static_image/{upload_type}/{proper_file_name}"

                file_uploaded_urls.append(file_uploaded_url)
        
        except KeyError:
            data = {
                "status": "error",
                "message": "Invalid File or File not Found!!!"
            }

        data = {
            "status": "success",
            "message": "Image Uploaded Successfully",
            "image_upload_paths": file_uploaded_urls,
        }
        return Response(data, status=status.HTTP_200_OK)



    def post(self, request):
        upload_type = request.data.get('upload_type')

        is_valid_upload_type = True if upload_type in ['profile_image', 'product_image', 'demo_video'] else False

        if not is_valid_upload_type:
            data = {
                "status": "error",
                "message": "Invalid Upload Type"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
        if upload_type == 'product_image':
            return self.handle_product_image_upload(request, upload_type)

        try:
            file_name = request.FILES["file_name"].name
            
            file_uplaod_path = os.path.join(settings.STATICFILES_DIRS[0], upload_type)
            proper_file_name = self.get_proper_file_name(file_name)
            file_to_upload = os.path.join(file_uplaod_path, proper_file_name)

            if not os.path.exists(file_uplaod_path):
                os.makedirs(file_uplaod_path)

            with open(file_to_upload, "wb") as destination:
                for chunk in request.FILES["file_name"].chunks():
                    destination.write(chunk)
                    destination.close()
                    
        except KeyError:
            data = {
                "status": "error",
                "message": "Invalid File or File not Found!!!"
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            data = {
                "status": "error",
                "message": str(e)
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
        if ENVIRONMENT == 'local':
            file_uploaded_url = f"{os.environ['APP_URL']}/static/{upload_type}/{proper_file_name}"
        elif ENVIRONMENT == 'production':
            file_uploaded_url = f"{os.environ['APP_URL']}/static_image/{upload_type}/{proper_file_name}"

        data = {
            "status": "success",
            "message": "Image Uploaded Successfully",
            "image_upload_path": file_uploaded_url,
        }
        return Response(data, status=status.HTTP_200_OK)

