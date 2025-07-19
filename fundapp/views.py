from django.shortcuts import render, redirect
from .models import Contribution
from .forms import ContributionForm
from django.contrib.auth.decorators import login_required


TARGET_AMOUNT = 20585000

@login_required(login_url='login')
def tracker_view(request):
    contributions = Contribution.objects.order_by('-timestamp')
    total_collected = sum(c.amount for c in contributions)
    progress = round((total_collected / TARGET_AMOUNT) * 100, 2) if TARGET_AMOUNT else 0

    if request.method == 'POST':
        form = ContributionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracker')
    else:
        form = ContributionForm()

    context = {
        'form': form,
        'contributions': contributions,
        'total_collected': total_collected,
        'progress': progress,
        'target_amount': TARGET_AMOUNT,
    }
    return render(request, 'tracker.html', context)


def contribution_list(request):
    contributions = Contribution.objects.all().order_by('-timestamp')  # most recent first
    return render(request, 'table.html', {'contributions': contributions})
