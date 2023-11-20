from django.shortcuts import render

def data_render(request):
    data='this is an assumption'
    d={'assumption':data}
    return render(request,'data_render.html',context=d)

def login(request):
    data='sudheer'
    d={'username':data}
    return render(request,'data_render.html',context=d)

