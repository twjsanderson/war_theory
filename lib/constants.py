import sys

start_up_art = '''              
                /\                         \\    //\\    //    //\\     ||\\\\\\
                ||                          \\  //  \\  //    //==\\    ||\\\\
                ||                           \\//    \\//    //    \\   || \\\\
                ||            
                ||            
                ||            __________    
                ||                ||      ||   ||   ||////    //||\\\\    ||\\\\\\    \\\\  //
                ||                ||      ||===||   ||//     ||    ||   ||\\\\      \\\\//
                ||                ||      ||   ||   ||////    \\\||//    || \\\\      //
          /____________\            
                []            
                []            
                []            
                              
                            '''

start_up_description = '''
    WAR THEORY
    ----------
    Assemble a team of warriors and hold the line against waves of unrelenting orcs 
    seeking to destory your people and their way of life. In this turn based, text adventure 
    you will choose 3 heros to lead the fight against the northern hordes. Unlock new powers
    and call in allies when things get desparate. Finally, kill the orc Chieftain and save 
    the kingdom once and for all. 

    COMMANDS
    ---------
    You can enter '-exit' at anytime to quit the game

    HIT ENTER TO BEGIN

    * Game commands are NOT case sensitive

    CREDITS
    ----------
    Created by twjsanderson (2021)
    Repo - https://github.com/twjsanderson/war_theory
    
'''

