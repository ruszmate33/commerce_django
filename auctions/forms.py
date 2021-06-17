from django import forms

class NewListingForm(forms.Form):
    title = forms.CharField(label="title", max_length=64)
    description = forms.CharField(label="description", max_length=64)
    startingBid = forms.DecimalField(max_digits=6, decimal_places=2)
    imageUrl = forms.URLField(label="URL for image", max_length=200)
    category = forms.CharField(label="category",max_length=200)