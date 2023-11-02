from django.shortcuts import render, redirect
# import from the Django framework
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# import Finch model   
from .models import Finch
# import FeedingForm from forms.py
from .forms import FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_idx(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches,
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id = finch_id)
    # instantiate FeedingForm to be rendered in template
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch,
        # include feeding_form in context
        'feeding_form': feeding_form
    })

def add_feeding(request, finch_id):
    # create ModelForm instance using data in 'request.POST'
    form = FeedingForm(request.POST)
    # validate form
    if form.is_valid():
        # don't save form to DB until it
        # has an assigned 'finch_id'
        new_feeding = form.save(commit = False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id = finch_id)

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
  
class FinchUpdate(UpdateView):
    model = Finch
    # let all but 'name' be editable
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    # redirect to index page
    success_url = '/finches'