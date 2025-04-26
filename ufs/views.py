from django.views.generic.edit import CreateView
from .forms import MessageForm
from .models import Message

class MessageCreateView(CreateView):
    model = Message
    # form_class = MessageForm
    fields = ['title','effected_crop','Description','Images']
    template_name = 'ufs/message.html'
    context_object_name = 'form'
    success_url = '/'
