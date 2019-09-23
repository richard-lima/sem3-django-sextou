from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'nomes':[
            'eric',
               'bruno',
                
        ]
    }
    return render(request, context)