from django.db import models


# send product image in assets/images folder
def file_location(instance, filename):
    file_path = f"static/photos/{instance.label}-{filename} "
    return file_path


class Species(models.Model):
    species = models.CharField(max_length=20)

    class Meta:
        db_table = "Espèces"

    def __str__(self):
        return self.species


class Status(models.Model):
    status = models.CharField(max_length=30)

    class Meta:
        db_table = "Status"

    def __str__(self):
        return self.status


class Color(models.Model):
    color = models.CharField(max_length=25)

    class Meta:
        db_table = "Couleur"

    def __str__(self):
        return self.color


class Animal(models.Model):
    species = models.ForeignKey(Species, models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=20)
    personnality = models.TextField()
    history = models.TextField()
    color = models.ManyToManyField(Color, related_name='animal')
    status = models.ForeignKey(Status, models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = "Animal"

    def __str__(self):
        return self.name


class Photo(models.Model):
    photo = models.ImageField(upload_to=file_location, blank=True, null=True)
    animal = models.ForeignKey(Animal, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = "Photo"

