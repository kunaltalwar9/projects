import smtplib
from email.message import EmailMessage
import os
from email.utils import formataddr

'''

# === CONFIGURATION ===
your_email = "1996kunaltalwar@gmail.com"
your_password = "lnqk bkzs fspm jtwz"  # For 2FA, use App Password
to_emails = ["rohansahai1993@gmail.com", "kunaltalwar1996@gmail.com", "kunal.a.talwar@gmail.com"]
subject = "CV for SAP Hybris | Quality Assurance Engineer"
body = """\
Hi,

I hope you are doing well. I am reaching out to express my interest in Quality Assurance opportunities and have attached my CV for your consideration.

I would appreciate the opportunity to be considered and am happy to provide any additional information if required. Looking forward to your response.


Thanks and Regards,
Kunal Talwar
+91 9686128467
"""

cv_path = r"E:\\PRS-20211022T081111Z-001\\PRS\\CV32.pdf"

# === LOAD ATTACHMENT ONCE ===
try:
    with open(cv_path, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(cv_path)
except Exception as e:
    print(f"❌ Error reading CV file: {e}")
    exit()

# === SEND EMAIL ONE BY ONE ===
for recipient in to_emails:
    msg = EmailMessage()
    msg["From"] = formataddr(("Kunal Talwar", your_email))
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content(body)
    msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(your_email, your_password)
            smtp.send_message(msg)
        print(f"✅ Email sent successfully to: {recipient}")
    except Exception as e:
        print(f"❌ Failed to send email to {recipient}: {e}")


'''
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
import os

