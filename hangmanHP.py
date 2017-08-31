import random

def hangman(word):
    wrong = 0
    guessed = []
    stages = ["",
              "___________     ",
              "|        /      ",
              "|        \      ",
              "|        /      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               ",
              "|_______________"]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Harry Potter Hangman")
    print("\n".join(stages))

    while wrong < len(stages)-1:
        print("\n")
        print(" ".join(board))
        if len(guessed) > 0:
            print("You have guessed: " + " ".join(guessed))
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                    'o','p','q','r','s','t','u','v','w','x','y','z']
        msg = "Guess a letter "
        char = input(msg).lower()
        while char not in alphabet:
            msg = "Invalid input. Please guess a letter "
            char = input(msg).lower()
        guessed.append(char)
        guessed = sorted(guessed)
        if char in rletters:
            while char in rletters:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
        else:
            wrong += 1
        e = wrong+1
        if "__" not in board:
            print("\n".join(stages))
            print("You win! It was:")
            print("".join(board))
            win = True
            break
        else:
            print("\n".join(stages[:e]))
    if not win:
        print("\n".join(stages))
        print("You lose! It was {}.".format(word))

HPwords = ['accio','aconite','acromantula','alchemy','alohomora','animagus',
           'aparecium','apparate','arithmancy','astronomy','auror','azkaban',
           'basilisk','beater','beauxbatons','bezoar','skrewt','bludger',
           'bowtruckle','broomstick','bubotuber','butterbeer','centaur','charm',
           'chaser','colloportus','cruciatus','deathday','dementor','densaugeo',
           'snare','diffindo','disapparate','disillusionment','dissendium',
           'divination','doxy','dragon','duelling','dungbomb','durmstrang',
           'eeylops','engorgio','evanesco','patronus','expelliarmus',
           'ferula','fidelius','firebolt','flagrate','flobberworm','floo',
           'furnunculus','galleon','ghoul','giant','gillyweed','gnome','goblin',
           'gobstones','gryffindor','gringotts','snitch','grim','grindylow',
           'heliopath','hellebore','herbology','hinkypunk','hippogriff',
           'hogsmeade','hogwarts','honeydukes','elf','howler','hufflepuff',
           'impedimenta','imperius','incarcerous','incendio','kappa','keeper',
           'knut','kwikspell','cauldron','legilimency','mandrake','marauders',
           'merpeople','metamorphmagus','ministry','erised','mobilicorpus',
           'levicorpus','monkshood','mosmordre','muggle','murtlap','nargles',
           'niffler','nimbus','lumos','nox','obliviate','occlumency',
           'ollivanders','omnioculars','owl','parselmouth','parseltongue',
           'pensieve','potion','phoenix','sneakoscope','poltergeist',
           'polyjuice','portkey','protego','pumpkin','deluminator',
           'quaffle','quibbler','quidditch','quietus','sonorus','ravenclaw',
           'reducio','reducto','relashio','remembrall','rennervate','reparo',
           'rictusempra','riddikulus','boggart','salamander','scourgify',
           'quill','seeker','seer','sickle','silencio','skelegro','slytherin',
           'sorting','spellotape','splinching','stupefy','tarantallegra',
           'thestral','transfiguration','triwizard','curse','unicorn',
           'unspeakable','veritaserum','wand','werewolf','wizengamot',
           'wolfsbane','zonkos']

hangman(random.choice(HPwords))
