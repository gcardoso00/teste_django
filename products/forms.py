from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
	title = forms.CharField(label='',
		widget=forms.TextInput(attrs={"placeholder": "Your title"}))



	class Meta:		
		model = Product
		fields = [
			'title','description','price'
	]

	def clean_title(self, *arg, **kwargs):
			title = self.cleaned_data.get("title")
			if not "CFE" in title:
				raise forms.ValidationError("Thisis not a valid title")
			return title

class RawProductForm(forms.Form):
	title = forms.CharField()
	description = forms.CharField()
	price = forms.DecimalField()
			
		
		
			
				