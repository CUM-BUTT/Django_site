
from .models import Person
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
# Опять же, спасибо django за готовую форму аутентификации.
from django.contrib.auth.forms import AuthenticationForm
# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.
from django.contrib.auth import login
#from django.registration.models import Registration
from django.views.generic.base import View
from django.contrib.auth import logout


from django.contrib.auth.hashers import check_password, make_password

class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("")

class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "log in.html"

    # В случае успеха перенаправим на главную.
    success_url = ""

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    #success_url = "/log in/"
    success_url = "/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

class HomeView(TemplateView):
    template_name = "Home.html"


class AboutView(TemplateView):
    template_name = "About.html"

class DonateView(TemplateView):
   template_name = "Donate.html"

class TakeALoanView(TemplateView):
   template_name = "TakeALoan.html"




"""def start(request):
  return index(request)

def index(request):
  if request.method == 'GET':
    person_list = Person.objects.order_by('-name')
    template = loader.get_template('indexTemplate.html')
    context = {
          'person_list': person_list,
      }
    return HttpResponse(template.render(context, request))
  else:
    if request.method == 'POST' and request.is_ajax():
      try:
        data0 = json.loads(request.body.decode())  
        data = SomeForm(data0)
      except ValueError:
        return JsonResponse({'error': 'bla bla bla',})
      
      if data.is_valid():
        #assert False
        person = Person(
          name=data.cleaned_data['name'],                  
          description=data.cleaned_data['description'],                 
          release_date=data.cleaned_data['release_date'],              
          rating=data.cleaned_data['rating'],)
        person.save()
        return render(request,"indexTemplate.html",context = {'person_list' : Person.objects.order_by('-name')})
    else:
     return render(request,"indexTemplate.html",context = {'person_list' : Person.objects.order_by('-name')})"""
 
# получение данных из бд
def index(request):
    #people=Person.objects.get(pk=people_id)
    people = Person.objects.all()
   
    return render(request, "TakeALoan.html",{"people":people})
 
# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom = Person()
        tom.card_num = request.POST.get("card_num")
        tom.name = request.POST.get("name")
        tom.cvc= request.POST.get("cvc")
        #tom.password= request.POST.get("password")
        password= request.POST.get("password")
        tom.password = make_password(password, salt=None,hasher='default')
        tom.save()
        """
        b = get_object_or_404(Person.objects.all())
        data = {'message': 'create'.format(b)}
        return HttpResponse(json.dumps(data),content_type='application/json')
        """
 
    return HttpResponseRedirect("/") 

"""def update(request):
  if request.method == 'GET':
    persons = list(Person.objects.all())
    n = len(persons)
    context = n
  return HttpResponse(context,request)"""


from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import json
from django.http import JsonResponse

"""
if request.user.is_authenticated() and request.is_ajax() and request.POST:
        object_id = request.POST.get('id', None)
        b = get_object_or_404(Company, id=object_id)
        b.delete()
        data = {'message': 'delete'.format(b)}
    return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return JsonResponse({'error': 'Only authenticated users'}, status=404)
"""
 
def update(request):
    if  request.is_ajax():
      b = get_object_or_404(Person,id = 52)
      
      data = {'message': 'update'.format(b)}
      index(request)
      return HttpResponse(json.dumps(data),content_type='application/json')
    else:
      print("else")
      return JsonResponse({'error': 'Only authenticated users'}, status=404)  

"""   
def update(request):
    if  request.is_ajax():
      p = Person.objects.get(max(Person.person_id))      
      b = get_object_or_404(Person,id = 51)
      
      data = {'message': 'update'.format(b)}
      index(request)
      return HttpResponse(json.dumps(data),content_type='application/json')
    else:
      print("else")
      return JsonResponse({'error': 'Only authenticated users'}, status=404)  
      """