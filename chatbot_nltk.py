from nltk.chat.util import Chat, reflections

QA = [
    [
        r"Hey|Hello|Hi",
        [
            "Hello","Hey there"
        ],
    ],
    [
        r"Who are you?",
        [
           "I am a bot built by Niyati Patil to respond to any questions you might have about our college."
        ],
    ],
    [
        r"What is the name of |the college?",
        [
           "Vidyavardhini's College of Engineering and Technology, VCET"
        ],
    ],
    [
        r"(.*) college website",
        [
           "https://vcet.edu.in/"
        ],
    ],
    [
        r"(.*) mail id",
        [
           "vcet_inbox@vcet.edu.in"
        ],
    ],
    [
        r"College phone number?",
        [
            "You may contact us on 0250 233 8234"
        ],
    ],
    [
        r"(.*) youtube",
        [
           "https://www.youtube.com/channel/UCjBw5a7WU00GwkxaTjF9jqg"
        ],
    ],
    [
        r"(.*) linkedIn",
        [
           "https://www.linkedin.com/school/vcetvasai/"
        ],
    ],
    [
        r"(.*) facebook",
        [
           "https://www.facebook.com/vidyavardhinicollege/"
        ],
    ],
    [
        r"(.*) erp portal",
        [
           "http://erp.vcet.edu.in/login.htm"
        ],
    ],
    [
        r"Where is this college?",
        [
            "Vasai, Palghar"
        ],
    ],
    [
        r"(.*) address",
        [
            "K.T. Marg, Vartak College Campus, Vasai Road (W), Dist-Palghar, Vasai, Maharashtra 401202"
        ],
    ],
    [
        r"How far is the railway station from college?",
        [
            "It is a short, two minutes walk from Vasai Road(W) Railway Station."
        ],
    ],
    [
        r"Who is the Principal (.*)",
        [
            "Dr.Harish Vankudre is the Principal of the college"
        ],
    ],
    [
        r"Who is the President of |the college",
        [
            "Mr.Vikas Vartak is the President of the college"
        ],
    ],
    [
        r"What is the vision of VCET",
        [
           "To be a premier institution of technical education, aiming at becoming a valuable resource for industry and society"
        ],
    ],
    [
        r"What is the mission of VCET",
        [
           "To provide technologically inspiring environment for learning. To promote creativity, innovation and professional activities."
           "\nTo inculcate ethical and moral values. To cater personal, professional and societal needs through quality education."
        ],
    ],
    [
        r"What is the admission procedure?",
        [
            "All the seats are filled through centralized admission procedure (CAP) and other seats filled through Institute level."
        ],
    ],
    [
        r"What is the length of course?",
        [
            "4 years, UG Course"
        ],
    ],
    [
        r"What is the medium of instruction?",
        [
            "English"
        ],
    ],
    [
        r"(.*) lectures start",
        [
            "The lectures commence by 9:00 am"
        ],
    ],
    [
        r"How many courses|departments|programs does the College provides?",
        [
            "The college offers provides 7 courses","7 courses"
        ],
    ],
    [
        r"Which courses are offered by the college?",
        [
            "Computer Engineering"
            "\nComputer Science and Engineering (Data Science)"
            "\nInformation Technology"
            "\nArtificial Intelligence and Data Science"
            "\nMechanical Engineering"
            "\nElectronics and Telecommunication Engineering"
            "\nCivil Engineering"
        ],
    ],
    [
        r"HOD of Computer Engineering department",
        [
            "Dr. Megha Trivedi is the Head Of Department & Associate Professor of Computer Engineering department"
        ],
    ],
    [
        r"HOD of Computer Science and Engineering|(Data Science) department",
        [
            "Dr. Vikas Gupta is the HOD of Computer Science Engineering(Data Science) department"
        ],
    ],
    [
        r"Deputy HOD of Computer Science and Engineering|(Data Science) department",
        [
            "Mr. Yogesh Pingle is the Deputy HOD & Asst. Prof of Computer Science Engineering(Data Science) department"
        ],
    ],
    [
        r"HOD of Information Technology department",
        [
            "Dr. Thaksen Parvat is the Head Of Department & Professor of Information Technology department"
        ],
    ],
    [
        r"Deputy HOD of Artificial Intelligence and Data Science department",
        [
            "Ms. Sejal D’mello is the Deputy HOD & Asst. Professor Artificial Intelligence and Data Science department"
        ],
    ],
    [
        r"HOD of Mechanical Engineering department",
        [
            "Dr. Uday Aswalekar is the Head Of Department of Mechanical Engineering department"
        ],
    ],
    [
        r"HOD of Electronics and Telecommunication Engineering department",
        [
            "Dr. Amrita Ruperee is the Head of Department & Associate Professor of Electronics and Telecommunication Engineering department"
        ],
    ],
    [
        r"HOD of Civil department department",
        [
            "Dr. Ajay Radke is the HOD & Professor of Civil department"
        ],
    ],
    [
        r"(.*) FE Coordinator",
        [
            "Dr. Sunayana Jadhav is the FE Coordinator"
        ],
    ],
    [
        r"What is the number of intake(.*)",
        [
            "Computer Engineering - 60"
            "\nComputer Science and Engineering (Data Science) - 60"
            "\nInformation Technology - 60"
            "\nArtificial Intelligence and Data Science - 60"
            "\nMechanical Engineering - 90"
            "\nElectronics and Telecommunication Engineering - 60"
            "\nCivil Engineering - 30"
        ],
    ],
    [
        r"(.*) university",
        [
            "Mumbai University"
        ],
    ],
    [
        r"How many semester|s (.*)",
        [
            "8 semesters"
        ],
    ],
    [
        r"(.*) fees (.*) FE|First Year",
        [
            "116225.00 rs"
        ],
    ],
    [
        r"(.*) fees (.*) dse|Direct Second Year",
        [
            "116100.00 rs"
        ],
    ],
    [
        r"Where is the college office?",
        [
            "The college office is on the first floor of the main building."
        ],
    ],
    [
        r"Is there a Library?",
        [
            "Yes there is a Library in VCET located on the Fifth Floor."
        ],
    ],
    [
        r"What are |the Library timings",
        [
            "Monday to Friday 8:00 am to 6:00 pm"
            "\nSaturday and Sunday closed."
        ],
    ],
    [
        r"Name of |the librarian",
        [
            "Name of the Librarian is Mr.Dinesh Jadhav"
        ],
    ],
    [
        r"Is there a ladies common room?",
        [
            "Yes there is a Ladies Common Room in VCET on the First Floor."
        ],
    ],
    [
        r"Is there a Gymkhana in the college?",
        [
            "Yes, there is a Gymkhana at VCET, located in a different building next to the main building."
        ],
    ],
    [
        r"Extra curricular activities in VCET",
        [
            "The Extra-Curricular activities in VCET are \nStudent's Council \nSports Committee \nLiterati \nNSS"
        ],
    ],
    [
        r"Co curricular|Co-curricular activities in vcet",
        [
            "The Co-Curricular activities in VCET are \nIEEE \nSAE \nISA \nCSI \nIETE \nISHRAE \nVMEA \nHACKATHON"
        ],
    ],
    [
        r"(.*) fests (.*)",
        [
            "We have Zeal, annual cultural fest and Avahan, annual sports event"
        ],
    ],
    [
        r"college committee|s",
        [
            "Student's Council \nSports Committee \nLiterati \nE-Cell \nNSS and many more."
        ],
    ],
    [
        r"(.*)about Student's Council",
        [
            "The Students’ Council of Vidyavardhini’s College of Engineering and Technology cardinally aims on a holistic approach to enhance the students’ life at V.C.E.T, "
            "\nfostering the students to grow inside the classroom and outside of it too. We conduct and organize a multifarious array of events throughout the year thereby creating "
            "\nan ambience for building engineers to learn, hone their talents and showcase their competences on wider platform."
        ],
    ],
    [
        r"Events conducted by Student's Council",
        [
            "Events like FE Orientation, Fresher’s Party, Teacher’s Day, Garba Night, Zeal, BE Farewell are conducted by Student's Council."
        ],
    ],
    [
        r"(.*)about Sports Committee",
        [
            "The Sports Committee organizes its annual Sports fest AVAHAN, 11 day long Inter and Intra college event. We aim at culminating our eleven days of sports celebration(festivities)"
            "\ninto a grandeur of enthusiasm and thrill, goosebumps and the sounds of victory, strategy and skill."
        ],
    ],
    [
        r"Events conducted by Sports Committee",
        [
            "Events like Induction Program, Team Selection and Participation, AVAHAN are conducted by Sports Committee."
        ],
    ],
    [
        r"(.*)about Literati",
        [
            "The magazine committee was remoulded and renamed and took its form as the LITERATI – THE LITERARY CLUB. The sole responsibility of this committee is to spread the "
            "\nlight of knowledge about literature, art and display the outstanding work of our creative-minded vcetians through our annual college magazine ‘VISTA’."
        ],
    ],
    [
        r"Events conducted by Literati",
        [
            "Events like Inaugraduation Of ‘VISTA’, VCET Podcast, Unscripted – Extempore, Marathi and Hindi Kavi Sammelan, Faceoff, Faceoff – Intercollegiate, Lit Fest, "
            "\nMarathi Bhasha Diwas are conducted by Literati."
        ],
    ],
    [
        r"What is NSS?",
        [
            "NSS is the National Service Scheme."
        ],
    ],
    [
        r"(.*)about NSS",
        [
            "The National Service Scheme (NSS) Government of India, Ministry of Youth Affairs & Sports provides an opportunity to the student youth of INDIA to take part in various government "
            "\nled community service activities & programs. The sole aim of the NSS is to provide hands-on experience to young students in delivering community service. UDAAN was founded in "
            "\nthe academic year 2014-2015 at VCET. Now UDAAN comes under the NSS committee of VCET."
        ],
    ],
    [
        r"Events conducted by NSS",
        [
            "Events like Blood Donation Survey, Donation Campaign, Constitution Day Webinar, Tree Plantation in Society, Meditation and Yoga Session are conducted by NSS."
        ],
    ],
    [
        r"Co-ordinator of NSS",
        [
            "Dr. Pradip Gulbhile(Humanity Department) is the co-ordinator of NSS."
        ],
    ],
    [
        r"(.*)about IEEE",
        [
            "IEEE is the world’s largest technical professional organization dedicated to advancing technology. IEEE Student Branch VCET aims at empowering students "
            "\n& inculcating in them essential professional skills like teamwork, leadership, managerial skills, etc. through events like Technical Workshops and seminars, "
            "\nGuest lectures by industry experts from diverse backgrounds, hands-on software and hardware workshops and training sessions "
            "\n& our marquee annual technical Product Showcase event ‘Anveshan’."
        ],
    ],
    [
        r"(.*)about SAE",
        [
            "SAE International is the global leader in technical learning for the mobility industry whereas SAEINDIA is India’s leading resource for mobility technology."
            "\nThe Mechanical Engineering Department of VCET is associated with the SAEINDIA from long time. Various teams like Team ETHAN, Team SOLECTHON, Team CENTURION "
            "\nparticipates in national level events under the umbrella of SAE-VCET committee."
        ],
    ],
    [
        r"(.*)about ISA",
        [
            "The International Society of Automation, functioning since 1945, is a non-profit professional association in USA. The VCET ISA Students’ Chapter is "
            "\ninstrumental from many years into organizing technical events such as workshops, seminars, training and talks etc. in the field of process instrumentation and automation. "
            "\nThe motto of this committee is to bring the industry closer to the students and provide the students a platform to be a better Instrumentation Engineer."
        ],
    ],
    [
        r"(.*)about CSI",
        [
            "Computer Society of India is the first and largest body of computer professionals in India. Amidst all, it’s other responsibilities the CSI students chapter understands "
            "\nthat the primary objective of its existence is to promote the development of a coding culture and to help students ameliorate their technical skills. "
            "\nTo achieve this, CSI-VCET organizes various technical seminars, workshops, coding competitions, and project showcases every year."
        ],
    ],
    [
        r"(.*)about IETE",
        [
            "The Institution of Electronics and Telecommunication Engineers (IETE) is India’s leading recognized professional society devoted to the advancement of "
            "\nScience and Technology of Electronics, Telecommunication & IT. VCET IETE-SF promotes and conducts basic engineering and continuing technical education programmes "
            "\nfor human resource development. Every year, VCET IETE-SF organizes events like Oscillations (technical paper presentation), VNPS (VCET National level product showcase), "
            "\nInterdepartmental quiz competition, seminars and workshops on various topics in the EXTC domain."
        ],
    ],
    [
        r"(.*)about ISHRAE",
        [
            "MISSION: To advance the arts and sciences of heating, ventilating, air conditioning and refrigerating to serve humanity and promote a sustainable world. "
            "\nVISION: ISHRAE will be the global leader, the fore most source technical and educational information, and the primary provider of opportunity for professional growth "
            "\nin the arts and sciences of heating, ventilating, air conditioning and refrigerating."
        ],
    ],
    [
        r"(.*)about VMEA",
        [
            "VMEA stands for Vidyavardhini’s Mechanical Engineers Association. It is a committee built entirely on the drive of its members. "
            "\nVMEA involves organizing events and competitions such as Product showcases, Quiz competitions, Project competitions etc. "
            "\nVMEA along with organizing such great events also primarily focuses upon building core technical knowledge of the students which enables them to develop a technical perspective."
        ],
    ],
    [
        r"(.*)about HACKATHON",
        [
            "VCET-Hackathon is an inter-collegiate national level coding competition which involves 30 hours of incessant coding followed by the pitching round. "
            "\nParticipants have to come up with some working prototype/solutions to address some worthy and challenging problems in these 30 hours after which the projects "
            "\nare judged by a panel of judges. There is a continuous monitoring of the projects by the jury members. "
        ],
    ],
    [
        r"Is there an ecell(.*)",
        [
            "Yes VCET has an entrepreneurship cell also known as E-Cell."
        ],
    ],
    [
        r"(.*)about ecell|E-Cell",
        [
            "The entrepreneurship cell of V.C.E.T., known as ‘E-Cell’ is formed with an objective of fostering entrepreneurship skills amongst the students of V.C.E.T."
            "\nIt is a student-driven and faculty-guided cell striving to channel the competencies of the budding engineers. With a variety of programs "
            "\nE-Cell plays a key role in the development of entrepreneurial skills and giving an opportunity to the deserving."
        ],
    ],
    [
        r"Events conducted by ecell|E-Cell",
        [
            "E-Cell hosts events such as E-Summit, Bizmaster, Internship Fair, and many more."
        ],
    ],
    [
        r"Staff incharge of ecell|E-Cell",
        [
            "Mr. Chandan Kolvankar, Co-ordinator of E-cell"
            "\nmail: chandan.kolvankar@vcet.edu.in"
            "\nphone no.:9049863248"
        ],
    ],
    [
        r"(.*) placement related queries",
        [
            "You can contact \nMr. Prafulla Patil, Placement Manager"
            "\nplacements@vcet.edu.in\n7710070966"
        ],
    ],
    [
        r"Placement companies",
        [
            "TCS, Capgemini, Infosys, BYJUS, Johnson Controls, Coca-Cola, Mahindra, IBM, HLS, Jio, Cognizant"
        ],
    ],
    [
        r"(.*) placement statistic|s",
        [
            "2016-17 = 258"
            "\n2017-18 = 299"
            "\n2018-19 = 320"
            "\n2019-20 = 263"
            "\n2020-21 = 199"
            "\n2021-22 = 337"
        ],
    ],
    [
        r"(.*) scholarship and freeship forms",
        [
            "You can fill the forms for scholarship and freeship on the mahadbt website \nFor more  details you can also contact the college office \nphone no 75583 51747"
        ],
    ],
    [
        r"Scholarship schemes",
        [
            "Scholarships such as Dr. Panjabrao Deshmukh Vastigruh Nirvah Bhatta Yojna(DTE)"
            "\nRajarshi Chhatrapati Shahu Maharaj Shikshan Shulkh Shishyavrutti Yojna(EBC)"
            "\nStudents from Minority Communities Pursuing Higher and Professional Courses.(DTE) and more."
        ],
    ],
    [
        r"Criteria for filling the scholarship or freeship form",
        [
            "You can only apply for only one of the both schemes. \nYour family's annual income must be less than 1 lakh rupees for the scholarship application and less than 8 lakh rupees for the freeship application."
        ],
    ],
    [
        r"Bye|Byee|!",
        [
            "Byee!!"
        ],
    ],
[
        r"Thanks|Thankyou",
        [
            "Welcome! I hope I resolved all of your queries."
        ],
    ],
]

def mybot():
    print("Hi \nYou can ask your Questions here!")

chat = Chat(QA, reflections)
if __name__ =="__main__":
    mybot()

    chat.converse()