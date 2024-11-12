from rest_framework import serializers
from .models import User ,Contact,SpamReport

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'phone', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['name', 'phone', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            phone=validated_data['phone'],
            name=validated_data['name'],
            password=validated_data['password'],
            email=validated_data.get('email')
        )
        return user

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email']
        read_only_fields = ['phone']  # Phone number should not be editable
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone']

class CreateContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'phone']

    def create(self, validated_data):
        # Automatically associate the contact with the current user
        user = self.context['request'].user
        return Contact.objects.create(user=user, **validated_data)
    
class SpamReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpamReport
        fields = ['id', 'phone_number', 'reported_by']
        read_only_fields = ['reported_by']

    def create(self, validated_data):
        # Automatically set the user who reported the number
        validated_data['reported_by'] = self.context['request'].user
        return super().create(validated_data)
    
class SearchResultSerializer(serializers.ModelSerializer):
    spam_likelihood = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'phone', 'spam_likelihood']

    def get_spam_likelihood(self, obj):
        # Calculate the spam likelihood for the user's phone number
        return SpamReport.objects.filter(phone_number=obj.phone).count()
    
class PhoneSearchResultSerializer(serializers.ModelSerializer):
    spam_likelihood = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'phone', 'spam_likelihood']

    def get_spam_likelihood(self, obj):
        # Calculate spam likelihood for the user's phone number
        return SpamReport.objects.filter(phone_number=obj.phone).count()


class ContactSearchResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'phone']


class UserDetailSerializer(serializers.ModelSerializer):
    spam_likelihood = serializers.SerializerMethodField()
    email_visible = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'phone', 'email', 'spam_likelihood', 'email_visible']

    def get_spam_likelihood(self, obj):
        # Calculate the spam likelihood for the user's phone number
        return SpamReport.objects.filter(phone_number=obj.phone).count()

    def get_email_visible(self, obj):
        # Email is visible only if the requesting user is in the person's contact list
        request = self.context.get('request')
        if request and Contact.objects.filter(user=obj, phone=request.user.phone).exists():
            return obj.email
        return None


class ContactDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'phone']