# ---------- CONFIGURATION ----------
WHICH_EMAIL = 1
your_email = ["1996kunaltalwar@gmail.com", "kunaltalwar1996@gmail.com" ,"kunal.a.talwar@gmail.com", "kunaltalwarthegreat@gmail.com"]
your_password = ["lnqk bkzs fspm jtwz","uetg uzjd tmyj bfpg", "byom wvrs bqif gonv"] # For 2FA, use App Password
to_emails = []#, ]
# deloitte_emails = ["nnagaonkar@deloitte.com","akalkeri.ext@deloitte.com","nekan.ext@deloitte.com","shdandekar@deloitte.com","pdhole.ext@deloitte.com", "sumchaudhary@deloitte.com","riyam.ext@deloitte.com","sadsouza@deloitte.com","jdsa.ext@deloitte.com", "abhombore@deloitte.com", "maadulla@deloitte.com"]
# "hemanth.durga@tekishub.in", "tarun@uplevelsolutions.in", "manu.chandrappa@capgemini.com", "tarun@uplevelsolutions.in", "hemanth.durga@tekishub.in", " tejaswini@elabsinfotech.com", "anjali.shah@rediansoftware.com", "prathyusha@zortechs.in", "stutia@softwareco.com", "subhamingale@yerlat.com", "magesh-b@hcltech.com", "mihir@highring.com", "aditi@mathesislabs.com", "Priya.walia@codersbrain.com", "Lakshmi.narayanan2@comcast.com", "vindhyasri@elabsinfotech.com",
# To test emails #to_emails = ["kunaltalwarthegreat@gmail.com", "kunaltalwar1996@gmail.com", "1996kunaltalwar@gmail.com", "kunal.a.talwar@gmail.com", "rohansahai1993@gmail.com"]
old_sent_email_list = ["bhavana.b@yallas.tech", "villina.sebastian@fnz.com", "Divya_Kumpatla@persolkelly.com", "kaustiv.saha@hexaware.com", "infosys.referral123@gmail.com","mohit_kumar@outlook.com","ssnreddy120@gmail.com", "nikita.negi@infosys.com", "shree.yr@gmail.com","manivardhanreddy.vanukuri@tcs.com", "md.irfan1@tcs.com", "shilpa.kondapuram@cgi.com", "choubeyarpit963@gmail.com","chanchal@nagarro.com", "shivangi.sharma@paytmbank.com", "kshama.chanda@nagarro.com", "chanchal.yadav@nagarro.com", "Indrakanta.Gupta@fisglobal.com", "dhirajkumar.nk@gmail.com", "manidhull@gmail.com", "alok.dcsa@gmail.com", "tushar.narayan@thoughtworks.com", "gauravgarg0408@gmail.com", "udayn@moback.com", "jayantap@moback.com", "pagarwal@tsys.com", "bmohanty503@gmail.com", "ranjeet.c@testyantra.com", "pkuswaha477@gmail.com", "siddharthnahata05@gmail.com", "kapilskelkar@gmail.com",
                       "sarmita@vahan.co", "amoghgowda5@gmail.com", "gauravgarg0408@gmail.com", "shaik.roshan@sapiens.com", "dipesh.nagpal@citiustech.com", "anish.nayak.rpg@gmail.com", "inlinesam66@gmail.com", "cddhrth@gmail.com", "satyam.a@cgi.com","meenashree.ratha@ibm.com", "saraswathi.r@cgi.com","prathikponnanna.kodava@cgi.com", "ayushi.mahajan@nagarro.com", "swati.sanjagiri@tcs.com", "arun_negi@infosys.com","Sreeja@interaslabs.com", "hr@niyaraconsulting.com", "bvenky@nastechglobal.in", "tejaswini@elabsinfotech.com", "tech5@Impeccablehr.com", "surendher@vysystems.com", "shivangi.parshad@ditstek.com", "andhar@teksystems.com", "abushan@buxtonconsulting.com", "varsha@brimlabs.ai", "muskan.rastogi@truelancer.com", "Vishal.tyagi@vvdntech.in","aravindh.r@encora.com", "josmy.jacob@bt.com", "ganesh.n@talentwood.org", "sakthivelr@hexaware.com", "Mayank.k@rediansoftware.com",
                       "rachna.jha@irissoftware.com", "hr@theninehertz.com", "sathya.m@encora.com", "anu.mittal@testingxperts.com", "surendra@diversitynexus.net", "hr1@ioweb3.io", "saniya_hemt@quinstreet.com", "tarun@creoinvent-tech.com", "anjali.shah@rediansoftware.com", "vandana@leegality.com", "roshni.sah@ltimindtree.com", "Pavithra@tagletconsulting.com", "sonia@d2nsolutions.com", "nvinod@thoughtframeworks.com", "maheswari.m@hashroot.com", "Neelaveni.c@prachodayathglobal.com", "harshwardhan@bytesar.com", "hr@imposglobal.com", "Pinky.rao@varite.com", "bhuvaneswari.v@techedge-solution.com", "sheelu@talent-arabia.com", "manoharan@atriaconsultingservices.com", "prakiran@teksystems.com", "aarti.arvikar@valuedx.com", "gauri@hexagonselect.com", "meera.singh@varite.com", "venu@santosystems.com", "navaneethan@reveilletechnologies.com", "deepti.mishra@zilliontechnologies.com",
                       "hrhub@derbium.com", "gkarthik@softpathtech.com", "careers@softpathtech.com", "preetam@talenttoppers.com", "aman.pal@gartner.com", "deepika@absika.com", "srinivas@zclus.com", "vinti.bhutda@covetus.com", "sita@evolutyz.com", "nareshkumar.g@sisocsemi.com", "nisha.k@rhrint.in", "careers@vervesquare.com", "anwesha.roy@moolya.com", "divya.vivek@codersbrain.com", "prathyusha@zortechs.in", "hr@nxtentry.com","sudhakart@celcomsolutions.com", "hari@tcsin.com", "hr1@ioweb3.io", "stutia@softwareco.com", "subhamingale@yerlat.com", "harikrishnan.r@twsol.com", "jigishaben.biradar@ltimindtree.com", "kalpita@renovatecareer.co.in", "magesh-b@hcltech.com","Amisha.Dubey@lancesoft.in", "kareem@askconsulting.com", "Jyothsna@promachrsolutions.com", "nikita.sharma@trreta.com", "hr@mywisepower.in", "shishir.kumar@mywisepower.in", "tamanna.sharma@reveation.io", "qa-tester@jobs.kcsos.in",
                       "geetha@compugra.com", "Jaimin@gracehire.com", "hr.aparajita@infoigy.com", "recruitment@infoigy.com", "nikita.sharma@trreta.com", "jyoti.kumari@fiserv.com", "admin@smartplacement.biz", "mazhar.khan@capgemini.com", "navyas@hankersystems.in", "rajiv.raju@placeelements.com", "navyam@systechcorp.in", "sajan.m@techmantraglobal.com", "nikitha@pso.amktechnology.com", "gharishk@tblocks.com", "shailly@spaceogroup.com", "mayank.gupta@diverselynx.com", "mazhar.khan@capgemini.com", "hr@emeriosoft.com", "hire-india@onedatasoftware.com", "khushbu@adlerqa.in", "rachna.bhagat@alliancebernstein.com", "rachna.bhagat@alliancebernstein.com", "snehalata.rath@hankersystems.in", "rachna.bhagat@alliancebernstein.com", "susheel.jaiswal@talteam.com", "asirohi@marquistech.com", "g.mahesh@vhsconsulting.net", "sakshi.gupta@natwest.com", "namratha.katke@neutrinotechlabs.com", "arpita.shinde@sgsconsulting.com",
                       "diksha.ranpise@capgemini.com", "r1@hiking-it.com", "gopalnehaa@gmail.com", "hiringsejal4@gmail.com", "CV@bluestoneprime.com","chandna.awasthi@fidelity.co.in", "mehak.dhawan@fil.com", "manikanta.sanagapalli@intelliswift.com", "tanya.talwar@intelliswift.com", "ashwini.bhuvanagiri@intelliswift.com", "abhishek.patel@htmanpower.com", "aditi@mathesislabs.com", "rajiv.raju@placeelements.com","aastha.s@kaygen.com", "rp.adusumilli@hypergts.com", "aishwarya.chugh@opstree.com", "neha.sharma@testingxperts.com", "shailaja.vejendla@teamlease.com", "prerana.w@prometteursolutions.com", "swetha.s@vivotexindia.com", "hr@refermegroup.com", "prashanth.chunchu@namsbel.com", "hr@refermegroup.com", "shivangee.singh@qtsolv.com", "nancy_khandelwal@epam.com", "namrata.jena@survik.com", "shraddha.p@anlage.co.in", "r.rahul@azentio.com", "hr@sqelabs.com", "sumany@hexaware.com", "nikki.kansal@applore.in",
                       "Soniya.tak@covetus.com", "manisha.sawwalakhe@tescra.com", "suhashini.singh@irissoftware.com", "shehnila.r@tekitsolution.com", "diksha.ranpise@capgemini.com", "subha@kaerusworld.com", "Vibhuti.gupta@geminisolutions.com", "mariavi@epidata.net", "sravani@nexwave.in", "manish.l@ipsator.com", "Sujatha@compugra.com", "Gayathri@spruceinfotech.com", "Teja.c@in.csiglobal.co.uk", "neha.ruhela@nagarro.com", "anusha.hs@ltts.com", "tanu@consignspacesolutions.com", "Sarath.m@ubique-systems.com", "Jyoti.katyal@exlservice.com", "sonal.gupta4@globallogic.com", "hariprasanth@vysystems.com", "hariprasanth@vysystems.com", "ishan.shukl@nykaa.com", "neha.saluja@infogain.com", "tanyajain@thegrowthpartners.in", "Priya.walia@codersbrain.com", "hbellary@primusglobal.com", "deepika.g@glentzestech.com", "t.kantharaju@glentzestech.com", "india.team@poweritservices.com", "shiva.d@randstaddigital.com",
                       "swati.damani@irissoftware.com", "gauri.dudeja@sakashgroup.in", "swati.kumari@antino.com", "madhushree@maplelms.com", "keshav.banoth@arisetg.com", "kanishtha.mathur@publicissapient.com", "hr9@pioneercadsolution.com", "prajakta@thecorporatedemands.com", "ragesh.ac@cielhr.com", "rihana.s@costaffglobal.in", "Viswanathan_v@epam.com", "neha.ruhela@nagarro.com", "priyadarshini-v@hcltech.com", "namratha.katke@neutrinotechlabs.com", "snehalata.rath@hankersystems.in", "silpa.e@se-mentor.com", "Lakshmi.narayanan2@comcast.com", "shalvi.saxena@adactin.com", "chetan.singh@auragold.in", "metilda.j@msphitect.com.my", "oshin.nandanwar@harjai.com", "simran.agarwal@devlabstechnology.com", "sneha.g@tekitsolution.com", "pushpam.s@okool.com", "praveen.sonkamble@paraminfo.com", "rpatel@neuroniks.com", "shraddha.sai@sivarsa.com", "placements@fortunecloudindia.com", "sejal.inamdar@ampcustech.com",
                       "bhavana@ketsoftware.com", "narayan@rajcons.com", "rajat_kaushik@optum.com", "meenu.rani@sourcefuse.com", "tripta.narula@appzlogic.com", "isha.mahajan@appzlogic.com", "manne.malleswari@tcs.com", "neha.gupta02@irissoftware.com", "anil.dhiman88@gmail.com", "dhivyar@destarinc.com", "jyothi.edugu@coforge.com", "bhargavi.l@manvision.net", "amit.soni1@in.ey.com", "shivani.ganatra@programming.com", "Indra.k@testyantra.com", "mihir@highring.com", "kriti@insbytech.com", "aswini.b@twsol.com", "pravalikad@hankersystems.in", "mchandra@thehive.ai", "shilpa.soreng@intileo.com", "haritha.k@people-prime.com", "info@techstackindia.com", "careers@freetimehospitality.in", "rupika@rightbrain.co.in", "Nutan.anand1@genpact.com", "ayush.sharma1@rsystems.com", "Krishnaveni.kathi@hankersystems.in", "sudhanshu.mishra@truelancer.com", "nkrishnakumar@primusglobal.com", "shivani@groupvb.com",
                       "vanshika.jagtap@arrise.com", "saranya.r@balbhas.com", "tarun@uplevelsolutions.in", "vibha.singh@ltimindtree.com", "vindhyasri@elabsinfotech.com", "sasati@eteaminc.com", "shailesh.parmar@collabera.com", "gurunath@vrdella.com", "premnath.elamasan@vysystems.com", "sonali@fxconsulting.in", "careers@kratikal.com", "Sivaprasad.s@tavant.com", "vvemula@radiants.com", "geetesh.indorewale@appzlogic.com", "sweety@questhiring.com", "cdhiring@zomato.com","vaishnavi.suvarna@acldigital.com","tripta.narula@appzlogic.com", "tag@ksolves.com"]
