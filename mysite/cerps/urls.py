from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("view", views.view, name="view"),
    path("journal", views.journal, name="journal"),
    path("book", views.book, name="book"),
    path("patent", views.patent, name="patent"),
    path("grant", views.grant, name="grant"),
    path("award", views.award, name="award"),
    path("history", views.history, name="history"),
    path("vision_mission", views.vision_mission, name="vision_mission"),
    path("staff", views.staff, name="staff"),
    path("program_coor", views.program_coor, name="program_coor"),
    path("contact", views.contact, name="contact"),
    path("introduction", views.introduction, name="introduction"),
    path("taught_pro", views.taught_pro, name="taught_pro"),
    path("research_pro", views.research_pro, name="research_pro"),
    path("add_req", views.add_req, name="add_req"),
    path("app_process", views.app_process, name="app_process"),
    path("registration", views.registration, name="registration"),
    path("fees", views.fees, name="fees"),
    path("progress_rev", views.progress_rev, name="progress_rev"),
    path("min_max_dur", views.min_max_dur, name="min_max_dur"),
    path("course_req", views.course_req, name="course_req"),
    path("thesis_format", views.thesis_format, name="thesis_format"),
    path("thesis_examiners", views.thesis_examiners, name="thesis_examiners"),

    path("research_areas", views.research_areas, name="research_areas"),
    path("research_labs", views.research_labs, name="research_labs"),
    path("ongoing", views.ongoing, name="ongoing"),
    path("collab_partners", views.collab_partners, name="collab_partners"),
    path("research_grants", views.research_grants, name="research_grants"),
    path("publication_facilitation", views.publication_facilitation, name="publication_facilitation"),
    path("funding_ag", views.funding_ag, name="funding_ag"),
    path("faculty_excel", views.faculty_excel, name="faculty_excel"),
    path("university_excel", views.university_excel, name="university_excel"),
    path("research_performance", views.research_performance, name="research_performance"),
    path("cvcd", views.cvcd, name="cvcd"),
    path("regulations", views.regulations, name="regulations"),
    path("for_staff", views.for_staff, name="for_staff"),
    path("for_students", views.for_students, name="for_students"),
    path("news", views.news, name="news"),
    path("events", views.events, name="events"),
    path("achievements", views.achievements, name="achievements"),
    path("news_ind/<str:news_id>", views.news_ind, name="news_ind"),
    path("event_ind/<str:event_id>", views.event_ind, name="event_ind"),
    path("achievement_ind/<str:achievement_id>", views.achievement_ind, name="achievement_ind"),
]