from typing import Any, Dict
from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .models import Poster, Category, Comment
from .forms import PostForm ,EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

class HomeListView(ListView):
    model = Poster
    template_name = "hom.html"
    ordering = ['id']
    # ordering = ['-Post_date']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["Cat_list"] = Category.objects.all()
        return context

# doing Same thing as above we do for Poster But now we do in old ways like using functions
def CategoryView(request, cats):
    category_post = Poster.objects.filter(category=cats)
    return render (request, 'categories.html', {'cats': cats.title(), 'category_post': category_post })

# Function for save like of a post in database
def LikeView(request, pk):
    post = get_object_or_404(Poster, id = request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
    else:        
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

# def UnLikeView(request, pk):
#     post = get_object_or_404(Poster, id = request.POST.get('unpost_id'))
#     unliked = False
#     if post.unlikes.filter(id = request.user.id).exists():
#         post.unlikes.remove(request.user)
#     else:
#         post.unlikes.add(request.user)
#         unliked = True
#     return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
    

class ArticleDetailView(DetailView):
    model = Poster
    template_name = "Article_detail.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu

        stuff= get_object_or_404(Poster, id = self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes

        liked=False
        if stuff.likes.filter(id= self.request.user.id).exists():
            liked=True
        context["liked"] = liked
        # unlike_stuff = get_object_or_404(Poster, id = self.kwargs['pk'])
        # total_unlikes = unlike_stuff.total_unlikes()
        # context['total_unlikes'] = total_unlikes
        return context

class AddCreateView(CreateView):
    model = Poster
    template_name = "add_post.html"
    form_class = PostForm

class AddCommentView(CreateView):
    model = Comment
    template_name = "Add_comment.html"
    form_class = CommentForm
    success_url = reverse_lazy("hom")
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

 
class Add_categoryCreateView(CreateView):
    model = Category
    template_name = "Add_category.html"
    fields= "__all__"
 
class Update_PostUpdateView(UpdateView):
    model = Poster
    template_name = "Update_post.html"
    form_class = EditForm

class DeleteDeleteView(DeleteView):
    model = Poster
    template_name = "delete_post.html"
    success_url = reverse_lazy("hom")
