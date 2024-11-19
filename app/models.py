from django.db import models
import random

class Questions(models.Model):
    question = models.TextField()
    answer = models.TextField()
    choices = models.TextField()
    category = models.TextField()

def construct_question(question,answer,choices,category,id):
    q = Questions(question=question,answer=answer,choices=choices,category=category,id=id)
    q.save()
    return q
def load_questions(clear=True):
    if clear == True:
        Questions.objects.all().delete()
    number = 0
    for q in questionBank:
            number += 1
            construct_question(
                q['question'],
                q['answer'],
                q['choices'],
                q['category'],
                number
            )
def QInfo(id,info):
    if info == 'question':
        return Questions.objects.get(id=id).question
    if info == 'answer':
        return Questions.objects.get(id=id).answer
    if info == 'choices':
        return Questions.objects.get(id=id).choices
    if info == 'category':
        return Questions.objects.get(id=id).category
    if info == 'id':
        return Questions.objects.get(id=id).id
def split_choices(id):
    split = (Questions.objects.get(id=id).choices).split(',')
    if 'True' in split:
        return split
    else:
        return random.sample(split,len(split))
questionBank = [
    {
        'question': 'Who played Austin Powers?',
        'answer': 'Mike Myers',
        'choices': 'Mike Myers,Joe Pesci,Michael Myers,Seth Green',
        'category': 'Pop Culture',
    },
    {
        'question': 'In what year was the United States formed?',
        'answer': '1776',
        'choices': '1776,1775,1777,1778',
        'category': 'History',
    },
    {
        'question': 'Which of these actors was the first to play James Bond?',
        'answer': 'Barry Nelson',
        'choices': 'Barry Nelson,Sean Connery,Roger Moore,Pierce Brosnan,Daniel Craig',
        'category': 'Pop Culture',
    },
    {
        'question': 'Vatican City is a city in Italy.',
        'answer': 'False',
        'choices': 'True,False',
        'category': 'Geography',
    },
    {
        'question': 'Whose assassination is considered the spark that ignited the First World War?',
        'answer': 'Franz Ferdinand',
        'choices': 'Franz Ferdinand,Franz Kafka,Winston Churchill,Vladimir Lenin',
        'category': 'History',
    },
    {
        'question': 'Which of these actors was the first to play Bruce Wayne, a.k.a. Batman?',
        'answer': 'Adam West',
        'choices': 'Adam West,George Clooney,Michael Keaton,Robert Pattinson,Val Kilmer',
        'category': 'Pop Culture',
    },
    {
        'question': 'Who was the first man in space?',
        'answer': 'Yuri Gagarin',
        'choices': 'Edwin Aldrin,Neil Armstrong,Yuri Gagarin,Alan Shepard',
        'category': 'History',
    },
    {
        'question': 'Which of these characters was not in the original Super Smash Bros. on the Nintendo 64?',
        'answer': 'Princess Peach',
        'choices': 'Ness,Jigglypuff,Princess Peach,Captain Falcon,Donkey Kong',
        'category': 'Pop Culture',
    },
    {
        'question': "Who was the founder of the Coca-Cola Company?",
        'answer': 'Asa Griggs Candler',
        'choices': 'Asa Griggs Candler,John Pemberton,Will Keith Kellogg,James Quincey',
        'category': 'Industry',
    },
    {
        'question': "Which fruit is known as the 'king of fruits'?",
        'answer': 'Durian',
        'choices': 'Durian,Pineapple,Mango,Banana',
        'category': 'Food',
    },
    {
        'question': "Which country is the largest producer of coffee in the world?",
        'answer': 'Brazil',
        'choices': 'Ethiopia,Brazil,Vietnam,Colombia',
        'category': 'Food',
    },
    {
        'question': "Who was the longest serving President of the United States?",
        'answer': 'Franklin D. Roosevelt',
        'choices': 'Franklin D. Roosevelt,Teddy Roosevelt,George Bush,Andrew Jackson,Ronald Reagan',
        'category': 'History',
    },
    {
        'question': "Who was the President of the United States at the end of World War II?",
        'answer': 'Harry Truman',
        'choices': 'Franklin D. Roosevelt,Harry Truman,Herbert Hoover,William Taft,Calvin Coolidge',
        'category': 'History',
    },
    {
        'question': "Which of these literary works was not written by Edgar Alan Poe?",
        'answer': 'What the Moon Brings',
        'choices': 'The Tell-Tale Heart,The Raven,Black Cat,The Cask of Amontillado,What the Moon Brings',
        'category': 'Literature',
    },
    {
        'question': "What is the tallest building in the world?",
        'answer': 'Burj Khalifa',
        'choices': 'Burj Khalifa,Shanghai Tower,Central Park Tower,Empire State Building',
        'category': 'Geography',
    },
    {
        'question': "What color were the pyramids of Egypt originally?",
        'answer': 'White',
        'choices': 'White,Yellow,Beige,Gray',
        'category': 'History',
    },
    {
        'question': "What is the first element on the periodic table?",
        'answer': 'Hydrogen',
        'choices': 'Hydrogen,Helium,Carbon,Oxygen',
        'category': 'Science',
    },
    {
        'question': "What is the second element on the periodic table?",
        'answer': 'Helium',
        'choices': 'Hydrogen,Helium,Carbon,Nitrogen',
        'category': 'Science',
    },
    {
        'question': "In plant cells, what organelle is responsible for photosynthesis?",
        'answer': 'Chloroplast',
        'choices': 'Chloroplast,Lysosome,Vacuole,Endoplasmic Reticulum',
        'category': 'Science',
    },
    {
        'question': "What day of the year is 'Good King Wenceslas' associated with?",
        'answer': 'December 26',
        'choices': 'December 26,December 25,December 24,December 31',
        'category': 'Music',
    },
    {
        'question': "What city is Elvis Presley from?",
        'answer': 'Tupelo',
        'choices': 'Memphis,Tupelo,Vicksburg,Knoxville',
        'category': 'Music',
    },
    {
        'question': "Who plays the main character in the movie 'Top Gun'?",
        'answer': 'Tom Cruise',
        'choices': 'Tom Hanks,Tom Cruise,Tom Skerritt,Tim Robbins',
        'category': 'Pop Culture',
    },
    {
        'question': "In the 2004 film 'Spider-Man 2', who plays the villain, Doctor Octopus?",
        'answer': 'Alfred Molina',
        'choices': 'Alfred Molina,Willem Dafoe,Tobey Maguire,James Franco',
        'category': 'Pop Culture',
    },
    {
        'question': "What was the codename for the Normandy Landings on June 6th 1944 (D-Day)?",
        'answer': 'Operation Neptune',
        'choices': 'Operation Neptune,Operation Phobos,Operation Beached Whale,Operation Mincemeat',
        'category': 'History',
    },
    {
        'question': "What year did the Titanic sink?",
        'answer': '1912',
        'choices': '1912,1911,1913,1910',
        'category': 'History',
    },
    {
        'question': "In 1941, during what month did the United States officially enter World War II?",
        'answer': 'December',
        'choices': 'December,November,January,February',
        'category': 'History',
    },
    {
        "question": "Who wrote 'The Great Gatsby'?",
        "answer": "F. Scott Fitzgerald",
        "choices": "F. Scott Fitzgerald,Ernest Hemingway,John Steinbeck,William Faulkner",
        "category": "Literature"
    },
    {
        "question": "What is the capital city of Italy?",
        "answer": "Rome",
        "choices": "Rome,Milan,Venice,Florence",
        "category": "Geography"
    },
    {
        "question": "What is the largest island in the world?",
        "answer": "Greenland",
        "choices": "Greenland,New Guinea,Borneo,Madagascar",
        "category": "Geography"
    },
    {
        "question": "What is the chemical formula for water?",
        "answer": "H2O",
        "choices": "H2O,CO2,O2,NaCl",
        "category": "Science"
    },
    {
        "question": "Who was the first person to reach the South Pole?",
        "answer": "Roald Amundsen",
        "choices": "Roald Amundsen,Robert Falcon Scott,Ernest Shackleton,Edmund Hillary",
        "category": "History"
    },
    {
        "question": "Who painted the ceiling of the Sistine Chapel?",
        "answer": "Michelangelo",
        "choices": "Michelangelo,Leonardo da Vinci,Raphael,Donatello",
        "category": "Art"
    },
    {
        "question": "What is the capital city of Canada?",
        "answer": "Ottawa",
        "choices": "Ottawa,Toronto,Vancouver,Montreal",
        "category": "Geography"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "answer": "Japan",
        "choices": "Japan,China,South Korea,Thailand",
        "category": "Geography"
    },
    {
        "question": "What is the main ingredient in guacamole?",
        "answer": "Avocado",
        "choices": "Avocado,Tomato,Onion,Garlic",
        "category": "Food"
    },
    {
        "question": "Who is known as the 'Father of Computers'?",
        "answer": "Charles Babbage",
        "choices": "Charles Babbage,Alan Turing,John von Neumann,Bill Gates",
        "category": "Industry"
    },
    {
        "question": "Who discovered penicillin?",
        "answer": "Alexander Fleming",
        "choices": "Alexander Fleming,Marie Curie,Isaac Newton,Sigmund Freud",
        "category": "Science"
    },
    {
        "question": "What is the smallest country in the world?",
        "answer": "Vatican City",
        "choices": "Vatican City,Monaco,San Marino,Liechtenstein",
        "category": "Geography"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "answer": "Leonardo da Vinci",
        "choices": "Leonardo da Vinci,Michelangelo,Rembrandt,Van Gogh",
        "category": "Art"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "answer": "Au",
        "choices": "Au,Ag,Fe,Pt",
        "category": "Science"
    },
    {
        "question": "What is the capital city of Australia?",
        "answer": "Canberra",
        "choices": "Canberra,Sydney,Melbourne,Brisbane",
        "category": "Geography"
    },
    {
        "question": "Mount Everest is the tallest mountain in the world.",
        "answer": "True",
        "choices": "True,False",
        "category": "Geography"
    },
    {
        "question": "The chemical symbol for silver is Ag.",
        "answer": "True",
        "choices": "True,False",
        "category": "Science"
    },
    {
        "question": "The Amazon River is the longest river in the world.",
        "answer": "False",
        "choices": "True,False",
        "category": "Geography"
    },
    {
        "question": "The capital of France is Paris.",
        "answer": "True",
        "choices": "True,False",
        "category": "Geography"
    },
    {
        "question": "The Pacific Ocean is the largest ocean on Earth.",
        "answer": "True",
        "choices": "True,False",
        "category": "Geography"
    },
    {
        "question": "The Great Wall of China is visible from space.",
        "answer": "False",
        "choices": "True,False",
        "category": "Geography"
    },
    {
        "question": "Who wrote '1984'?",
        "answer": "George Orwell",
        "choices": "George Orwell,Aldous Huxley,Ray Bradbury,Kurt Vonnegut",
        "category": "Literature"
    },
    {
        "question": "What is the chemical symbol for potassium?",
        "answer": "K",
        "choices": "K,Pb,Pt,Kr",
        "category": "Science"
    },
    {
        "question": "In which year did World War I begin?",
        "answer": "1914",
        "choices": "1914,1918,1939,1945",
        "category": "History"
    },
    {
        "question": "What is the largest continent by area?",
        "answer": "Asia",
        "choices": "Asia,Africa,North America,Europe",
        "category": "Geography"
    },
    {
        "question": "Who painted 'Starry Night'?",
        "answer": "Vincent van Gogh",
        "choices": "Vincent van Gogh,Pablo Picasso,Claude Monet,Salvador Dali",
        "category": "Art"
    },
    {
        "question": "What is the smallest country in South America?",
        "answer": "Suriname",
        "choices": "Suriname,Guyana,Uruguay,Paraguay",
        "category": "Geography"
    },
    {
        "question": "Who was the 16th President of the United States?",
        "answer": "Abraham Lincoln",
        "choices": "Abraham Lincoln,George Washington,Thomas Jefferson,Theodore Roosevelt",
        "category": "History"
    },
    {
        "question": "What is the hardest naturally occurring mineral?",
        "answer": "Diamond",
        "choices": "Diamond,Quartz,Topaz,Ruby",
        "category": "Science"
    },
    {
        "question": "Which planet is known as the Morning Star?",
        "answer": "Venus",
        "choices": "Venus,Mars,Jupiter,Saturn",
        "category": "Science"
    },
    {
        "question": "The capital of Spain is Barcelona.",
        "answer": "False",
        "choices": "True,False",
        "category": "Geography"
    },
    {
        "question": "What is the largest lake in the world by area?",
        "answer": "Caspian Sea",
        "choices": "Caspian Sea,Lake Superior,Lake Victoria,Lake Huron",
        "category": "Geography"
    },
    {
        "question": "Which country is known as the Land of the Midnight Sun?",
        "answer": "Norway",
        "choices": "Norway,Sweden,Finland,Japan",
        "category": "Geography"
    },
    {
        "question": "Who wrote 'Moby-Dick'?",
        "answer": "Herman Melville",
        "choices": "Herman Melville,Mark Twain,Charles Dickens,Edgar Allan Poe",
        "category": "Literature"
    },
    {
        "question": "What is the tallest waterfall in the world?",
        "answer": "Angel Falls",
        "choices": "Angel Falls,Niagara Falls,Victoria Falls,Iguazu Falls",
        "category": "Geography"
    },
    {
        "question": "Who was the first woman in space?",
        "answer": "Valentina Tereshkova",
        "choices": "Valentina Tereshkova,Sally Ride,Mae Jemison,Christa McAuliffe",
        "category": "History"
    },
    {
        "question": "What is the largest land animal?",
        "answer": "African Elephant",
        "choices": "African Elephant,Asian Elephant,Hippopotamus,Rhinoceros",
        "category": "Science"
    },
    {
        "question": "Who wrote 'The Catcher in the Rye'?",
        "answer": "J.D. Salinger",
        "choices": "J.D. Salinger,Ernest Hemingway,F. Scott Fitzgerald,John Steinbeck",
        "category": "Literature"
    },
    {
        "question": "What is the capital city of Germany?",
        "answer": "Berlin",
        "choices": "Berlin,Munich,Frankfurt,Hamburg",
        "category": "Geography"
    },
    {
        "question": "Who developed the polio vaccine?",
        "answer": "Jonas Salk",
        "choices": "Jonas Salk,Albert Sabin,Alexander Fleming,Edward Jenner",
        "category": "Science"
    },
    {
        "question": "What is the smallest planet in our solar system?",
        "answer": "Mercury",
        "choices": "Mercury,Mars,Venus,Pluto",
        "category": "Science"
    },
    {
        "question": "Who was the first woman to win a Nobel Prize?",
        "answer": "Marie Curie",
        "choices": "Marie Curie,Florence Nightingale,Jane Goodall,Rosalind Franklin",
        "category": "History"
    },
    {
        "question": "What is the largest desert in the world?",
        "answer": "Sahara",
        "choices": "Sahara,Arabian,Gobi,Kalahari",
        "category": "Geography"
    },
    {
        "question": "What is the capital city of Egypt?",
        "answer": "Cairo",
        "choices": "Cairo,Alexandria,Giza,Luxor",
        "category": "Geography"
    },
    {
        "question": "Who wrote 'The Odyssey'?",
        "answer": "Homer",
        "choices": "Homer,Virgil,Ovid,Sophocles",
        "category": "Literature"
    },
    {
        "question": "What is the chemical symbol for sodium?",
        "answer": "Na",
        "choices": "Na,So,Sa,Sn",
        "category": "Science"
    },
    {
        "question": "In which year did the Berlin Wall fall?",
        "answer": "1989",
        "choices": "1989,1985,1991,1993",
        "category": "History"
    },
    {
        "question": "What is the largest country by area?",
        "answer": "Russia",
        "choices": "Russia,Canada,China,United States",
        "category": "Geography"
    },
    {
        "question": "Who painted 'The Persistence of Memory'?",
        "answer": "Salvador Dali",
        "choices": "Salvador Dali,Pablo Picasso,Claude Monet,Henri Matisse",
        "category": "Art"
    },
    {
        "question": "What is the hardest substance in the human body?",
        "answer": "Tooth enamel",
        "choices": "Tooth enamel,Bone,Nail,Cartilage",
        "category": "Science"
    },
    {
        "question": "Which country is known as the Land of Fire and Ice?",
        "answer": "Iceland",
        "choices": "Iceland,Greenland,Norway,Finland",
        "category": "Geography"
    },
    {
        "question": "Who was the first person to circumnavigate the globe?",
        "answer": "Ferdinand Magellan",
        "choices": "Ferdinand Magellan,Christopher Columbus,Vasco da Gama,James Cook",
        "category": "History"
    },
    {
        "question": "What is the largest bird in the world?",
        "answer": "Ostrich",
        "choices": "Ostrich,Emu,Albatross,Condor",
        "category": "Science"
    },
    {
        "question": "What is the largest bone in the human body?",
        "answer": "Femur",
        "choices": "Femur,Tibia,Humerus,Radius",
        "category": "Science"
    },
    {
        "question": "What is the title of the series finale of 'Breaking Bad'?",
        "answer": "Felina",
        "choices": "Felina,Ozymandias,Face Off,Live Free Or Die",
        "category": "Pop Culture"
    },
    {
        "question": "Who directed the movie 'Inception'?",
        "answer": "Christopher Nolan",
        "choices": "Christopher Nolan,Steven Spielberg,James Cameron,Quentin Tarantino",
        "category": "Pop Culture"
    },
    {
        "question": "Which TV show is set in the fictional town of Hawkins, Indiana?",
        "answer": "Stranger Things",
        "choices": "Stranger Things,The X-Files,Supernatural,The Twilight Zone",
        "category": "Pop Culture"
    },
    {
        "question": "Who is the author of the 'Game of Thrones' book series?",
        "answer": "George R.R. Martin",
        "choices": "George R.R. Martin,J.R.R. Tolkien,J.K. Rowling,Stephen King",
        "category": "Pop Culture"
    },
    {
        "question": "Which movie features the character Jack Sparrow?",
        "answer": "Pirates of the Caribbean",
        "choices": "Pirates of the Caribbean,Indiana Jones,The Mummy,National Treasure",
        "category": "Pop Culture"
    },
    {
        "question": "Who played the character of Tony Stark in the Marvel Cinematic Universe?",
        "answer": "Robert Downey Jr.",
        "choices": "Robert Downey Jr.,Chris Evans,Chris Hemsworth,Mark Ruffalo",
        "category": "Pop Culture"
    },
    {
        "question": "Who created the TV show 'The Simpsons'?",
        "answer": "Matt Groening",
        "choices": "Matt Groening,Seth MacFarlane,Trey Parker,Matt Stone",
        "category": "Pop Culture"
    },
    {
        "question": "Who is the lead singer of the band Queen?",
        "answer": "Freddie Mercury",
        "choices": "Freddie Mercury,David Bowie,Elton John,Mick Jagger",
        "category": "Pop Culture"
    },
    {
        "question": "Who played the character of Harry Potter in the movie series?",
        "answer": "Daniel Radcliffe",
        "choices": "Daniel Radcliffe,Elijah Wood,Tom Felton,Rupert Grint",
        "category": "Pop Culture"
    },
    {
        "question": "Who is known as the 'Queen of Pop'?",
        "answer": "Madonna",
        "choices": "Madonna,Beyoncé,Lady Gaga,Rihanna",
        "category": "Pop Culture"
    },
    {
        "question": "Who played the character of Forrest Gump in the movie?",
        "answer": "Tom Hanks",
        "choices": "Tom Hanks,Robin Williams,Brad Pitt,Leonardo DiCaprio",
        "category": "Pop Culture"
    },
    {
        "question": "Who directed the movie 'Pulp Fiction'?",
        "answer": "Quentin Tarantino",
        "choices": "Quentin Tarantino,Martin Scorsese,Francis Ford Coppola,Stanley Kubrick",
        "category": "Pop Culture"
    },
    {
        "question": "Which movie features the character Neo?",
        "answer": "The Matrix",
        "choices": "The Matrix,Inception,Blade Runner,Minority Report",
        "category": "Pop Culture"
    },
    {
        "question": "Quentin Tarantino's 2012 film 'Django Unchained' takes it's name from a spaghetti western from which decade?",
        "answer": "1960s",
        "choices": "1960s,1950s,1970s,1980s",
        "category": "Pop Culture"
    },
    {
        "question": "Which game is considered the first commercially successful video game, released in 1972?",
        "answer": "Pong",
        "choices": "Pong,Space Invaders,Pac-Man,Asteroids",
        "category": "Pop Culture"
    },
    {
        "question": "What is the best-selling video game console of all time as of 2020?",
        "answer": "PlayStation 2",
        "choices": "PlayStation 2,Nintendo Wii,Xbox 360,PlayStation 4",
        "category": "Pop Culture"
    },
    {
        "question": "Which game series features a post-apocalyptic world with a 1950s American aesthetic?",
        "answer": "Fallout",
        "choices": "Fallout,Borderlands,The Last of Us,Metro",
        "category": "Pop Culture"
    },
    {
        "question": "What is the name of the main character in the Legend of Zelda series?",
        "answer": "Link",
        "choices": "Link,Zelda,Ganon,Sheik",
        "category": "Pop Culture"
    },
    {
        "question": "Which game, released in 2013, allows players to explore a vast open world and switch between three protagonists?",
        "answer": "Grand Theft Auto V",
        "choices": "Grand Theft Auto V,Red Dead Redemption 2,The Witcher 3: Wild Hunt,Assassin's Creed IV: Black Flag",
        "category": "Pop Culture"
    },
    {
        "question": "What is the name of the block-building game that became a global phenomenon after its release in 2011?",
        "answer": "Minecraft",
        "choices": "Minecraft,Roblox,Fortnite,Terraria",
        "category": "Pop Culture"
    },
    {
        "question": "Which game series features the characters Master Chief and Cortana?",
        "answer": "Halo",
        "choices": "Halo,Mass Effect,Gears of War,Destiny",
        "category": "Pop Culture"
    },
    {
        "question": "What is the name of the 1980 arcade game where players control a yellow circle that eats dots and avoids ghosts?",
        "answer": "Pac-Man",
        "choices": "Pac-Man,Pong,Donkey Kong,Galaga",
        "category": "Pop Culture"
    },
    {
        "question": "Who created the comic book character Spider-Man?",
        "answer": "Stan Lee",
        "choices": "Stan Lee,Todd McFarlane,Sam Raimi,Jack Kirby",
        "category": "Pop Culture"
    },
    {
        "question": "Who created the comic book character Spawn?",
        "answer": "Todd McFarlane",
        "choices": "Stan Lee,Todd McFarlane,Frank Miller,Robert Kirkman",
        "category": "Pop Culture"
    },
    {
        "question": "Who created the comic book character Invincible?",
        "answer": "Robert Kirkman",
        "choices": "Robert Kirkman,Todd McFarlane,Jeff Allen,Ryan Ottley",
        "category": "Pop Culture"
    },
    {
        "question": "Who created the comic book character Darkseid?",
        "answer": "Jack Kirby",
        "choices": "Jack Kirby,Stan Lee,Marv Wolfman,Bob Kane",
        "category": "Pop Culture"
    },
    {
        "question": "In the comic series 'Watchmen' which character is murdered at the beginning of the story?",
        "answer": "The Comedian",
        "choices": "The Comedian,Rorschach,Moloch,Captain Metropolis",
        "category": "Pop Culture"
    },
    {
        "question": "In the 1985 DC comics event 'Crisis On Infinite Earths', which of these characters did not die?",
        "answer": "Psycho Pirate",
        "choices": "Robin,Supergirl,The Flash,Psycho Pirate",
        "category": "Pop Culture"
    },
    {
        "question": "Django is a coding framework primarily based in what language?",
        "answer": "Python",
        "choices": "Python,Javascript,HTML,C++,C#",
        "category": "Science"
    },
    {
        "question": "How many provinces are in Canada?",
        "answer": "10",
        "choices": "8,9,10,11,12,13",
        "category": "Geography"
    },
]