from django.shortcuts import render, get_object_or_404
from .forms import GenerateFAQForm
from django.http import JsonResponse
from .models import Faq
import pandas as pd
from .functions import give_an_answer, create_update_csv, similarity_score

def home(request):
    form = GenerateFAQForm(request.POST)
    if form.is_valid():
        
        question_text = form.cleaned_data['question']
        related_faqs = similarity_score('interface_backend/static/interface_backend/question_and_answer.csv', question_text)

        
        dictionary_csv = give_an_answer(question_text, 'interface_backend/static/interface_backend/final_summary.csv')
        
        # Manually create a new Faq instance
        newFaq = Faq(question=dictionary_csv['question'], answer=dictionary_csv['answer'])
        newFaq.save()  # Save the new instance

        create_update_csv('interface_backend/static/interface_backend/question_and_answer.csv', dictionary_csv['question'], dictionary_csv['answer'])

        context = {
            'answer': newFaq.answer,
            'faqId': newFaq.id,
            'q1': related_faqs['question1'],
            'a1': related_faqs['answer1'],
            'q2': related_faqs['question2'],
            'a2': related_faqs['answer2'],
            'q3': related_faqs['question3'],
            'a3': related_faqs['answer3'],
            'q4': related_faqs['question4'],
            'a4': related_faqs['answer4'],
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
        
        faq.helpful = 'T'
        faq.save()
        context = {
            'message': 'Successfully liked!',
        }
        return JsonResponse(context)
    
def dislike_it(request, faq_pk):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        faq = get_object_or_404(Faq, pk=faq_pk)
        
        faq.helpful = 'F'
        faq.save()
        context = {
            'message': 'Successfully unliked!',
        }
        return JsonResponse(context)