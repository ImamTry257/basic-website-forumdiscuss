from django.db.models import fields
from django.forms import ModelForm
from .models import *

class CreateInForum(ModelForm):
    class Meta:
        model = Forum
        fields = "__all__"

class CreateInDiscuss(ModelForm):
    class Meta:
        model = Forum
        fields = "__all__"