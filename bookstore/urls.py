from django.urls import path
from library.views import RegisterView, LoginView, BookView, BookDeleteView


urlpatterns = [
    path('auth/register', RegisterView.as_view()),
    path('auth/login', LoginView.as_view()),
    path('books', BookView.as_view()),
    path('books/<int:id>', BookDeleteView.as_view()),
]
