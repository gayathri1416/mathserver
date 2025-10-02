# Ex.05 Design a Website for Server Side Processing
# Date:
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
urls.py

from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.calculation,name='calculation'),
]

views.py

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

cal.html


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
body{
    background: #000000ea;
}
   .title{
        text-align: center;
        margin-top: 1cm;
        block-size: auto;
        background-color:lightgoldenrodyellow;
        color: rgba(160, 20, 20, 0.818);
   }
   .file{
  border: 3px dotted rgba(255, 196, 0, 0.871);   
  padding:20px;                 
  margin: 13cm;         
  border-radius: 10px;    
  margin-top:1cm;   
  color: white;
  width: fit-content;
}
.file img{
  max-width: 100%;
  height: auto;
  display: block;
  margin-bottom: 30px;
}
label,input{
    font-size:larger;
}
.button{
    display: block;
    margin-left: 0.3cm;
    background:maroon;
    border: 1px dashed yellow;
    color: aliceblue;
    font-family:fantasy;
}
.result{
    margin-left: 2%;
}
</style>
<body>
    <h1 class="title">POWER CALCULATION OF A LAMP FILAMENT</h1>
    <form method="POST">
    {% csrf_token %}
    <div class="file">
        {% load static %}
        <img src="{% static 'backgroung.jpg' %}" alt="bg pic">
        <label for="intensity">Enter the intensity:</label>
        <input type="number" id="intensity"  name="intensity" value="{{intensity}}"><br><br>
        <label for="resis" >Enter the resistance:</label>
        <input type="number" id="resis" name="resistance" value="{{resistance}}"><br><br>
        <input type="submit" value="CALCULATE" class="button">
        <div class="result">
        {% if message %}
          <h4>{{message}}</h4>
        {% endif %}
        <h3>Power is : {{power}} </h3>  
     </div>     
    </div>
    </form>
</body>
</html>
```

# HOMEPAGE:
![alt text](<Screenshot 2025-10-02 170312.png>)
![alt text](<Screenshot 2025-10-02 170248.png>)
# RESULT:
The program for performing server side processing is completed successfully.
