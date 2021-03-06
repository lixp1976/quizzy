"""DDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views
import login.views
import polls.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login.views.user_login),
    url(r'^logout/$', login.views.logout_page),
    url(r'^register/$', login.views.register),
    url(r'^register/success/', login.views.register_success),
    url(r'^$', views.home),
    url(r'^contact',polls.views.contact),
    url(r'^test/',include('polls.urls')),
    url(r'submitq/$',polls.views.submitq),
    url(r'',include('forums.urls')),
    url(r'^submitq/$',polls.views.submitq),
    url(r'^javachart/',polls.views.show_javachart),
    url(r'^phpchart/',polls.views.show_phpchart),
    url(r'^pychart/',polls.views.show_pychart),
    url(r'^performance/',polls.views.show_perfindex),
    url(r'^leaderboard/',polls.views.showleadindex),
    url(r'^javaleaderboard/',polls.views.javaleaderboard),
    url(r'^phpleaderboard/',polls.views.phpleaderboard),
    url(r'^pyleaderboard/',polls.views.pyleaderboard),
]
