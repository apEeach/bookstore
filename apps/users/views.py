from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View


class ShoppingCartView(View):
    def get(self, request):
        return render(
            request,
            'shopping_cart.html',
        )
