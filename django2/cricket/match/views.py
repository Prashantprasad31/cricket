from django.shortcuts import render,redirect
from match.models import Match
from match.forms import MatchForm

# Create your views here.
def view_match(request):
    all_matches=Match.objects.all()
    data={'matches':all_matches}
    return render(request,'match/view_match.html',context=data)


def add_match(request):
    if(request.method=='GET'):
        match_form= MatchForm()
        form = {'form':match_form}
        return render(request,'match/add_match.html',context=form)
    else:
        form_data = MatchForm(request.POST)
        if(form_data.is_valid()):
            form_data.save(commit=True)
            return redirect('/match/view')
        
def delete_match(request,matchid):
    match=Match.objects.get(id=matchid)
    match.delete()
    return redirect('/match/view')

def update_product(request,matchid):
    match=Match.objects.get(id=matchid)
    data = {'match':match}
    if(request.method=='POST'):
        form_data = MatchForm(request.POST,instance=match)
        if(form_data.is_valid()):
            form_data.save(commit=True)
            return redirect('/match/view')
    return render(request,'match/update_match.html',context=data)

    
