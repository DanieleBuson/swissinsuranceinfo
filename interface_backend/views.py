from django.shortcuts import render, get_object_or_404
from .forms import GenerateFAQForm
from django.http import JsonResponse
from .models import Faq

def home(request):
    form = GenerateFAQForm(request.POST)
    if form.is_valid():
        print('INSIDE FORM')
        question_text = form.cleaned_data['question']
        print(question_text)

        context = {
            'status': 'ok',
            'faqId': 1,
        }
        return JsonResponse(context)
    else: 
        context = {
            'form':form,
        }
        return render(request, 'interface_backend/home.html', context)


def like_it(request, faq_pk):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        faq = get_object_or_404(Faq, pk=faq_pk)
        
        faq.helpful = True
        faq.save()
        context = {
            'message': 'Successfully liked!',
        }
        return JsonResponse(context)
    
def dislike_it(request, faq_pk):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        faq = get_object_or_404(Faq, pk=faq_pk)
        
        faq.helpful = False
        faq.save()
        context = {
            'message': 'Successfully unliked!',
        }
        return JsonResponse(context)