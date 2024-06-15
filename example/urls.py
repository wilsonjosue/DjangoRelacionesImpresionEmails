# example/urls.py: Añade la URL para la vista de generación de PDFs.
from django.urls import path
from .views import send_test_email, generate_invoice_pdf

urlpatterns = [
    path('send-email/', send_test_email, name='send_email'),
    path('generate-invoice-pdf/', generate_invoice_pdf, name='generate_invoice_pdf'),
]
