import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

print(nltk.data.path)

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

# Example chat conversation (you can replace this with real chat data)
chat_text = """
[11:39 am, 14/9/2024] +91 62320 98300:  Trifecta showdown: Three Legends; One Legacy
 Date: 29th September 2024
 Time: 9:00am - 6:00pm
 Venue: SMV Classrooms
Join us for a showdown of the ages!
BRSI is back with a bang this graVITas'24 with Trifecta Showdown, a triple threat event that has something for everyone!x
Feel that itch that only a good game of strategy and brains can scratch?
Join us for Battleship, with a life-size twist to keep the competition fresh and unexpected!
Craving a traditional game of Family Feud(ing) with your friends; loaded with all your fan favourites from S-Tier Fandoms.
An exhilarating heist for the ages, perhaps? Stealing the long-lost treasure; claimed waste by Davy Jones?
We have a little bit of something for a little bit of everyone, so ma…
[11:39 am, 14/9/2024] +91 62320 98300:   Alchemix: Design Your Fix
 September 27th & 28th | 9 AM - 5 PM
 Venue: Homi Baba Gallery, SJT
Join us at graVITas, the renowned technology fest hosted by VIT Vellore, for an exclusive event – Alchemix by BRSI, a 2-day computational drug design hackathon! Whether you're a seasoned pro or a complete beginner, you'll dive into the future of medicine, learning to design drugs using cutting-edge bioinformatics and machine learning tools.
 What’s in store?"
Comprehensive workshops & expert guest lectures
Learn the science behind drug design and how to use cutting-edge tools
Wrap up with a thrilling Global Health Forum, where finalists tackle real-world health policy challenges
Be a part of graVITas 2024 and shape the future of h…
[12:31 pm, 14/9/2024] +91 76768 00794:  The Bioinformatics Blueprint :  Navigating Your Career Journey
 Date: 14/09/2024
 Time: 6.00PM - 7.00PM
 Platform: Google Meet
 Link: https://meet.google.com/tgt-pvgz-tni
 Join us for an exclusive webinar!
Are you ready to dive into the world of bioinformatics?
Explore how to kick-start and shape a rewarding career in this fast-evolving field with Ashish Kumar Choudhary, an experienced Bioinformatics Scientist at Strand Life Sciences, with over 4 years of expertise in computational genomics and NGS data analysis.
Don't miss this opportunity to gain valuable insights from someone who's been at the forefront of bioinformatics innovation. Discover the key skills and tools needed to excel in the field and learn how you can build a successful c…
[1:15 pm, 14/9/2024] +91 836 899 4540:  https://tinyurl.com/Survey-PublicSpeaking
[7:03 pm, 14/9/2024] +91 85040 05876:   Auction to Action:
Embark on an exciting competition that challenges your creativity, strategy, and negotiation skills across three action-packed rounds!
 In Round 1, participate in a high-stakes auction where you’ll bid on critical resources to kick-start your project.
 Round 2 adds the element of surprise with a thrilling mystery box auction, testing your adaptability and quick thinking.
 The final round is all about negotiation and trading, where teams will develop innovative solutions.
 Date: 20th September
 Time: 10 AM
 Full day OD will be given
Don’t miss your chance to take part in this unique experience!
Register here: https://gravitas.vit.ac.in/events/17f37986-aab4-46c3-9010-7625556a69a8
Follow us for more …
[10:10 pm, 14/9/2024] +91 7439 613 826:  https://forms.gle/qLhEwRiKBJHBBBSo7
[10:10 pm, 14/9/2024] +91 7439 613 826:  Please  fill up this form. I is a part of our research.
[2:18 pm, 15/9/2024] +91 98660 71109:   Attention All Tech Enthusiasts!
Get ready for Electrolympics , an electrifying competition brought to you by IEEE SPS at Gravitas '24!
 Are you a wizard of circuits and soldering iron? Prove your skills in this round-based competition focused on basic electronics.  Whether you're a beginner or a pro, this event is for YOU!
 Register Now & Show Off Your Circuit Mastery!
 https://gravitas.vit.ac.in/events/81a32598-d98c-47e2-a8d4-4aa9bd36ed60
 Prizes Await the Champs! Don’t miss out on the electrifying experience!
[4:01 pm, 15/9/2024] +91 97945 76602:  https://forms.gle/4rHCf4nwqLw76s3C8
[4:02 pm, 15/9/2024] +91 97945 76602:  guys please fill this
[4:24 pm, 15/9/2024] +91 62320 98300:  Trifecta showdown: Three Legends; One Legacy
 Date: 29th September 2024
 Time: 9:00am - 6:00pm
 Venue: SMV Classrooms
Join us for a showdown of the ages!
BRSI is back with a bang this graVITas'24 with Trifecta Showdown, a triple threat event that has something for everyone!
Feel that itch that only a good game of strategy and brains can scratch?
Join us for Battleship, with a life-size twist to keep the competition fresh and unexpected!
Craving a traditional game of Family Feud(ing) with your friends; loaded with all your fan favourites from S-Tier Fandoms.
An exhilarating heist for the ages, perhaps? Stealing the long-lost treasure; claimed waste by Davy Jones?
We have a little bit of something for a little bit of everyone, so ma…
[4:24 pm, 15/9/2024] +91 62320 98300:   Alchemix: Design Your Fix
 September 27th & 28th | 9 AM - 5 PM
 Venue: Homi Baba Gallery, SJT
Join us at graVITas, the renowned technology fest hosted by VIT Vellore, for an exclusive event – Alchemix by BRSI, a 2-day computational drug design hackathon! Whether you're a seasoned pro or a complete beginner, you'll dive into the future of medicine, learning to design drugs using cutting-edge bioinformatics and machine learning tools.
 What’s in store?"
Comprehensive workshops & expert guest lectures
Learn the science behind drug design and how to use cutting-edge tools
Wrap up with a thrilling Global Health Forum, where finalists tackle real-world health policy challenges
Be a part of graVITas 2024 and shape the future of h…
No timestamp No message text
[10:11 pm, 15/9/2024] +91 79911 57896:  https://forms.gle/WmBLEctbMeJyPbiu9
Please fill this quick survey
[1:41 pm, 16/9/2024] +91 62320 98300:  Trifecta showdown: Three Legends; One Legacy
 Date: 29th September 2024
 Time: 9:00am - 6:00pm
 Venue: SMV Classrooms
Join us for a showdown of the ages!
BRSI is back with a bang this graVITas'24 with Trifecta Showdown, a triple threat event that has something for everyone!
Feel that itch that only a good game of strategy and brains can scratch?
Join us for Battleship, with a life-size twist to keep the competition fresh and unexpected!
Craving a traditional game of Family Feud(ing) with your friends; loaded with all your fan favourites from S-Tier Fandoms.
An exhilarating heist for the ages, perhaps? Stealing the long-lost treasure; claimed waste by Davy Jones?
We have a little bit of something for a little bit of everyone, so ma…
[1:41 pm, 16/9/2024] +91 62320 98300:   Alchemix: Design Your Fix
 September 27th & 28th | 9 AM - 5 PM
 Venue: Homi Baba Gallery, SJT
Join us at graVITas, the renowned technology fest hosted by VIT Vellore, for an exclusive event – Alchemix by BRSI, a 2-day computational drug design hackathon! Whether you're a seasoned pro or a complete beginner, you'll dive into the future of medicine, learning to design drugs using cutting-edge bioinformatics and machine learning tools.
 What’s in store?"
Comprehensive workshops & expert guest lectures
Learn the science behind drug design and how to use cutting-edge tools
Wrap up with a thrilling Global Health Forum, where finalists tackle real-world health policy challenges
Be a part of graVITas 2024 and shape the future of h…
[2:52 pm, 16/9/2024] +91 85059 72727:   Get Ready for AeroStrike M1!
                                                                                                                                                                  

Unleash your creativity and skills in an exciting two-day journey into the world of aircraft design! Whether you're an aspiring aerospace engineer or just curious about aviation, AeroStrike M1 has something for YOU!!
 Event Date: 27th & 28th September 2024
 Special feature : Participate in the Best Landing challenge and stand a chance to win prizes
 Why Attend?
 Guest Lecture: Learn from a Boeing engineer and VIT Albatross alumnus as they guide you through the world of aircra…
[2:53 pm, 16/9/2024] +91 91037 42242:   Get Ready for AeroStrike M1!
                                                                                                                                                                  

Unleash your creativity and skills in an exciting two-day journey into the world of aircraft design! Whether you're an aspiring aerospace engineer or just curious about aviation, AeroStrike M1 has something for YOU!!
 Event Date: 27th & 28th September 2024
 Special feature : Participate in the Best Landing challenge and stand a chance to win prizes
 Why Attend?
 Guest Lecture: Learn from a Boeing engineer and VIT Albatross alumnus as they guide you through the world of aircra…
[6:12 pm, 16/9/2024] +91 95489 34341:   Get Ready for AeroStrike M1!
                                                                                                                                                                  

Unleash your creativity and skills in an exciting two-day journey into the world of aircraft design! Whether you're an aspiring aerospace engineer or just curious about aviation, AeroStrike M1 has something for YOU!!
 Event Date: 27th & 28th September 2024
 Special feature : Participate in the Best Landing challenge and stand a chance to win prizes
 Why Attend?
 Guest Lecture: Learn from a Boeing engineer and VIT Albatross alumnus as they guide you through the world of aircra…
[6:23 pm, 16/9/2024] +91 60062 99469:   CODE TO SURVIVE! Where every secret is deadly… 
Mozilla Firefox Club presents to you , the ultimate challenge—are you ready to outsmart, outlast, and outrun? Step into the role of a detective racing against time to catch a criminal. A gripping fusion of escape room puzzles, murder mystery intrigue, and high-stakes strategy awaits you.
Three intense rounds, countless challenges, and only the sharpest teams will make it out.

Team Size: 3-5 members
Seats are filling fast.Follow this link and register now.
http://surl.li/xzlzyp
Think you've got what it takes to crack the case? Then let the games begin!
[7:20 pm, 16/9/2024] +91 91066 89527:   TechWars - Conquer the Universe
 Mozilla Firefox Club presents an electrifying adventure at graVITas’24!
Unleash your inner strategist as you outwit your opponents, claim territories, and emerge as the ultimate champions!
Join us for an unforgettable experience filled with excitement, competition, and fun.  Be part of this cosmic challenge and show the universe who’s the boss!     
 Team Size: 2 to 4
 Why should you join?
 Exciting Prize Pool - Win rewards for your stellar performance!
 Explore the VIT Campus - Discover all the hidden gems while having fun!
 Network with Like-Minded Peers - Meet other tech enthusiasts and build lasting connections!
 Engaging Challenges - Test your skills and outsmart your opponents!
 Register Now!
https://surl.li/isnhtl
See you there!
MFC-VIT
[9:19 pm, 16/9/2024] +91 836 899 4540:  I would request everyone to fill in this short survey form  whenever you’re free, thanks.
[9:20 pm, 16/9/2024] +91 836 899 4540:  https://tinyurl.com/Survey-PublicSpeaking
[9:25 pm, 16/9/2024] +91 83004 76056:  https://docs.google.com/forms/d/e/1FAIpQLSd2F8Xnw7NQRjgIc2c_ZOENi7XSfKEG4sDdepc47Jzs9Klarg/viewform?usp=sf_link
Please answer this form so that It will be useful for my technical Report Writing
[1:57 pm, 17/9/2024] +91 63875 14459:  https://docs.google.com/forms/d/e/1FAIpQLSeOrIwOmWSq1HicMxmHZWar-wLbwqw4_hI17JMKC3RXzYCGYA/viewform?usp=sf_link
[1:57 pm, 17/9/2024] +91 63875 14459:  Please fill out this form for technical report writing
[2:10 pm, 17/9/2024] +91 62320 98300:  Trifecta showdown: Three Legends; One Legacy
 Date: 29th September 2024
 Time: 9:00am - 6:00pm
 Venue: SMV Classrooms
Join us for a showdown of the ages!
BRSI is back with a bang this graVITas'24 with Trifecta Showdown, a triple threat event that has something for everyone!
Feel that itch that only a good game of strategy and brains can scratch?
Join us for Battleship, with a life-size twist to keep the competition fresh and unexpected!
Craving a traditional game of Family Feud(ing) with your friends; loaded with all your fan favourites from S-Tier Fandoms.
An exhilarating heist for the ages, perhaps? Stealing the long-lost treasure; claimed waste by Davy Jones?
We have a little bit of something for a little bit of everyone, so ma…
[2:15 pm, 17/9/2024] +91 62320 98300:   Alchemix: Design Your Fix
 September 27th & 28th | 9 AM - 5 PM
 Venue: Homi Baba Gallery, SJT
Join us at graVITas, the renowned technology fest hosted by VIT Vellore, for an exclusive event – Alchemix by BRSI, a 2-day computational drug design hackathon! Whether you're a seasoned pro or a complete beginner, you'll dive into the future of medicine, learning to design drugs using cutting-edge bioinformatics and machine learning tools.
 What’s in store?"
Comprehensive workshops & expert guest lectures
Learn the science behind drug design and how to use cutting-edge tools
Wrap up with a thrilling Global Health Forum, where finalists tackle real-world health policy challenges
Be a part of graVITas 2024 and shape the future of h…
[2:41 pm, 17/9/2024] +91 816 869 6925:  https://docs.google.com/forms/d/e/1FAIpQLSfBsXRqjUqoR-as1DRxhwDfGcq5PZOICoaNfNfSPQ8_-vsOJw/viewform?usp=sf_link
Please fill out this form. It is a part of our English project.
It will not take more than 2 minutes.
[3:22 pm, 17/9/2024] +91 63819 81284:   Exciting news alert!!
AIGENda registrations, which reached capacity in just 4 hours, have now increased the seats just for you!
Register NOW for just ₹50 because you don't want to miss out twice.
Seats are filling up fast!!
Register with this link before its too late:
https://gravitas.vit.ac.in/events/f82a3e68-65b9-4498-ad3c-91ea0f3e6277
[5:37 pm, 17/9/2024] +91 99875 93366:  https://forms.gle/eAfVurmXbcuWs1gC6
Dear participants,
This questionnaire aims to analyse gambling patterns amongst youth. we hope to gauge the physical and emotional impacts on the individual.
All your responses to this survey will be kept confidential. Your cooperation in this matter is solicitated and will be highly appreciated.
[5:50 pm, 17/9/2024] +91 877 886 1684:  Trifecta showdown: Three Legends; One Legacy
 Date: 29th September 2024
 Time: 9:00am - 6:00pm
 Venue: SMV Classrooms
Join us for a showdown of the ages!
BRSI is back with a bang this graVITas'24 with Trifecta Showdown, a triple threat event that has something for everyone!
Feel that itch that only a good game of strategy and brains can scratch?
Join us for Battleship, with a life-size twist to keep the competition fresh and unexpected!
Craving a traditional game of Family Feud(ing) with your friends; loaded with all your fan favourites from S-Tier Fandoms.
An exhilarating heist for the ages, perhaps? Stealing the long-lost treasure; claimed waste by Davy Jones?
We have a little bit of something for a little bit of everyone, so ma…
[9:12 pm, 17/9/2024] +91 73026 08625:  I lost half part of my laptop's charger infront of the library at the collection point  It also has a red mark. (HP BRAND).Contact me on: 7983333283
[10:02 pm, 17/9/2024] +91 93263 98561:  Anyone interested to form a team for event "Hackovation"?
[10:38 pm, 17/9/2024] +91 89252 48118:  https://forms.gle/QnVWSxtUytWmz7pZ6
[10:39 pm, 17/9/2024] +91 89252 48118:  Could you please take a moment to complete this form? I’d really appreciate it. Thanks so much!
[11:56 pm, 17/9/2024] Aishwarya CSE Core:  https://docs.google.com/forms/d/e/1FAIpQLScvTsPW3t5H1xNHQu1ofxxIOkUa4XCpp7LCGbRFOUIL7xIm0A/viewform?usp=sf_link        
This is for our English report. Pls take a few minutes to fill it.
[12:16 pm, 18/9/2024] +91 91503 06736:  Does anyone have Kalyanaraman sir's phone number ?
[4:33 pm, 18/9/2024] +91 84383 50259:  The wait is finally over!
Robowars 2024 is here!
https://www.instagram.com/reel/DADiXJrPFGm/?igsh=bHgwZXNqdTBmOWoy
Join us as incredible creations clash in battles of strategy, speed, and pure power!
From agile fighters  to heavy-hitting giants, every robot showcases human ingenuity and engineering genius.
Don’t miss out on this epic showdown!
[5:35 pm, 18/9/2024] +91 877 886 1684:  Trifecta showdown: Three Legends; One Legacy
 Date: 29th September 2024
 Time: 9:00am - 6:00pm
 Venue: SMV Classrooms
Join us for a showdown of the ages!
BRSI is back with a bang this graVITas'24 with Trifecta Showdown, a triple threat event that has something for everyone!
Feel that itch that only a good game of strategy and brains can scratch?
Join us for Battleship, with a life-size twist to keep the competition fresh and unexpected!
Craving a traditional game of Family Feud(ing) with your friends; loaded with all your fan favourites from S-Tier Fandoms.
An exhilarating heist for the ages, perhaps? Stealing the long-lost treasure; claimed waste by Davy Jones?
We have a little bit of something for a little bit of everyone, so ma…
[7:07 pm, 18/9/2024] +91 85040 05876:   STARTUP STREET 9.0 IS HERE!
Ready to turn your startup dreams into reality? Startup Street 9.0 is where innovators and future founders come together to create and compete.
No coding required – just bring your boldest ideas!
Why join?
 Launch your startup journey
 Network with venture capitalists
 Compete for funding and prizes
 Pitch your startup ideas to Shark Tank funded entrepreneurs
Register now and kickstart your venture.
 Register here:
https://gravitas.vit.ac.in/events/531497e2-55c9-4323-9736-f274c55d090c
 Follow us for updates: https://www.instagram.com/csed.vit?igsh=MWtjaGhneGRyd2o5NA==
[9:12 pm, 18/9/2024] +91 83004 76056:  https://docs.google.com/forms/d/e/1FAIpQLSd2F8Xnw7NQRjgIc2c_ZOENi7XSfKEG4sDdepc47Jzs9Klarg/viewform?usp=sf_link
Please answer this form so that It will be useful for my technical Report Writing
[10:53 pm, 18/9/2024] +91 733 763 5656:  https://forms.gle/3XygeS5vKbwQGiRu7
pls fill out this form
[7:42 am, 19/9/2024] +91 96264 32075:   Dream Team 6.0 is here!
Are you ready to Dream Big, Bid Bigger?
Get your squad of 5 together and gear up for the ultimate IPL auction experience!  Build your dream cricket team by bidding for top players – from power-hitting batsmen to game-changing bowlers, including international stars!  The stakes are high, and the rewards? Even higher!
 Dates: 21st & 22nd September
 Venue: CS Hall
 Exciting prizes await the team with the best squad!
Register now: https://gravitas.vit.ac.in/events/18010858-d11d-4e3c-97d6-b1510e3229dc
 Follow us for updates: https://www.instagram.com/dreammerchantsvit?igsh=MTBydGFoM3g4Z2VjZA==
Don’t miss out! It's time to make your bid and create your Dream Team!
Registrations now open!!
[8:15 am, 19/9/2024] +91 89584 08553:  Titan Clash: The Kaiju Code Wars
“Defend, Code, Conquer: Become the Ultimate Kaiju Slayer!”
Get ready for an electrifying showdown! IE(I) proudly presents Titan Clash: The Kaiju Code Wars, a premium graVITas event where coding meets colossal monsters. Test your coding skills with your team for the 3 extensive rounds and defend the city against monstrous Kaiju.  Bid for the Codes and save the city with your own preferred language!!
 Team size:3-5 members

 September 29, 2024
Don't miss out – Limited spots available!
Register now: [https://gravitas.vit.ac.in/events/e3edb524-4555-47b6-84da-595517720edc]
Cheers,
IE(I)-VIT
[10:57 am, 19/9/2024] +91 98660 71109:   *BioSculpt: Where Biology Meets Electronics! *                                                                           

                                                                                                                                                                  
                 The IEEE SPS is excited to bring you BioSculpt, a thrilling event as part of Gravitas '24!
 What’s in store?                                                                                                                                             Speaker Session: Hear from industry experts about the latest advancements in Biomedical Electronics!
 Hands-on Workshop: Dive into the world of electronics in biom…
[5:26 pm, 19/9/2024] +91 90792 34586:  https://forms.gle/vm4uf5a2B3j8rWhi8
Please fill out this form and share it with your friends as well.
No timestamp No message text
[10:06 am, 20/9/2024] +91 62014 00754:  https://docs.google.com/forms/d/e/1FAIpQLSfGtYDr2XqnqUl-th_LgX4GXK8tD3-nYzwrv5nWqE41AaZWTQ/viewform?usp=sf_link
Please fill out this form and share with your friends
Your small contribution will help me a lot
[12:31 pm, 20/9/2024] +91 91760 97620:  https://docs.google.com/forms/d/e/1FAIpQLSfmOc6kem0Gip9YI6cHMn3Giv1zsLQtQG_Tw0Ev3KnorfUmfg/viewform?usp=sf_link
[12:31 pm, 20/9/2024] +91 91760 97620:  can everyone fill this form this is for  technical report writing
[1:35 pm, 20/9/2024] +91 733 849 7601:  https://docs.google.com/forms/d/e/1FAIpQLScmun7WdfnSej2ygZ5D6_NFKwYYIsvBfHcqgAZaCzGBgI1XWg/viewform?usp=sf_link
[1:37 pm, 20/9/2024] +91 733 849 7601:  Can everyone please fill this form
It is for my English project
[2:56 pm, 20/9/2024] +91 80111 89252:  Anyone knows the exact venue of this?
[5:56 pm, 20/9/2024] +91 93416 52249:  Hey has anyone seen these earbuds in sjt labs or in prp? If u have, kindly dm me
[6:11 pm, 20/9/2024] Yash CSE Core:  Has anyone seen these earbuds in SJT G19 today? If yes, kindly DM me
[10:19 am, 21/9/2024] +91 62320 98300:  Trifecta showdown: Three Legends; One Legacy
 Date: 29th September 2024
 Time: 9:00am - 6:00pm
 Venue: SMV Classrooms
Join us for a showdown of the ages!
BRSI is back with a bang this graVITas'24 with Trifecta Showdown, a triple threat event that has something for everyone!
Feel that itch that only a good game of strategy and brains can scratch?
Join us for Battleship, with a life-size twist to keep the competition fresh and unexpected!
Craving a traditional game of Family Feud(ing) with your friends; loaded with all your fan favourites from S-Tier Fandoms.
An exhilarating heist for the ages, perhaps? Stealing the long-lost treasure; claimed waste by Davy Jones?
We have a little bit of something for a little bit of everyone, so ma…
[4:41 pm, 22/9/2024] +91 7520 833 300:  "https://docs.google.com/forms/d/e/1FAIpQLScpQfG1TA88Wz2D1g_iA91htKwfJzoYE3n-oCENfuy0wcPhEw/viewform?embedded=true"       
[9:31 pm, 22/9/2024] +91 7520 833 300:  https://docs.google.com/forms/d/e/1FAIpQLScN1XHm3NqI9xb2f6AtQYKdNSI8HIqYLzI71xKXFO6QxojFqw/viewform?usp=sf_link
[11:44 pm, 22/9/2024] +91 63804 95918:  Hello, can you help me by filling up a survey for my English project? It'd just take a few minutes!
https://docs.google.com/forms/d/e/1FAIpQLSdIOGQccQsh_M5sCXuJudQh_HNaBXolLbyTwOxRjj1WTVym5Q/viewform?usp=sharing
Thanks!
[12:19 am, 23/9/2024] +91 63868 38272:  https://forms.gle/jNuJMvGwbhmPYuTB6
Please fill this form, it'd be very helpful for my trw
[9:18 am, 23/9/2024] +91 63868 38272:  https://forms.gle/1Jbq1c6UximsciNZ8
Could you please fill this again, your previous responses are saved just fill the newer fields. It'd be very helpful of you
[11:13 am, 23/9/2024] +91 85977 45534:  https://forms.gle/pG2Dazq2v6vG9Q7h9
Please fill out this form..it would just take 5-7 mins of your time..
[4:58 pm, 24/9/2024] +91 84383 50259:  Robowars is here, get ready for the thrill and intrigue. Three days full of adrenaline. Time to watch combat robots clash in an arena of sparks and chaos Robowars is the ultimate battle for robotic supremacy! 
The graVITas flagship event of VIT, with the biggest arena in the South India! Don't miss out the combat robotic competition!
   28-29 September
  9am - 9pm
  SJT Ground
 Register now to witness the epic Robowars live!
https://gravitas.vit.ac.in/events/c87e7f52-b3f5-43d8-846d-a29b60a2f6eb
[10:51 pm, 24/9/2024] +91 60062 99469:  https://docs.google.com/forms/d/e/1FAIpQLScjY8swK9vyo2opv5w5AYQ0E5UzkVNg2fjoew8DqPi8sVLJjA/viewform?usp=sf_link
Please fill it out for a project. Won't take more than 2mins. Thank you!!
[11:10 pm, 24/9/2024] +91 80921 54081:   Ignite Your Career at Softwave Solutions!
Are you ready to revolutionize the world of MSMEs? Softwave Solutions is on a mission to transform how Micro, Small, and Medium Enterprises operate, and we need YOUR creative genius to make it happen! If you're passionate about technology and creativity, we want you on our team!
 We're Scouting for Superstars!
 Social Media Manager
 Can handle different social media handles regularly and post regular given content
 Turn likes into leads with data-driven strategies
 Keep our feeds lit with trending topics and viral challenges
 Be the voice of our brand in social media
 Designer
 Craft eye-popping posters that demand double-takes
 Turn bland ideas into visual masterpieces
 Ride the wa…
[1:43 pm, 25/9/2024] +91 8074 384 335:  Ladies, please fill this google form,genuinely.we are doing a research paper.
       It will be used for analysis, it just takes 5 to 10 minutes to fill it.
https://forms.gle/xyQQV1jY2dyjzbDB6
"""

# Create a parser for the chat text
parser = PlaintextParser.from_string(chat_text, Tokenizer("english"))

# Initialize the LexRank summarizer
summarizer = LexRankSummarizer()

# Summarize the chat conversation to the top 3 sentences
summary = summarizer(parser.document, 3)  # Adjust the number to control summary length

# Print the summarized output
print("Summary of Chat Conversation:")
for sentence in summary:
    print(sentence)
