from django.shortcuts import render
from modelformapp.forms import MyModelForm

# Create your views here.
def modelFormView(request):
    myForm = MyModelForm()
    return render (request, 'index2.html', {'forms': myForm})
    # return render(request, 'index.html', {'form': myForm})
