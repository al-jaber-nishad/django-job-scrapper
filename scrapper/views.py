from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.

t_r = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")
t_soup = BeautifulSoup(t_r.content, 'lxml')
jobs = t_soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

news_link = []
news_title = []
skills = []
result = {}
for job in jobs:
  title = job.find('h2').strong.text
  link = job.find('h2').a["href"]
  # news_link.append(link)
  # news_title.append(title)
  skill = job.find('span', class_="srp-skills").text.replace(" ", "")
  # skills.append(skill)

  result[title] = (link, skill)

def index(request):
  return render(request, 'scrapper/index.html', {'result':result})