from django.db import models

# Create your models here.
class Chai(models.Model):
  CHAI_TPYE_CHOICES = [
    ('Masala Chai', 'Masala Chai'),
    ('Ginger Chai', 'Ginger Chai'),
    ('Lemon Chai', 'Lemon Chai'),
    ('Black Tea', 'Black Tea'),
    ('Green Tea', 'Green Tea'),
    ]
  
  name = models.CharField(max_length=100)
  email=models.EmailField()
  phone=models.CharField(max_length=10)
  image=models.ImageField(upload_to='photos')
  type=models.CharField(max_length=15, choices=CHAI_TPYE_CHOICES, default='Masala Chai')

  def __str__(self):
    return self.name
