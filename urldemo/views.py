from django.shortcuts import render
from django.http import HttpResponse


def article_detail(request, article_id, slug):
    # The captured values from the URL are passed as positional arguments.
    # Here, article_id will contain the numeric value and slug will contain the word.
    
    # Sample implementation: Construct a response with the captured values.
    response = f"Article ID: {article_id}, Slug: {slug}"
    return HttpResponse(response)


def product_detail(request, product_name, product_id):
    # The captured values from the URL are passed as positional arguments.
    # Here, product_name will contain the word and product_id will contain the numeric value.
    
    # Sample implementation: Construct a response with the captured values.
    response = f"Product Name: {product_name}, Product ID: {product_id}"
    return HttpResponse(response)
