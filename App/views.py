from django.shortcuts import redirect, render
import requests
from django.contrib import messages
# Create your views here.


def url():
    url = requests.get(
        "https://newsapi.org/v2/top-headlines?country=us&apiKey=4e173c532bd24890b026af71dad2caaa").json()
    data = url
    return data


def getnews(search):
    url = requests.get(
        f"https://newsapi.org/v2/everything?q={search}&apiKey=4e173c532bd24890b026af71dad2caaa").json()
    data = url
    return data


def home(request):
    data = url()
    global search
    if request.method == "POST":
        search = request.POST.get("search")
        return redirect('result')

    context = {'data': data}
    return render(request, 'App/home.html', context)


def result(request):
    data = getnews(search)
    if int(data['totalResults']) == 0:
        messages.warning(request, "No Result Found")
        print("No Result Found")
    total = data['totalResults']
    print(total)
    context = {'data': data, 'search': search}
    return render(request, 'App/result.html', context)
