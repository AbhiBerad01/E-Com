import json

from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum
import razorpay

client = razorpay.Client(auth=("rzp_test_OBuUgKuzJgcgZq", "EQ2RprNWXSrOx7kKyGuPT8nx"))
MERCHANT_KEY = 'kbzk1DSbJiV_03p5'


def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'product_id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlide = (n // 4) + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlide), nSlide])
    params = {"allProds": allProds}
    return render(request, 'shop/index.html', params)


def searchMatch(query, item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower() or query in item.product_name or query in item.product_name.upper():
        print('true')
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'product_id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = (n // 4) + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query) < 3:
        params = {'msg': 'please make sure you Entered proper product name'}
    return render(request, 'shop/search.html', params)


def productView(request, product_id):
    product = Product.objects.filter(product_id=product_id)

    return render(request, 'shop/prodView.html', {'product': product[0]})


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    if request.method == 'POST':
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status": "success", "updates": updates, "item_json": order[0].item_json},
                                          default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status": "noitem"}')
        except Exception as e:
            return HttpResponse('{"status": "error"}')
    return render(request, 'shop/tracker.html')


def checkout(request):
    if request.method == 'POST':
        item_json = request.POST.get('item_json', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address1', '') + "" + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        order = Order(item_json=item_json, name=name, email=email, phone=phone, address=address, city=city, state=state,
                      zip_code=zip_code, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The Order has been placed")
        update.save()
        thanks = True
        id = order.order_id
        # return render(request, 'shop/checkout.html', {'thanks': thanks, 'id': id})
        # here is the post request to the paytm
        print(amount)
        data = {"amount": str(amount)+"00", "currency": "INR", "receipt": str(id)}
        payment = client.order.create(data=data)

        return render(request, 'shop/paytm.html', {'payment': payment})
    return render(request, 'shop/checkout.html')


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here

    return render(request, 'shop/paymentstatus.html')
