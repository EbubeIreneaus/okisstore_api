from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from .forms import profileForm
import string
import random
from .models import Profile
# Create your views here.

def generate_Id():
    id = ''
    for i in range(30):
        id += random.choice(string.ascii_letters + string.digits)
    try:
        profile = Profile.objects.get(id = id)
        generate_Id()
    except:
        return id


class Auth(APIView):
    def post(self, request):
        form = profileForm(request.POST)
        if form.is_valid():
            id = generate_Id()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            psw = form.cleaned_data['psw']
            try:
                Profile.objects.create(id=id, name=name, email=email, psw=psw)
                return JsonResponse({'status':'success', 'profile-id':id})
            except Exception as e:
                return JsonResponse({'status':'failed', 'msg':'Could not create Profile', 'code':str(e)})
        return JsonResponse({'status': 'failed','msg':'form is not valid', 'code': str(form.errors)})

    def get(self, request):
        email = request.GET.get('email', '')
        psw = request.GET.get('password', '')

        try:
            profile = Profile.objects.get(email = email, psw = psw)
            return JsonResponse({'status':'success', 'id':profile.id})
        except Exception as e:
            return JsonResponse({'status':'failed','msg':'user not found on our system', 'code':str(e)})