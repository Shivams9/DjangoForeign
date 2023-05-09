from django.db import models


# Create your models here.
class jobModel(models.Model):
    name = models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    details = models.CharField(max_length=60)
    experience=models.CharField(max_length=50)
    resume=models.FileField() #for creating file input


class employeeModel(models.Model):
    user_name = models.CharField(max_length=100)
    emp=models.ForeignKey(jobModel,on_delete=models.CASCADE)

    def name(self):
        return self.emp.name

    def __str__(self):
        return "name={0},email={1},contact={2},details={3},experience={4},resume={5}".format(self.name, self.email,
                                                                                 self.contact, self.details,self.experience,self.resume)


