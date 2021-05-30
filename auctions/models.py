from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

# Models: Your application should have at least three models in addition to the User model: 
# one for auction listings, 
# one for bids, and 
# one for comments made on auction listings. It’s up to you to decide what fields each model should have, and what the types of those fields should be. You may have additional models if you would like.

class Listing(models.Model):
    pass

class Bid(models.Model):
    pass

