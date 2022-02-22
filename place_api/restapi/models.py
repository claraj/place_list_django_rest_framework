from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

class Place(models.Model):
    user = models.ForeignKey('auth.User', blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    reason = models.CharField(max_length=200, blank=True, null=True)  # reason not required
    starred = models.BooleanField(default=False, null=False)
    # dateAdded = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = [ ['user', 'name' ] ]

    
    def save(self, *args, **kwargs):
        if not self.id: # no ID so new object, not updating an existing object 
            if Place.objects.filter(user=self.user).filter(name__iexact=self.name).first():
                raise ValidationError(f'Duplicate place name {self.name}')

        super().save(*args, **kwargs)

    def __str__(self):
        return f'Place {self.id}. Name: {self.name} reason: {self.reason or "no reason"} starred: {self.starred}  belongs to {self.user}'