from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Place(models.Model):
    user = models.ForeignKey('auth.User', blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    reason = models.CharField(max_length=200, blank=True, null=True)  # reason not required
    # priority = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        unique_together = [ ['user', 'name' ] ]

    def __str__(self):
        return f'Place {self.id}. Name: {self.name} reason: {self.reason or "no reason"} rating: {self.priority} belongs to {self.user}'