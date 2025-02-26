from django.shortcuts import render
import requests

BASE_URL = 'https://api.github.com/users/'


# Create your views here.
def home(request):
    return render(request,'index.html')

def handleGit(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        URL = BASE_URL+str(username)
        response = requests.get(URL)
        response = response.json()
        if response:
            context = {'name':response.get('name'),
                       'repos':response.get('repos_url'),
                   'avatar':response.get('avatar_url'),
                   'location':response.get('location'),
                   'email':response.get('email'),
                   'bio':response.get('bio'),
                   'public_repos':response.get('public_repos'),
                   'followers':response.get('followers'),
                   'created_at':response.get('created_at'),
                   'username':response.get('login')}
        
            return render(request,'user.html',context)
    
    return render(request,'user.html')


def repos(request):
    
    if request.method == 'POST':
        username = request.POST.get('gitname')
        REPO_URL = f'https://api.github.com/users/{username}/repos'
        response = requests.get(REPO_URL).json()
        if response:
            return render(request,'repos.html',{'context':response,'length':len(response)})
        
    return render(request,'repos.html')