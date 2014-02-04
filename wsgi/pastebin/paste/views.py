from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext

from paste.models import Paste
from paste.forms import PasteForm

def get_instance(pk):
	if pk:
		return get_object_or_404(Paste, pk=int(pk))
	return None

def home_response(request, pk=None, form=None):
	return render_to_response('index.html', 
				{'form': form, 
				'pastes': Paste.objects.all()[:30], 
				'pk': pk if pk and not request.GET.get('q') else ''
				},
				RequestContext(request))

def home(request, pk=None):
	if request.method == 'POST':
		form = PasteForm(request.POST, instance=get_instance(request.POST.get('pk', '')))
		if form.is_valid():
			p = form.save()
			return HttpResponseRedirect(p.get_absolute_url())
		else:
			return home_response(request, request.POST.get('pk', ''), form)
	else:
		form = PasteForm(instance = get_instance(pk))
		return home_response(request, pk, form)