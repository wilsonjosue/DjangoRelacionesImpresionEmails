# example/urls.py: Añade la URL para la vista de generación de PDFs.
from django.urls import path
from .views import generate_invoice_pdf

urlpatterns = [
    path('generate-invoice-pdf/', generate_invoice_pdf, name='generate_invoice_pdf'),
]
