from django.http import HttpResponse
from django.shortcuts import render

def index(reguest):
	return render(reguest,'index.html')
	
def about(request):
	return render(request,'about.html')
	
def contact(request):
	return render(request,'contact.html')

def analyze(request):
	djtext = request.POST.get('text','default')
	removepunc = request.POST.get('removepunc','off')
	uppercase = request.POST.get('uppercase','off')
	newlineremover = request.POST.get('newlineremover','off')
	ex = request.POST.get('ex','off')
	
	punc='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
	
	if removepunc=='on':
		w=""
		for char in djtext:
			if char not in punc:
				w=w+char
		djtext=w
		
	if uppercase=='on' :
		w=""
		for char in djtext:
			w=w+char.upper()
		djtext=w

	if newlineremover=='on':
		w=""
		for char in djtext:
			if char !="\n" and char !='\r':
				w=w+char
		djtext=w
		
	if ex=='on':
		w=djtext.replace("  ","")
					
	djtext=w
	if removepunc !='on' and uppercase !='on' and newlineremover != 'on' and ex !='on':
		return HttpResponse('kuch choose kr lo')
	
	else:
		return render(request,'analyzed.html',{'after':djtext})
		
		
		
	