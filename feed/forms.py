from django import forms
from .models import Post
from django.core.files.base import ContentFile
from django.utils.text import slugify
from urllib import request

# formularz odpowiedzalny za przekazywanie obrazow
class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'img' ,'url' , 'description')

        widgets = {
            'img:': forms.ImageField,
            'url': forms.HiddenInput
        }
    # metoda clean_ url dziek ktorej mozliwe bedzie sprawdzienie url zdjecia z formatem 'jpeg' , 'jpg'

    def clean_url(self):
        url = self.cleaned_data['url']
        suppExt = ['jpeg', 'jpg', 'png']
        ext = url.rsplit('.', 1)[1].lower
        if ext not in suppExt:
            raise forms.ValidationError('Niestety ten adres URL posiada '
                                        'nieobsługiwany przez nas format.')
        return url

    # metoda save dzieki ktorej mozliwy bedzie zapis w bazie danych

    def save(self, force_insert=False, force_update=False, commit=True ):
        img = super(CreatePostForm, self).save(commit=False)
        img_url = self.cleaned_data['url']
        img_name = '{}.{}'.format(slugify(img.title),
                                  img_url.rsplit('.', 1)[1].lower())
        reply = request.urlopen(img_url)
        img.img.save(img_name,ContentFile(reply.read()), save=False)
        if commit:
            img.save()
        return img
