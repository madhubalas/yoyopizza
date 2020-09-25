from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import models

@csrf_exempt
def bot(request):
    if request.method=='POST':
        data=request.POST
        sentence=data.get('data')
        if sentence == 'Track Order':
            context=trackorder()
        elif sentence=="track_order_details":
            context=showorddata(request)
        elif sentence=='Place Order':
            context=getpizzatype()
        elif sentence=='get_pizza':
            context=getpizza()
        elif sentence=='pizza_deleivery_detail':        
            context=getpizzadelivery()
        elif sentence=='order_placed':
            ord_name=data.get('ord_prs_name')
            ord_mobile=data.get('ord_prs_mobile')
            ord_address=data.get('ord_prd_address')
            ord_details=models.register(order_name=ord_name,order_mobile=ord_mobile,order_address=ord_address,order_status='Order Placed')
            ord_details.save()
            context=orderplaced()
        else:
            context={
                'question':"what would you like to do",
                'option1':"Track Order",
                'option2':'Place Order',
                'curent_status':'select_action'
            }
        return render(request,'index.html',{'s':context})
    else:
        context={
                'question':"what would you like to do",
                'option1':"Track Order",
                'option2':'Place Order',
                'curent_status':'select_action'
            }
        return render(request,'index.html',{'s':context})

def trackorder():
    data={
        'question':"Enter Mobile Number and Name to see all ur order details",
        'curent_status':'track_order'
    }
    return data

def showorddata(request):
    data=request.POST
    name=data.get('track_name')
    mobile=data.get('track_mobile')
    order_details=models.register.objects.all()
    context={
        'curent_status':'ord-details-display',
        'mess':'your order details',
        'name':name,
        'mobile':int(mobile),
        'details':order_details
    }
    return context

def getpizzatype():
    context={
        'curent_status':'pizza_type',
        'question':'What kind of person are you ;)',
        'option1':'Veg',
        'option2':'Non Veg'
    }
    return context

def getpizza():
    context={
        'curent_status':'ord_pizza',
        'pizzas':[
            {
                'img':'m2.jfif',
            'p_name':'peporonite pizza',
            'p_size':'Medium',
            'p_price':'Rs.300'
        },
        {
            'img':'s1.jpg',
            'p_name':'marshmelo pizza',
            'p_size':'small',
            'p_price':'Rs.100'
        },
        {
            'img':'s1.jpg',
            'p_name':'veg pizza',
            'p_size':'small',
            'p_price':'Rs.100'
        },
        {
            'img':'lg.png',
            'p_name':'fried pizza',
            'p_size':'Large',
            'p_price':'Rs.500'
        }
        ]
    }
    return context

def getpizzadelivery():
    context={
        'question':'Enter your Delivery Address and Details',
        'curent_status':'pizza_delevery',
    }
    return context

def orderplaced():
    context={
        'question':'your order has been placed',
        'curent_status':'order_placed'
    }
    return context