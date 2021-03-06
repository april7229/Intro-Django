from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
# id is randomly generated by UUID
# https://en.wikipedia.org/wiki/Universally_unique_identifier
# Primary key is how the database tracks records.
# Default calls a function to randomly generate a unique identifier.
# We make editable false because we never want to change the key.
# Put it at the top of the list of fields
# because it’s sort of like the index for the record.
# `auto_now_add` only sets on create and `auto_now` for both create and update


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<{self.__class__.__name__}: {self.id} {self.title}>'


# foreign key to create a reference to data on another table.
# It works sort of like a pointer in C.
# `on_delete=models.CASCADE` helps with the integrity of the data
class PersonalNote(Note):   # Inherits from Note!
    user = models.ForeignKey(User, on_delete=models.CASCADE)
