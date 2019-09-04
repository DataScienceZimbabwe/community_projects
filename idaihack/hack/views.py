from django.shortcuts import render
from .models import DataSet
import random


def home(request):
    obj = DataSet.objects.all()
    context = {'obj': obj}
    template = "hack/index.html"
    return render(request, template, context)


def index(request):
    context = {}
    template = "hack/index.html"

    area = ['Chimanimani', 'Mutare', 'Buhera', 'Chivhu', 'Nyanga', 'Chipinge', 'Makoni', 'Mutasa']
    gps_cordinates = ['-18.96167 32.40557', '-18°5742.01', 'S 32°2420.05 E', '-18°5742.01', '-18°5742.01', '-18°5742.01', '-18°5742.01', '-18°5742.01']
    demographic_data = ['10000', '50000', '20000', '30000', '15000', '10000', '12000', '13000']
    satellite_images = ['satellite/images/img1.jpg', 'satellite/images/img2.jpg', 'satellite/images/img3.jpg',
                        'satellite/images/img4.jpg', 'satellite/images/img5.jpg', 'satellite/images/img6.jpg',
                        'satellite/images/img7.jpg', 'satellite/images/img8.jpg']
    news_articles = ['news title 1', 'news title 2', 'news title 3', 'news title 4', 'news title 5', 'news title 6',
                     'news title 7', 'news title 8']
    geo_data = ['geographic data1', 'geographic data2', 'geographic data3', 'geographic data4', 'geographic data5',
                'geographic data6', 'geographic data7', 'geographic data8']

    i = 1
    while i <= 100:
        a = random.choices(area)
        b = random.choices(gps_cordinates)
        c = random.choices(demographic_data)
        d = random.choices(satellite_images)
        e = random.choices(news_articles)
        f = random.choices(geo_data)
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)

        payment = DataSet(
            area=a,
            gps_cordinates=b,
            demographic_data=c,
            satellite_images=d,
            news_articles=e,
            geo_data=f
        )
        payment.save(force_insert=True)

        i += 1
    return render(request, template, context)
