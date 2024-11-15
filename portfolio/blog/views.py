from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "blog/blog.html")

def variables(request):

    return render(request=request, template_name="blog/vars.html")