# Toggle True for same subject/body/attachment to all
use_same_subject_body_cv = True

# Common subject, body, and CV path (if sending same to all)
common_subject = "Experienced QA Engineer (6.5 Yrs) | Expert in Defect Analysis & Release Quality"#"CV for Quality Assurance Engineer | 6.5 Years Experience "
common_body = """\
Hi,

Focused on Streamlining test cycles and ensuring zero-defect releases, I have consistently delivered quality that scales.

As a seasoned QA professional dedicated to flawless user experiences, I bring over 6.5 years of hands-on experience in Quality Assurance — including manual testing, automation (Selenium with Python), and API testing. I have a sharp eye for detail, strong defect analysis skills, and a passion for delivering stable, user-centric applications. My expertise lies in ensuring seamless product releases.

I have attached my CV for your review and would be grateful for the opportunity to contribute my expertise to your team. 
Please feel free to reach out if you need any additional information.

Looking forward to the possibility of connecting.

Warm regards,
Kunal Talwar
+91 9686128467
"""
"""
Hi,

I hope you are doing well. I am reaching out to express my interest in Quality Assurance opportunities and have attached my CV for your consideration.
I would appreciate the opportunity to be considered and am happy to provide any additional information if required. 
Looking forward to your response.


Thanks and Regards,
Kunal Talwar
+91 9686128467
"""

