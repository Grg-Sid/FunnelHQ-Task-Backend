from django.db import models
from django.conf import settings

GENRE_FIC = "FIC"
GENRE_NONFIC = "NFIC"
GENRE_FANTASY = "FAN"
GENRE_ROMANCE = "ROM"
GENRE_MYSTERY = "MYS"
GENRE_SCIFI = "SCI"
GENRE_HORROR = "HOR"
GENRE_HISTORY = "HIS"

GENRE_CHOICES = [
    (GENRE_FIC, "Fiction"),
    (GENRE_NONFIC, "Non-Fiction"),
    (GENRE_FANTASY, "Fantasy"),
    (GENRE_ROMANCE, "Romance"),
    (GENRE_MYSTERY, "Mystery"),
    (GENRE_SCIFI, "Science Fiction"),
    (GENRE_HORROR, "Horror"),
    (GENRE_HISTORY, "History"),
]


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    bio = models.TextField(max_length=500, blank=True)
    genre = models.CharField(max_length=4, choices=GENRE_CHOICES, blank=True)
    fav_author = models.CharField(max_length=100, blank=True)


class Books(models.Model):
    title = models.CharField(max_length=100, blank=True)
    author = models.CharField(max_length=100, blank=True)
    genre = models.CharField(max_length=4, choices=GENRE_CHOICES, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="books"
    )

    def __str__(self):
        return self.title
