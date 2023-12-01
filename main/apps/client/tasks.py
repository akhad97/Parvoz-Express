# # tasks.py
# from celery import shared_task
# from django.template.loader import render_to_string
# import pdfkit
# from datetime import datetime
# from django.http import HttpResponse
# from .serializers import ClientSerializer  # Make sure to import your actual serializer
# from .models import Client  # Import your Client model
# from django.template.loader import render_to_string

# @shared_task
# def generate_pdf(client_id):
#     client = Client.objects.get(pk=client_id)

#     serializer = ClientSerializer(client)
#     client_first_name = client.first_name
#     client_last_name = client.last_name
#     client_middle_name = client.middle_name
#     client_passport_series = client.passport_series
#     current_date = datetime.now() 
#     year = current_date.year
#     month = current_date.strftime('%B')
#     day = current_date.day
#     hotel_name = client.hotel.title
#     html_content = render_to_string('client.html', 
#                                     {
#                                         'data': serializer.data, 
#                                         'client_first_name': client_first_name,
#                                         'client_last_name': client_last_name,
#                                         'client_middle_name': client_middle_name,
#                                         'client_passport_series': client_passport_series,
#                                         'year': year,
#                                         'month': month,
#                                         'day': day,
#                                         'hotel_name': hotel_name,
#                                     })

#     pdf_file = pdfkit.from_string(html_content, False) 

#     # Save the PDF into the client_pdf field
#     client.client_pdf.save(f'{client.first_name}_{client.last_name}_{current_date.year}_{current_date.month}_{current_date.day}.pdf', ContentFile(pdf_file))

#     return f'PDF saved to {client.client_pdf.url}'

