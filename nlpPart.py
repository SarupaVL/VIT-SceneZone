import re
from collections import Counter
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from transformers import pipeline

# Example chat data (Replace this with actual data input from WhatsApp extraction)
chat_data = """
[4:27 pm, 24/9/2024] Josithaa:  IM PRETTY SURE IT WAS VERY VERY VERY DIFFERENT WHEN WE WERE KIDS
[4:27 pm, 24/9/2024] Josithaa:  not kids lets say some years back
[4:27 pm, 24/9/2024] Josithaa:  okie guys thookam is coming, i go eep
[4:27 pm, 24/9/2024] Josithaa:  byebyee
[4:28 pm, 24/9/2024] Sachin:  Eep
[4:28 pm, 24/9/2024] Josithaa:  eep bakcwards
[4:28 pm, 24/9/2024] Josithaa:  pee
[4:28 pm, 24/9/2024] Josithaa:  sorry bye.
[4:28 pm, 24/9/2024] Sachin:  I just did that
[4:28 pm, 24/9/2024] Sachin:  Bye
[4:28 pm, 24/9/2024] Josithaa:  TMI
[4:28 pm, 24/9/2024] Sachin:  No message text
[5:58 pm, 24/9/2024] Sarupa:  Bloop
[5:58 pm, 24/9/2024] Sarupa:  What's tmi
[5:58 pm, 24/9/2024] Rithul Sandeep:  Teri meri izzat
[5:59 pm, 24/9/2024] Sarupa:  Oh
[5:59 pm, 24/9/2024] Sachin:  Too much information
[6:00 pm, 24/9/2024] Sarupa:  Oh
[6:00 pm, 24/9/2024] Prince:  Tu mera ishq
[6:00 pm, 24/9/2024] Prince:  Howzzat
[6:00 pm, 24/9/2024] Sarupa:  Wow
[6:00 pm, 24/9/2024] Rithul Sandeep:  Best TMI
[6:00 pm, 24/9/2024] Kevin:  Nicee
[6:01 pm, 24/9/2024] Sarupa:  Doesn't keerthika p take phones away @Kevin
[6:01 pm, 24/9/2024] Kevin:  Nope
[6:01 pm, 24/9/2024] Prince:  Wtf
[6:02 pm, 24/9/2024] Prince:  Bap
[6:02 pm, 24/9/2024] Prince:  Gap
[6:02 pm, 24/9/2024] Kevin:  I am excluded from that rule
[6:02 pm, 24/9/2024] Prince:  Nab
[6:02 pm, 24/9/2024] Prince:  Gab fab
[6:02 pm, 24/9/2024] Sarupa:  Why
[6:02 pm, 24/9/2024] Sarupa:  What did you do
[6:02 pm, 24/9/2024] Kevin:  Same reason I said in morning
[6:03 pm, 24/9/2024] Sarupa:  I don't remember
[6:03 pm, 24/9/2024] Sachin:  Bro cooked
[6:03 pm, 24/9/2024] Kevin:  I am _____
[6:03 pm, 24/9/2024] Kevin:  Discrete class
[6:03 pm, 24/9/2024] Sarupa:  Huh
[6:03 pm, 24/9/2024] Sachin:  Ironman
[6:04 pm, 24/9/2024] Sachin:  Isthriwaala
[6:04 pm, 24/9/2024] Kevin:  Adorable
[6:05 pm, 24/9/2024] Sachin:  Chi thu
[6:05 pm, 24/9/2024] Kevin:  Truth is sometimes bitter
[6:05 pm, 24/9/2024] Sachin:  Chi chi thu thu
[6:06 pm, 24/9/2024] Sarupa:  Who me?
Ik that already
[6:06 pm, 24/9/2024] Sachin:  Chi chi chi thu thu thu
[6:06 pm, 24/9/2024] Sarupa:  No message text
[6:07 pm, 24/9/2024] Sarupa:  I want ice lolly
[6:07 pm, 24/9/2024] Kevin:  Delulu/cope/hope
[6:08 pm, 24/9/2024] Sachin:  Rope
[6:08 pm, 24/9/2024] Kevin:  Hang
No timestamp No message text
No timestamp No message text
No timestamp No message text
[6:43 pm, 24/9/2024] Rithul Sandeep:  You guys when I say English or Spanish
[6:43 pm, 24/9/2024] Rithul Sandeep:  .
[6:43 pm, 24/9/2024] Rithul Sandeep:  .
[6:43 pm, 24/9/2024] Rithul Sandeep:  .
[6:43 pm, 24/9/2024] Sachin:  What
[6:43 pm, 24/9/2024] Kevin:  We move
[6:43 pm, 24/9/2024] Sachin:  Ohhh
[6:44 pm, 24/9/2024] Kevin:  UK the joke da
[6:44 pm, 24/9/2024] Sachin:  Right
[6:44 pm, 24/9/2024] Prince:  Fuck y’all
[6:44 pm, 24/9/2024] Kevin:  Why da
[6:44 pm, 24/9/2024] Sachin:  Lmk the time and place
[6:45 pm, 24/9/2024] Prince:  Wtff
[6:45 pm, 24/9/2024] Prince:  Rithull
[6:45 pm, 24/9/2024] Kevin:
[6:45 pm, 24/9/2024] Prince:  Guys he had my phone
[6:45 pm, 24/9/2024] Prince:  Wth
[6:45 pm, 24/9/2024] Sachin:  Nice
[6:45 pm, 24/9/2024] Kevin:  Just the phone
[6:45 pm, 24/9/2024] Prince:  Sus
[6:46 pm, 24/9/2024] Sachin:  No message text
[6:46 pm, 24/9/2024] Parvathy:  Y'all r gay man
[6:46 pm, 24/9/2024] Prince:  We know that
[6:47 pm, 24/9/2024] Prince:  Anything new pls
No timestamp No message text
[6:47 pm, 24/9/2024] Kevin:  Great discover,
[6:48 pm, 24/9/2024] Parvathy:  New?
[7:06 pm, 24/9/2024] Prince:  Tell us anything that wdk
[7:07 pm, 24/9/2024] Parvathy:  Right
No timestamp No message text
[7:29 pm, 24/9/2024] Josithaa:  No message text
[7:30 pm, 24/9/2024] Josithaa:  what is this da
[7:34 pm, 24/9/2024] Kevin:  Java
[7:36 pm, 24/9/2024] Josithaa:  damn bro
[7:36 pm, 24/9/2024] Josithaa:  crazybrocrazy
[7:39 pm, 24/9/2024] Prince:  Word palindrome
[7:50 pm, 24/9/2024] Josithaa:  HAHXHHSHSHAJA YEAS YES
[7:50 pm, 24/9/2024] Josithaa:  peas peas
[7:50 pm, 24/9/2024] Josithaa:  bro
[7:50 pm, 24/9/2024] Josithaa:  did you know
[7:50 pm, 24/9/2024] Josithaa:  any word
[7:50 pm, 24/9/2024] Josithaa:  if you repeat it twice
[7:50 pm, 24/9/2024] Josithaa:  it becomes a word palindrome
[7:50 pm, 24/9/2024] Josithaa:
[8:07 pm, 24/9/2024] Sachin:  Hmm hmm
[9:01 pm, 24/9/2024] Josithaa:  YES YES
[9:07 pm, 24/9/2024] Sachin:  Ok ok
[1:21 am, 25/9/2024] Josithaa:  hahah
[1:21 am, 25/9/2024] Rithul Sandeep:  Hey
[1:21 am, 25/9/2024] Rithul Sandeep:  Go sleep
[1:21 am, 25/9/2024] Josithaa:  OH 121
[1:21 am, 25/9/2024] Josithaa:  11²
[1:21 am, 25/9/2024] Rithul Sandeep:  You're not allowed to be awake this late
[1:21 am, 25/9/2024] Josithaa:  No message text
[1:21 am, 25/9/2024] Rithul Sandeep:  Palindrome
[1:21 am, 25/9/2024] Josithaa:  wyd bros
[1:21 am, 25/9/2024] Josithaa:  yess
[1:21 am, 25/9/2024] Josithaa:  SARUPA HELLO
[1:22 am, 25/9/2024] Josithaa:  MY POOKIE
[1:22 am, 25/9/2024] Rithul Sandeep:  Cooking chapati
[1:22 am, 25/9/2024] Sarupa:  Why are y'all awake
[1:22 am, 25/9/2024] Sarupa:  Hello there
[1:22 am, 25/9/2024] Josithaa:  nightslip bro :(
[1:22 am, 25/9/2024] Sarupa:  My cookieeeeee
[1:22 am, 25/9/2024] Sarupa:  Snacking
No timestamp No message text
[1:22 am, 25/9/2024] Josithaa:  ooh damn
[1:22 am, 25/9/2024] Rithul Sandeep:  That's our ceiling
[1:22 am, 25/9/2024] Josithaa:  WOAH
[1:22 am, 25/9/2024] Josithaa:  I ALSO WANT
[1:23 am, 25/9/2024] Rithul Sandeep:  No message text
[1:23 am, 25/9/2024] Sarupa:  Wtf how
Show me
[1:23 am, 25/9/2024] Rithul Sandeep:  K go to settings
[1:23 am, 25/9/2024] Rithul Sandeep:  There's an option for background
[1:23 am, 25/9/2024] Josithaa:  GIMME FOR ONE DAY BRO
[1:23 am, 25/9/2024] Rithul Sandeep:  Change to aurora Borealis
[1:23 am, 25/9/2024] Rithul Sandeep:  And then customize colour
[1:23 am, 25/9/2024] Sarupa:  No message text
[1:23 am, 25/9/2024] Sarupa:  So cool
Swimming pool
[1:23 am, 25/9/2024] Sarupa:  Huh
[1:23 am, 25/9/2024] Josithaa:  I WANT ALSO BRO
[1:24 am, 25/9/2024] Josithaa:  WHOS IS IT
[1:24 am, 25/9/2024] Rithul Sandeep:  Hitesh's
[1:24 am, 25/9/2024] Rithul Sandeep:  Our roommate
[1:24 am, 25/9/2024] Rithul Sandeep:  I think Prince and Hitesh bought it last sem
[1:24 am, 25/9/2024] Josithaa:  oh :(
[1:24 am, 25/9/2024] Josithaa:  then its both of theirs no
[1:24 am, 25/9/2024] Rithul Sandeep:  Yesh
"""

