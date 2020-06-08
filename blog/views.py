from django.shortcuts import render , redirect , get_object_or_404
from .models import Post , Category , Places , People
from .forms import PostForm , CommentForm ,SignUpForm, loginForm , PlacesForm , PeopleForm ,Comment2Form
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required

#@login_required
def allposts(request):
    post = Post.objects.filter(approved_post=1).order_by('published_date')
    placess = Places.objects.filter(approved_post=1).order_by('published_date')
    peoples = People.objects.filter(approved_post=1).order_by('published_date')
    return render(request, 'index.html', {'posts': post ,'placess':placess , 'peoples':peoples })
    
def posts(request):
    post = Post.objects.filter(approved_post=1).order_by('published_date')
    return render(request, 'posts.html', {'posts': post})

def places(request):
    placess = Places.objects.filter(approved_post=1).order_by('published_date')
    return render(request, 'places.html', {'placess': placess,})

def people(request):
    peoples = People.objects.filter(approved_post=1).order_by('published_date')
    return render(request, 'people.html', {'peoples': peoples,})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def people_detail(request,id):
    people = get_object_or_404(People, id=id)
    return render(request, 'people_detail.html', {'people': people,})

def places_detail(request,pk):
    places = get_object_or_404(Places, pk=pk)
    return render(request, 'places_detail.html', {'places': places,})

@login_required
def Category(request):
    return render (request, 'Category.html' )

@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('allposts')
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})

@login_required
def post_people(request):
    # people = get_object_or_404(People)
    if request.method == "POST":
        people_form = PeopleForm(request.POST, request.FILES)
        
        if people_form.is_valid():
            people = people_form.save(commit=False)
            people.save()
            return redirect('allposts')
    else:
        people_form = PeopleForm()
       

    return render(request, 'people_edit.html', {'people_form': people_form})
                                                        
@login_required
def post_places(request):
    if request.method == "POST":
        places_form = PlacesForm(request.POST, request.FILES)
        
        if places_form.is_valid():
            places = places_form.save(commit=False)
            places.save()
            return redirect('allposts')
    else:
        places_form = PlacesForm()
       

    return render(request, 'places_edit.html', {'places_form': places_form})

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})

@login_required
def places_comment(request, pk):
    places = get_object_or_404(Places, pk=pk)
    if request.method == "POST":
        form = Comment2Form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.places = places
            comment.save()
            return redirect('places_detail',pk=places.pk)
    else:
        form = Comment2Form()
    return render(request, 'add_comment_to_post.html', {'form': form})
    
@login_required
def people_comment(request, pk):
    post = get_object_or_404(People, pk=pk)
    if request.method == "POST":
        form = Comment2Form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('people_detail', pk=people.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('posts')
    else:
        form = loginForm()
    return render(request, 'registration/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})




