from django.contrib.auth.models import AbstractUser
from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=64, default='auction_title')
    # description = models.CharField(max_length=64)
    # startingBid = models.DecimalField(max_digits=6, decimal_places=2)
    # imageUrl = models.URLField(max_length=200)
    # category = models.CharField(max_length=200)
    #comment = models.ForeignKey()


class User(AbstractUser):
    pass
    #listings = models.ManyToManyField(Listing, blank=True, related_name="auctions")

# Models: Your application should have at least three models in addition to the User model: 
# one for auction listings, 
# one for bids, and 
# one for comments made on auction listings. It’s up to you to decide what fields each model should have, and what the types of those fields should be. You may have additional models if you would like.



class Bid(models.Model):
    # 
    pass

