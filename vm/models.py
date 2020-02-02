from django.db import models


class Convener(models.Model):
    #vp = vp means ... visitng person 
    vp_id = models.AutoField(primary_key =  True )
    vp_name = models.CharField(max_length = 200 , default = '')
    vp_mobile = models.CharField(max_length = 13 , default = "")
    vp_email = models.CharField(max_length = 100 , default = "")
    vp_profession = models.CharField(max_length = 500 , default="") #what is the couurent job status ..
    vp_work = models.CharField(max_length = 500) #what is he doing ??
    vp_start_time = models.TimeField()
    vp_end_time = models.TimeField()

    def __str__(self):
        return self.vp_name

    def get_absolute_url(self):
        pass

# Create your models here.
class Visitor(models.Model):
    v_id = models.AutoField(primary_key =  True )
    v_name = models.CharField(max_length = 200 , default = '')
    v_mobile = models.CharField(max_length = 13 , default = "")
    v_email = models.CharField(max_length = 100 , default = "")
    v_perpose = models.CharField(max_length = 100 , default = "")
    v_address = models.CharField(max_length = 100 , default = "")
    v_time = models.DateTimeField(auto_now_add = True)
    v_otp = models.CharField(default="", max_length=10)
    v_mobile_verify = models.BooleanField( default=False )
    # vp valu baki
    def __str__(self):
        return self.v_name

    def get_absolute_url(self):
        # return reverse("Visitor_detail", kwargs={"pk": self.pk})
        pass





class Meeting(models.Model):
    m_id = models.AutoField( primary_key = True )
    v_id = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    vp_id = models.ForeignKey(Convener, on_delete=models.CASCADE)
    v_login_time = models.DateTimeField(blank=True, null=True)
    v_logout_time = models.DateTimeField(blank=True, null=True)
    v_meeting_done = models.BooleanField( default= False )
    vp_approved = models.BooleanField( default= True )

    def __str__(self) :
        str = f'{self.m_id} .  {self.v_id} => {self.vp_id}' 
        return  str

    def get_absolute_url(self):
        pass