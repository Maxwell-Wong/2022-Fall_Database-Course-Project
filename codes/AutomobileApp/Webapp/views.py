from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Vehicle, Dealer, Options, Model, Brand, Sold
from collections import Counter
import json

def db_web(request):
    vehicles = Vehicle.objects.all()
    dealers = Dealer.objects.all()
    models = Model.objects.all()
    options = Options.objects.all()
    brands = Brand.objects.all()
    context1 = {
        'dealers': dealers
    }

    if request.method == 'POST':
        dealer_id = request.POST.get('dealer_id')
        print('check dealer id: ', dealer_id)
        dealer_owned_vehicle = Vehicle.objects.filter(dealer_id=dealer_id)
        dealer_name = Dealer.objects.filter(dealer_id=dealer_id).first().dealer_name

        info = {}
        for i, obj in enumerate(dealer_owned_vehicle):

            features = {}
            model = Model.objects.filter(model_id=obj.model_id).first()
            option = Options.objects.filter(option_id=obj.option_id).first()
            brand = Brand.objects.filter(brand_id=model.brand_id).first()
            sold = Sold.objects.filter(vin=obj.vin).first()
            print(sold)
            features['VIN'] = obj.vin
            features['brand'] = brand.brand_name
            features['model'] = model.model_name
            features['color'] = option.color
            features['engine'] = option.engine
            features['transmission'] = option.transmission
            features['price'] = obj.price
            features['stock_date'] = obj.stock_date
            if sold is None:
                features['sold_date'] = 'Inventory'
            else:
                features['sold_date'] = str(sold.sale_date.year) + '-' \
                                        + str(sold.sale_date.month) + '-' + str(sold.sale_date.day)
            info[i] = features
        print(info)

        result = {
            'dealers': dealers,
            'info': info,
            'dealer_name': dealer_name

        }

        return render(request, 'index.html', context=result)

    return render(request, 'index.html', context=context1)

def db_react(request):
    dataList = []
    if request.method == 'GET':
        data = Dealer.objects.all()
        for item in data:
            dataList.append({
                "id": item.dealer_id,
                "name": item.dealer_name,
            })
    return JsonResponse({
        "code": 200,
        "data": dataList
    })

