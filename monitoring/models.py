from django.db import models
from django.core.mail import send_mail
# Create your models here.
#mydb model for table that have DATA
class mydb(models.Model):
    temp = models.FloatField(null=True)
    hum = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True,null=True)

    #This Model for send alerts to email when temp > 40
    def __str__(self):
        return str(self.temp)    
        
    def save(self, *args, **kwargs):
        if self.temp > 40:
            send_mail(
                'température dépasse la normale,' + str(self.temp),
                'anomalie dans la machine, Merci de Vérifier Votre Machine/Sensor',
                'anouar.harrou@ump.ac.ma', #from 
                ['anouar_-_harrou@outlook.fr'], # to adress reception
                fail_silently=False,)
        
        return super().save(*args, **kwargs)