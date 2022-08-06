from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datetime import date,datetime

bot = ChatBot('Buddy',storage_adapter='chatterbot.storage.SQLStorageAdapter',database_uri='sqlite:///database.sqlite3')
trainer=ListTrainer(bot)

trainer.train([
'Hi',
'Hello',
'Who are You?',
'I am a bot built by Niyati Patil to respond to any questions you might have about our college.',
'What is the name of college?',
'Vidyavardhini College of Engineering and Technology, VCET',
'Where is this college?',
'Vasai, Palghar',
'What is the college address?',
'K.T. Marg, Vartak College Campus, Vasai Road (W), Dist-Palghar, Vasai, Maharashtra 401202',
'How far is the railway station from college?',
'It is a short, two minutes walk from Vasai Road(W) Railway Station.',
'Who is the Principal?',
'Dr.Harish Vankudre is the Principal of the college.',
'Who is the President of the college?',
'Mr.Vikas Vartak is the President of the college.',
'What is the vision of VCET?',
'To be a premier institution of technical education, aiming at becoming a valuable resource for industry and society',
'What is the mission of VCET?',
'To provide technologically inspiring environment for learning. To promote creativity, innovation and professional activities. To inculcate ethical and moral values. To cater personal, professional and societal needs through quality education.',
'What is the admission procedure?',
'All the seats are filled through centralized admission procedure (CAP) and other seats filled through Institute level.',
'What is the length of course?',
'4 years, UG Course.',
'What is the medium of instruction?',
'English.',
'When do the lectures start?',
'The lectures commence by 9:00 am',
'How many Semesters?',
'8 semesters.',
'What is the college website?',
'https://vcet.edu.in/',
'What is college email?',
'It is vcet_inbox@vcet.edu.in',
'What are contact available for reference?',
'You can refer this contact: 0250 233 8234',
'What is the college Youtube channel?',
'https://www.youtube.com/channel/UCjBw5a7WU00GwkxaTjF9jqg',
'What is the college LinkedIn?',
'https://www.linkedin.com/school/vcetvasai/',
'What is the college facebook account?',
'https://www.facebook.com/vidyavardhinicollege/',
'How many courses does the college provide?',
'The college offers 7 courses.',
'What are courses available in VCET?',
'Courses available are: Comps, CSE-DS, AI-DS, IT, CIVIL, Mechanical, EXTC',
'How many Seats available for all courses?',
'Mechanical:90, Comps, IT, EXTC, AI & CSE:60, Civil:30',
'What are the annual functions or fests in the college?',
'Many events are organized in the college, like Zeal, Avahan, Hackathon, Lit Fest and much more.',
'Thank You',
'Welcome! I hope I cleared all your questions.',
'Byee',
'Bye!'
])

name=input("Enter Your Name:")
now=datetime.now()
today=now.strftime("%A")
time=now.strftime("%H:%M:%S")

print("Hi,I am Bot created by Niyati Patil")
print(f"Today is {today},current time is {time}")
print("Please let me know how I can assist you")

while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot:Bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)