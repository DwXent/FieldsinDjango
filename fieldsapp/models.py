from django.db import models
import uuid
from django.template.defaultfilters import slugify
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.auth.models import User

my_choices = (
    ('one', 'number one'),
    ('two', 'number two')
)

class TestModel(models.Model):
    boolean = models.BooleanField(
        default=True, verbose_name="This is Raman site"
    )
    char = models.CharField(verbose_name="Name", max_length=5 ,unique=True, help_text="added help text")
    date = models.DateField(default=timezone.now)
    decimal = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField(max_length=200)
    file = models.FileField(upload_to='uploads', blank=False)
    image = models.ImageField(upload_to='uploads', blank=False)
    integer = models.IntegerField()
    positive_int =models.PositiveIntegerField()
    positive_small_int =models.PositiveSmallIntegerField()
    


    slug = models.SlugField(blank=False)


    text = models.TextField()
    url = models.URLField(max_length=200)
    uuid1 = models.UUIDField(default=uuid.uuid4)
    uuid2 = models.UUIDField(default=uuid.uuid4,primary_key=True, editable=False)
    updated = models.DateTimeField(auto_now=False)
    created = models.DateTimeField(auto_now_add=False)
    date_and_time = models.DateTimeField()

    choice = models.CharField(max_length=10, choices=my_choices)

    phone_number= PhoneNumberField()
    new_field = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    new_field = models.CharField(max_length=10, null=True, blank=False)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.text[:30])
        super(TestModel, self).save(*args, **kwargs)
























