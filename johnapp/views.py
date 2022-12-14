from django.shortcuts import render
from .forms import RegisterForm
from django.http import HttpResponse
from .models import Register,pool
import json
import openai

import smtplib
import ssl
from email.message import EmailMessage


def index(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            registermodel = Register.objects.all()
            #print("from first model",registermodel)
            #convert to list
            registermodeljson = list(registermodel.values())
            registermodeljson = registermodeljson[::-1]
            print("from second model",registermodeljson[0])
            # event_name=registermodeljson[0]['event_name']
            # event_type=registermodeljson[0]['event_type']
            # event_date=registermodeljson[0]['event_date']
            # duration=registermodeljson[0]['duration']
            # venue=registermodeljson[0]['venue']
            # target_group=registermodeljson[0]['target_group']
            # print("data collected from forms:",event_name,event_type,event_date,duration,venue,target_group)
            ai=aimodel(registermodeljson[0])
            
            no_of_participants=find_no_participtants(registermodeljson[0]["event_type"])    
            names_of_participants = find_participants(registermodeljson[0]["event_type"])
            print("Number of Matches found for the interest ", registermodeljson[0]['event_type']," is ",no_of_participants,". And there names are: ",names_of_participants)    

            if ai:
                return render(request, 'aimodel.html', {'ai':ai,"names_of_participants":names_of_participants,"no_of_participants":no_of_participants})

           # aimodel(registermodeljson)
            return render(request, 'index.html', {'registermodeljson': registermodeljson,'ai':ai})
    else:
        form = RegisterForm()
    return render(request, 'index.html', {'form': form})

#creating content for the email
def aimodel(request):

    event_name=request['event_name']
    event_type=request['event_type']
    event_date=request['event_date']
    duration=request['duration']
    venue=request['venue']
    target_group=request['target_group']

    # query1 = "Name: "+event_name + "\nInterest: "+event_type + "\nEvent_Name: "+event_name + "\nDuration: "+duration + "\nVenue: "+venue +"\nDate: "+str(event_date)+"\n\nOutput: "

    users_all=pool.objects.filter()
    
    name = "Johns Baby"
    key1 = "sk-fNSgLM91"
    key2 = "hl9CZAXl"
    key3 = "arXtT3Bl"
    key4 = "bkFJhKz"
    key5 = "jdMFNRy3"
    key6 = "yWivkse6P"
    key = key1+key2+key3+key4+key5+key6
    
    if 1:
        query ="I recently saw a post by "+name+" on LinkedIn sharing his experience about a hackathon that he recently participated. Generate an Invitation mail to "+name+" inviting him to a "+duration+", "+event_type+" Hackathon conducted by "+venue+" on "+str(event_date)+" and mention that i'm inviting him because i saw his recent post on linkedin about his interest in attending hackthons. "
    # print("query1",query1)


    # Define email sender and receiver
    email_sender = 'wel.ai.marketing@gmail.com'
    email_password = 'zwrp btjp foxt whsp'
    email_receiver = 'johns.baby@mca.christuniversity.in'
    

    openai.api_key = key
    response = openai.Completion.create( 
        engine = "text-davinci-003",
        prompt=query,
        temperature=0.1, # how deterministic should your response be, so higher the temp:lower precise it is
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print("------------------------------------------")
    content = response.choices[0].text.split('.')
    print("content obtained",content)

    k=""
    for i in range(len(content)):
        k+=content[i]

    print("filtered content",k)

    body = k

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = "Invitation to "+event_name+" Hackathon!!"
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver,em.as_string())

    eventandinv={'eventname':event_name, 'event_type':event_type, 
    'event_date':event_date, 'duration':duration, 
    'venue':venue, 'target_group':target_group,"message":k}


    return eventandinv


# finds the names of the participants
def find_participants(interest):
    users_all=pool.objects.all().filter(interest=interest)
    lst=[]
    for i in users_all:
        lst.append(i.name)
    return lst

def find_no_participtants(interest):
    users_all=pool.objects.all().filter(interest=interest)
    return users_all.count()    