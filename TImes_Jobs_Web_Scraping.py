import requests 
from bs4 import BeautifulSoup
import re
import pandas as pd
url = " https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35&clusterName=CLUSTER_FA&hc=CLUSTER_FA"
res= requests.get(url).text
soup = BeautifulSoup(res,"lxml")
ans = soup.find_all("h2")
lis= []

job_list =[]
job_des_list=[]
job = soup.find_all(class_="heading-trun")
for i in job:
    job_list.append(i.text[9:])
desc= soup.find_all(class_="job-description__")
for k in desc:
    job_des_list.append(re.sub(r"\s{2,}|\n+"," ",k.text))

loc = soup.find_all(class_="srp-zindex location-tru")
loc_li=[]
for i in loc:
    loc_li.append(i.text[5:])
loc_list = []
for i in loc_li:
    ad = re.sub(r"\s|\n"," ",i.strip())
    loc_list.append(ad)

extract_all = soup.find_all("ul",class_="top-jd-dtl mt-16 clearfix")
ext_lis=[]
for i in extract_all:
    
    ad = re.sub(r"\s{2,}|\n+"," ",i.text.strip())
    ext_lis.append(ad)
lis= []
for j in ext_lis:
    a = re.split(r"(\d+\s*-\s*\d+\s*Years)",j.strip())
    lis.append(a)
    
loc=[]
exp=[]
sal=[]
for i in lis:
    loc.append(i[0])
    exp.append(i[1])
    sal.append(i[2])
comp_name= soup.find_all("h3",class_="joblist-comp-name")
comp_list=[]
for i in comp_name:
    comp_list.append(re.sub(r"\s{2,}|\n+"," ",i.text).strip())

tab =pd.DataFrame(
    {
        "Position":job_list,
        "Company" : comp_list,
        "Description":job_des_list,
        "Location":loc,
        "Required Experience":exp,
        "Salary":sal,
        # "links":links
    }
)

tab.index+=1
# tab.to_csv("Times_Jobs_List.csv",index=True)
print("Completed")


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

def send_email(subject, body, sender_email, receiver_email, password):
    """
    Send an email using SMTP with the provided job summary.
    """
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    part = MIMEText(body, "plain")
    message.attach(part)

    try:
        # Example uses Gmail's SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)
        
email_body = "Latest LinkedIn Job Postings:\n\n"

all_info = [job_list[0],
         comp_list[0],
        job_des_list[0],
        loc[0],
        exp[0],
       sal[0]]

email_body += (f"Job Title: {all_info[0]}\n"
                  f"Company: {all_info[1]}\n"
                  f"Description: {all_info[2]}\n\n"
                  f"Location: {all_info[3]}"
                  f"Experiance: {all_info[4]}"
                  f"Salary: {all_info[5]}")

sender = "kalurimanju@gmail.com"
receiver = "kalurimanjunath@gmail.com"
email_password = "Fake@19020"  

send_email("Latest LinkedIn Job Postings", email_body, sender, receiver, email_password)


##### Tested Code ##### 

# def fun(tag):
#     return tag.has_attr('class') and tag.find('href')

# skills = soup.find_all(class_="more-skills-sections")
# skills_list=[]
# for i in skills:
#     skills_list.append(i.text[10:])
# # print(skills_list[0])
# cleaned_list=[]
# for i in skills_list:
#     ad=re.sub(r'\s{2,}|\n+',' ',i.strip())
#     cleaned_list.append(ad.split())
# print(cleaned_list)
# print(job_list)
# print(job_des_list)
# print(loc_list)
# exp = soup.li.find_all(class_="srp-icons experience")
# exp_li=[]
# for i in exp:
#     # exp_li.append(i.text)
#     print(i.text)
# print(loc_li)
# exp_list = []
# for i in exp_li:
#     ad = re.sub(r"\s{2,}|\n"," ",i.strip())
#     exp_list.append(ad)
# print(exp_list)
# print(exp_li)

# exp = soup.find_all("li",string=lambda x:x and "Years" in x)
# print(exp)

# job_table=pd.DataFrame(job_list)
# job_des_table= pd.DataFrame(job_des_list)


# Find all job listings
# job_lists = soup.find_all("ul", class_="top-jd-dtl mt-16 clearfix")

# # Extract details for each job listing
# jobs = []
# for job in job_lists:
#     details = {}

#     # Extract location (handles missing cases safely)
#     location_tag = job.find("li", class_="srp-zindex location-tru")
#     details["Location"] = location_tag.get_text(strip=True) if location_tag else "N/A"

#     # Extract experience
#     experience_tag = job.find("li", string=lambda x: x and "Years" in x)
#     details["Experience"] = experience_tag.get_text(strip=True) if experience_tag else "N/A"

#     # Extract salary
#     salary_tag = job.find("li", string=lambda x: x and ("$" in x or "Not disclosed" in x))
#     details["Salary"] = salary_tag.get_text(strip=True) if salary_tag else "N/A"

#     jobs.append(details)

# # Print extracted job listings
# for job in jobs:
#     print(job)
# print(job_table)
# print(job_des_table)

# for i in ans :
    # if len(i.text)>10:
        # lis.append(i.text[9:])
        # print(i.text[9:])
# len(lis)
# print(lis)

# print(loc)
# print(exp)
# print(sal)
# print(lis)
# print(comp_list)
# print(ext_lis)
# print(i.text)
# print(loc_li)

# links = []
# for tag in soup.find_all("a"):
#     link = tag.get("href")
#     if link :
#         links.append(link)
# print(links)
# job = soup.find("li",class_ = "clearfix job-bx wht-shd-bx")
# links=[]
# for i in job:
#     link= job.header.h2.a["href"]
#     links.append(link)
