import spacy

# Load SpaCy language model
nlp = spacy.load('en_core_web_sm')

# Example long chat conversation
chat_text = """
[2023-09-26 19:05] Emma: Hey guys, are we still on for the movie night this weekend? I’m thinking of doing a little popcorn bar setup with different toppings.
[2023-09-26 19:06] Aman: Sounds cool! I’m totally in. What movie are we watching though? Please, no horror. 🥲
[2023-09-26 19:06] Sara: I thought we agreed on horror already? Come on, it’s spooky season! We could do something like The Conjuring.
[2023-09-26 19:07] Aman: I’m 100% vetoing The Conjuring. How about something lighter? Like a mystery?
[2023-09-26 19:08] Josh: How about Knives Out? It’s got that mystery element but isn’t too scary. Plus, it’s fun to figure out the clues!
[2023-09-26 19:09] Emma: Knives Out could work, yeah. I’ve been wanting to rewatch that anyway. And Josh, bring your famous brownies, please?
[2023-09-26 19:09] Josh: If I must. 🙄 But I charge in compliments.

[2023-09-26 19:10] Emma: By the way, did anyone see the email about Gravitas? They just confirmed some of the project showcases!
[2023-09-26 19:11] Sara: Oh, right! I heard they’re going to showcase UniPool and ExamCooker this year. Both are getting a lot of attention lately. 🤩
[2023-09-26 19:12] Josh: I heard CLI-RPG is also going to be up there. Pretty cool seeing all these student-led projects make it to Gravitas.
[2023-09-26 19:13] Aman: Yeah, and they’re having it at the Kamraj Auditorium this time, right? So glad we finally have a decent venue.
[2023-09-26 19:14] Sara: Oh, speaking of, does anyone know who’s hosting the main event? I didn’t catch that part.
[2023-09-26 19:14] Emma: I think they’re still deciding. Probably someone from ACM-VIT, since they’re organizing Codex Cryptum 3.0 too.

[2023-09-26 19:15] Aman: So, random question, does anyone know a good way to scrape WhatsApp chats? I’ve been looking into it for a project and I’m stuck.
[2023-09-26 19:15] Josh: Dude, why do you want to scrape WhatsApp chats? 😅
[2023-09-26 19:16] Aman: It’s for this summarizer I’m building. Trying to use Selenium for scraping, then plug the chats into a summarization model. Long story, but yeah. I just need a better way to scrape efficiently.
[2023-09-26 19:17] Emma: Ohhh, I’ve heard people use Selenium for that, but doesn’t it get blocked sometimes?
[2023-09-26 19:17] Aman: Yeah, that's my issue. It keeps failing halfway through. Plus, my Wi-Fi is trash right now so I can’t even debug properly. 😩
[2023-09-26 19:18] Sara: Ugh, I feel you on the Wi-Fi struggles. Mine’s been terrible all week. Anyway, have you tried using a different library for scraping?
[2023-09-26 19:18] Josh: Maybe look into WhatsApp’s Web API? It might be less prone to errors, especially with connection issues. Also, heard about this DialoGPT model being used with custom summarization. That could help you with the summarizing part.
[2023-09-26 19:19] Aman: Yeah, I’m already using DialoGPT + custom summarization from Huggingface, but I’ll check out the Web API. Thanks for the tip!

[2023-09-26 19:20] Emma: Ok, so while we're talking tech, can we all just acknowledge how ExamCooker has blown up? I was checking their stats and they’ve got, like, thousands of users now.
[2023-09-26 19:21] Josh: Yeah, last I heard, they had over 3,000 users after CAT1. Pretty insane growth in just a few months. What’s the secret sauce there?
[2023-09-26 19:22] Sara: I think it’s just really useful. I mean, who wouldn’t want curated notes and question papers right before exams?
[2023-09-26 19:22] Emma: And the UI is actually nice, which makes a big difference.
[2023-09-26 19:23] Josh: True. Oh, did you guys hear about the feature they’re adding where students can upload notes directly? But they won’t get published until moderators approve.
[2023-09-26 19:23] Sara: That’s a smart move. Keeps things clean and organized. I just hope they can handle the scale since it’s not officially tied to VIT.
[2023-09-26 19:24] Aman: I wonder if they’re going to integrate any AI to automate some of that moderation. Could speed things up a lot.

[2023-09-26 19:25] Emma: Ok, pivoting back to movie night – Aman, you bringing snacks or just freeloading?
[2023-09-26 19:25] Aman: 😑 I’m bringing chips! And salsa, if that counts.
[2023-09-26 19:26] Sara: Knives Out and chips? That works for me. Should we also do a mini scavenger hunt, like in the movie? 🕵️‍♀️
[2023-09-26 19:26] Emma: Haha, that could be fun! I’ll set it up if you guys are down.
[2023-09-26 19:27] Josh: Always. We could hide clues around your house, and each clue leads to a different snack. Solve the mystery, win a snack. Perfect combo.

[2023-09-26 19:30] Sara: By the way, did you guys sign up for the AI workshop this weekend? I heard it’s called ‘Mind Over Matter,’ and it’s under the CASA campaign. It’s online though.
[2023-09-26 19:30] Josh: I saw the email! It’s focusing on the role of the tech community in substance abuse awareness, right?
[2023-09-26 19:31] Emma: Yeah, I’m thinking of joining. They’re doing it on YouTube Live at 10 PM. Plus, it’s a good cause, so why not.
[2023-09-26 19:31] Aman: I’m always down to support a good cause, but 10 PM? That’s a little late.
[2023-09-26 19:32] Josh: It’s fine, it’ll probably run for just an hour. I think it’ll be an interesting discussion on how tech can actually make a difference. We could even get involved afterward.
[2023-09-26 19:33] Emma: You’re right. I’ll definitely join. It’s not often we see tech being integrated into something like this.

[2023-09-26 19:35] Sara: Speaking of workshops, isn’t Codex Cryptum 3.0 also coming up?
[2023-09-26 19:35] Josh: Yep! Pre-Gravitas event. It’s on cryptography and cybersecurity this time. Should be pretty fun.
[2023-09-26 19:36] Aman: I heard it’s beginner-friendly too, which is good because I’m definitely not a crypto expert. 😅
[2023-09-26 19:36] Sara: Same here. But I think it’s cool that they’re mixing a speaker session with hands-on activities. Makes it less intimidating.
[2023-09-26 19:37] Emma: If you guys are going, I’ll tag along. I need to brush up on my cybersecurity knowledge anyway.
[2023-09-26 19:37] Josh: Looks like we’re all in. Should be a good prep for Gravitas too. There’s a lot of cool stuff happening this year.

[2023-09-26 19:40] Sara: Ok, but let’s not forget that movie night comes first! Everyone cool with Friday?
[2023-09-26 19:40] Aman: Friday works. I’ll be there, chips and all.
[2023-09-26 19:41] Emma: Great, see you all then!
"""

# Process the conversation using SpaCy
doc = nlp(chat_text)

# Extract important sentences: based on entities or longer sentences
important_sentences = []
for sent in doc.sents:
    if len(sent.text.split()) > 5:  # Consider longer sentences for summary
        important_sentences.append(sent.text)

# Display the summary
print("Summary of Chat Conversation:")
for sentence in important_sentences:
    print(sentence)

# Optional: Extract key entities (like names, dates) to enhance the summary
#print("\nKey Entities:")
#for ent in doc.ents:
#    print(ent.text, ent.label_)
