from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
# Create your views here.
@csrf_exempt
def DataUploadAPI(request):
    if request.method == "POST":
        Data = json.loads(request.body)

        Fullname = Data.get('Fullname')
        Number = Data.get('Phone')
        Location = Data.get('Location')
        Type = Data.get('Type')
        Status = Data.get('Status')

        DataStore.objects.create(
            Name = Fullname,
            Phone = Number,
            Location = Location,
            Type = Type,
            Status = Status
        )
    return JsonResponse({
        "Status" : "Done",
        "Message" : "Data Uploaded done"
    })

def DataViewAPI(request):
    if request.method == "GET":
        records = []

        for x in DataStore.objects.all():
            details = model_to_dict(x)
            records.append(details)

        return JsonResponse({
            "Status": "Data fetched",
            "Data": records
        })

    return JsonResponse({
        "Status": "Error",
        "Message": "Only GET allowed"
    })

@csrf_exempt
def DataDeleteAPI(request, id):
    if request.method == "DELETE":
        data = DataStore.objects.get(id = id)
        data.delete()

        return JsonResponse({
            "Status" : "Deleted",
            "Messages" : "Data Deleted Successfully"
        })
    else:
        return None

