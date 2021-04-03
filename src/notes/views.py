from django.shortcuts import render
from .models import Note
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Note
from .serializers import PostSerializer
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.generics import CreateAPIView
# Create your views here.
def note_list_view(request):
    notes = Note.objects.all()
    context = {
        'notes': notes
    }
    return render(request, "note_list.html", context)

class PostView(APIView):
    permission_classes = {AllowAny,}


    def get(self, request, *args, **kwargs):
        queryset = Note.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class PostCreateView(CreateAPIView):
    permission_classes = {AllowAny, }
    serializer_class = PostSerializer
    queryset = Note.objects.all()


def search(request):
    notes = Note.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            notes = notes.filter(title__icontains=keyword)
    context = {
        'notes': notes
    }
    return render(request, 'search.html', context)
         