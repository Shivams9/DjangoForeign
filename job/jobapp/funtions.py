def handle_uploaded_file(f):
    with open('jobapp/static/upload/'+f.name,'wb+') as destination:
        for chunk in f.cunks():
            destination.write(chunk)