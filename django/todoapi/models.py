from django.db import models

from datetime import date

# Create the Recipee class to describe the model.
class Recepee(models.Model):
    """Stores a recipee."""
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)

    # Date the Recipee was created.
    created_on = models.DateField(default=date.today)

    # Due date.
    due_date = models.DateField(default=date.today)

    # Meta data about the database table.
    class Meta:
        # Set the table name.
        db_table = 'task'

        # Set default ordering
        ordering = ['id']

    # Define what to output when the model is printed as a string.
    def __str__(self):
        return self.title
