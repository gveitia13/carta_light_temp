from .models import *
from django.forms import *


class ProductoForm(ModelForm):
    # categoria = ModelChoiceField(queryset=Categoria.objects.filter(usuario=User.objects.get(username='angulo')))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # populates the post
        user = ""
        try:
            user = get_object_or_404(User, username=self.instance.cfg.usuario.username)
        except:
            return
        self.fields['categoria'].queryset = Categoria.objects.filter(usuario=User.objects.get(username=user))

    class Meta:
        model = Product
        fields = '__all__'
