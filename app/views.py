from django.db import models
from core.settings import BASE_DIR
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.db.models import F

# Create your views here.
from .models import Multiple, Danger


def upload(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images')
 
        for img in images:
            fs = FileSystemStorage(location='/media/photos')
            # fs = lst.append(img)
            file_path = fs.save(img)
            fs = file_path.append(img)
            print(fs)

    # images = Multiple.objects.all()
    lst = []
    lst.append(images)
    # print(lst)
    # for i in lst:
    Danger.objects.save(lst)
    # print(lst)
    return render(request, 'index.html', {'images': images})       

def thisupload(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        for img in images:
            Multiple.objects.create(images=img)
            fs = FileSystemStorage()
            # fs = lst.append(img)
            file_path = fs.save(img.name, img)
            # fsss = file_path.append(img)
            file = fs.url(file_path)
            # print(file)
            lst = []
            lst.append(file)
            print(lst)
        
            for i in lst:
                dj = Danger.objects.create(name=i)
                print(dj)
    dj = Danger.objects.all()
    for i in dj:
        dj.delete()    
    return render(request, 'home.html')           



# def newview(request):
#     dj = Danger.objects.filter(id=id).delete()
#     for d in dj:
#         print(d.delete())
#     return render(request, '')    


    # for ls in file:
    #         Danger.objects.create(file=ls)    
    # thisssss = Multiple.objects.all()
    # print(type(list(thisssss)))
    # lst = []
    # # lst.append(Multiple.objects.all())
    # # print(lst)
    # lssssst = Danger.objects.all()

    # for th in thisssss:
    #     # print(th)
    #     lst.append(th)
        # print(lst)
        # wee = th.append(lst)
    # print(wee)
    # print(images)
    # lst = []
    # lst.append(images)
    # print(lst)
    # Danger.objects.save(lst)

    # for i in lst:
    #     Danger.objects.save(lst)
    # print(lst)
    # for ls in urlsssss:
    # return render(request, 'home.html')       



            # print(i)
        # for img in images:
        #     fs = FileSystemStorage()
        #     # fs = lst.append(img)
        #     file_path = fs.save(img.name, img)
        #     # fsss = file_path.append(img)
        #     file = fs.url(file_path)
        #     print(file)
        #     lst = []
        #     lst.append(file)
            # print(lst)
        # for i in lst:
        #     print(i)    
        # lst = []
        # lst.append(file)
        # for i in lst:
        #     lst.append(i)
        # print(lst)

             # print(images)
        # lst = []
        # Danger.objects.save(lst)
        # print(Danger)


               # print(images)

        # for img in images:
        #     Danger.objects.create(images=img)
        # for img in images:
        #     Danger.objects.save(images=img)
        # lst = []
        # Danger.objects.save(lst)
        # print(Danger)



               # print(images)

        # for img in images:
        #     Danger.objects.create(images=img)
        # for img in images:
        #     Danger.objects.save(images=img)
        # lst = []
        # Danger.objects.save(lst)
        # print(Danger)