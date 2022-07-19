from django.shortcuts import render


def products(request):
    """ A view to return the index page """

    return render(request, 'products/products.html')
