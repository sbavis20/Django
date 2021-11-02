
from django.http import  HttpResponse
from django.shortcuts import render


def index(request):

    return render(request,'index.html')


def about(request):
    return HttpResponse("hello about")

def analyze(request):
    #Get Text
    djtext = request.GET.get('text', 'default')

    #Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    #Check checkbox value is on
    if removepunc == "on":
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Remove Punctuations','analyzed_text': analyzed}
        #Analyze Text
        return render(request, 'analyze.html', params)
    elif(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose' : 'Changed to UPPERCASE', 'analyzed_text' : analyzed}
        # Analyze Text
        return render(request, 'analyze.html', params)
    elif(newlineremover == "on"):
        analyzed = ""
        for char in djtext :
            if char !="\n":
                analyzed = analyzed + char
        params = {'purpose' : 'New Line Removed', 'analyzed_text' : analyzed}
        # Analyze Text
        return render(request, 'analyze.html', params)
    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not djtext[index] == " " and djtext[index+1]==" ":
                analyzed = analyzed + char

        params = {'purpose' : 'Extra Space Removed', 'analyzed_text' : analyzed}
        # Analyze Text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")




