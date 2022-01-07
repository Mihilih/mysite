import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from datetime import date

from cerps.models import *

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "cerps/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "cerps/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# Create your views here.
def index(request):
    return render(request, "cerps/index.html")

@login_required(login_url='login')
def add(request):
    return render(request, "cerps/add.html")
    #link in the research dropdown

def view(request):
    journals=Journal.objects.all()
    books=Book.objects.all()
    patents=Patent.objects.all()
    grants=Grant.objects.all()
    awards=Award.objects.all()
    return render(request, "cerps/view.html",{
        'journallist':journals,
        'booklist':books,
        'patentlist':patents,
        'grantlist':grants,
        'awardlist':awards,
    })
    #link in the research dropdown

#add journal
@login_required(login_url='login')
def journal(request):
    if request.method == "POST":
        name=request.POST['name']
        title=request.POST['title']
        authors=request.POST['authors']
        authlist=[x.strip() for x in authors.split(',')]
        auth=[]
        for x in authlist:
            try:
                person=People.objects.get(name=x)
                auth.append(person)
            except People.DoesNotExist:
                person=People()
                person.name=x
                person.save()
                per=People.objects.get(name=x)
                auth.append(per)
        volume=request.POST['volume']
        issue=request.POST['issue']
        pages=request.POST['pages']

        journal=Journal()
        journal.name=name
        journal.title=title
        journal.volume=volume
        journal.issue=issue
        journal.pages=pages
        journal.save()
        for x in auth:
            journal.authors.add(x)
        journal.save()
        return render(request, "cerps/journaladd.html")
    else:
        return render(request, "cerps/journaladd.html")

#add book
@login_required(login_url='login')
def book(request):
    if request.method == "POST":
        book_or_chap=request.POST['chap']
        book_title=request.POST['book_title']
        chap_title=request.POST['chap_title']
        if book_or_chap=="book":
            chap=True
            if book_title == "":
                return render(request, "cerps/error.html",{
                'message':"Enter book title"
            } )
        else:
            chap=False
            if chap_title == "":
                return render(request, "cerps/error.html",{
                'message':"Enter chapter title"
            } )
        authors=request.POST['authors']
        authlist=[x.strip() for x in authors.split(',')]
        auth=[]
        for x in authlist:
            try:
                person=People.objects.get(name=x)
                auth.append(person)
            except People.DoesNotExist:
                person=People()
                person.name=x
                person.save()
                per=People.objects.get(name=x)
                auth.append(per)
        isbn=request.POST['isbn']
        year=request.POST['year']
        if int(year)>date.today().year or int(year)<1900:
            return render(request, "cerps/error.html",{
                'message':"Enter valid year"
            } )
        publisher=request.POST['publisher']

        book=Book()
        book.book_bool=chap
        if chap:
            book.book_title=book_title
            if chap_title is not "":
                book.chapter_title=chap_title
        else:
            book.chapter_title=chap_title
            if book_title is not "":
                book.book_title=book_title
        book.year=year
        book.isbn=isbn
        book.publisher=publisher
        book.save()
        for x in auth:
            book.authors.add(x)
        book.save()
        return render(request, "cerps/bookadd.html")
    else:
        return render(request, "cerps/bookadd.html")

#add patent
@login_required(login_url='login')
def patent(request):
    if request.method == "POST":
        agency=request.POST['agency']
        title=request.POST['title']
        number=request.POST['number']
        authors=request.POST['authors']
        authlist=[x.strip() for x in authors.split(',')]
        auth=[]
        for x in authlist:
            try:
                person=People.objects.get(name=x)
                auth.append(person)
            except People.DoesNotExist:
                person=People()
                person.name=x
                person.save()
                per=People.objects.get(name=x)
                auth.append(per)
        year=request.POST['year']
        if int(year)>date.today().year or int(year)<1900:
            return render(request, "cerps/error.html",{
                'message':"Enter valid year"
            } )

        patent=Patent()
        patent.agency=agency
        patent.title=title
        patent.number=number
        patent.year=year
        patent.save()
        for x in auth:
            patent.authors.add(x)
        patent.save()
        return render(request, "cerps/patentadd.html")
    else:
        return render(request, "cerps/patentadd.html")

#add grant
@login_required(login_url='login')
def grant(request):
    if request.method == "POST":
        agency=request.POST['agency']
        title=request.POST['title']
        pi=request.POST['pi']
        co_investigators=request.POST['investigators']
        authlist=[x.strip() for x in co_investigators.split(',')]
        auth=[]
        for x in authlist:
            try:
                person=People.objects.get(name=x)
                auth.append(person)
            except People.DoesNotExist:
                person=People()
                person.name=x
                person.save()
                per=People.objects.get(name=x)
                auth.append(per)
        budget=request.POST['budget']
        duration_from=request.POST['from']
        duration_to=request.POST['to']

        grant=Grant()
        grant.agency=agency
        grant.title=title
        grant.pi=pi
        grant.budget=budget
        grant.duration_from=duration_from
        grant.duration_to=duration_to
        grant.save()
        for x in auth:
            grant.co_investigators.add(x)
        grant.save()
        return render(request, "cerps/grantadd.html")
    else:
        return render(request, "cerps/grantadd.html")

