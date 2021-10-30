import sys
from story import *
from character_module.character import *

game_state = {
    'player': '',
    'heros': [],
    'enemies': [],
    'ally': 'ally choice',
    'boss': 'boss type',
    'default': {
        '-exit': sys.exit,
        '-help': 'Enter -exit to quit the game, Hit enter to continue from where you left off.'
    },
    1 : {
        'story_point': '',
        'responses': {
            '': 2,
        }
            
    },
    2 : {
        'story_point': story[0],
        'responses': {
            '': 3,
        }
            
    },
    3 : {
        'story_point': story[1],
        'responses': {
            4: 4
        }
            
    },
    4 : {
        'story_point': story[2],
        'responses': {
            5: 5 
        }
            
    },
    5 : {
        'story_point': story[3],
        'responses': {
            6:6
        }    
    },
    6 : {
        'story_point': story[3],
        'responses': {
            7:7
        }
            
    },

    
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
