from django.db import models

# Create your models here.


# Model for Selling of Phone

class Selling(models.Model):

    #sellers info 
    name_of_customer = models.CharField(max_length=60, null = True)
    contact_number = models.IntegerField(null = True)
    email = models.CharField(max_length=60, null = True)

    #product info 
    name_of_phone = models.CharField(max_length = 100, null = True)
    about = models.CharField(max_length=240, null = True)
    ram = models.IntegerField(null = True)
    color = models.CharField(max_length=60, null = True)
    storage = models.IntegerField( null = True)


    #pricing 
    price = models.FloatField(max_length = 40, null=True)

    #images of product 
    image1 = models.ImageField(null = True , upload_to = "products")
    image2 = models.ImageField(null = True , upload_to = "products")
    
    
    #status 
    Status =  (
        ('Pending' , 'Pending'),
        ('Sold', 'Sold'),
        ('Approved', 'Approved'),
    )

    status = models.CharField(choices=Status, null=False  ,max_length = 60, default="Pending")#default status will be Pending as soon as The seller submits the form

    #date and timme
    date_time = models.DateTimeField(auto_now_add=True, null= True)


    def __unicode__(self):
        return self.name_of_phone

