from django import forms

from paste.models import Paste

class PasteForm(forms.ModelForm):
	class Meta:
		model = Paste
		exclude = ['expiration']

	def clean_title(self):
		title = self.cleaned_data['title']
		if not title.strip():
			title = "Untitled"
		return title