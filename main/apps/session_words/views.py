from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'session_words/index.html')

def add(request):
    if 'it' not in request.session:
        request.session['it'] = []

    if 'big_fonts' not in request.POST:
        size = 'small'
    else:
        size = 'big'
    
    words = {
        'word' : request.POST['word'],
        'color' : request.POST['color'],
        'size' : size
    }
    request.session['it'].append(words)
    request.session.modified = True
    print(request.POST)
    return redirect('/')

def destroy(request):
    request.session.clear()
    return redirect('/')
