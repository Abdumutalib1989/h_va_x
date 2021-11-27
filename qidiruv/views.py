from django.shortcuts import render
from .models import soz, nosoz

def index(request):
    return render(request, 'qidiruv/index.html')

def natija(request):
    qidiruv_sozi = request.GET.get('k_soz')
    t_soz = soz.objects.filter(correct=qidiruv_sozi)

    if len(t_soz)>0:
       n_soz = nosoz.objects.filter(soz_id=t_soz[0].id)
       return render(request, 'qidiruv/natija.html',{'t_soz': t_soz[0].correct, 'n_soz': n_soz})
    else:
        not_soz = nosoz.objects.filter(wrong=qidiruv_sozi)
        if len(not_soz) > 0:
            tog_soz = soz.objects.filter(correct=not_soz[0].soz_id)
            not_soz = nosoz.objects.filter(soz_id=tog_soz[0].id)
            return render(request, 'qidiruv/natija.html', {'t_soz': tog_soz[0].correct, 'n_soz': not_soz})
        else:
            return render(request, 'qidiruv/natija.html', {'t_soz': "Ma'lumotlar omborida bunday so'z yo'q!"})


