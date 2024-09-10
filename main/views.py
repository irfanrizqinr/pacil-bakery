from django.shortcuts import render

def index(request) :
    context = {
        'namaApp' : 'PacilBakery',
        'nama' : 'Irfan Rizqi Nurrahman',
        'kelas' : 'PBP C',
    }
    return render(request, "main.html", context)