from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import RegisterSerializer,UserSerializer
from .models import pet_usereg


# Create your views here.


class RegList(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
    def get(self,request):
        try:
            f=pet_usereg.objects.all()
            serializer=UserSerializer(f,many=True)
            print(serializer.data)
            return Response(serializer.data)
        except Exception as e:
            print(e)

def login_form(request):
    print("loggggg")
    try:
        user=request.GET.get("uname")
        passw=request.GET.get("password")
        print(user,passw)
        o=pet_usereg.objects.filter(uname=user,password=passw)
        c=o.count()
        print(c)
        if c==1:
            o2=pet_usereg.objects.get(uname=user,password=passw)
            request.session["uid"]=o2.id
            return HttpResponse("success")
        else:
            return HttpResponse("Wrong Password/username")
    except Exception as e:
            print(e)
            return HttpResponse("Wrong Password/username")
