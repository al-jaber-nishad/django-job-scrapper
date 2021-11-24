

from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.

# Careerjet Website
t_r = requests.get("https://www.careerjet.com.bd/django-jobs.html")
t_soup = BeautifulSoup(t_r.content, 'lxml')
jobs = t_soup.find_all('article', class_="job clicky")

bd_jobs = []
for item in jobs:
  dict = {}

  h = item.find('header').text
  li = item.find('a')['href']
  li = "https://www.careerjet.com.bd" + li
  f = item.find('footer').text
  loc = item.find('ul', class_="location").text
  sal = item.find('ul', class_="salary")
  d = item.find('div', class_="desc").text
  
  dict['header'] = h
  dict['link'] = li
  dict['des'] = d
  dict['location'] = loc
  if sal:
    dict['salary'] = sal.text
  else:
    dict['salary'] = "Not mentioned"
  dict['days'] = f
  
  bd_jobs.append(dict)

# Internshala Website
t_r = requests.get("https://internshala.com/internships/work-from-home-python%2Fdjango-jobs")
t_soup = BeautifulSoup(t_r.content, 'lxml')
jobs = t_soup.find_all('div', class_="internship_meta")

indian_jobs = []
for item in jobs:
  dict = {}

  h = item.find('div', class_='heading_4_5 profile')
  li = h.find('a')['href']
  li = "https://internshala.com" + li
  sal = item.find('span', class_="stipend")
  f = item.find('div', class_="apply_by").text
  
  dict['header'] = h.text
  dict['link'] = li
  if sal:
    dict['salary'] = sal.text
  else:
    dict['salary'] = "Not mentioned"
  dict['days'] = f
  
  indian_jobs.append(dict)


def index(request):
  return render(request, 'scrapper/index.html', {'bd_jobs':bd_jobs, 'indian_jobs':indian_jobs})

def bdJobs(request):
  return render(request, 'scrapper/bd-jobs.html', {'bd_jobs':bd_jobs})

def indJobs(request):
  return render(request, 'scrapper/ind-jobs.html', {'indian_jobs':indian_jobs})