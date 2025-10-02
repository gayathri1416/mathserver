from django.shortcuts import render
def calculation(request):
    intensity_ = None
    resistance_ = None
    power = None
    message = None

    if request.method=="POST":
        intensity=request.POST.get("intensity")
        resistance=request.POST.get("resistance")
        if not intensity or not resistance:
            message="Please enter the values for intensity and resistance "
        else:
            intensity_=float(intensity)
            resistance_=float(resistance)
            power=(intensity_*intensity_)*resistance_
        return render(request,'cal.html',{'intensity':intensity_,'resistance':resistance_,'power':power,'message':message})
    return render(request,'cal.html')
