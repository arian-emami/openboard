from django.db import models


class IndexPage(models.Model):
    """acts as a setting for index page."""

    welcome_title = models.CharField(max_length=50)
    welcome_description = models.TextField()
    is_default = models.BooleanField()

    def save(self, *args, **kwargs):
        """make it so only one indexpage can be the default"""
        if self.is_default:
            try:
                temp = IndexPage.objects.get(is_default=True)
                if self != temp:
                    temp.is_default = False
                    temp.save()
            except IndexPage.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"default: {self.is_default} || {self.welcome_title}"


class Board(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    rules = models.TextField()
    is_default = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """make it so only one board can be the default"""
        if self.is_default:
            try:
                temp = Board.objects.get(is_default=True)
                if self != temp:
                    temp.is_default = False
                    temp.save()
            except Board.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["name"], name="unique board")]

    def tag_count(self):
        return self.tag_set.count()

    def post_count(self):
        return self.post_set.count()

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.SlugField(max_length=15)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    show_in_header = models.BooleanField(
        default=False
    )  # if True the tag will be shown at top of the page as a shortcut

    class Meta:
        ordering = ["name"]

    def post_count(self):
        return self.post_set.count()

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=80, blank=False)
    date_posted = models.DateTimeField(blank=False)
    url = models.URLField(blank=False)
    url_title = models.TextField(max_length=200, blank=False)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, blank=False)
    post_text = models.TextField(max_length=600, blank=False)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ["-date_posted"]

    def __str__(self) -> str:
        return self.title


class Reply(models.Model):
    date_posted = models.DateTimeField(blank=False)
    post_text = models.TextField(max_length=600, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False)

    class Meta:
        ordering = ["-date_posted"]

    def __str__(self) -> str:
        return f"{str(self.date_posted)} on {self.post}"
