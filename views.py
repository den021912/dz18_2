from django.shortcuts import render

# Create your views here.
def class_template(request):
    return render(request, 'templates/second_task/class_template.html')
def func_template(request):
    return render(request, 'templates/second_task/func_template.html')