# Function to split chat messages into structured format
def parse_chat(chat_data):
    messages = []
    lines = chat_data.splitlines()
    
    for line in lines:
        match = re.match(r'\[(.*?)\] (.*?): (.*)', line)
        if match:
            timestamp, sender, message = match.groups()
            messages.append({"timestamp": timestamp, "sender": sender, "message": message})
    return messages

# Function to identify questions, URLs, and announcements
def identify_key_events(messages):
    questions = []
    urls = []
    announcements = []
    
    for msg in messages:
        if '?' in msg['message']:
            questions.append(msg)
        if 'http' in msg['message']:
            urls.append(msg)
        if "announce" in msg['message'].lower() or "important" in msg['message'].lower():
            announcements.append(msg)
    
    return questions, urls, announcements

# Function to summarize chat data using LSA
def summarize_chat(messages, num_sentences=3):
    chat_text = " ".join([msg['message'] for msg in messages])
    
    if len(chat_text) > 50:
        parser = PlaintextParser.from_string(chat_text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, num_sentences)
        return " ".join([str(sentence) for sentence in summary])
    else:
        return "Not enough text to summarize."

# Main function to process chat and summarize key points
def process_chat_summary(chat_data):
    messages = parse_chat(chat_data)
    questions, urls, announcements = identify_key_events(messages)
    
    print("\nKey Questions:")
    for q in questions:
        print(f"[{q['timestamp']}] {q['sender']}: {q['message']}")
    
    print("\nShared Links:")
    for url in urls:
        print(f"[{url['timestamp']}] {url['sender']}: {url['message']}")
    
    print("\nAnnouncements:")
    for ann in announcements:
        print(f"[{ann['timestamp']}] {ann['sender']}: {ann['message']}")
    
    summary = summarize_chat(messages)
    print("\nChat Summary:")
    print(summary)

summarizer = pipeline("summarization")

def using_pipeline(chat_data):
    summary = summarizer(chat_text, max_length=50, min_length=10, do_sample=False)
    print("Summary:", summary[0]['summary_text'])

# Example usage
# process_chat_summary(chat_data)
using_pipeline(chat_data)