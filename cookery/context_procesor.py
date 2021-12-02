#Reference: https://docs.djangoproject.com/en/1.9/ref/templates/api/#writing-your-own-context-processors
#This file is in yourapp/ directory

from .models import ConfiguracionGodlango
def foo(request):
  # you might need this line for unit tests
  cfg = ""
  if request.user.is_authenticated and request.user.is_active:
    cfg = ConfiguracionGodlango.objects.all()[0].url
  return {"cfg_global" :cfg}