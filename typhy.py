from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load T5 model and tokenizer
tokenizer = T5Tokenizer.from_pretrained('t5-base')
model = T5ForConditionalGeneration.from_pretrained('t5-base')

# Example chat text (can be longer)
chat_text = """
[11:39 am, 14/9/2024] +91 62320 98300: Hey everyone, are we still on for the movie night this weekend? I’m thinking of doing a little popcorn bar setup with different toppings.

[11:40 am, 14/9/2024] +91 99876 54321: Sounds cool! I’m totally in. What movie are we watching though? Please, no horror. 🥲

[11:41 am, 14/9/2024] +91 98765 43210: I thought we agreed on horror already? Come on, it’s spooky season! We could do something like The Conjuring.

[11:41 am, 14/9/2024] +91 99876 54321: I’m 100% vetoing The Conjuring. How about something lighter? Like a mystery?

[11:42 am, 14/9/2024] +91 87654 32109: How about Knives Out? It’s got that mystery element but isn’t too scary. Plus, it’s fun to figure out the clues!

[11:43 am, 14/9/2024] +91 62320 98300: Knives Out could work, yeah. I’ve been wanting to rewatch that anyway. And Josh, bring your famous brownies, please?

[11:43 am, 14/9/2024] +91 87654 32109: If I must. 🙄 But I charge in compliments.

[11:44 am, 14/9/2024] +91 62320 98300: By the way, did anyone see the email about Gravitas? They just confirmed some of the project showcases!

[11:45 am, 14/9/2024] +91 98765 43210: Oh, right! I heard they’re going to showcase UniPool and ExamCooker this year. Both are getting a lot of attention lately. 🤩

[11:45 am, 14/9/2024] +91 87654 32109: I heard CLI-RPG is also going to be up there. Pretty cool seeing all these student-led projects make it to Gravitas.

[11:46 am, 14/9/2024] +91 99876 54321: Yeah, and they’re having it at the Kamraj Auditorium this time, right? So glad we finally have a decent venue.

[11:46 am, 14/9/2024] +91 98765 43210: Oh, speaking of, does anyone know who’s hosting the main event? I didn’t catch that part.

[11:47 am, 14/9/2024] +91 62320 98300: I think they’re still deciding. Probably someone from ACM-VIT, since they’re organizing Codex Cryptum 3.0 too.

[11:48 am, 14/9/2024] +91 99876 54321: So, random question, does anyone know a good way to scrape WhatsApp chats? I’ve been looking into it for a project and I’m stuck.

[11:48 am, 14/9/2024] +91 87654 32109: Dude, why do you want to scrape WhatsApp chats? 😅

[11:49 am, 14/9/2024] +91 99876 54321: It’s for this summarizer I’m building. Trying to use Selenium for scraping, then plug the chats into a summarization model. Long story, but yeah. I just need a better way to scrape efficiently.

[11:50 am, 14/9/2024] +91 62320 98300: Ohhh, I’ve heard people use Selenium for that, but doesn’t it get blocked sometimes?

[11:50 am, 14/9/2024] +91 99876 54321: Yeah, that's my issue. It keeps failing halfway through. Plus, my Wi-Fi is trash right now so I can’t even debug properly. 😩

[11:51 am, 14/9/2024] +91 98765 43210: Ugh, I feel you on the Wi-Fi struggles. Mine’s been terrible all week. Anyway, have you tried using a different library for scraping?

[11:51 am, 14/9/2024] +91 87654 32109: Maybe look into WhatsApp’s Web API? It might be less prone to errors, especially with connection issues. Also, heard about this DialoGPT model being used with custom summarization. That could help you with the summarizing part.

[11:52 am, 14/9/2024] +91 99876 54321: Yeah, I’m already using DialoGPT + custom summarization from Huggingface, but I’ll check out the Web API. Thanks for the tip!

[11:53 am, 14/9/2024] +91 62320 98300: Ok, so while we're talking tech, can we all just acknowledge how ExamCooker has blown up? I was checking their stats and they’ve got, like, thousands of users now.

[11:54 am, 14/9/2024] +91 87654 32109: Yeah, last I heard, they had over 3,000 users after CAT1. Pretty insane growth in just a few months. What’s the secret sauce there?

[11:54 am, 14/9/2024] +91 98765 43210: I think it’s just really useful. I mean, who wouldn’t want curated notes and question papers right before exams?

[11:55 am, 14/9/2024] +91 62320 98300: And the UI is actually nice, which makes a big difference.

[11:55 am, 14/9/2024] +91 87654 32109: True. Oh, did you guys hear about the feature they’re adding where students can upload notes directly? But they won’t get published until moderators approve.

[11:56 am, 14/9/2024] +91 98765 43210: That’s a smart move. Keeps things clean and organized. I just hope they can handle the scale since it’s not officially tied to VIT.

[11:56 am, 14/9/2024] +91 99876 54321: I wonder if they’re going to integrate any AI to automate some of that moderation. Could speed things up a lot.

[11:57 am, 14/9/2024] +91 62320 98300: Ok, pivoting back to movie night – Aman, you bringing snacks or just freeloading?

[11:57 am, 14/9/2024] +91 99876 54321: 😑 I’m bringing chips! And salsa, if that counts.

[11:58 am, 14/9/2024] +91 98765 43210: Knives Out and chips? That works for me. Should we also do a mini scavenger hunt, like in the movie? 🕵️‍♀️

[11:59 am, 14/9/2024] +91 62320 98300: Haha, that could be fun! I’ll set it up if you guys are down.

[11:59 am, 14/9/2024] +91 87654 32109: Always. We could hide clues around your house, and each clue leads to a different snack. Solve the mystery, win a snack. Perfect combo.

[12:00 pm, 14/9/2024] +91 98765 43210: By the way, did you guys sign up for the AI workshop this weekend? I heard it’s called ‘Mind Over Matter,’ and it’s under the CASA campaign. It’s online though.

[12:01 pm, 14/9/2024] +91 87654 32109: I saw the email! It’s focusing on the role of the tech community in substance abuse awareness, right?

[12:01 pm, 14/9/2024] +91 62320 98300: Yeah, I’m thinking of joining. They’re doing it on YouTube Live at 10 PM. Plus, it’s a good cause, so why not.

[12:02 pm, 14/9/2024] +91 99876 54321: I’m always down to support a good cause, but 10 PM? That’s a little late.

[12:02 pm, 14/9/2024] +91 98765 43210: It’s fine, it’ll probably run for just an hour. I think it’ll be an interesting discussion on how tech can actually make a difference. We could even get involved afterward.

[12:03 pm, 14/9/2024] +91 87654 32109: Count me in! Let’s make sure to discuss our thoughts during the movie night after, too.

[12:03 pm, 14/9/2024] +91 62320 98300: Deal! It’s going to be a packed weekend!

[12:04 pm, 14/9/2024] +91 99876 54321: Perfect, looking forward to it! And don’t forget the popcorn bar!
"""

# Tokenize the input chat text
inputs = tokenizer.encode("summarize: " + chat_text, return_tensors="pt", max_length=512, truncation=True)

# Generate summary
summary_ids = model.generate(inputs, max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print("Summary:")
print(summary)
