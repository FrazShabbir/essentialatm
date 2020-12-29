from django.shortcuts import render 
# Create your views here.
def index(request):
    # products= addproduct.objects.order_by('-p_date_update').all()
    # return render(request,'index.html',{'products':products})
    return render(request,'index.html')