common_cv_path = r"E:\\PRS-20211022T081111Z-001\\PRS\\CV32.pdf"

# OR provide separate values (if use_same_subject_body_cv = False)
subjects = [
    "CV for Senior Test Analyst",""
    "CV for SAP Hybris QA",
    "CV for SDET/Test Automation Engineer"]
bodies = [
    """\
    Hi,

I hope you are doing well. I am reaching out to express my interest in Quality Assurance opportunities and have attached my CV for your consideration.

I would appreciate the opportunity to be considered and am happy to provide any additional information if required. Looking forward to your response.


Thanks and Regards,
Kunal Talwar
+91 9686128467

    
    """,
    """\
    Hi,

I hope you are doing well. I am reaching out to express my interest in SAP Hybris QA opportunities and have attached my CV for your consideration.

I would appreciate the opportunity to be considered and am happy to provide any additional information if required. Looking forward to your response.


Thanks and Regards,
Kunal Talwar
+91 9686128467

    """,
    """\
    Hi,

I hope you are doing well. I am reaching out to express my interest in SDET/Test Automation opportunities and have attached my CV for your consideration.

I would appreciate the opportunity to be considered and am happy to provide any additional information if required. Looking forward to your response.


Thanks and Regards,
Kunal Talwar
+91 9686128467

    """
    ]
cv_paths = [
    r"E:\\PRS-20211022T081111Z-001\\PRS\\CV32.pdf",
    r"E:\\PRS-20211022T081111Z-001\\PRS\\CV32A.pdf",
    r"E:\\PRS-20211022T081111Z-001\\PRS\\Kunal Talwar Resume.pdf"
]

