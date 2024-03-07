from django.urls import path

from .views import GoogleSocialAuthView, FacebookSocialAuthView, TwitterSocialAuthView,list_accessible_customers

urlpatterns = [
    path('google/', GoogleSocialAuthView.as_view()),
    # path('facebook/', FacebookSocialAuthView.as_view()),
    # path('twitter/', TwitterSocialAuthView.as_view()),
    path('google/list-accessible-customers/', list_accessible_customers),


]
