from links.models import Booklink
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
# from django.views.generic.list import ListView

# Create your views here.
# def links_view(request):
#     return render(request,"links/study.html")

# class links_view(ListView):
#     template_name = "links/study.html"
#     model = Booklink
#     context_object_name = "booklist"
#     # queryset = Booklink.objects.filter(object.book_link == "Weekly News Headlines")
    
class links_view(TemplateView):
    template_name = "links/study.html" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        qu1 = Booklink.objects.filter(book_type=6)
        context["qu1"] = qu1
        qu2 = Booklink.objects.filter(book_type=4)
        context["qu2"] = qu2
        qu3 = Booklink.objects.filter(book_type=3)
        context["qu3"] = qu3
        qu4 = Booklink.objects.filter(book_type=1)
        context["qu4"] = qu4
        qu5 = Booklink.objects.filter(book_type=5)
        context["qu5"] = qu5
        qu6 = Booklink.objects.filter(book_type=2)
        context["qu6"] = qu6
        return context

    
