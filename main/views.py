from django.shortcuts import render

def index(request) :
    context = {
        'namatoko' : 'PacilBakery',
        'namapemilik' : 'Irfan Rizqi Nurrahman',
        'kelaspemilik' : 'PBP C',
    }
    return render(request, "main.html", context)