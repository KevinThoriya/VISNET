from django.shortcuts import render
from django.http import HttpResponse
from .models import Visitor, Convener, Meeting
from .aTools import otp as otpa
'''
import random

# Create your views here.
def make_message():
    length = 6
    number = 0
    for i in range(length):
        number *=10
        number += random.randrange( 1, 10, 1 )
    return number
'''

def index(request):
    return render(request, 'index.html')

def scanface(request):
    return render(request, 'scan_face.html')

def register(request):
    return render(request, 'registration.html')

def verify(request):
    params = { 'name' : '-' , 
                'email': '-' ,
                'mobile' : '-' , 
                'address':'-',
                'perpose': '-',
                'vp_name': '-',
                'v_id': '-',
                }
    if request.method == "POST":
        name = request.POST.get('fname') + ' ' + request.POST.get('sname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        perpose = request.POST.get('perpose')
        vp_id = request.POST.get('towhom')
        otp = otpa.make_message()
        
        visitor = Visitor(v_name = name , v_email = email , v_mobile = mobile , v_perpose = perpose , v_address = address , v_otp = otp )
        visitor.save()
        
        vp = Convener.objects.filter( vp_id = int(vp_id) )
        meeting = Meeting( vp_id = vp[0] , v_id = visitor )
        meeting.save()

        params = { 'name' : name , 
                    'email': email ,
                    'mobile' : mobile , 
                    'address':address,
                    'perpose': perpose,
                    'vp_name': vp[0].vp_name,
                    'v_id' : visitor.v_id
                    }
        return render(request, 'verify.html', params )

    return render(request, 'verify.html')

def access(request):
    params={'visitor': [] }
    if request.method == 'POST':
        id = request.POST.get('id')
        visitor = Visitor.objects.filter(v_id = id )
        if len(visitor) > 0 :
            visitor = visitor[0]
            params = {
                'visitor' : visitor 
            }
            # genrate the access card for visitor veriable
            return render(request, 'access.html', params )
    return render(request, 'access.html', params)

def qr(request):
    return render(request, 'qr.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def verifyotp(request):
    message = ''
    v_id = request.GET.get('id')
    v_otp = request.GET.get('otp')
    vv_id = Visitor.objects.filter(v_id = v_id)
    if len(vv_id) > 0 :
        vv_id = vv_id[0]
        if str(vv_id.v_otp) == str(v_otp):
            message = 'Thanks For Verify Number.'
        else : 
            message = 'Wrong verifing Code Try Again! with correct one..'
    else :
        message = "server error ... contact to admin please.."
    return HttpResponse(message)

'''

list of superuser:
username = kevin -> password = admin

'''