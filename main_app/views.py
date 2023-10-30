from django.shortcuts import render

# BABY STEP: 
finches = [
    {
    'name': 'Atticus',
    'breed': 'Hoary Redpoll',
    'description': 'Atticus is a very logical and practical, almost like he was a lawyer in his past life...',
    'age': 7,
    },
    {
    'name': 'Vegeta',
    'breed': 'Japanese grosbeak',
    'description': 'A feisty finch, he always seems like he\'s trying go further beyond...',
    'age': 5,
    },
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_idx(request):
    return render(request, 'finches/index.html', {
        'finches': finches,
    })