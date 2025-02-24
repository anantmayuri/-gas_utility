from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

def service_request_list(request):
    requests = ServiceRequest.objects.all()  # Fetch existing requests
    return render(request, 'service_requests/list.html', {'requests': requests})

def service_request_create(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()  # Save the request to the database
            return redirect('service_requests_list')  # Redirect to list page
    else:
        form = ServiceRequestForm()

    return render(request, 'service_requests/create.html', {'form': form})
