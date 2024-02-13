from django       import forms
from home.models  import *

class ProductReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Write review'}))
    
    class Meta:
        model  = Review
        fields = ['review','rate']