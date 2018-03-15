from django.shortcuts import render
#new addition
from django.views.generic import UpdateView, ListView, View, FormView
from django.http import HttpResponse
from django.template.loader import render_to_string
# from myapp.models import Item
# from myapp.forms import ItemForm

from newsletter.forms import JoinForm

# Create your views here.

# def home(request):
# 	return render(request, "home.html", {})

class HomeView(FormView):
    template_name = 'templates/home.html'
    form_class = JoinForm
# """
# items list
# """
# class ItemListView(ListView):
#     model = Item
#     template_name = 'myapp/item_list.html'

#     def get_queryset(self):
#         return Item.objects.all()

# """
# Edit item
# """
# class ItemUpdateView(UpdateView):
#     model = Item
#     form_class = ItemForm
#     template_name = 'myapp/item_edit_form.html'

#     def dispatch(self, *args, **kwargs):
#         self.item_id = kwargs['pk']
#         return super(ItemUpdateView, self).dispatch(*args, **kwargs)

#     def form_valid(self, form):
#         form.save()
#         item = Item.objects.get(id=self.item_id)
#         return HttpResponse(render_to_string('myapp/item_edit_form_success.html', {'item': item}))