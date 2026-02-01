from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from MyApp.models import *


def login(request):
    return render(request, 'login index.html')


def login_post(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    res = Login.objects.filter(Username=username, password=password)
    if res.exists():
        res2 = Login.objects.get(Username=username, password=password)
        request.session['lid'] = res2.id
        if res2.type == 'admin':
            return HttpResponse('''<script>alert("login successfully");window.location="/MyApp/ahome/"</script>''')
        elif res2.type == 'policestation':

            return HttpResponse('''<script>alert("login successfully");window.location="/MyApp/policehome/"</script>''')
        elif res2.type == 'Houseowner':

            return HttpResponse('''<script>alert("login successfully");window.location="/MyApp/houseownerhome/"</script>''')

        else:
            return HttpResponse('''<script>alert("login failed");window.location="/MyApp/login/"</script>''')
    else:
        return HttpResponse('''<script>alert("login failed");window.location="/MyApp/login/"</script>''')


def addpolicestation(request):
    return render(request, 'Admin/Add police station.html')



def admin_view_criminallist(request):
    res = Criminal.objects.all()
    return render(request, 'Admin/View criminal.html', {"data": res})

def addpolicestation_post(request):
    name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    phoneNo = request.POST['textfield5']
    email = request.POST['textfield6']
    lobj = Login()
    lobj.Username = email
    lobj.password = phoneNo
    lobj.type = 'policestation'
    lobj.save()
    obj = PoliceStation()
    obj.policestationname = name
    obj.place = place
    obj.post = post
    obj.pin = pin
    obj.phoneno = phoneNo
    obj.email = email
    obj.LOGIN = lobj
    obj.save()
    return HttpResponse('''<script>alert("added successfully");window.location="/MyApp/ahome/"</script>''')


def changepassword(request):
    return render(request, 'Admin/Change password.html')


def changepassword_post(request):
    Currentpassword = request.POST['textfield']
    Newpassword = request.POST['textfield2']
    Confirmpassword = request.POST['textfield3']
    res = Login.objects.filter(id=request.session['lid'], password=Currentpassword)
    if res.exists():
        if Newpassword == Confirmpassword:
            res = Login.objects.filter(id=request.session['lid'], password=Currentpassword).update(
                password=Confirmpassword)
            return HttpResponse('''<script>alert("changed successfully");window.location="/MyApp/login/"</script>''')
        else:
            return HttpResponse(
                '''<script>alert("password mismatch");window.location="/MyApp/changepassword/"</script>''')

    else:
        return HttpResponse('''<script>alert("invalid");window.location="/MyApp/changepassword/"</script>''')


def editpolicestation(request, id):
    res = PoliceStation.objects.get(LOGIN_id=id)
    return render(request, 'Admin/Edit police station.html', {"data": res})


def editpolicestation_post(request):
    Name = request.POST['textfield']
    place = request.POST['textfield2']
    post = request.POST['textfield3']
    pin = request.POST['textfield4']
    phoneNo = request.POST['textfield5']
    Email = request.POST['textfield6']
    id = request.POST['id']
    lobj = PoliceStation.objects.get(LOGIN_id=id)
    lobj.policestationname = Name

    lobj.place = place
    lobj.post = post
    lobj.pin = pin
    lobj.phoneno = phoneNo
    lobj.email = Email
    lobj.save()
    Login.objects.filter(id=id).update(Username=Email)
    return HttpResponse('''<script>alert("updated");window.location='/MyApp/viewpolicestation/'</script>''')


def Sendreply(request, id):

    c=Complaints.objects.get(id=id)
    return render(request, 'Admin/Send reply.html', {'id': id, 'complaint': c.complaint})


def Sendreply_post(request):
    Reply = request.POST['textfield']
    id = request.POST['id']
    res = Complaints.objects.filter(id=id).update(reply=Reply, status='replied')
    return HttpResponse('''<script>alert("submitted");window.location='/MyApp/viewcomplaint/'</script>''')


def Viewcomplaint(request):
    res = Complaints.objects.all()
    return render(request, 'Admin/View complaint.html', {"data": res})


def Viewcomplaint_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    res = Complaints.objects.filter(date__range=[fromdate, todate])
    return render(request, 'Admin/View complaint.html', {"data": res})


def Viewpolicestation(request):
    res = PoliceStation.objects.all()
    return render(request, 'Admin/View police station.html', {"data": res})


def Viewpolicestation_post(request):
    search = request.POST['textfield']
    res = PoliceStation.objects.filter(policestationname__icontains=search)
    return render(request, 'Admin/View police station.html', {"data": res})


def delete_policestation(request, id):
    PoliceStation.objects.filter(id=id).delete()
    return HttpResponse(
        '''<script>alert('policestation deleted');window.location='/MyApp/viewpolicestation/'</script>''')


def Viewregisteredhouseowners(request):
    res = Houseowner.objects.all()
    return render(request, 'Admin/View Registered House owners.html', {'data': res})


def Viewregisteredhouseowners_post(request):
    search = request.POST['textfield']
    res = Houseowner.objects.filter(ownername__icontains=search)
    return render(request, 'Admin/View Registered House owners.html', {'data': res})


def ViewSuggestions(request):
    res = Suggestions.objects.all()
    return render(request, 'Admin/View Suggestions.html', {"data": res})


def Viewsuggestions_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    res = Suggestions.objects.filter(date__range=[fromdate, todate])
    return render(request, 'Admin/View Suggestions.html', {"data": res})


def ahome(request):
    return render(request, 'Admin/homeindex.html')


################################

def addcrimehistory(request):
    return render(request, 'police station/add crime history.html')


def addcrimehistory_post(request):
    casenumber = request.POST['textfield']
    datereposted = request.POST['textfield2']
    dateoccured = request.POST['textfield3']
    crimetype= request.POST['textfield4']
    location = request.POST['textfield5']
    victim = request.POST['textfield6']
    suspect = request.POST['textfield7']
    arrestdate= request.POST['textfield8']
    charge = request.POST['textfield9']
    description=request.POST['textfield10']

    a=Crimehistory()
    a.casenumber=casenumber
    a.date_reposted=datereposted
    a.date_occured=dateoccured
    a.crime_type=crimetype
    a.location=location
    a.victim=victim
    a.suspect=suspect
    a.arrest_date=arrestdate
    a.charge=charge
    a.sentence=description
    a.POLICE=PoliceStation.objects.get(LOGIN_id=request.session['lid'])
    a.save()
    return HttpResponse('''<script>alert('Add Criminal History');window.location='/MyApp/addcrimehistory/'</script>''')


def addcriminal(request):
    return render(request, 'police station/Add criminal.html')


def addcriminal_post(request):
    Name = request.POST['textfield']
    photo = request.FILES['fileField']
    from datetime import datetime
    date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    fs = FileSystemStorage()
    fs.save(date, photo)
    path = fs.url(date)

    Identification = request.POST['textfield3']
    DOB = request.POST['textfield4']
    Offense = request.POST['textfield5']
    Height = request.POST['textfield6']
    Weight = request.POST['textfield7']
    Gender = request.POST['RadioGroup1']
    Phoneno = request.POST['textfield9']
    Email = request.POST['textfield10']
    c = Criminal()
    c.criminalname = Name
    c.photo = path
    c.identification = Identification
    c.dob = DOB
    c.offense = Offense
    c.height = Height
    c.weight = Weight
    c.gender = Gender
    c.phoneno = Phoneno
    c.email = Email
    c.save()
    return HttpResponse('''<script>alert('Add Criminal');window.location='/MyApp/addcriminal/'</script>''')


def police_changepassword(request):
    return render(request, 'police station/Change password.html')


def police_changepassword_post(request):
    Currentpassword = request.POST['textfield']
    Newpassword = request.POST['textfield2']
    Confirmpassword = request.POST['textfield3']
    res = Login.objects.filter(id=request.session['lid'], password=Currentpassword)
    if res.exists():
        if Newpassword == Confirmpassword:
            res = Login.objects.filter(id=request.session['lid'], password=Currentpassword).update(
                password=Confirmpassword)
            return HttpResponse('''<script>alert("changed successfully");window.location="/MyApp/login/"</script>''')
        else:
            return HttpResponse(
                '''<script>alert("password mismatch");window.location="/MyApp/police_changepassword/"</script>''')

    else:
        return HttpResponse('''<script>alert("invalid");window.location="/MyApp/police_changepassword/"</script>''')


def editcrimehistory(request):
    return render(request, 'police station/edit  crime history.html')


def editcrimehistory_post(request):
    crimedetail = request.POST['textfield']
    policestation = request.POST['textfield2']
    date = request.POST['textfield3']
    return HttpResponse("ok")


def editcriminal(request, id):
    data = Criminal.objects.get(id=id)
    return render(request, 'police station/edit criminal.html', {'data': data})


def editcriminal_post(request):
    id = request.POST['id']
    Name = request.POST['textfield']
    Identification = request.POST['textfield3']
    DOB = request.POST['textfield4']
    Offense = request.POST['textfield5']
    Height = request.POST['textfield6']
    Weight = request.POST['textfield7']
    Gender = request.POST['RadioGroup1']
    Phoneno = request.POST['textfield9']
    Email = request.POST['textfield10']
    c = Criminal.objects.get(id=id)
    if 'fileField' in request.FILES:
        Photo = request.FILES['fileField']
        if Photo != "":
            from datetime import datetime
            date = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
            fs = FileSystemStorage()
            fs.save(date, Photo)
            path = fs.url(date)
            c.photo = path

    c.criminalname = Name
    c.identification = Identification
    c.dob = DOB
    c.offense = Offense
    c.height = Height
    c.weight = Weight
    c.gender = Gender
    c.phoneno = Phoneno
    c.email = Email
    c.save()
    return HttpResponse("'''<script>alert('updated successfully');window.location='/MyApp/viewcriminal/'</script>''')")


def viewcrimehistory(request):
    a=Crimehistory.objects.all()
    return render(request, 'police station/view crime history.html',{"data":a})


def viewcrimehistory_post(request):
    Fromdate = request.POST['textfield']
    Todate = request.POST['textfield2']
    a=Crimehistory.objects.filter(date_reposted__range=[Fromdate,Todate])
    return render(request, 'police station/view crime history.html',{"data":a})


def viewcriminal(request):
    data = Criminal.objects.all()
    return render(request, 'police station/View criminal.html', {'data': data})


def viewcriminal_post(request):
    search = request.POST['textfield']
    data = Criminal.objects.filter(criminalname__icontains=search)
    return render(request, 'police station/View criminal.html', {'data': data})


def deleteCriminal(request, id):
    Criminal.objects.filter(id=id).delete()
    return redirect('/MyApp/viewcriminal/')


def viewprofile(request):
    data = PoliceStation.objects.get(LOGIN_id=request.session['lid'])
    return render(request, 'police station/view profile.html', {"data": data})


def policehome(request):
    return render(request, 'police station/policestationindex.html')


###############################


def flutt_login(request):
    username = request.POST['username']
    password = request.POST['password']
    res = Login.objects.filter(Username=username, password=password)
    if res.exists():
        res2 = Login.objects.get(Username=username, password=password)
        lid = res2.id
        if res2.type == 'Houseowner':
            return JsonResponse({'status':'ok','lid':str(lid)})
        else:
            return JsonResponse({'status':'no'})

    else:
        return JsonResponse({'status': 'no'})


def flutt_changepassword(request):
    currentpassword = request.POST['currentpassword']
    newpassword = request.POST['newpassword']
    confirmpassword = request.POST['confirm']
    lid = request.POST['lid']
    res = Login.objects.filter(id=lid, password=currentpassword)
    if res.exists():
        if newpassword == confirmpassword:
            res = Login.objects.filter(id=lid, password=currentpassword).update(
                password=confirmpassword)
            return JsonResponse({'status':'ok'})
        else:
            return JsonResponse({'status':'no'})

    else:
         return JsonResponse({'status': 'no'})


def houseownerhome(request):
    try:
        hid = request.session.get('lid')
        house = Houseowner.objects.get(LOGIN_id=hid)
    except Exception:
        house = None
    return render(request, 'houseowner/home.html', {'house': house})

def flutt_register(request):
    ownername = request.POST['ownername']
    housename = request.POST['housename']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    phoneno = request.POST['phoneno']
    photo = request.POST['photo']
    email = request.POST['email']
    password = request.POST['password']
    confirmpassword = request.POST['confirmpassword']


    date=datetime.now().strftime("%y%m%d%H%M%S")
    import base64
    a=base64.b64decode(photo)
    fh=open("C:\\Riss\\Gems\\SMARTBELLWEB\\media\\user\\"+date+".jpg","wb")


    path ="/media/user/"+date+".jpg"
    fh.write(a)
    fh.close()




    lg=Login()
    lg.Username=email
    lg.password=confirmpassword
    lg.type="Houseowner"
    lg.save()
    obj=Houseowner()
    obj.ownername=ownername
    obj.housename=housename
    obj.place=place
    obj.post=post
    obj.pin=pin
    obj.phoneno=phoneno
    obj.LOGIN=lg
    obj.photo=path
    obj.email=email
    obj.save()

    # import qrcode

    # # House Owner's WhatsApp number (with country code)
    # whatsapp_number = "91"+phoneno  # Replace with actual number

    # # WhatsApp call link
    # whatsapp_url = f"https://wa.me/{whatsapp_number}?call"

    # # Generate QR Code
    # qr = qrcode.make(whatsapp_url)

    # # Save the QR code
    # qr.save("C:\\Users\\abhir\\Downloads\\Telegram Desktop\\SMARTBELL\\SMARTBELL\\MyApp\\qr\\"+ownername+".jpg")

    # print("QR Code generated successfully: whatsapp_call_qr.png")

    # import qrcode
    # img = qrcode.make(str(obj.id))
    # type(img)  # qrcode.image.pil.PilImage
    # img.save("C:\\Users\\DELL\\PycharmProjects\\SMARTBELL\\MyApp\\qr\\" + str(obj.id) + ".png")

    # qr = QRcode()
    # qr.HOUSEOWNER = obj
    # qr.date = datetime.now().today()
    # qr.qrimage = '/media/qr/'+str(obj.id)+".png"
    # qr.save()
    return JsonResponse({'status':'ok'})





def qrchecking(request):
    qr=QRcode()
    lid=request.POST['lid']
    scan_id=request.POST['scan_id']
    if Houseowner.objects.filter(LOGIN=lid)==scan_id:
        return JsonResponse({'status': 'ok'})
    else:
        c=Houseowner.objects.get(id=scan_id).phoneno
        return JsonResponse({'status': 'call','number':c})




def flutt_editprofile(request):
    ownername = request.POST['ownername']
    housename = request.POST['housename']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    phoneno = request.POST['phoneno']
    photo = request.POST['photo']
    email = request.POST['email']
    lid = request.POST['lid']
    obj=Houseowner.objects.get(LOGIN=lid)

    if len(photo)>0:

        date=datetime.now().strftime("%y%m%d%H%M%S")
        import base64
        a=base64.b64decode(photo)
        fh=open("C:\\Users\\abhir\\Downloads\\Telegram Desktop\\SMARTBELL\\SMARTBELL\\media\\user\\"+date+".jpg","wb")


        path ="/media/user/"+date+".jpg"
        fh.write(a)
        fh.close()
        obj.photo = path
        obj.save()

    lg=Login.objects.get(id=lid)
    lg.Username=email
    lg.save()
    obj.ownername=ownername
    obj.housename=housename
    obj.place=place
    obj.post=post
    obj.pin=pin
    obj.phoneno=phoneno
    obj.LOGIN=lg
    obj.email=email
    obj.save()
    return JsonResponse({'status': 'ok'})

def flutt_viewprofile(request):
    lid=request.POST['lid']
    data=Houseowner.objects.get(LOGIN_id=lid)
    return JsonResponse({

        'status': 'ok',
        'name':data.ownername,
        'housename':data.housename,
        'place':data.place,
        'post':data.post,
        'pin':data.pin,
        'phoneno':data.phoneno,
        'photo':data.photo,
        'email':data.email,


                         })


def flutt_manageuserdetails(request):
    name = request.POST['name']
    email = request.POST['email']
    phoneno = request.POST['phoneno']
    lid=request.POST['lid']
    photo=request.POST['photo']
    post=request.POST['post']
    pin=request.POST['pin']
    place=request.POST['place']

    date = datetime.now().strftime("%y%m%d%H%M%S")
    import base64
    a = base64.b64decode(photo)
    fh = open("C:\\Riss\\Gems\\SMARTBELLWEB\\media\\member\\" + date + ".jpg", "wb")

    path = "/media/member/" + date + ".jpg"
    fh.write(a)
    fh.close()

    obj=Familymember()
    obj.name=name
    obj.email=email
    obj.phoneno=phoneno
    obj.photo=path
    obj.place=place
    obj.post=post
    obj.pin=pin
    obj.HOUSENAME=Houseowner.objects.get(LOGIN=lid)
    obj.save()


    return JsonResponse({'status': 'ok'})


def flutt_viewcriminals(request):
    data=Criminal.objects.all()
    l=[]
    for i in data:
        l.append({"id":i.id,
                  "criminalname":i.criminalname,
                  "photo":i.photo,
                  "identification":i.identification,
                  "offense":i.offense,
                  "height":i.height,
                  "weight":i.weight,
                  "gender":i.gender})
    return JsonResponse({"status":"ok","data":l})







def flutt_ViewPolicestation(request):
    data=PoliceStation.objects.all()
    l=[]
    for i in data:
        l.append({"id":i.id,
                  "policestationname":i.policestationname,
                  "place":i.place,
                  "post":i.post,
                  "pin":i.pin,
                  "phoneno":i.phoneno,
                  "email":i.email
                  })
    return JsonResponse({"status":"ok","data":l})







def flutt_viewcriminaldetection(request):
    lid=request.POST['lid']
    a=Criminaldetection.objects.filter(HOUSENAME__LOGIN_id=lid)
    l=[]
    for i in a:
        l.append({"id":i.id,
                  "time":i.time,
                  "photo":i.photo,
                  "date":i.date,
                  "criminalname":i.CRIMINALNAME.criminalname,
                  "identification":i.CRIMINALNAME.identification,
                  "height":i.CRIMINALNAME.height,

                  })

    return JsonResponse({"status":'ok',"data":l})


def flutt_sendsuggestions(request):
    suggestion=request.POST['suggestion']
    lid=request.POST['lid']
    sug=Suggestions()
    sug.date=datetime.now()
    sug.suggestion=suggestion
    sug.HOUSEOWNER=Houseowner.objects.get(LOGIN_id=lid)
    sug.save()
    return JsonResponse({'status': 'ok'})


def flutt_sendcomplaint(request):
    complaint=request.POST['complaint']
    lid=request.POST['lid']
    cmp=Complaints()
    cmp.complaint=complaint
    cmp.date=datetime.now()
    cmp.reply='pending'
    cmp.status='pending'
    cmp.HOUSEOWNER=Houseowner.objects.get(LOGIN_id=lid)
    cmp.save()
    return JsonResponse({'status': 'ok'})
def flutt_viewreply(request):
    lid=request.POST['lid']
    a=Complaints.objects.filter(HOUSEOWNER__LOGIN_id=lid)
    l=[]
    for i in a:
        l.append({"id":i.id,"complaint":i.complaint,"reply":i.reply,"date":i.date,"status":i.status})

    return JsonResponse({"status":'ok',"data":l})


def flutt_cameramanagement(request):
    return JsonResponse({'status': 'ok'})
def flutt_viewuser(request):
    lid=request.POST['lid']
    a=Familymember.objects.filter(HOUSENAME__LOGIN_id=lid)
    l=[]
    for i in a:
        l.append({"id":i.id,"name":i.name,"email":i.email,"phoneno":i.phoneno,"photo":i.photo,"place":i.place,"post":i.post,"pin":i.pin,})

    return JsonResponse({"status":'ok',"data":l})

def flutt_deleteuser(request):
    id=request.POST['id']
    Familymember.objects.get(id=id).delete()
    return JsonResponse({'status':'ok'})


def flutt_editfamilymemeber(request):
    name = request.POST['name']
    email = request.POST['email']
    phoneno = request.POST['phoneno']
    lid=request.POST['lid']
    photo=request.POST['photo']
    post=request.POST['post']
    pin=request.POST['pin']
    place=request.POST['place']
    id=request.POST['id']

    obj=Familymember.objects.get(id=id)

    if len(photo)>0:
        date = datetime.now().strftime("%y%m%d%H%M%S")
        import base64
        a = base64.b64decode(photo)
        fh = open("C:\\Users\\abhir\\Downloads\\Telegram Desktop\\SMARTBELL\\SMARTBELL\\media\\member\\" + date + ".jpg", "wb")

        path = "/media/member/" + date + ".jpg"
        fh.write(a)
        fh.close()
        obj.photo = path
        obj.save()

    obj.name=name
    obj.email=email
    obj.phoneno=phoneno
    obj.place=place
    obj.post=post
    obj.pin=pin
    obj.HOUSENAME=Houseowner.objects.get(LOGIN=lid)
    obj.save()


    return JsonResponse({'status': 'ok'})



def flutt_edituserget(request):
    id=request.POST['id']
    data=Familymember.objects.get(id=id)
    return JsonResponse({

        'status': 'ok',
        'name':data.name,
        'email':data.email,
        'phoneno':data.phoneno,
        'place':data.place,
        'pin':data.pin,
        'photo':data.photo,
        'post':data.post,


                         })



def Viewnotificationalert(request):
    nid=request.POST['nid']
    if nid=="null":
        nid=0
    res=Criminaldetection.objects.filter(id__gt=nid).order_by("id")
    if res.exists():
        i=res[0]
        return JsonResponse({"status":"ok","message":i.CRIMINALNAME.criminalname,'nid':i.id})
    else:
        return JsonResponse({'status':'no'})


def deletecriminaldetection(request):
    id=request.POST['id']
    Criminaldetection.objects.get(id=id).delete()
    return JsonResponse({"status":"ok"})




###################

# import qrcode
# id_value = "1"
# import qrcode
# img = qrcode.make(str(id_value))
# type(img)
# img.save("C:\\Users\\abhir\\Downloads\\Telegram Desktop\\SMARTBELL\\SMARTBELL\\MyApp\\qr\\" + str(id_value) + ".png")
# def get_user(request):
#     h="http://localhost:8000/{id_value}"
#     qr = qrcode.make(h)
#     c = Houseowner.objects.get(id=id_value).phoneno
#     qr.save()
#     return


