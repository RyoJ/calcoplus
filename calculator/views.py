from django.shortcuts import render
from django.http import HttpResponse

def hello(req):
  return HttpResponse('Hello, World !!')
  
def index(request):
    return render(request, 'index.html')

def calc(request):
    with open('/home/ec2-user/environment/django_projects/calculator/hp.txt','r') as f:
        rhp = f.read()
        #print(rhp) #読み込む時点ではphpより大きい。計算する時点では
    
    damage = int(request.POST['val2'])

    with open('/home/ec2-user/environment/django_projects/calculator/hp.txt','w+') as f:
        php = int(rhp) - int(damage)
        #print(php)
        f.write(str(php)) #事後の（新しい）hpが常に記録される
    context = {
    'rhp': rhp,
    'php': php,
    }
    return render(request, 'index.html', context)
    
'''def some_view(request):
    if request.method == 'POST':
        if 'button_1' in request.POST:
            php = int(php) - 10'''