# ---------- SENDING EMAIL ----------
for i, recipient in enumerate(to_emails):
    try:
        msg = EmailMessage()

        # Set From with name
        msg["From"] = formataddr(("Kunal Talwar", your_email[WHICH_EMAIL-1]))
        msg["To"] = recipient

        # Decide subject, body, cv based on toggle
        if use_same_subject_body_cv:
            msg["Subject"] = common_subject
            body = common_body
            cv_path = common_cv_path
        else:
            msg["Subject"] = subjects[i]
            body = bodies[i]
            cv_path = cv_paths[i]

        msg.set_content(body)

        # Attach CV
        with open(cv_path, "rb") as f:
            file_data = f.read()
            file_name = os.path.basename(cv_path)
        msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

        # Send Email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(your_email[WHICH_EMAIL-1], your_password[WHICH_EMAIL-1])
            smtp.send_message(msg)

        print(f"✅ Email sent to: {recipient}")

    except Exception as e:
        print(f"❌ Failed to send email to: {recipient}\n   Error: {e}")





'''

import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import tkinter as tk
from tkinter import filedialog
import random
import time
import re

# Load CSV file with Company Names and Emails And resume attachment
# data = pd.read_csv("/content/email_test.csv", encoding="ISO-8859-1")
analyst_resume = "E:\\PRS-20211022T081111Z-001\\PRS\\CV32.pdf" # Path to the uploaded resume in Colab

sender_email = "1996kunaltalwar@gmail.com"
password = "lnqk bkzs fspm jtwz"
#APP PASSWORD AND MAIL FROM MAIL TO SEND


def get_email_subject(role): # Define the subject of the email
    subject = f"Application for {role} – Ashish Ahlawat" #add your name in subject
    return subject

def get_email_body(company, role, Head): # Define the body of the email
    body = f"""
Dear {Head},

I am excited to apply for the {role} position at {company}. With a strong educational background from IIT Gandhinagar and professional experience at Caratlane, Vetic, and Z-King, I bring a proven ability to transform data into actionable insights and support decision-making processes.

At Caratlane, I analyzed trends and delivered insights that informed strategic business decisions.

Proficient in SQL and Excel, I am skilled in creating dashboards and visualizations to present processed data. My strong communication skills and ability to solve unstructured problems make me a great fit for this role.

I have attached my resume for your review. Thank you for considering my application.

Best regards,
Ashish Ahlawat
Email: ashish1adb@gmail.com
Phone: +919416972728
LinkedIn: https://www.linkedin.com/in/ashish-ahlawat-196707182
    """
    return body


def send_emails(sender_email, analyst_resume, start_row, end_row, data):
    failed_rows = []
    email_regex = r"[^@]+@[^@]+\.[^@]+"

    try:
        # Setup SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)

        for index, row in data.iloc[start_row:end_row].iterrows():
            company = row['Company Name']
            recipient_email = str(row['email']).strip()
            role = row['role']
            Head = row['Head']

            # Validate email
            if not re.match(email_regex, recipient_email):
                print(f"Invalid email format: {recipient_email}")
                failed_rows.append(index)
                continue

            # Get the email body
            body = get_email_body(company, role, Head)
            subject = f"Application for {role} – Manish Ahlawat"

            # Create the email
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Attach resume
            try:
                with open(analyst_resume, "rb") as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header("Content-Disposition", f"attachment; filename={analyst_resume.split('/')[-1]}")
                    msg.attach(part)
            except FileNotFoundError:
                print(f"Analyst Resume not found: {analyst_resume}")
                failed_rows.append(index)
                continue

            # Send the email
            try:
                server.sendmail(sender_email, [recipient_email], msg.as_string())
                print(f"Email sent to {company} at {recipient_email}")

                # Random delay
                delay = random.randint(0, 5)
                print(f"Waiting {delay}s before next...")
                time.sleep(delay)

            except Exception as e:
                print(f"Failed to send email to {company} at {recipient_email}: {e}")
                failed_rows.append(index)

    except Exception as e:
        print(f"An error occurred during setup or login: {e}")

    finally:
        server.quit()
        print("Server connection closed.")
        if failed_rows:
            print(f"Emails failed for the following rows: {failed_rows}")
        else:
            print("All emails sent successfully.")

# Example usage
send_emails(sender_email, analyst_resume, 0, len(data), data)


'''