from django.db.models import Count
from rest_framework.exceptions import NotFound
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User ,Contact,SpamReport
from .serializers import RegisterSerializer, UserSerializer, UpdateProfileSerializer ,ContactSerializer, CreateContactSerializer,SpamReportSerializer,SearchResultSerializer,PhoneSearchResultSerializer,ContactSearchResultSerializer,ContactDetailSerializer,UserDetailSerializer


class ProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

# Update Profile
class UpdateProfileView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdateProfileSerializer

    def get_object(self):
        return self.request.user


# Register View
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

# Logout View
class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successful"})
        except Exception as e:
            return Response({"error": str(e)}, status=400)

# List and Create Contacts
class ContactListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ContactSerializer

    def get_queryset(self):
        # Only return contacts for the logged-in user
        return Contact.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateContactSerializer
        return ContactSerializer

# Delete a Contact
class ContactDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Contact.objects.all()

    def get_queryset(self):
        # Ensure users can only delete their own contacts
        return Contact.objects.filter(user=self.request.user)

class SpamReportCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SpamReportSerializer

# Check spam likelihood for a phone number
class SpamLikelihoodView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        phone_number = self.kwargs.get('phone_number')
        # Count total reports for the given phone number
        total_reports = SpamReport.objects.filter(phone_number=phone_number).count()
        return Response({"phone_number": phone_number, "spam_likelihood": total_reports})
    
class SearchByNameView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SearchResultSerializer

    def get_queryset(self):
        query = self.request.query_params.get('name', '').strip()
        if not query:
            return User.objects.none()  # Return empty if no query provided

        # Exact matches first, then partial matches
        exact_matches = User.objects.filter(name__istartswith=query)
        partial_matches = User.objects.filter(name__icontains=query).exclude(id__in=exact_matches)

        return exact_matches | partial_matches



class SearchByPhoneNumberView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, phone_number):
        # Check if the phone number belongs to a registered user
        user = User.objects.filter(phone=phone_number).first()
        if user:
            # If it's a registered user, return their details
            serializer = PhoneSearchResultSerializer(user)
            return Response({"registered_user": serializer.data})

        # If not, return all contacts matching the phone number
        contacts = Contact.objects.filter(phone=phone_number)
        contact_serializer = ContactSearchResultSerializer(contacts, many=True)
        return Response({"contacts": contact_serializer.data})

class ViewDetailsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        # Check if the person is a registered user
        user = User.objects.filter(id=pk).first()
        if user:
            serializer = UserDetailSerializer(user, context={'request': request})
            return Response({"user_details": serializer.data})

        # If not found as a registered user, check contacts
        contact = Contact.objects.filter(id=pk, user=request.user).first()
        if contact:
            serializer = ContactDetailSerializer(contact)
            return Response({"contact_details": serializer.data})

        # If neither found, return a 404 error
        raise NotFound("Details not found.")