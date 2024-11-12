from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, LogoutView,ProfileView, UpdateProfileView ,  ContactListCreateView, ContactDeleteView,SpamReportCreateView, SpamLikelihoodView, SearchByNameView, SearchByPhoneNumberView,ViewDetailsView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update/', UpdateProfileView.as_view(), name='profile_update'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('contacts/', ContactListCreateView.as_view(), name='contact_list_create'),
    path('contacts/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact_delete'),
    path('spam/', SpamReportCreateView.as_view(), name='spam_report'),
    path('spam/<str:phone_number>/', SpamLikelihoodView.as_view(), name='spam_likelihood'),
    path('search/name/', SearchByNameView.as_view(), name='search_by_name'),
    path('search/phone/<str:phone_number>/', SearchByPhoneNumberView.as_view(), name='search_by_phone'),
    path('details/<int:pk>/', ViewDetailsView.as_view(), name='view_details'),
]
