import re
import fitz  # PyMuPDF
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Aadhar
from .serializers import AadharSerializer
from django.shortcuts import render

def index(request):
    return render(request, 'document/index.html')

@api_view(['POST'])
def extract_aadhar(request):
    file = request.FILES.get('document_pdf')
    
    if not file or not file.name.endswith('.pdf'):
        return Response({"error": "Please upload a valid PDF file."}, status=status.HTTP_400_BAD_REQUEST)

    # Initialize an empty string to hold PDF text
    pdf_text = ""
    
    # Extract text from PDF using PyMuPDF
    with fitz.open(stream=file.read(), filetype="pdf") as pdf:
        for page_num in range(pdf.page_count):
            page = pdf[page_num]
            pdf_text += page.get_text()

    # Find a 12-digit sequence that matches an Aadhar number format
    aadhar_match = re.search(r'\b\d{4}\s?\d{4}\s?\d{4}\b', pdf_text)

    if not aadhar_match:
        return Response({"error": "No Aadhar number found in the document."}, status=status.HTTP_400_BAD_REQUEST)

    # Extract the matched Aadhar number and remove spaces
    aadhar_number = aadhar_match.group().replace(" ", "")

    # Save Aadhar number to the database
    serializer = AadharSerializer(data={"aadhar_number": aadhar_number})
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
