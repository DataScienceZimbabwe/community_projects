import random

area = ['Chimanimani', 'Mutare', 'Buhera', 'Chivhu', 'Nyanga', 'Chipinge', 'Makoni', 'Mutasa']
gps_cordinates = ['-18.96167 32.40557', '-18°5742.01', 'S 32°2420.05 E', '-18°5742.01', '-18°5742.01', '-18°5742.01', '-18°5742.01', '-18°5742.01']
demographic_data = ['10000', '50000', '20000', '30000', '15000', '10000', '12000', '13000']
satellite_images = ['satellite/images/img1.jpg', 'satellite/images/img2.jpg', 'satellite/images/img3.jpg',
                    'satellite/images/img4.jpg', 'satellite/images/img5.jpg', 'satellite/images/img6.jpg',
                    'satellite/images/img7.jpg', 'satellite/images/img8.jpg']
news_articles = ['news title 1', 'news title 2', 'news title 3', 'news title 4', 'news title 5', 'news title 6',
                 'news title 7', 'news title 8']
geo_data = ['geographic data', 'geographic data', 'geographic data', 'geographic data', 'geographic data',
            'geographic data', 'geographic data', 'geographic data']

i = 1
while i <= 10:
    a = random.choices(gps_cordinates)
    b = random.choices(area)
    print(a)
    print(b)
    i += 1
