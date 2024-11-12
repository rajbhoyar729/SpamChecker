import os
import random
from faker import Faker
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spam_checker.settings")
django.setup()

from api.models import User, Contact, SpamReport

# Initialize Faker
fake = Faker()

def create_users(n=10):
    """Create random users."""
    print(f"Creating {n} users...")
    for _ in range(n):
        name = fake.name()
        phone = fake.phone_number()
        email = fake.email()
        password = "password123"  # Default password for all users
        User.objects.create_user(phone=phone, name=name, email=email, password=password)
    print("Users created.")

def create_contacts(user, n=5):
    """Create random contacts for a user."""
    print(f"Creating {n} contacts for user {user.name}...")
    for _ in range(n):
        name = fake.name()
        phone = fake.phone_number()
        Contact.objects.create(user=user, name=name, phone=phone)
    print("Contacts created.")

def create_spam_reports(n=10):
    """Create random spam reports."""
    print(f"Creating {n} spam reports...")
    users = list(User.objects.all())
    for _ in range(n):
        phone_number = fake.phone_number()
        reported_by = random.choice(users)
        SpamReport.objects.create(phone_number=phone_number, reported_by=reported_by)
    print("Spam reports created.")

def populate():
    """Run the population script."""
    # Create users
    create_users(n=10)
    
    # Create contacts for each user
    users = User.objects.all()
    for user in users:
        create_contacts(user, n=5)
    
    # Create spam reports
    create_spam_reports(n=20)

if __name__ == "__main__":
    print("Starting database population...")
    populate()
    print("Database population complete.")
