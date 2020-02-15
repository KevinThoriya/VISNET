from django.shortcuts import render
from django.http import HttpResponse
from .models import Visitor, Convener, Meeting
from .Extra_Tools import otp as otpa
from .Extra_Tools import genrate_access as ga
from .Extra_Tools import send_email as se
import datetime
import base64
from PIL import Image
from io import BytesIO


def index(request):
    return render(request, 'index.html')

def scanface(request):
    return render(request, 'scan_face.html')

def edit(request):
    if request.method == 'POST':
        id = request.POST.get('id');
        visitor = Visitor.objects.filter(v_id=id)[0]
        params = { 'fname' : visitor.v_name.split()[0] , 
                    'lname': visitor.v_name.split()[1] ,
                    'email': visitor.v_email ,
                    'mobile' : visitor.v_mobile , 
                    'address': visitor.v_address,
                    'perpose': visitor.v_perpose,
                    'id_number' : visitor.v_id,
                    'v_image' : '/media/ids/display_pic/'+str(visitor.v_id)+'.png'
                    }
        # print(visitor.v_name.split()[0])
    return render(request, 'registration.html',params)

def register(request):
    #form value submisstion..
    params = { 'fname' : '' , 
                'lname': '' ,
                'email': '' ,
                'mobile' : '' , 
                'address':'',
                'v_id': '',
                'perpose': False,
                'id_number' : '',
                'v_image' : ''
                }
    if request.method == 'POST':
        if True:        
            img = request.POST.get("img");
            params['v_image'] = img;
    return render(request, 'registration.html',params)

def verify(request):
    params = { 'name' : '' , 
                'email': '' ,
                'mobile' : '' , 
                'address':'',
                'perpose': False,
                'vp_name': '',
                'v_id': '',
                'v_image' : '' }
    if request.method == "POST":
        name = request.POST.get('fname') + ' ' + request.POST.get('sname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        perpose = request.POST.get('perpose')
        vp_id = request.POST.get('towhom')
        otp = otpa.make_message()
        id_number = request.POST.get('id_number')

        image = request.POST.get('image')

        vp = Convener.objects.get(vp_id=vp_id)
        if id_number :
            visitor = Visitor.objects.filter(v_id=int(id_number))[0]
            print(visitor)
            print(visitor.v_name)
            visitor.v_name = name
            print(visitor.v_name)
            visitor.v_email = email
            visitor.v_mobile = mobile
            visitor.v_address = address
            visitor.v_perpose = perpose
            visitor.v_otp = otpa.make_message()            
            # print(visitor.v_image)
            visitor.save()
            print(visitor)
        else:
            visitor = Visitor(v_name = name , v_email = email , v_mobile = mobile , v_perpose = perpose , v_address = address , v_otp = otp,  )
            visitor.save()
            image_path = save_image(image , visitor.v_id)
            visitor.v_image = image_path
            visitor.save()

            meeting = Meeting( vp_id = vp , v_id = visitor )
            meeting.save()
        
        #sending OTP here 
        # otpa.OTP(visitor.v_mobile,visitor.v_otp)
        
        params = { 'name' : name , 
                    'email': email ,
                    'mobile' : mobile , 
                    'address':address,
                    'perpose': perpose,
                    'vp_name': vp.vp_name,
                    'v_id' : visitor.v_id,
                    'v_image' : '/media/ids/display_pic/'+str(visitor.v_id)+'.png' 
                    }
        return render(request, 'verify.html', params )
    return render(request, 'verify.html',params)

def access(request):
    params={'visitor': [], "img": 'access.png' }
    if request.method == 'POST':
        id = request.POST.get('id')
        visitor = Visitor.objects.filter(v_id = id )
        if len(visitor) > 0 :
            visitor = visitor[0]
            ga.genrateId(visitor.v_id,visitor.v_name,visitor.v_perpose,visitor.v_address)
            params = {
                'visitor' : visitor ,
                'img' : '/media/ids/'+str(visitor.v_id) + '.png'
            }
            #send email to v_email address
            # se.sendmail(visitor.v_id,visitor.v_email)
            # genrate the access card for visitor veriable
            return render(request, 'access.html', params )
    return render(request, 'access.html', params)

def verifyotp(request):
    message = ''
    v_id = request.GET.get('id')
    v_otp = request.GET.get('otp')
    vv_id = Visitor.objects.filter(v_id = v_id)
    if len(vv_id) > 0 :
        vv_id = vv_id[0]
        if str(vv_id.v_otp) == str(v_otp):
            message = 'Thanks for Verification. please wait ... '
        else : 
            message = 'Wrong Verification Code. Try Again ! with Correct code...'
    else :
        message = "server error ... contact to admin please.."
    return HttpResponse(message)

def qr(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        perpose = request.POST.get('perpose')
        collage = request.POST.get('collage')
        string = ''

        meeting_ob = Meeting.objects.filter( v_id = id)
        if len(meeting_ob) >= 1:
            meeting_ob = meeting_ob[len(meeting_ob)-1]
            if not (meeting_ob.v_login_time):
                meeting_ob.v_login_time = datetime.datetime.now()
                meeting_ob.save()
                string = f'Wel Come, {name}.<br/> you are logged in ...'        
            else:
                meeting_ob.v_logout_time = datetime.datetime.now()
                meeting_ob.save()
                string = f"nice to meet you {name}.<br/> you are logged out ..."
        return HttpResponse(string)
        
    return render(request, 'qr.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def save_image(img,id):
    image = img.split(',')
    if  (len(image)) >= 2 :
        im = Image.open(BytesIO(base64.b64decode(image[1])))
        # im.save('new_image.png', 'PNG')
        width, height = im.size 
        im1 = im.crop((50, 0, 50 + height , height)) 
        save_path =  'media/ids/display_pic/'+ str(id) +'.png'
        im1.save(save_path)
        return save_path



'''

list of superuser:
username = kevin -> password = admin

'''