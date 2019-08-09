from django.contrib import admin
from django.urls import path, include
import kindAnimal.views
import mainPage.views
import animalGoods.views
import animalShop.views
import personal.views
import application.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainPage.views.mainPage, name='mainPage'),
    path('mainApplicant/', mainPage.views.mainApplicant, name='mainApplicant'),
    path('createMain/', mainPage.views.createMain, name='createMain'),
    path('kindAnimal/', kindAnimal.views.kindAnimal, name='kindAnimal'),
    
    path('dressApplication/', kindAnimal.views.dressApplication, name='dressApplication'),
    path('createDress/', kindAnimal.views.createDress, name='createDress'),
    path('animalShop/', animalShop.views.animalShop, name='animalShop'),

    path('personal/', personal.views.personal, name='personal'),
    path('personal/delete/<int:personal_id>',
         personal.views.delete, name="delete"),
    path('personal/<int:personal_id>/', personal.views.detail, name='detail'),
    path('personal/writePerson/', personal.views.writePerson, name='writePerson'),
    path('personal/createPerson/', personal.views.createPerson, name='createPerson'),


    path('animalGoods/', animalGoods.views.animalGoods, name='animalGoods'),
    path('animalGoods/comment', animalGoods.views.comment, name="comment"),
    path('animalGoods/create', animalGoods.views.create, name="create"),
    path('animalGoods/write/', animalGoods.views.write, name='write'),
    path('animalGoods/detail/', animalGoods.views.detail, name='detail'),


    path('accounts/', include('accounts.urls')),

    path('application/', application.views.application, name='application'),
    path('createApplication/', application.views.createApplication, name='createApplication'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
