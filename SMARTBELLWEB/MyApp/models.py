from django.db import models


# Create your models here.
class Login(models.Model):
    Username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=100)


class PoliceStation(models.Model):
    policestationname = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)


class Houseowner(models.Model):
    ownername = models.CharField(max_length=100)
    housename = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=20)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    photo = models.CharField(max_length=200)
    email = models.CharField(max_length=100)


class Complaints(models.Model):
    complaint = models.CharField(max_length=100)
    date = models.DateField()
    reply = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    HOUSEOWNER = models.ForeignKey(Houseowner, on_delete=models.CASCADE)


class Suggestions(models.Model):
    suggestion = models.CharField(max_length=100)
    date = models.DateField()
    HOUSEOWNER = models.ForeignKey(Houseowner, on_delete=models.CASCADE)


class Criminal(models.Model):
    criminalname = models.CharField(max_length=100)
    photo = models.CharField(max_length=200)
    identification = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    offense = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=20)
    email = models.CharField(max_length=100)


class Crimehistory(models.Model):
    casenumber = models.CharField(max_length=100)
    date_reposted = models.CharField(max_length=100)
    date_occured = models.CharField(max_length=100)
    crime_type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    victim = models.CharField(max_length=100)
    suspect = models.CharField(max_length=100)
    arrest_date = models.CharField(max_length=100)
    charge = models.CharField(max_length=100)
    sentence = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    POLICE = models.ForeignKey(PoliceStation, on_delete=models.CASCADE)


class Familymember(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=20)
    photo = models.CharField(max_length=200)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    HOUSENAME = models.ForeignKey(Houseowner, on_delete=models.CASCADE)


class Criminaldetection(models.Model):
    date=models.DateField()
    time=models.CharField(max_length=100)
    photo=models.CharField(max_length=250)
    type=models.CharField(max_length=100)
    CRIMINALNAME = models.ForeignKey(Criminal, on_delete=models.CASCADE)
    HOUSENAME = models.ForeignKey(Houseowner, on_delete=models.CASCADE)



class QRcode(models.Model):
    HOUSEOWNER = models.ForeignKey(Houseowner, on_delete=models.CASCADE)
    date=models.DateField()
    qrimage=models.CharField(max_length=300)



class familiarpersondetection(models.Model):
    date=models.DateField()
    time=models.CharField(max_length=100)
    photo=models.CharField(max_length=250)
    HOUSENAME = models.ForeignKey(Houseowner, on_delete=models.CASCADE)

