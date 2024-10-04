from django.views import View
from django.shortcuts import render, redirect
from .forms import ContactForm

class IndexView(View):
    index_template_name = 'index.html'
    career_template_name = 'career.html'
    home_template='home.html'

    def get(self, request, page=None):
        if page == 'home':
            return render(request, self.home_template)
        elif page=='career':
            return render(request,self.career_template_name)
        return render(request, self.index_template_name)




def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the data to the database
            return redirect('success')  # Redirect to a success page or the same page with a success message
    else:
        form = ContactForm()

    return render(request, 'your_template.html', {'form': form})  # Replace 'your_template.html' with the actual template name

