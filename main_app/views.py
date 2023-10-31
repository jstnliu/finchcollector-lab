from django.shortcuts import render
# import Finch model   
from .models import Finch

# # BABY STEP: 
# finches = [
#     {
#     'name': 'Atticus',
#     'breed': 'Hoary Redpoll',
#     'description': 'Atticus is a very logical and practical, almost like he was a lawyer in his past life...',
#     'age': 7,
#     },
#     {
#     'name': 'Vegeta',
#     'breed': 'Japanese grosbeak',
#     'description': 'A feisty finch, he always seems like he\'s trying go further beyond...',
#     'age': 5,
#     },
# ]

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
    return render(request, 'finches/detail.html', {
        'finch': finch
    })
