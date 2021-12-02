from .models import *
from django.forms import *
class ProductoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)  # populates the post
        self.fields['categoria'].queryset = Categoria.objects.filter(usuario=self.instance.cfg.usuario)


    class Meta:
        model = Product
        fields = "__all__"
