print("-----------------------Downfall of the Demonic Stronghold-----------------------")
# This is only a trial game. I'm just showing how I collect user input and return a response based on that data. I will make a
# slightly better version using Branching and Functions and While Loops.
print('''key words/phrases to play this game:
- main gate
- attack
- proceed
- left
- engage
- proceed
- kill
- portal
- eliminate
- fight
- kill
- spare
- surround
- retreat
- leave alone
- regroup
- right
- slay or Slay
- find alternative route
- sewers
- Are you not entertained? or are you not entertained?

Good Luck and may the Ancient Gods be by your side!!''')

print("\nYou start off in a courtyard inside the Demonic Stronghold which you and your legion of Sentinel Warriors are"
      "\nattacking. There is a main gate in front of you and a sewer somewhere off to your left. How should you proceed?:")

choice = input("> ")

if choice == "main gate":
    print("You walk through the main gates and up some stairs straight after. A few minutes later you are now inside "
          "\nthe Demonic Citadel at the very heart of the Stronghold. You see two demonic warriors in front of you."
          "\nAs you unsheathe your Sentinel axe, you ready yourself for a battle. What do you do?:")
    sub_choice1 = input("> ")
    if sub_choice1 == "attack":
        print("With all your Sentinel strength, you dispatch the two demonic warriors with ease. The path is now clear"
              "\nahead. Do you proceed forward or find an alternate route?:")
        sub_choice2 = input("> ")
        if sub_choice2 == "proceed":
            print("You move forward. The Citadel becoming more sinister than ever. Suddenly, a massive chandelier falls"
                  "\nfrom the ceiling 100 feet above your location. The path is now blocked. There are two corridors to"
                  "\nyour left and right. How should you proceed?:")
            sub_choice3 = input("> ")
            if sub_choice3 == "left":
                print("You go left. Down this corridor, there is a slim stairwell ahead of you. You go forth up the"
                      "\nstairwell and in no time, you reach the second floor. But the Sentinels begin to storm the"
                      "\nCitadel. A horde of demonic warriors appears in front of them and engages them in combat.")
                print("\nYou look to your left, along the upper floor of the Citadel, you see a big and bulky demon towering"
                      "in front of you, ready to attack. What do you do?:")
                sub_choice4 = input("> ")
                if sub_choice4 == "engage":
                    print("You run towards the demonic brute as he charges at you. With one swipe of your lethal"
                          "\nSentinel axe, you slice him in two. The way ahead is now clear. How should you proceed?:")
                    sub_choice5 = input("> ")
                    if sub_choice5 == "proceed":
                        print("You move deeper into the Citadel, to the backend. As you peer over the edge on your right,"
                              "\nyou see a Summoner below you who looks to be summoning these warriors directly from Hell."
                              "\nDo you wish to kill the Summoner or leave him alone?:")
                        sub_choice6 = input("> ")
                        if sub_choice6 == "kill":
                            print("You leap down from the ledge and plummet down towards the Summoner. He looks up, his"
                                  "\nface widens with fear as you land upon him, flattening him entirely but leaving a"
                                  "\npatch of blood behind.")
                            print("\nThe Sentinel Warriors overrun the enemy and rejoin behind the alter. A portal opens"
                                  "\nup on the wall to your left which is directly opposite the main entrance where you"
                                  "\nentered the Citadel. What do you do?:")
                            sub_choice7 = input("> ")
                            if sub_choice7 == "portal":
                                print("You and your Sentinel Warriors go through the portal and arrive in a demonic"
                                      "\nchamber deep underneath the Stronghold. There is a fleshy substance ahead of you"
                                      "\nsurrounded by a group of cultists and the Stronghold commander. How should you"
                                      "\nproceed?:")
                                sub_choice8 = input("> ")
                                if sub_choice8 == "eliminate":
                                    print("You lead your Sentinel force against the last vestiges of the Demonic"
                                          "\nStronghold. You hack and slash your way through multiple ways of enemies until"
                                          "\nyou get to the very end of the chamber, where the Stronghold commander is waiting"
                                          "\nfor you.")
                                    print("\nAs he readies his Argent weapon of choice, you ready your Sentinel axe and"
                                          "prepare to engage. How should you proceed?:")
                                    final_choice1 = input("> ")
                                    if final_choice1 == "fight":
                                        print("You charge towards the Stronghold commander and clash your weapons together"
                                              "\nthe noise echoeing throughout the chamber. Later on, you knock the Stronghold"
                                              "\ncommanders' weapon out of his hand, clattering against the far wall and"
                                              "\nsmashes to pieces. He kneels at your feet, begging for mercy.")
                                        print("\nDo you wish to spare his life or kill him?:"
                                              "\n\nWARNING: This choice will determine your fate with Sentinel Prime. Be careful"
                                              "\nwhat you choose!!")
                                        final_choice2 = input("> ")
                                        if final_choice2 == "kill":
                                            print("You execute him!! VICTORY")
                                        elif final_choice2 == "spare":
                                            print("You lower your Sentinel axe but the Stronghold commander sees this"
                                                  "\nas a sign of weakness and produces a small knife. He lunges at you"
                                                  "\nand impales you in the neck, blood splattering everywhere.")
                                            print("\nDEFEAT")
                                        else:
                                            exit(0)
                                elif sub_choice8 == "surround":
                                    print("You and your Sentinel forces attack the cultist and Stronghold commander in the"
                                          "\nchamber. Soon later, you and your forces overrun them and have them surrounded."
                                          "\nThey are outnumbered and surrender immediately.")
                                    print("\nVICTORY")
                                else:
                                    exit(0)
                            elif sub_choice7 == "retreat":
                                print("Just before you go through the portal, the wall behind it falls away, the portal"
                                      "\nclosing up. A Titan rears up and roars at you and your Sentinel legion. As you turn"
                                      "\nand retreat back out of the Citadel, the Titan seals you inside with a ring of fire."
                                      "\nAs the Titan stomps towards you, you know you have met your end.")
                                print("\nDEFEAT")
                            else:
                                exit(0)
                        if sub_choice6 == "leave alone":
                            print("You leave him alone. As you turn and walk away, he summons a group of blaster soldiers"
                                  "\nthat outnumber you within seconds.")
                            print("\nDEFEAT")
                    if sub_choice5 == "regroup":
                        print("As you turn to regroup with your Sentinel legion, you feel a slight hesitance about you."
                              "\nYou venture outside and you see you Sentinel force suddenly retreating or some reason."
                              "\nYou look around you, trying to spot anything that would tell you why your forces are retreating.")
                        print("Soon enough, a Sentinel warship begins its assault on the Stronghold. Using its cannons,"
                              "\nit fires upon the Stronghold, killing everything in its path. You stand at the Citadel watching"
                              "\nthis happen as it approaches you. The Sentinel warship's cannons begin targetting you but"
                              "\nknowing your status among the Sentinel Prime, you tell them you are King Novik and the warship"
                              "\ninstead targets the Citadel behind you, destroying everything.")
                        print("However, the Stronghold may now be destroyed, but its commander still lives.")
                        print("\nDEFEAT")
            elif sub_choice3 == "right":
                print("You go right. Down this corridor looks to be a dead end but to the left is a secret corridor."
                      "\nApproaching it, you inadvertently step on a trap. You hear it ticking away as you dive into the"
                      "\nsecret corridor. It explodes, sealing you inside.")
                print("You can only forward now. You reach the end of the corridor and approach a door. It push it open"
                      "\nand you come into a small room with a demonic figure standing in front of you, facing in the opposite"
                      "\ndirection. What do you do?:")
                easter_egg = input("> ")
                if easter_egg == "slay":
                    print("You ignite your Sentinel axe and raise it above your head. The demonic figure whirls round,"
                          "\nrevealing his identity. You glare into his eyes and say: 'Hell Priest!!'. With one swing, you"
                          "\nlob off the Hell Priest's head, blood squirting out of the stump of the neck like a strong in"
                          "\na hot beverage. The body falls to the floor, its staff clatter to the ground.")
                    print("\nSECRET REVEALED!! Good Job")
            else:
                exit(0)
        elif sub_choice2 == "find alternative route":
            print("As you turn and find an alternative route to try and through the demons off balance, a Summoner at the"
                  "\nopposite end of the Citadel summons a Fallen Angel. Using its divine powers, it strikes at you, leaving"
                  "\nyou no time to react. You are disintegrated, leaving behind only your helmet and Sentinel axe")
            print("\nKILLED IN BATTLE")
        else:
            exit(0)
elif choice == "sewers":
    print("You take the sewers. As you venture through the sewers towards the Demonic Citadel at the heart of the Stronghold,"
          "\nyou can see a ladder up ahead of you. Pace increasing, as you start running towards the ladder, you suddenly"
          "\nstep on a hidden grate and plummet into an unknown area below.")
    print("Before you do anything you see a figure in black standing on a ledge overlooking the area. The figure clicks"
          "\nhis fingers and summons a unique demonic warrior. As it turns out, you are in an Arena of some sort. The unique"
          "\ndemonic warrior ignites its axe, swings it once then twice before charging at you. With very little time to"
          "\nreact, you ignite yours and parry the warriors' axe away. With one retaliatory swipe, you slice off his arm,"
          "\nleaving him weakened. How do you do this?:")
    easter_egg2 = input("> ")
    if easter_egg2 == "Are you not entertained?" or "are you not entertained?":
        print("You execute the warrior! The crowd cheers in your name and now the Stronghold above is now under your"
              "\ncontrol.")
        print("\nSECRET REVEALED!! Good Job")
else:
    exit(0)
