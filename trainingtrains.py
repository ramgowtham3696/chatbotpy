from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
     [
        r"what is your name ?",
        ["My name is Chatty and what is your name?",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i am doing good",
        ["\nNice to hear that\n\nWhat are looking for?\n1.Course\n2.Inplant Training\n3.Certification",]
    ],
    [
        r"hi|hey|hello",
        ["Hey there.\nWELCOME TO TRAINING TRAINS\n",]
    ],
    [
        r"1|2|3",
        ["Thats great\n\nWhat topic are you looking for?\n\na.JAVA\nb.PYTHON\nc.HTML/CSS\nd.AI\ne.Data Science\nf.Machine learning\ng.C panel\nh.Android\ni.Game development\nj.Digital Marketing\nk.PHP/MySQL\nl.d\Data Structures\nm.workpress\nn.Angular JS\no.Web Designing\np.Cloud Computing\nq.XML technology\nr.laravel framework\ns.Software Testing\nt.Google Firebase\n"]
        
    ],
    [
        r"b|d|f|g|h|i|j|k|m|n|o|p|r|s|t",
        ["Hmm, Looks Like a Smart decision.\n\nI am registering the name for you.\nWhat else I can help you?",]
        
    ],
	[
        r"e",
        ["\nHmm, Looks Like a Smart decision.\n\nThese are the syllabus,\n*Math\n*Programming R/Python\n*Data Analysis and Visualization\n*Data Wrangling\n*Machine Learning\n*Big Data\n\nI am registering the name for you.\nWhat else I can help you?",]
        
    ],
	[
        r"a",
        ["\nHmm, Looks Like a Smart decision.\n\nThese are the syllabus\n*Overview of Programming with Java\n*Simple Programs and environment\n*OOP's concepts\n*Exceptions\n*Multithreading\n*Java Thread Model\n*Frameworks\n*Ultility classes\n\nI am registering the name for you.\nWhat else I can help you?",]
        
    ],
    [
        r"(.*) created ?",
        ["Nagesh created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"location|city|address",
        ['\nWe have centres in two locations,\n\n1.COIMBATORE\nOffice number: 9025337847\nFirst Floor 169\nNvn Layout New Siddhapudur\nNear to Sree Ayyappan Temple\nCoimbatore 641044, Tamil Nadu 641044\n\n2.ERODE\nOffice no:9498860729,\n2nd Floor, Dheeran Bakes Upstair,\nNear Taluk Near Taluk Office, Bungalow Street,\nPerundurai, Tamil Nadu 638052',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    
[
        r"what is the fee",
        ["\nIt only cost,\nRs.6000 for 2-3 months\nRs.3000 for 20 days"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"contact",
        ["Boopathi Kumar\n\nMobile:9698548633/9025010144\nE-mail:trainingtrains@gmail.com\nWebpage:www.trainingtrains.com / www.trainingtrains.in",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
],
    [
        r"quit",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]
def chatty():
	chat = Chat(pairs, reflections)
	chat.converse()
if __name__ == "__main__":
    chatty()