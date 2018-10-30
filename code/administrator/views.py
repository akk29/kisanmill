from django.shortcuts import render
from ufs.models import Message
from customercorner.models import Product
from django.views.generic import DetailView, ListView , CreateView , DeleteView , TemplateView

class MessageListView(ListView):
    model = Message
    template_name = 'administrator/complaints.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.all()

class MessageDetailView(DetailView):
    model = Message
    template_name = 'administrator/complaint_description.html'
    context_object_name = 'complaint_detail'

def adminhome(request):
    return render(request,'administrator/admin.html')
