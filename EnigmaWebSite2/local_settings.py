
SECRET_KEY = 'e+m!8g(d==%hpd9$5(6++jxv^gm0d!9s-qfo+l#kynbb5+1=d%'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'website',
        'USER': 'root',
        'PASSWORD': '$7dlar7$',
        'HOST':'localhost',
        'PORT': "3306"
    },
    'phoebe': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'phoebe',
        'USER': 'root',
        'PASSWORD': 'Mechanical75',
        'HOST': 'localhost',
        'PORT': "3306"
    }
}