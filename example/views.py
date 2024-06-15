from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
import datetime

# Create your views here.
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src) # Cargar la plantilla HTML.
    html = template.render(context_dict) # Renderizar la plantilla con el contexto.
    result = BytesIO() # Crear un buffer en memoria para el PDF.
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result) # Convertir HTML a PDF.
    if not pdf.err: # Si no hubo errores en la conversión.
        return HttpResponse(result.getvalue(), content_type='application/pdf') # Devolver el PDF como respuesta HTTP.
    return None # Devolver None si hubo algún error.

"""Vista para generar un PDF basado en una plantilla HTML y un contexto."""
def generate_invoice_pdf(request):
    context = {
        'invoice_number': 12345,
        'customer_name': 'John Doe',
        'amount': '$100.00',
        'date': datetime.datetime.now().strftime("%Y-%m-%d")
    }
    pdf = render_to_pdf('pdfs/invoice.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="invoice.pdf"'
        return response
    return HttpResponse("Error generating PDF", status=400)
