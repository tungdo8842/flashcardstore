from django.db import models


class CardList(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=256)

    def __str__(self):
        return self.name

# Create your models here.
class Card(models.Model):
    card_list = models.ForeignKey(CardList, on_delete=models.CASCADE)
    index = models.IntegerField()
    front = models.TextField(max_length=2048)
    back = models.TextField(max_length=2048)
    score = models.IntegerField()

    def __str__(self):
        return self.front
