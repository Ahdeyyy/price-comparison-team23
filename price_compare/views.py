from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import CommentForm , UserForm ,LoginForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from .models import Product 
from .scraper.jumia import get_jumia_product
from django.contrib.auth.decorators import login_required
from django.urls import reverse

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
            # username=request.POST.get('username')
            # password=request.POST.get('password')
            #user=authenticate(username=username, password=password)
            if user is not None and user.is_active:
                
                login(request, user)
                return HttpResponse('You have Succefully LoggedIn')
           

            else:
                return HttpResponse('disabled account')

        else:
            return HttpResponse('invalid login')
            
    else:
        form = LoginForm()

    return render(request,'registration/login.html',{'form': form})
def UserView(request):
    registered=False
    if request.method=='POST':
        form=UserForm(data=request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponse('You have Succefully Registered')
           
        else:
            print(form.errors)
    else:
        form=UserForm()       
    return render(request,'registration/signup.html',{'show':form,'registered':registered})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('landing'))