#add award
@login_required(login_url='login')
def award(request):

    if request.method == "POST":
        name=request.POST['name']
        award_title=request.POST['award']
        agency=request.POST['agency']
        year=request.POST['year']
        if int(year)>date.today().year or int(year)<1900:
            return render(request, "cerps/error.html",{
                'message':"Enter valid year"
            } )

        award=Award()
        award.name=name
        award.award=award_title
        award.agency=agency
        award.year=year
        award.save()
        return render(request, "cerps/awardadd.html")
        pass
    else:
        return render(request, "cerps/awardadd.html")

#history
def history(request):
    return render(request, "cerps/history.html")

#vision and mission
def vision_mission(request):
    return render(request, "cerps/vision_mission.html")

#staff
def staff(request):
    return render(request, "cerps/staff.html")

#program coordinators
def program_coor(request):
    return render(request, "cerps/program_coor.html")

#contact
def contact(request):
    return render(request, "cerps/contact.html")

#introduction
def introduction(request):
    return render(request, "cerps/introduction.html")

#taught programs
def taught_pro(request):
    return render(request, "cerps/taught_pro.html")

#reserch programs
def research_pro(request):
    return render(request, "cerps/research_pro.html")

#admission requirements
def add_req(request):
    return render(request, "cerps/add_req.html")

#application process
def app_process(request):
    return render(request, "cerps/app_process.html")

#registration
def registration(request):
    return render(request, "cerps/registration.html")

#tuition and other fees
def fees(request):
    return render(request, "cerps/fees.html")

#program review
def progress_rev(request):
    return render(request, "cerps/progress_rev.html")

#minimum and maximum duration
def min_max_dur(request):
    return render(request, "cerps/min_max_dur.html")

#course requirements
def course_req(request):
    return render(request, "cerps/course_req.html")

#format, submission and evaluation of thesis
def thesis_format(request):
    return render(request, "cerps/thesis_format.html")

#thesis examiners
def thesis_examiners(request):
    return render(request, "cerps/thesis_examiners.html")

#research areas
def research_areas(request):
    return render(request, "cerps/research_areas.html")
    
#researcg laboratories
def research_labs(request):
    return render(request, "cerps/research_labs.html")
    
#ongoing research
def ongoing(request):
    return render(request, "cerps/ongoing.html")

#collaboration partners 
def collab_partners(request):
    return render(request, "cerps/collab_partners.html")
    
#research grants
def research_grants(request):
    return render(request, "cerps/research_grants.html")
    
#publication facilitation
def publication_facilitation(request):
    return render(request, "cerps/publication_facilitation.html")

#other funding agencies
def funding_ag(request):
    return render(request, "cerps/funding_ag.html")

#faculty research excellence award    
def faculty_excel(request):
    return render(request, "cerps/faculty_excel.html")

#university reserach excellence award    
def university_excel(request):
    return render(request, "cerps/university_excel.html")

#research oerformance scheme    
def research_performance(request):
    return render(request, "cerps/research_performance.html")

#cvcd    
def cvcd(request):
    return render(request, "cerps/cvcd.html")

#regulations    
def regulations(request):
    return render(request, "cerps/regulations.html")

#for staff    
def for_staff(request):
    return render(request, "cerps/for_staff.html")

#for students    
def for_students(request):
    return render(request, "cerps/for_students.html")

#news        
def news(request):
    return render(request, "cerps/news.html")

#events
def events(request):
    return render(request, "cerps/events.html")

#achievements
def achievements(request):
    return render(request, "cerps/achievements.html")

#view news
def news_ind(request, news_id):
    return render(request, "cerps/news{0}.html".format(news_id))

#view events
def event_ind(request, event_id):
    return render(request, "cerps/event{0}.html".format(event_id))

#view achievements
def achievement_ind(request, achievement_id):
    return render(request, "cerps/achievement{0}.html".format(achievement_id))

#edit journal entry
@login_required(login_url='login')
def editjournal(request, journal_id):
    pass

#edit book entry
@login_required(login_url='login')
def editbook(request, book_id):
    pass

#edit patent entry
@login_required(login_url='login')
def editpatent(request, patent_id):
    pass

#edit grant entry
@login_required(login_url='login')
def editgrant(request, grant_id):
    pass

#edit award entry
@login_required(login_url='login')
def editaward(request, award_id):
    pass

#delete journal entry
@login_required(login_url='login')
def deletejournal(request, journal_id):
    record = Journal.objects.get(id = journal_id)
    record.delete()
    return redirect('view')

#delete book entry
@login_required(login_url='login')
def deletebook(request, book_id):
    record = Book.objects.get(id = book_id)
    record.delete()
    return redirect('view')

#delete patent entry
@login_required(login_url='login')
def deletepatent(request, patent_id):
    record = Patent.objects.get(id = patent_id)
    record.delete()
    return redirect('view')

#delete grant entry
@login_required(login_url='login')
def deletegrant(request, grant_id):
    record = Grant.objects.get(id = grant_id)
    record.delete()
    return redirect('view')

#delete award entry
@login_required(login_url='login')
def deleteaward(request, award_id):
    record = Award.objects.get(id = award_id)
    record.delete()
    return redirect('view')