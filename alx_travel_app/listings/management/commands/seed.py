"""
    script file used to populate the database with sample listings data.
"""

from django.core.management.base import BaseCommand

from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review

from datetime import date, timedelta

import random

class Command(BaseCommand):
    help = 'Populate the database with sample listings data'

    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        Booking.objects.all().delete()
        Listing.objects.all().delete()
        Review.objects.all().delete()
        
        # Create 10 users
        users_names = [
            'Alice', 'Bob', 'Charlie', 'David', 'Eve',
            'Frank', 'Grace', 'Hannah', 'Ivan', 'Jack'
        ]
        
        users = []
        for name in users_names:
            user, _ = User.objects.get_or_create(
                username=name.lower(),
                email=f"{name.lower()}@example.com",
            )
            users.append(user)
        
         # Create 10 Listings
        listing_names = [
            "Ocean View Villa", "Mountain Retreat", "City Apartment",
            "Beach Bungalow", "Country House", "Modern Loft",
            "Lakeside Cabin", "Penthouse Suite", "Desert Oasis", "Jungle Treehouse"
        ]
        locations = [
            "California", "Colorado", "New York",
            "Hawaii", "Texas", "Florida",
            "Michigan", "Nevada", "Arizona", "Costa Rica"
        ]
        listings = []
        for i in range(10):
            listing, _ = Listing.objects.get_or_create(
                name=listing_names[i],
                description=f"A beautiful {listing_names[i]} located in {locations[i]}.",
                location=locations[i],
                price_per_night=random.randint(50, 300),
            )
            listings.append(listing)
        
         # Create 10 Bookings
        for i in range(10):
            start_date = date.today() + timedelta(days=random.randint(1, 30))
            end_date = start_date + timedelta(days=random.randint(1, 7))
            listing = random.choice(listings)
            user = random.choice(users)
            Booking.objects.get_or_create(
                user=user,
                listing=listing,
                start_date=start_date,
                end_date=end_date,
                total_price=listing.price_per_night * (end_date - start_date).days,
                status=random.choice(["pending", "confirmed", "canceled"]),
            )

        # Create 10 Reviews
        for i in range(10):
            listing = random.choice(listings)
            user = random.choice(users)
            Review.objects.get_or_create(
                user=user,
                listing=listing,
                rating=random.randint(1, 5),
                comment=f"Great experience at {listing.name}!",
            )

        self.stdout.write(self.style.SUCCESS("Database seeded successfully with sample and realistic data 👍🏽✅"))