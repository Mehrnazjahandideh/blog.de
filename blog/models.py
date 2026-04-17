from django.db import models


# Create your models here.
class Post(models.Model):
    STATUS=(
        ('pub','published'),
        ('drf','draft')
    )
   
    ABOUT=(
        ('BAVARIA','Bavaria'),
        ('BADEN-WURTTEMBERG','Baden-wurttemburg'),
        ('NORTH RHINE-WESTPHALIA','North Rhine-Westphalia'),
        ('BERLIN','Berlin'),
        ('HAMBURG','Hamburg'),
        ('BRANDENBURG','Brandenburg'),
        ('BREMEN','Bremen'),
        ('HESSEN','Hessen'),
        ('MECKLENBURG-VORPOMMERN','Mecklenburg‑Vorpommern'),
        ('NIEDERSACHSEN','Niedersachsen'),
        ('RHEINLAND-PFALZ','Rheinland‑Pfalz'),
        ('SAARLAND','Saarland'),
        ('SACHSEN','Sachsen '),
        ('SACHSEN-ANHALT','Sachsen‑Anhalt'),
        
    )
    title=models.CharField(max_length=150)
    text=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    status=models.CharField(choices=STATUS,max_length=20)
    about=models.CharField(choices=ABOUT)
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    def __str__(self):
        return self.title