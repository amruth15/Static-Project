from django.shortcuts import render
def view1(request):
    name="Amruth"
    favplayer="dhoni"
    favanimal="lion"
    favsubject="python"
    d={'name':name,'player':favplayer,'subject':favsubject,'animal':favanimal}
    return render(request,'myapp/1.html',d)
