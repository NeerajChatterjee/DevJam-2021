from django.shortcuts import render
import sys
import wolframalpha
import wikipedia
import webbrowser
import speech_recognition as sr
import pyaudio
import pyttsx3
# import requests
from subprocess import run, PIPE
from django.core.files.storage import FileSystemStorage

listener = sr.Recognizer()


def index(request):
    return render(request,'devjam/index.html')

def index_search(request):
    return render(request,'devjam/index_search.html')


def search_engine(request):
    query = request.GET.get('query')

    try:
        client = wolframalpha.Client("H5T9W7-VA87UKVW6K")
        res = client.query(query)
        ans = next(res.results).text
        return render(request, 'devjam/index_search.html', {'ans': ans, 'query': query})

    except Exception:
        try:
            ans = wikipedia.summary(query,sentences=20)
            return render(request, 'devjam/index_search.html', {'ans': ans, 'query': query})

        except Exception:
            ans = "FOUND NOTHING"
            return render(request, 'devjam/index_search.html', {'ans': ans, 'query': query})

def index_note(request):
    return render(request,'devjam/index_note.html')


def note_maker(request):
    title = request.GET.get('title')
    notes = request.GET.get('notes')

    try:
        with open("media/notes.txt", 'w') as f:
            f.write('Title - '+ title)
            f.write('\n')
            f.write("Notes -\n"+ notes)
            ans = "File saved successfully! Click on DOWNLOAD."
            filename = 'notes.txt'
            fs = FileSystemStorage()
            templateurl = fs.url(filename)
            # finalname = templateurl.replace(filename, "notes.txt")
            print('file name is ', filename)
            print('template url is ', templateurl)
            # print('final name is ', finalname)
            return render(request, 'devjam/index_note.html', {'ans': ans,"download_file":templateurl})
    except Exception:
        ans = "Sorry unable to save the notes."
        return render(request, 'devjam/index_note.html', {'ans': ans})

def index_convert(request):
    return render(request, 'devjam/index_converter.html')


def imgtopdf(request):
    Image = request.FILES['image']
    print('image is', Image)
    fs = FileSystemStorage()
    filename = fs.save(Image.name, Image)
    templateurl = fs.url(filename)
    fileurl = fs.open(filename)
    image = run([sys.executable, "C:\\Users\\Neeraj\\Desktop\\CODES\\Python\\dev_jam\\devJam 2021\\devjam\\convert_imgtopdf.py", str(
        fileurl), (filename)], shell=False, stdout=PIPE)
    # finalname = templateurl.replace(filename, "converted.pdf")
    # print('file name is ', filename)
    # print('template url is ', templateurl)
    # print('final name is ', finalname)
    # print("image is ",image)
    return render(request, 'devjam/index_converter.html', {'done': " Conversion successful, Click DOWNLOAD "})


def doctopdf(request):
    doc = request.FILES['doc_file']
    print('document is ', doc)
    fs = FileSystemStorage()
    filename = fs.save(doc.name, doc)
    templateurl = fs.url(filename)
    fileurl = fs.open(filename)
    image = run([sys.executable, "C:\\Users\\Neeraj\\Desktop\\CODES\\Python\\dev_jam\\devJam 2021\\devjam\\convert_doctopdf.py", str(
        fileurl), (filename)], shell=False, stdout=PIPE)
    # finalname = templateurl.replace(filename, "converted.pdf")
    # print(templateurl)
    return render(request, 'devjam/index_converter.html', {'done1': " Conversion successful, Click DOWNLOAD "})

# def connect_ext(request):
#     return render(request,'../../')
