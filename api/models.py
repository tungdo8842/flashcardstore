from django.db import models

class Deck(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=256)

    def __str__(self):
        return self.name


class Card(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    index = models.IntegerField()
    front = models.TextField(max_length=2048)
    back = models.TextField(max_length=2048)
    score = models.IntegerField()
    pk = models.CompositePrimaryKey("deck_id", "index")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["deck", "index"], name="unique_deck_index")
        ]
        ordering = ["deck", "index"]


    def __str__(self):
        return self.front
