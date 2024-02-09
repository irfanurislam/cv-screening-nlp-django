 # jobs/views.py
# from django.shortcuts import render, redirect
# from .forms import CandidateForm

# def job_application(request):
#     if request.method == 'POST':
#         form = CandidateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('success_page')  # Redirect to a success page
#     else:
#         form = CandidateForm()

#     return render(request, 'jobs/job_application.html', {'form': form})



from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CandidateForm

def job_application(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Add a success message
            messages.success(request, 'Your application has been successfully submitted!')

            # Redirect to a success page or render a template with the submitted information
            # Example: return redirect('success_page')
            # Or render a template with the submitted information
            return render(request, 'jobs/success_page.html', {'candidate': form.instance})
    else:
        form = CandidateForm()

    return render(request, 'jobs/job_application.html', {'form': form})





from .models import Candidate

def job_list(request):
    candidate  = Candidate.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': candidate})

# jobs/views.py
from django.shortcuts import render, get_object_or_404

def job_detail(request, id):
    job = get_object_or_404(Candidate, pk= id)
    return render(request, 'jobs/job_detail.html', {'job': job})


# apply jobs
def apply_job(request,):
    return render(request, 'jobs/apply_job.html', )
