import cohere

from dotenv import load_dotenv
import os

load_dotenv()
cohere_api_key = os.getenv('cohere_API_KEY')

if not cohere_api_key:
    raise ValueError("Cohere API key is not set in the environment variables!")

# initialize Cohere client
co = cohere.Client(cohere_api_key)

conversation = """



[01:22, 25/9/2024] Rithul Sandeep Vit: That's our ceiling

[01:22, 25/9/2024] Josithaa Vit: WOAH

[01:22, 25/9/2024] Josithaa Vit: I ALSO WANT

[01:23, 25/9/2024] Amlu: Wtf how Show me

[01:23, 25/9/2024] Rithul Sandeep Vit: K go to settings

[01:23, 25/9/2024] Josithaa Vit: GIMME FOR ONE DAY BRO

[01:23, 25/9/2024] Rithul Sandeep Vit: There's an option for background

[01:23, 25/9/2024] Rithul Sandeep Vit: Change to aurora Borealis

[01:23, 25/9/2024] Rithul Sandeep Vit: And then customize colour

[01:23, 25/9/2024] Amlu: So cool Swimming pool

[01:23, 25/9/2024] Amlu: Huh

[01:23, 25/9/2024] Josithaa Vit: I WANT ALSO BRO

[01:24, 25/9/2024] Josithaa Vit: WHOS IS IT

[01:24, 25/9/2024] Rithul Sandeep Vit: Hitesh's

[01:24, 25/9/2024] Rithul Sandeep Vit: Our roommate

[01:24, 25/9/2024] Josithaa Vit: oh :(

[01:24, 25/9/2024] Rithul Sandeep Vit: I think Prince and Hitesh bought it last sem

[01:24, 25/9/2024] Josithaa Vit: then its both of theirs no

[01:24, 25/9/2024] Rithul Sandeep Vit: Yesh

[19:50, 24/9/2024] Josithaa Vit: peas peas

[19:50, 24/9/2024] Josithaa Vit: bro

[19:50, 24/9/2024] Josithaa Vit: did you know

[19:50, 24/9/2024] Josithaa Vit: any word

[19:50, 24/9/2024] Josithaa Vit: if you repeat it twice

[19:50, 24/9/2024] Josithaa Vit: it becomes a word palindrome

[19:50, 24/9/2024] Josithaa Vit:

[20:07, 24/9/2024] Sachin VIT: Hmm hmm

[21:01, 24/9/2024] Josithaa Vit: YES YES

[21:07, 24/9/2024] Sachin VIT: Ok ok

[01:21, 25/9/2024] Josithaa Vit: hahah

[01:21, 25/9/2024] Josithaa Vit: OH 121

[01:21, 25/9/2024] Josithaa Vit: 11²

[01:21, 25/9/2024] Rithul Sandeep Vit: Hey

[01:21, 25/9/2024] Rithul Sandeep Vit: Go sleep

[01:21, 25/9/2024] Rithul Sandeep Vit: You're not allowed to be awake this late

[01:21, 25/9/2024] Rithul Sandeep Vit: Palindrome

[01:21, 25/9/2024] Josithaa Vit: wyd bros

[01:21, 25/9/2024] Josithaa Vit: yess

[01:21, 25/9/2024] Josithaa Vit: SARUPA HELLO

[01:22, 25/9/2024] Josithaa Vit: MY POOKIE

[01:22, 25/9/2024] Rithul Sandeep Vit: Cooking chapati

[01:22, 25/9/2024] Amlu: Why are y'all awake

[01:22, 25/9/2024] Amlu: Hello there

[01:22, 25/9/2024] Josithaa Vit: nightslip bro :(

[01:22, 25/9/2024] Amlu: My cookieeeeee

[01:22, 25/9/2024] Amlu: Snacking

[01:22, 25/9/2024] Josithaa Vit: ooh damn

[18:08, 24/9/2024] Dry Man Kevin: Hang

[18:43, 24/9/2024] Rithul Sandeep Vit: You guys when I say English or Spanish

[18:43, 24/9/2024] Rithul Sandeep Vit: .

[18:43, 24/9/2024] Sachin VIT: What

[18:43, 24/9/2024] Dry Man Kevin: We move

[18:43, 24/9/2024] Sachin VIT: Ohhh

[18:44, 24/9/2024] Dry Man Kevin: UK the joke da

[18:44, 24/9/2024] Sachin VIT: Right

[18:44, 24/9/2024] Prince Sangani Vit: Fuck y’all

[18:44, 24/9/2024] Dry Man Kevin: Why da

[18:44, 24/9/2024] Sachin VIT: Lmk the time and place

[18:45, 24/9/2024] Prince Sangani Vit: Wtff

[18:45, 24/9/2024] Prince Sangani Vit: Rithull

[18:45, 24/9/2024] Dry Man Kevin:

[18:45, 24/9/2024] Prince Sangani Vit: Guys he had my phone

[18:45, 24/9/2024] Prince Sangani Vit: Wth

[18:45, 24/9/2024] Sachin VIT: Nice

[18:45, 24/9/2024] Dry Man Kevin: Just the phone

[18:45, 24/9/2024] Prince Sangani Vit: Sus

[18:46, 24/9/2024] Parvati Nair Vit: Y'all r gay man

[18:46, 24/9/2024] Prince Sangani Vit: We know that

[18:47, 24/9/2024] Prince Sangani Vit: Anything new pls

[18:47, 24/9/2024] Dry Man Kevin: Great discover,

[18:48, 24/9/2024] Parvati Nair Vit: New?

[19:06, 24/9/2024] Prince Sangani Vit: Tell us anything that wdk

[19:07, 24/9/2024] Parvati Nair Vit: Right

[19:30, 24/9/2024] Josithaa Vit: what is this da

[19:34, 24/9/2024] Dry Man Kevin: Java

[19:36, 24/9/2024] Josithaa Vit: damn bro

[19:36, 24/9/2024] Josithaa Vit: crazybrocrazy

[19:39, 24/9/2024] Prince Sangani Vit: Word palindrome

[19:50, 24/9/2024] Josithaa Vit: HAHXHHSHSHAJA YEAS YES

[18:01, 24/9/2024] Dry Man Kevin: Nope

[18:01, 24/9/2024] Prince Sangani Vit: Wtf

[18:02, 24/9/2024] Prince Sangani Vit: Bap

[18:02, 24/9/2024] Prince Sangani Vit: Gap

[18:02, 24/9/2024] Dry Man Kevin: I am excluded from that rule

[18:02, 24/9/2024] Prince Sangani Vit: Nab

[18:02, 24/9/2024] Prince Sangani Vit: Gab fab

[18:02, 24/9/2024] Amlu: Why

[18:02, 24/9/2024] Amlu: What did you do

[18:02, 24/9/2024] Dry Man Kevin: Same reason I said in morning

[18:03, 24/9/2024] Amlu: I don't remember

[18:03, 24/9/2024] Sachin VIT: Bro cooked

[18:03, 24/9/2024] Dry Man Kevin: I am _____

[18:03, 24/9/2024] Dry Man Kevin: Discrete class

[18:03, 24/9/2024] Amlu: Huh

[18:03, 24/9/2024] Sachin VIT: Ironman

[18:04, 24/9/2024] Sachin VIT: Isthriwaala

[18:04, 24/9/2024] Dry Man Kevin: Adorable

[18:05, 24/9/2024] Sachin VIT: Chi thu

[18:05, 24/9/2024] Dry Man Kevin: Truth is sometimes bitter

[18:05, 24/9/2024] Sachin VIT: Chi chi thu thu

[18:06, 24/9/2024] Amlu: Who me? Ik that already

[18:06, 24/9/2024] Sachin VIT: Chi chi chi thu thu thu

[18:07, 24/9/2024] Amlu: I want ice lolly

[18:07, 24/9/2024] Dry Man Kevin: Delulu/cope/hope

[18:08, 24/9/2024] Sachin VIT: Rope

[16:26, 24/9/2024] Josithaa Vit: AFTER I SPOKE TO YOU GUYS

[16:26, 24/9/2024] Josithaa Vit: I SAW THIS VIDEO IN WHICH I WAS TALKING

[16:26, 24/9/2024] Josithaa Vit: AND MY VOICE

[16:26, 24/9/2024] Josithaa Vit: IT SOUNDED EXACTLY LIKE MY SISTER WTF

[16:26, 24/9/2024] Dry Man Kevin: Nothing new

[16:27, 24/9/2024] Sachin VIT: Exactly

[16:27, 24/9/2024] Josithaa Vit: I WOULDVE ACTUALLY THOUGHT THAT WAS MY SISTER IF I HADNT REMEMBERED ME RECORDING THAT

[16:27, 24/9/2024] Josithaa Vit: WHEN DID OUR VOICES CHANGE

[16:27, 24/9/2024] Josithaa Vit: IM PRETTY SURE IT WAS VERY VERY VERY DIFFERENT WHEN WE WERE KIDS

[16:27, 24/9/2024] Josithaa Vit: not kids lets say some years back

[16:27, 24/9/2024] Josithaa Vit: okie guys thookam is coming, i go eep

[16:27, 24/9/2024] Josithaa Vit: byebyee

[16:28, 24/9/2024] Sachin VIT: Eep

[16:28, 24/9/2024] Josithaa Vit: eep bakcwards

[16:28, 24/9/2024] Josithaa Vit: pee

[16:28, 24/9/2024] Josithaa Vit: sorry bye.

[16:28, 24/9/2024] Sachin VIT: I just did that

[16:28, 24/9/2024] Sachin VIT: Bye

[16:28, 24/9/2024] Josithaa Vit: TMI

[17:58, 24/9/2024] Amlu: Bloop

[17:58, 24/9/2024] Amlu: What's tmi

[17:58, 24/9/2024] Rithul Sandeep Vit: Teri meri izzat

[17:59, 24/9/2024] Amlu: Oh

[17:59, 24/9/2024] Sachin VIT: Too much information

[18:00, 24/9/2024] Amlu: Oh

[18:00, 24/9/2024] Prince Sangani Vit: Tu mera ishq

[18:00, 24/9/2024] Prince Sangani Vit: Howzzat

[18:00, 24/9/2024] Amlu: Wow

[18:00, 24/9/2024] Rithul Sandeep Vit: Best TMI

[18:00, 24/9/2024] Dry Man Kevin: Nicee

[18:01, 24/9/2024] Amlu: Doesn't keerthika p take phones away @Dry Man Kevin

[15:51, 24/9/2024] Josithaa Vit: im not attending

[15:51, 24/9/2024] Josithaa Vit: re cat no

[15:52, 24/9/2024] Amlu: Ask abi to take a4 sheets from my bag

[16:05, 24/9/2024] Josithaa Vit: 404

[16:05, 24/9/2024] Josithaa Vit: SHT

[16:05, 24/9/2024] Josithaa Vit: MISSED IT

[16:18, 24/9/2024] Sachin VIT: 16:18

[16:19, 24/9/2024] Sachin VIT: 6+1:8+1

[16:19, 24/9/2024] Sachin VIT: 7:9

[16:19, 24/9/2024] Sachin VIT: 7+9

[16:19, 24/9/2024] Sachin VIT: 16

[16:19, 24/9/2024] Sachin VIT: 1+6

[16:19, 24/9/2024] Sachin VIT: 7

[16:20, 24/9/2024] Dry Man Kevin: Dey

[16:20, 24/9/2024] Josithaa Vit: huh

[16:21, 24/9/2024] Sachin VIT: Mic drop

[16:21, 24/9/2024] Josithaa Vit: oh

[16:21, 24/9/2024] Josithaa Vit: brother

[16:22, 24/9/2024] Josithaa Vit: wait kevin

[16:22, 24/9/2024] Josithaa Vit: you have lab no

[16:22, 24/9/2024] Josithaa Vit: what are you doing on your phone

[16:22, 24/9/2024] Josithaa Vit: pord cim

[16:22, 24/9/2024] Sachin VIT: Apparently he has finished his labcat

[16:22, 24/9/2024] Josithaa Vit: oh dam thats pretty quick

[16:22, 24/9/2024] Sachin VIT: So he doesn't need to attend

[16:22, 24/9/2024] Sachin VIT: No he did it last week

[16:22, 24/9/2024] Josithaa Vit: ohhh

[16:23, 24/9/2024] Josithaa Vit: why did he go today then

[16:23, 24/9/2024] Josithaa Vit: thats why i also skipped dsa today

[16:24, 24/9/2024] Dry Man Kevin: Attendance

[16:24, 24/9/2024] Josithaa Vit: oH

[16:25, 24/9/2024] Sachin VIT: Oh no

[16:25, 24/9/2024] Josithaa Vit: okie guys nini time goodnight, i have english assessment today

[16:25, 24/9/2024] Sachin VIT: But wait

[16:25, 24/9/2024] Sachin VIT: You don't need attendance

[16:25, 24/9/2024] Dry Man Kevin: Teh

[16:25, 24/9/2024] Josithaa Vit: ye

[16:25, 24/9/2024] Sachin VIT: Also jos, how is your vocal clone?

[16:26, 24/9/2024] Josithaa Vit: hahhxhahhxhaha

[16:26, 24/9/2024] Josithaa Vit: she’s fine bro hehe

[16:26, 24/9/2024] Josithaa Vit: DUDE

[15:50, 24/9/2024] Dry Man Kevin: Idk how

[15:50, 24/9/2024] Josithaa Vit: wow bros worlds ahead

[15:50, 24/9/2024] Dry Man Kevin: But it's nice

[15:50, 24/9/2024] Dry Man Kevin: I am running

[15:50, 24/9/2024] Amlu: Bro starting to stock up marks for next sem

[15:50, 24/9/2024] Josithaa Vit: hi running im jo

[15:50, 24/9/2024] Dry Man Kevin: Class??

[15:51, 24/9/2024] Dry Man Kevin: Lab vara la

[09:49, 24/9/2024] Sachin VIT: By mistake.

[13:50, 24/9/2024] Prince Sangani Vit: Guysss

[13:50, 24/9/2024] Prince Sangani Vit: Do they allow us to go out during gravitas

[13:50, 24/9/2024] Parvati Nair Vit: No

[13:50, 24/9/2024] Dry Man Kevin: Nah

[13:50, 24/9/2024] Prince Sangani Vit: Yavv

[13:50, 24/9/2024] Rithul Sandeep Vit: Proud of my boy

[13:52, 24/9/2024] Amlu: Yaa

[15:43, 24/9/2024] Prince Sangani Vit: Guys

[15:43, 24/9/2024] Prince Sangani Vit: Qs marks increased

[15:44, 24/9/2024] Josithaa Vit: WHAT

[15:45, 24/9/2024] Josithaa Vit: OHMYGOD YES

[15:45, 24/9/2024] Rithul Sandeep Vit: How much did you getttt

[15:48, 24/9/2024] Josithaa Vit: i got 12 weightage

[15:48, 24/9/2024] Josithaa Vit: wbyy

[15:49, 24/9/2024] Rithul Sandeep Vit: Ayyy

[15:49, 24/9/2024] Rithul Sandeep Vit: I got 10

[15:49, 24/9/2024] Rithul Sandeep Vit: Gg

[15:49, 24/9/2024] Prince Sangani Vit: I got 10.5

[15:49, 24/9/2024] Amlu: 12.5 But how

[15:49, 24/9/2024] Dry Man Kevin: 111

[15:49, 24/9/2024] Dry Man Kevin: 11 

[09:36, 24/9/2024] Josithaa Vit: PLS YES

[09:36, 24/9/2024] Amlu: BEJDJXKJDN3

[09:36, 24/9/2024] Amlu: Hehhsjejiejissikejfciix

[09:36, 24/9/2024] Amlu: NOOOOOOOOOO

[09:36, 24/9/2024] Josithaa Vit: HAHHXHSHSHHSHSHSHWHSHDHSUAHJAJW

[09:36, 24/9/2024] Josithaa Vit: HAHHSHXHSHSHSHSHSHWH

[09:36, 24/9/2024] Josithaa Vit: SO DAMN DUNNY

[09:36, 24/9/2024] Josithaa Vit: FUNNY

[09:36, 24/9/2024] Amlu: SURE

[09:37, 24/9/2024] Dry Man Kevin: The sweet face u fell for macha @Abimanyu

[09:37, 24/9/2024] Amlu: Noooooooooooooooooooo

[09:48, 24/9/2024] Amlu: SACHIN POSTED THIS ON HIS SNAP STORY

[09:48, 24/9/2024] Amlu: Whjsizkwnrnxkskwlmedmkzkak3jkzwdicuqjeifjsj4if

[09:48, 24/9/2024] Amlu: ,mnssjkxkxkzkjwkejcndjs4iciu,uaeuduhxjauwurt8e8287e7c7xiwi8rf8c

[09:48, 24/9/2024] Sachin VIT: By mistake

[09:48, 24/9/2024] Sachin VIT: I deleted it

[09:48, 24/9/2024] Amlu: Totally

[09:49, 24/9/2024] Amlu: Actually

[09:49, 24/9/2024] Amlu: Why

[09:36, 24/9/2024] Josithaa Vit: SACHIN

[09:36, 24/9/2024] Josithaa Vit: SEND

[09:36, 24/9/2024] Josithaa Vit: NORMALLY

[09:36, 24/9/2024] Sachin VIT: Okay

[09:36, 24/9/2024] Amlu: NO

[09:28, 24/9/2024] Sachin VIT: Very inspiring one

[09:28, 24/9/2024] Josithaa Vit: send bro send

[09:28, 24/9/2024] Sachin VIT: The feminine touch?

[09:28, 24/9/2024] Rithul Sandeep Vit: LIKE HE'S GAY

[09:28, 24/9/2024] Dry Man Kevin: Actually

[09:28, 24/9/2024] Rithul Sandeep Vit: YES

[09:28, 24/9/2024] Josithaa Vit: no?

[09:28, 24/9/2024] Sachin VIT: Wait

[09:28, 24/9/2024] Rithul Sandeep Vit: THAT WAS SACHIN

[09:28, 24/9/2024] Amlu: FRRRR

[09:28, 24/9/2024] Sachin VIT: Lmaoooo

[09:28, 24/9/2024] Amlu: Wtffff

[09:28, 24/9/2024] Josithaa Vit: everyone was summoned w one video lmao

[09:28, 24/9/2024] Sachin VIT: I've sent it

[09:28, 24/9/2024] Josithaa Vit: WHAT

[09:35, 24/9/2024] Amlu: Bye guys

[09:35, 24/9/2024] Josithaa Vit: bye bro

[09:35, 24/9/2024] Josithaa Vit: L

[09:35, 24/9/2024] Josithaa Vit: M

[09:35, 24/9/2024] Josithaa Vit: A

[09:35, 24/9/2024] Josithaa Vit: O

[09:35, 24/9/2024] Josithaa Vit: HWHXHSJXBHSHSHSHAHA

[09:35, 24/9/2024] Amlu: I'm scared

[09:35, 24/9/2024] Josithaa Vit: LOSING MY SHT

[16:57, 21/9/2024] Josithaa Vit: why??

[16:57, 21/9/2024] Josithaa Vit: did yu guys sleep?

[16:57, 21/9/2024] Josithaa Vit: yall were almost done w the thing no

[16:57, 21/9/2024] Prince Sangani Vit: Yes from 4-8

[16:57, 21/9/2024] Josithaa Vit: ohdamn 4 hours onli

[01:28, 22/9/2024] Rithul Sandeep Vit: From 4 to 9

[01:28, 22/9/2024] Rithul Sandeep Vit: Prince even longer

[01:28, 22/9/2024] Rithul Sandeep Vit: He slept at some 3:45

[01:28, 22/9/2024] Rithul Sandeep Vit: All to get drama only he's saying

[06:45, 22/9/2024] Josithaa Vit: lmao

[08:58, 22/9/2024] Parvati Nair Vit: He does watch big boss so

[09:27, 24/9/2024] Rithul Sandeep Vit: WHAT

[09:27, 24/9/2024] Josithaa Vit: AYEE AIR GESTURES MY PHONE ALSO HAS THAT

[09:27, 24/9/2024] Rithul Sandeep Vit: THAT'S SO COOL

[09:27, 24/9/2024] Rithul Sandeep Vit: LMAO

[09:27, 24/9/2024] Rithul Sandeep Vit: THE WAY HE LIKED THE POST

[09:27, 24/9/2024] Rithul Sandeep Vit: VERY DEMURE

[09:27, 24/9/2024] Rithul Sandeep Vit: VERY MINDFUL

[09:27, 24/9/2024] Josithaa Vit: VERY MINDFUL

[09:28, 24/9/2024] Josithaa Vit: so funni lmfao

[09:28, 24/9/2024] Sachin VIT: You should see that post

[09:28, 24/9/2024] Rithul Sandeep Vit: Y'ALL SEEN THAT VDO OF A BUS DRIVER SHIFTING GEARS

[16:04, 21/9/2024] Josithaa Vit: wassup bro

[16:04, 21/9/2024] Josithaa Vit: OH AHHXHAHAH HIII

[16:05, 21/9/2024] Prince Sangani Vit: Life and hack both are going on

[16:05, 21/9/2024] Josithaa Vit: she looks like shes doing yoga

[16:05, 21/9/2024] Prince Sangani Vit: Haha

[16:05, 21/9/2024] Josithaa Vit: heh nice nice

[16:53, 21/9/2024] Josithaa Vit: @Sachin VIT

[16:53, 21/9/2024] Sachin VIT: Oh shit

[16:54, 21/9/2024] Josithaa Vit: HAHXHXHSHAHA

[16:54, 21/9/2024] Josithaa Vit: gurlie pop onli

[16:55, 21/9/2024] Prince Sangani Vit: Are u guys out now

[16:56, 21/9/2024] Josithaa Vit: im out, but im meeting someone hehe

[16:56, 21/9/2024] Josithaa Vit: hows devjams going??

[16:56, 21/9/2024] Prince Sangani Vit: Bad.

[16:57, 21/9/2024] Prince Sangani Vit: We r tired.

[15:08, 20/9/2024] Josithaa Vit: the ac fc

[21:39, 20/9/2024] Parvati Nair Vit: https://forms.gle/hA48UiVgrDkk9kdE8

[21:39, 20/9/2024] Parvati Nair Vit: If u have time

[21:53, 20/9/2024] Sachin VIT: Yaaay Parvati and drugs

[21:53, 20/9/2024] Parvati Nair Vit: This ain't mine genius

[21:53, 20/9/2024] Dry Man Kevin: Drug development

[21:53, 20/9/2024] Parvati Nair Vit: Guys this survey ain't mine It's a friend's

[22:00, 20/9/2024] Rithul Sandeep Vit: Let's gooooo Parvathy getting on drugs let's gooooo

[22:01, 20/9/2024] Parvati Nair Vit: Hahahaha funny

[22:41, 20/9/2024] Parvati Nair Vit: https://docs.google.com/forms/d/e/1FAIpQLSf_z0r4R4_o1hjoNbSUZTC_99jGDosb5C7aQ2dJuzIr9ZdY3A/viewform?usp=sf_link

[22:41, 20/9/2024] Parvati Nair Vit: Guys do this

[09:50, 21/9/2024] Parvati Nair Vit: Guys

[09:50, 21/9/2024] Parvati Nair Vit: Today is a non instructional day right???

[09:50, 21/9/2024] Parvati Nair Vit: 4 hrs outing??

[09:50, 21/9/2024] Prince Sangani Vit: Yes

[09:50, 21/9/2024] Parvati Nair Vit: U sure? Pakka??

[09:52, 21/9/2024] Prince Sangani Vit: Ig

[09:57, 21/9/2024] Parvati Nair Vit: Tf?

[16:03, 21/9/2024] Josithaa Vit: 403

[16:03, 21/9/2024] Josithaa Vit: @Amlu

[16:03, 21/9/2024] Prince Sangani Vit: Wow

[16:03, 21/9/2024] Prince Sangani Vit: Palindrome

[16:04, 21/9/2024] Prince Sangani Vit: 404

[16:04, 21/9/2024] Josithaa Vit: 404

[16:04, 21/9/2024] Prince Sangani Vit: Error404

[16:04, 21/9/2024] Prince Sangani Vit: My room no also

[16:04, 21/9/2024] Josithaa Vit: YESS

[16:04, 21/9/2024] Josithaa Vit: sarupas house number also

[16:04, 21/9/2024] Prince Sangani Vit: Yess

[16:04, 21/9/2024] Josithaa Vit: your birthday also

[15:08, 20/9/2024] Prince Sangani Vit: Okok

[12:18, 20/9/2024] Josithaa Vit: mum and sis are coming da

[12:20, 20/9/2024] Amlu: java assessment :'(

[12:21, 20/9/2024] Amlu: Will join y'all if you're still there after 5:30

[12:25, 20/9/2024] Josithaa Vit: ah oki oki

[13:29, 20/9/2024] Dry Man Kevin: How was it

[13:29, 20/9/2024] Dry Man Kevin: The hackathon

[13:37, 20/9/2024] Prince Sangani Vit: Going good

[13:37, 20/9/2024] Dry Man Kevin: Nice

[13:53, 20/9/2024] Parvati Nair Vit: Hellooo Where should we come?

[13:57, 20/9/2024] Josithaa Vit: um

[13:57, 20/9/2024] Josithaa Vit: anywhere works

[13:57, 20/9/2024] Josithaa Vit: near fc dc?

[13:58, 20/9/2024] Parvati Nair Vit: Okk

[14:08, 20/9/2024] Rithul Sandeep Vit: Who's the handsome guy on the right?

[14:08, 20/9/2024] Rithul Sandeep Vit: Asking for a friend

[14:08, 20/9/2024] Parvati Nair Vit: Etho alavalathi

[14:09, 20/9/2024] Parvati Nair Vit: Don't ask Tell ur friend to get glasses

[14:09, 20/9/2024] Prince Sangani Vit: Lmao

[14:15, 20/9/2024] Rithul Sandeep Vit: Avakku glasses undu already

[14:15, 20/9/2024] Rithul Sandeep Vit: Vere college ila

[14:17, 20/9/2024] Parvati Nair Vit: Ohhhoooo aano

[14:17, 20/9/2024] Parvati Nair Vit: Avalde kshtakaalam entho cheyyan

[14:19, 20/9/2024] Rithul Sandeep Vit: Po dee patti

[15:05, 20/9/2024] Prince Sangani Vit: Jos where

[15:05, 20/9/2024] Rithul Sandeep Vit: Jose

[15:05, 20/9/2024] Rithul Sandeep Vit: Haveth your mother arrived

[15:08, 20/9/2024] Josithaa Vit: yessir

[15:08, 20/9/2024] Prince Sangani Vit: We r free now

[15:08, 20/9/2024] Josithaa Vit: we're in fc rn hehe

[15:08, 20/9/2024] Josithaa Vit: come off bro

[09:29, 20/9/2024] Sachin VIT: SW Newsletter presents, The Chronicles Quest Ready to dive into an experience where creativity meets chaos? The Chronicles Quest is not just another event where a whirlwind of unexpected twists, hilarious moments, and pure, unfiltered fun. Here, no idea is too wild, and no moment stays the same for long. Picture this: one minute, you're crafting a unique character, and the next, the music stops like a game of musical chairs and you're thrust into a new challenge. With three thrilling rounds, you'll face quick-fire creativity tests, spontaneous team showdowns, and even design an epic first look for your teams movie. Plus, get ready for some meme-worthy moments that will have you laughing out loud and sharing the fun. Think you've got the best team? Be prep…

[09:34, 20/9/2024] Sachin VIT: I'll give treat for the ones who register

[12:01, 20/9/2024] Josithaa Vit: guys

[12:01, 20/9/2024] Josithaa Vit: are yall free around 330?

[12:03, 20/9/2024] Josithaa Vit: ohwait rithul and prince have class till 5 no

[12:03, 20/9/2024] Dry Man Kevin: Yep

[12:03, 20/9/2024] Dry Man Kevin: Hackathon

[12:03, 20/9/2024] Josithaa Vit: when is that till?

[12:03, 20/9/2024] Josithaa Vit: devjams?

[12:05, 20/9/2024] Josithaa Vit: okie we'll be there from like 330 until 530-6 i think, meet mum and sis when yall are free

[12:06, 20/9/2024] Prince Sangani Vit: We will clme

[12:06, 20/9/2024] Prince Sangani Vit: Come

[12:06, 20/9/2024] Prince Sangani Vit: We have break from 3:30 to 9:30

[12:06, 20/9/2024] Prince Sangani Vit: So at 3:30 we will leave anna audi and come

[12:11, 20/9/2024] Josithaa Vit: okie nice nicee

[12:11, 20/9/2024] Rithul Sandeep Vit: It's overnight

[12:11, 20/9/2024] Rithul Sandeep Vit: Why what's up

[12:15, 20/9/2024] Parvati Nair Vit: Come where
"""

response = co.summarize(
    text=conversation, 
    length='long', 
    format='paragraph', 
    model='summarize-xlarge',
    temperature=0.5
)

summary = response.summary
print(summary)
