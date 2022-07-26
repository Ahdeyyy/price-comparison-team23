from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm , UserRegistrationForm ,LoginForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from .models import Product 
from .scraper.jumia import get_jumia_product

# Create your views here.

def product_detail(request,id,product):
    product = get_object_or_404(
        Product,
        slug=product,
        id = id,
    )

    comments = product.comments.filter(active=True)
    new_comment = None
    platforms = []
    prd = {
        'name':product.name,
        'brand':product.brand,
        'category':product.category
    }
    platforms.append(get_jumia_product(prd))

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.product = product
            new_comment.username = request.user.username
            new_comment.save()
    else:
            comment_form = CommentForm()

    return render(request,'product/detail.html',
                    {
                        'product':product,
                        'comments':comments,
                        'platforms':platforms,
                        'new_comment':new_comment,
                        'comment_form':comment_form
                    },            
    )


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product/list.html'

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                username=cd['username'],
                password=cd['password']
                )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')

                else:
                    return HttpResponse('disabled account')

        else:
            return HttpResponse('invalid login')
            
    else:
        form = LoginForm()

    return render(request,'user/login.html',{'form': form})



def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request,'registration/register_done.html',{'new_user': user})
    else:
        form=UserRegistrationForm()       
    return render(request,'registration/register.html',{'form':form})