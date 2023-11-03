from django.shortcuts import render, redirect
# import from the Django framework
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# AWS S3 imports
import os
import boto3
import uuid
# import Finch model   
from .models import Finch, Egg, Photo
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
    # get eggs finch doesn't have
    # first, create list of egg ids that finch DOES have
    id_list = finch.eggs.all().values_list('id')
    # query for eggs whose ids are not in list using exclude
    eggs_finch_doesnt_have = Egg.objects.exclude(id__in = id_list)
    # instantiate FeedingForm to be rendered in template
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch,
        # include feeding_form in context
        'feeding_form': feeding_form,
        # eggs in context
        'eggs': eggs_finch_doesnt_have
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

class EggList(ListView):
    model = Egg

class EggDetail(DetailView):
    model = Egg
    
class EggCreate(CreateView):
    model = Egg
    fields = '__all__'

class EggUpdate(UpdateView):
    model = Egg
    fields = ['name', 'color']

class EggDelete(DeleteView):
    model = Egg
    success_url = '/eggs'

def assoc_egg(request, finch_id, egg_id):
    # Note that you can pass a egg's id instead of the whole egg object
    Finch.objects.get(id = finch_id).eggs.add(egg_id)
    return redirect('detail', finch_id = finch_id)

def unassoc_egg(request, finch_id, egg_id):
    Finch.objects.get(id = finch_id).eggs.remove(egg_id)
    return redirect('detail', finch_id = finch_id)

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'breed', ]
  
class FinchUpdate(UpdateView):
    model = Finch
    # let all but 'name' be editable
    fields = ['name', 'breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    # redirect to index page
    success_url = '/finches'

def add_photo(request, finch_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to finch_id or finch (if you have a finch object)
            Photo.objects.create(url = url, finch_id = finch_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', finch_id = finch_id)