story = {
    1 : 
'''
    PART 1 - A Terrible Beginning
    -----------------------------

    Darkness rises from the east just as you enter the city hall. Shouting echos from the auditorium as you remove your cloak.
    
    'They are coming! Right now, from the Northern mountains, orcs march on your gates!', yells a desparate voice from
    the pulpit. 
    
    He looks exhausted, his clothes are covered in dried mud and stained with blood. The man scans the crowd deliriously, his 
    eyes are sunken and crazed. 
    
    'You must believe me!', he screams with even more intensity. The entire audience is now silent and staring in his direction.
    
    The exhuastion seems to be affecting him more now. The fear in his eyes is replaced with helplessness. His tone changes and 
    in a quiet but firm voice, he says...
    
    'My name is Tracon Bim. I am a hunter from the western city of StoneStill. Four days ago, I set out with a party of twenty, 
    of the finest huntsmen in the land, for the Western slopes of the Great Mountains. We reached our destination after 2 days, just 
    as the morning sun broke the night sky. But as soon as we entered the tree line, orcs riding vicious wargs were upon us. We had 
    no time to react. At first there was one and then two, by the time we knew what has happening half our party was dead. Those 
    of us who remained, were driven up the mountain and deep into the forest. Those damn monsters were clever... They surrounded 
    us to prevent our retreat back to the open plains with our horses. Most of us were too slow... but Fat John and I managed to 
    escape the slaughter with two surviving pack horses. We were quickly separated in the dense forest, but all we could do was run. 
    By mid-day my horse was exhausted, she tripped on a tree root and broke her leg, poor thing. I was thrown clear and woke up as 
    just as the sun began to set. In the distance I could hear wargs howling. They were on my trail... I began to run and did not 
    stop until I reached the edge of the Eastern plains. I peered into the darkness of the vast plain, looking for any sign of orc 
    or beast. In one direction I could see the faint light of your great city and in the other I saw lights from the foothills of 
    the Northern range. It was faint, but against the darkness of night, it was like a piercing beacon... I ran. I ran and 
    did not stop until I pounded on the gates of your city. I have no proof to show you with my hands... but I know in my soul 
    that those lights mark an army of death. And it is coming for this city... They are coming-'

    Just then, Ratheon, head of the city guard, approaches the pulpit and gently pulls Tracon away from the stage before
    turning back to address the hall.

    'People of Canrier. I am saddened to say... that this is not the first report we have heard of orc hordes moving south 
    from the reaches of the Great Mountains.', Ratheon proclaims in a clear voice.

    'Good Tracon, is correct in his intuition... Our scouts have just reported movement in the foothills. And confirmed the existence
    of an orc army.'
    
    The whole room begins to stir and panic seems to settle in the villagers around you. Ratheon, stares knowingly at the crowd and 
    raises his hand for silence. 

    'Do not mistake this threat as the end of our city.', Ratheon pauses and looks out at the crowd and at you. 

    'This is city has a secret. A powerful secret that will take more than an army of orcs to overcome... For we house, quietly and
    without fanfare, Heros from the King's War. Hero's whose ability on the field of battle is legendary. They are your neighbours,
    friends and barkeeps. These Hero's are the last remnance of the King's Guard.'

    The crowd gasps as Ratheon strides toward you.

    (Hit enter to continue)
''',
    2:
'''
    What is your Name?  
'''
    # '''
    #     '<name>, Captain of the famed King's Guard, you are again being called to protect your people in their time of need and repel 
    #     the Northern hordes. As was done in the old days, choose two of your best warriors, and meet me in the war room to we prepare for the battle.'
    # ''',
    # '''
    #     'With that, you exit the hall deep in thought. Who among the remaining King's guard should you call to fight by your side...'
        
    #     PALADIN, Ardeer. Fast, strong and fearless. (Strength +2, Hit points +2, Defense +2)
    #     SORCERESS, Quillian. Cunning and powerful. (Strength +4, Hit points +1, Defense +1)
    #     RANGER, Rafe. Precise and quick. (Strength +3, Hit points +1, Defense +2)
    #     MONK, Cathos. Patient, calm and unrelenting. (Strength +1, Hit points +4, Defense +1)
    #     ROGUE, Selwyn. Quiet and deadly. (Strength +2, Hit points +1, Defense +3)

    #     Choose your first companion: 
    # ''',
    # '''
    #     Choose your second companion: 
    # ''',
    # '''
    #     PART 2 - The Battle Begins
    #     -----------------------------

    #     You form up with your chosen companions and enter the war room to plan your strategy.
    # ''',
    # '''
    #     Ratheon greets your party, 
        
    #     'Welcome to the war room <name>, I see you have chosen your companions well. The orcs have moved much faster than we
    #     anticipated. They will be at our gates in a matter of hours. Our walls are weak and old, they will not hold. Our only choice is
    #     to meet them head on. Our troops are mainly retired soldiers, like yourself, and they are no stranger to war. Every one of our 
    #     soldiers is worth at least 3 of theirs on foot. We will spread our forces across 3 fronts and lure them into direct fight.' 
        
    #     He gestures to a large table with figures that represent the town and the invading orc army marching from the North.

    #         N
    #      W -|- E
    #         S
    #             Orc Command                     ++++
                
    #             Wargs                       >>>>>>>>>>>>

    #             Archers           \\\\\\\\\\\\\\     \\\\\\\\\\\\\\   

    #             Infantry    /////////////   /////////////   /////////////  

    #                         ---------------------------------------------

    #             Infantry       ///////         ///////        ///////   

    #             Archers               \\\\\\\\        \\\\\\\\

    #             Canrier Command                 ++++
        
    #     'As you can see they have us out numbered. But I am confident we can hold against them, using our archers to support the
    #     infantry as needed. Our real problem lies with their wargs... If those beasts hit one of our flanks, all is lost. 
    #     Your job will be to lead a small contingent of elite soldiers and meet the wargs where ever they attack. Engage and 
    #     destory them before they route our forces. From there, our army will depend on you to turn the tide and flank the horde
    #     to win the battle.'

    #     'Our scouts and archers will shoot a burning blue arrow in the direction of any warg attack. Watch the skies and be prepared
    #     to move fast. Finally, you will have the aide of a small team of archers to fire on the enemy when you are in dire need of 
    #     assistance. But be warned, arrows are a precious commodity in war, so this attack can only be called once... use it wisely.
    #     May the wings of Aethryn carry you to victory.' 

    #     With that you exit the tower and prepare for battle.
    # ''',
    # '''
    #     Within the hour the army is formed up and ready to fight. Suddenly, the sound of thunder rises from the approaching horde.
    #     Drums fill the air and war chants spill across the open plain. You stand tall amongst the quiet soldiers and yell at the top 
    #     of your lungs: <yell>
    # '''
    # '''
    #     The soldiers around you erupt into war chants, praising the ancients for their sacrifice and praying for a glorious death. 
    #     A horn blows and the army lurches forward to meet the horde in battle. 
    # ''',
    # '''
    #     The orc army charges and slams into the forces of Canrier. The archers fire over the lines, killing as many orc as they can. 
    #     A noise begins to build around you like a whistle, the sky begins to darken and you instinctively crouch to one knee and raise
    #     your shield. You yell at the top of your lungs, 'Arrows! Find cover!'

    #     You companions are already shielding themselves from the barrage, yet three soliders to your left are still pierced by arrows... 
    #     they were too slow.
    # ''',
    # '''
    #     To the east you see a bright blue arrow streaking through the sky. Wargs are attacking the eastern flank. You rally your unit and
    #     charge into the fight.
    # ''',
    # '''
    #     You dive into combat without slowing your pace by an inch. The wargs are already ripping through soldiers as you enter the fray. You
    #     form up with you companions and begin the fight.
    # ''',
    # ''' 
    #     A warg attacks you head on.
    # '''
}

# game_options = {
#     1: {
#         'dd': 'yup'
#     },
#     2: {
#         '': ''
#     },
#     3: {

#     },

#     '': '',
#     'exit': sys.exit
# }

