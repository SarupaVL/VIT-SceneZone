import spacy
from spacy.matcher import Matcher

# Load the pre-trained spaCy model for English
nlp = spacy.load("en_core_web_sm")

# Initialize the matcher
matcher = Matcher(nlp.vocab)

# Define patterns to identify event types and topics of interest
patterns = [
    # Event types (common keywords)
    [{"LOWER": "workshop"}],
    [{"LOWER": "conference"}],
    [{"LOWER": "seminar"}],
    [{"LOWER": "webinar"}],
    [{"LOWER": "session"}],
    [{"LOWER": "meetup"}],
    
    # Topics of interest (noun phrases commonly used as topics)
    [{"POS": "NOUN", "OP": "+"}, {"POS": "NOUN", "OP": "*"}],  # E.g., "stress management", "quantum computing"
]

# Add patterns to matcher
matcher.add("EventTypeOrTopic", patterns)

# Sample event descriptions
descriptions = [
    "Join us for an inspiring 'Yogic Pencil Sketch Event', where art meets mindfulness. This unique event invites participants of all ages to explore the beauty and depth of yoga through the art of pencil sketching. This event aims to foster mindfulness, creativity, and a sense of community, blending the tranquility of yoga with the expressive power of art.",
    
    "Sanskriti Shabdakoda Sohala, hosted by the Yuva Marathi- Marathi Literary Association, is an engaging event designed to test participants’ knowledge of the state’s diverse and rich cultural heritage. Participants will solve crossword puzzles featuring clues related to traditional festivals, cuisine, historical landmarks, art forms, and famous personalities from Maharashtra. This fun, intellectually stimulating event encourages people to explore the deep-rooted traditions as well as modern-day aspects of the state, all while competing for exciting prizes. Perfect for crossword enthusiasts and culture lovers alike, this event offers a unique way to celebrate and learn more about Maharashtra!",
    
    "TechLoop: Quantum Computing is an introductory session designed to equip participants with foundational knowledge in quantum computing. The event will cover essential mathematical concepts and theories to help you get started in this advanced field. The session will place a strong emphasis on Qiskit, an open-source quantum computing software development framework.",
    
    "Join us in an interactive session on 'Stress Management' featuring Mr. Muralitharan, who will guide us on how to tackle our thoughts and transform stress into a catalyst for positive change. Let's together join and manage stress by changing our perspective and not avoiding life challenges."
]

# Function to extract entities and tags using matcher
def extract_with_custom_matcher(text):
    doc = nlp(text)
    matches = matcher(doc)
    entities = []
    for match_id, start, end in matches:
        span = doc[start:end]
        entities.append(span.text)
    return entities

# Function to extract specific entities
def extract_entities(text):
    doc = nlp(text)
    # Extract entities using NER
    person_names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    
    # Extract topics and event types using custom matcher
    event_types_and_topics = extract_with_custom_matcher(text)
    
    return person_names, event_types_and_topics

# Iterate through event descriptions and extract entities
for description in descriptions:
    print(f"Description: {description}")
    person_names, event_types_and_topics = extract_entities(description)
    print(f"Person Names: {person_names}")
    print(f"Event Types / Topics: {event_types_and_topics}\n")
