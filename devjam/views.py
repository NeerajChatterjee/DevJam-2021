from django.shortcuts import render
import wolframalpha
import wikipedia
import webbrowser
import speech_recognition as sr
import pyaudio
import pyttsx3
# import sys
# import requests
# from subprocess import run, PIPE
# from django.core.files.storage import FileSystemStorage

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
        with open("1.txt", 'w') as f:
            f.write(title)
            f.write('\n')
            f.write(notes)
            ans = "File saved successfully!"
            return render(request, 'devjam/index_note.html', {'ans': ans})
    except Exception:
        ans = "Sorry unable to save the notes."
        return render(request, 'devjam/index_note.html', {'ans': ans})

# def index_convert(request):
#     return render(request, 'devjam/index_converter.html')


# def imgtopdf(request):
#     Image = request.FILES['image']
#     print('image is', Image)
#     fs = FileSystemStorage()
#     filename = fs.save(Image.name, Image)
#     templateurl = fs.url(filename)
#     fileurl = fs.open(filename)
#     image = run([sys.executable, "C:\\Users\\Neeraj\\Desktop\\CODES\\Python\\dev_jam\\File converter\\project1\\convert_imgtopdf.py", str(
#         fileurl), (filename)], shell=False, stdout=PIPE)
#     finalname = templateurl.replace(filename, "converted.pdf")
#     print('file name is ', filename)
#     print('template url is ', templateurl)
#     print('final name is ', finalname)
#     return render(request, 'devjam/index_converter.html', {'old_file': templateurl, "new_file": finalname, 'done': " Conversion successful, Click DOWNLOAD "})


# def doctopdf(request):
#     doc = request.FILES['doc_file']
#     print('document is ', doc)
#     fs = FileSystemStorage()
#     filename = fs.save(doc.name, doc)
#     templateurl = fs.url(filename)
#     fileurl = fs.open(filename)
#     image = run([sys.executable, "C:\\Users\\Neeraj\\Desktop\\CODES\\Python\\dev_jam\\File converter\\project1\\convert_doctopdf.py", str(
#         fileurl), (filename)], shell=False, stdout=PIPE)
#     finalname = templateurl.replace(filename, "converted.pdf")
#     print(templateurl)
#     return render(request, 'devjam/index_converter.html', {'old_file': templateurl, "new_file": finalname, 'done1': " Conversion successful, Click DOWNLOAD "})
