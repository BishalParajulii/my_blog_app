from django.shortcuts import render , redirect
from django.http import JsonResponse
from .models import PostModel 
from .forms import PostModelForm
from django.shortcuts import get_object_or_404



def index(request):
    posts = PostModel.objects.all()

    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('Home-page')

    else:
        form = PostModelForm()

    context = {
        'posts' : posts,
         'form':form,
         }


    return render(request , 'blog/index.html', context)



# def like_post(request, post_id):
#     post = get_object_or_404(Post, id=post_id)

#     # Ensure session exists
#     if not request.session.session_key:
#         request.session.create()

#     if request.user.is_authenticated:
#         like, created = Like.objects.get_or_create(post=post, user=request.user)
#         if not created:
#             like.delete()
#             liked = False
#         else:
#             liked = True
#     else:
#         session_key = request.session.session_key
#         anon_like, created = AnonymousLike.objects.get_or_create(post=post, session_key=session_key)
#         if not created:
#             anon_like.delete()
#             liked = False
#         else:
#             liked = True

#     total_likes = post.total_likes()
#     return JsonResponse({'liked': liked, 'total_likes': total_likes})
