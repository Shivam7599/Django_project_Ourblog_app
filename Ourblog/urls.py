
from django.urls import path
# from . import views

from .views import HomeListView, AddCreateView, ArticleDetailView,Update_PostUpdateView, AddCommentView, CategoryView,DeleteDeleteView, Add_categoryCreateView, LikeView
urlpatterns = [
    path('', HomeListView.as_view(), name="hom"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddCreateView.as_view(), name='Add'),
    path('update/<int:pk>', Update_PostUpdateView.as_view(), name='Update'),
    path('delete/<int:pk>/remove', DeleteDeleteView.as_view(), name='delete'),

    path('Add_Category', Add_categoryCreateView.as_view(), name='Add_Category'),
    path("category/<str:cats>/", CategoryView, name="category"),

    path('like/<int:pk>', LikeView, name="like_post"),
    # path('Unlike/<int:pk>', UnLikeView, name="unlike_post"),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='Add_comment'),
]

