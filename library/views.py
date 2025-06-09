from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer, BookSerializer, BookWithUserSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Book


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_401_UNAUTHORIZED)
    


class BookView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookWithUserSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({"error": "Token de autenticación requerido"}, status=status.HTTP_401_UNAUTHORIZED)
            
        data = request.data
        if Book.objects.filter(isbn=data.get('isbn')).exists():
            return Response({"error": "ISBN ya registrado"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            book = serializer.save(registered_by=str(request.user.id))
            return Response({"id": str(book.id)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, id):
        try:
            book = Book.objects.get(id=id)
            book.delete()
            return Response({"success": True}, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({"error": "Libro no encontrado"}, status=status.HTTP_404_NOT_FOUND)
