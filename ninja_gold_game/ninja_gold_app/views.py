from django.shortcuts import redirect, render, HttpResponse
import random
from datetime import datetime
# Create your views here.
def index(request):
    if 'total_gold' not in request.session or 'activities' not in request.session:
        request.session['total_gold'] = 0
        request.session['activities'] = []
    return render(request, 'index.html')

def process_money(request):
    if request.method == 'GET':
        return redirect('/')
    elif request.method == 'POST':
        if request.POST['farming']=='farm':
            gold = random.randint(10,20)
            request.session['activities'].append(f'Earned  {gold} golds from the farm! ({str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))})')
        if request.POST['farming']=='cave':
            gold = random.randint(5,10)
            request.session['activities'].append(f'Earned  {gold} golds from the cave! ({str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))})')
        if request.POST['farming']=='house':
            gold = random.randint(2,5)
            request.session['activities'].append(f'Earned  {gold} golds from the house! ({str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))})')
        if request.POST['farming']=='casino':
            gold = random.randint(-50,50)
            if gold >= 0:
                request.session['activities'].append(f'Earned  {gold} golds from the casino! ({str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))})')
            else:
                request.session['activities'].append(f'You lost {-gold} golds, keep trying! ({str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))})')
        request.session['total_gold'] += gold

        #if request.session['total_gold'] >= 100:
        #    a = request.session['total_gold']
        #    return HttpResponse(f'Your are the winner!!!, total {a} golds')
        
        #if request.session['total_gold'] <= -100:
        #    return HttpResponse(f'Your lost {gold} golds')
        


    return render(request, 'index.html')

def play_again(request):
    request.session.flush()
    return redirect('/') 