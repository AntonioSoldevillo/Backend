
from django.http import HttpResponse
from django.views import View

class TodoListView(View):
    def get(self, request):
        return HttpResponse("List of todos")
