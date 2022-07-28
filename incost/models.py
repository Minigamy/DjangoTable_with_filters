from django.db import models


class Clients(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Modes(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Durations(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    start = models.TextField(max_length=100)
    stop = models.TextField(max_length=100)
    mode_id = models.ForeignKey(Modes, on_delete=models.CASCADE)
    minutes = models.IntegerField()

