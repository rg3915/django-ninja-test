from django.shortcuts import render

def customer_list(request):
    template_name = 'crm/customer_list.html'
    return render(request, template_name)
