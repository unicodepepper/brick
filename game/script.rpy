init:
    python:
        #item declarations go down here
        blue_key=thing( name="Blue key",
                        description="Just a regular key.",
                        image="key_%s.png",
                        action="key")
        music_player=thing( name="music player",
                            description="A portable music player.",
                            image="key_%s.png",
                            action="music_player")
        wet_paintbrush=thing(   name="wet paintbrush",
                                description="A paintbrush. It's wet.",
                                image="key_%s.png",
                                action="wet_paintbrush")


default events = {  "home":None,
                    "courtyard":None,
                    "labo":None,
                    "track":None,
                    "studio":None}

default currplace= "home"

default connections={     "home":["courtyard"],
                          "courtyard":["home","labo","track","studio"],
                          "labo":["courtyard"],
                          "track":["courtyard"],
                          "studio":["courtyard"]}

default listeningToMusicPlayer = False


label bgshow:
    scene timebg with dissolve
    show timebg:
        zoom 1280 #TODO fix so that the colors represent the time
        linear 0.5 xalign clockint/4.0

    show expression "bg "+currplace as bg
    with dissolve
    return


define b = Character("{color=#f0f}blessed{/color}")
define c = Character("{color=#ff0}charmed{/color}")
define h = Character("{color=#0ff}hexed{/color}")
define s = Character("{color=#fff}strange{/color}")




label start:
    $events["labo"] = "hexed_intro"
    $events["track"] = "charmed_intro"
    $events["studio"] = "blessed_intro"
    call bgshow
    call time_advance
    s "I'm a writer."
    s "I write things."
    s "And yet, I don't write things."
    s "It's been a long time since the last time I put my thoughts to paper. I can't remember when it was."
    s "If there was some sort of writing license I had to renew, it would have surely expired by now."
    s "But it's okay right?"
    s "It's okay to wait for motivation, or inspiration."
    s "I make up for it by enjoying my time, anyways."
    s "After all, time that you enjoy spending is well spent."
    s "Is that right?"
    menu:
        "Is that right?"
        "Yes, I'm doing the best I can right now.":
            $firstvisit = "charmed"
            "That's right."
            "I don't have to stress so much. I should let things come by naturally instead."
            "Instead of just focusing on results, I should focus on myself and let results come."
            "Broken window theory."
            "I should take care of myself, and in turn, myself will take care of me."
            "...or something like that."
            "Maybe it would be a good idea to start by doing exercise."
            "There aren't any close places where I could do that, other than the running track in the courtyard."
            "Maybe I should head over there."
        "No, I really could do much better.":
            $firstvisit = "blessed"
            "..."
            "No, the fuck it's not!"
            "I haven't done anything useful or productive in the last few days."
            "I'm so frustrated with myself."
            "The only way I can turn that around is by actually doing something with my future time."
            "I want to write."
            "I want to make art."
            "..."
            "Maybe it would be a good idea to visit the art studio that's on the courtyard."
            "I'll hopefully find motivation over there."
        "No, but I should just stop trying anyways.":
            $firstvisit = "hexed"
            "Whatever. Worrying about it will just make me more stressed, and I don't want that."
            "I should just enjoy my time."
            "If it's meant to happen, it will happen."
            "I should do something productive in the meanwhile."
            "Maybe I'll go visit the computer lab that's on the courtyard."
            "One of my friends spends all their time there."
            "I don't know for sure what I'll do, but I'm sure it will be good."
    jump mainloop

label home:
    $currplace="home"
    return

label courtyard:
    $currplace="courtyard"
    return

label labo:
    $currplace="labo"
    return

label track:
    $currplace="track"
    return

label studio:
    $currplace="studio"
    return



label key:
    "you have a super secret key"
    return
label music_player:
    if listeningToMusicPlayer:
        "you took the music player off"
        $ listeningToMusicPlayer = False
    else:
        $ listeningToMusicPlayer = True
        "you put on the music player"
        "dun durun dun dun"
        "you just heard some music"
    return
label wet_paintbrush:
    "You hold the paintbrush."
    "It's wet."
    return
