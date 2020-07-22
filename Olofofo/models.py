from django.db import models

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

CATEGORY = (
    (0, "News"),
    (1, "Entertainment"),
    (2, "Sports"),
    (3, "WorldNews"),
)

AUTHOR = (
    (0, 'Seriki Oluwaranti'),
    (1, 'Seriki Ayo'),
)


class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    author = models.IntegerField(choices=AUTHOR, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='images/', blank=True)
    image1 = models.ImageField(upload_to='images/', blank=True)
    image2 = models.ImageField(upload_to='images/', blank=True)
    category = models.IntegerField(choices=CATEGORY, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/Olofofo/{self.slug}"

