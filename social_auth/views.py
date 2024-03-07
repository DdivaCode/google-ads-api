from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import GoogleSocialAuthSerializer, TwitterAuthSerializer, FacebookSocialAuthSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
import os
from dotenv import load_dotenv

import requests


load_dotenv()


class GoogleSocialAuthView(GenericAPIView):

    serializer_class = GoogleSocialAuthSerializer

    def post(self, request):
        """

        POST with "auth_token"

        Send an idtoken as from google to get user information

        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)


class FacebookSocialAuthView(GenericAPIView):

    serializer_class = FacebookSocialAuthSerializer

    def post(self, request):
        """

        POST with "auth_token"

        Send an access token as from facebook to get user information

        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)


class TwitterSocialAuthView(GenericAPIView):
    serializer_class = TwitterAuthSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes((IsAuthenticated, ))
def list_accessible_customers(request):
    token = request.data.get("token",None)

    if token is None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    headers = {

        'authorization': f'Bearer {token}',
        'developer-token': os.environ.get('GOOGLE_DEVELOPER_TOKEN'),

    }

    response = requests.get('https://content-googleads.googleapis.com/v16/customers:listAccessibleCustomers', headers=headers)


    return Response(data=response.json())



