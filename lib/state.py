state = {
    'character_ids': [],
    'hero': None,
    'companion': None,
    'monsters': {
        'easy': [],
        'hard': [],
        'boss': []
    },
    'battle_step': 'easy',
    'in_battle': False,
    'path': None,
    'story': [
        {
            'view': 
            '''
                PART 1 - A Terrible Beginning
                -----------------------------

                Darkness falls from the east just as you enter the Great Hall. Shouting echos from the auditorium as you remove your cloak.
                
                'They are coming! Right now, from the Northern mountains, orcs march on the gates!', yells a desperate voice from
                the pulpit. 
                
                He looks exhausted, his clothes are covered in dried mud and stained with blood. The man scans the crowd deliriously, his 
                eyes are sunken and crazed. 
                
                'You must believe me!', he screams with even more intensity. The entire audience is now silent and staring at him.
                
                The exhuastion seems to be affecting him more now. The fear in his eyes is replaced with helplessness. A tall man dressed 
                in fine robes gently pulls him aside, embraces him and whispers something in his ear.

                A moment later two clerics escort the shaken man out of the hall.

                The robed man is known to everyone in the Hall, he is Vilroy, First Assistant to the King. 
                
                Vilroy takes the pulpit and begins to speak, 
                
                'Dear friends; subjects of our wise and mighty King, Edward III, what that poor, exhausted individual has said is true.
                As of right now, there is an army of 10,000 orcs riding from the North to destory our city and all its inhabitants. The 
                King has declared a state of war. As I speak our soldiers are mobilizing along the city walls.'

                Vilroy pauses to let his words sink in and then continues,

                'Ergo, it is the King's wish that all who cannot fight must barricade themselves in the High Keep for protection. To all
                soldiers and able bodied citizens, please report to the Main Gate to be armed for battle. I know this may seem like a 
                bleak day but do not fall into despair, for the King has a powerful weapon to defend us against such a threat.'

                Again, Vilroy pauses and looks out into the crowd until his eyes land on you...

                He points and says, 'The King's Guard.'

                The crowd turns and begins to murmur. 

                (Hit enter to continue)
            ''',
            'actions': ['DISPLAY_VIEW', 'GET_INPUT'],
            'validations': []
        },
        {
            'view': 
            '''
                PART 1 - continued
                -----------------------------

                What is your Name?
            ''',
            'actions': ['DISPLAY_VIEW', 'GET_INPUT', 'CREATE_HERO'],
            'validations': ['VALID_LEN']
        },
        {
            'view': 
            ''' 
                PART 1 - continued
                -----------------------------

                Vilroy continues,

                '{name}, Captain of the King's Guard, the legendary warrior and killer of the Blue Dragon will lead the King's Guard to
                save our city and protect our King. He calls on you once again Captain, to take up your mantle and do your duty.
                Will you heed the call?'

                A hush settles over the crowd...

                Y. 'I hear the call of our king and his people in this time of need and I am ready to serve and protect!'
                N. 'You got the wrong guy! I am but a simple merchant who merely looks like a hero. In truth I am but a coward!'

                (Enter Y to continue or N to exit the game)
            ''',
            'actions': ['DISPLAY_VIEW_WITH_HERO_NAME', 'GET_INPUT'],
            'validations': ['Y_OR_N']
        },
        {
            'view': 
            ''' 
                PART 1 - continued
                -----------------------------

                The crowd cheers! Knowing that with the infamous King's Guard behind them, they cannot lose. 

                You salute Vilroy and exit the Great Hall.

                (Hit enter to continue)
            ''',
            'actions': ['DISPLAY_VIEW', 'GET_INPUT'],
            'validations': []
        },
        {
            'view': 
            ''' 
                PART 2 - Battle Plans
                -----------------------------

                You burst into the Hall of War. The King and his most trusted advisors circle a large table covered in maps. 
                They look up in unison as you appraoch. The King grins and says, 'Captain, you have arrived. And not a moment 
                too soon. We are preparing a defense of the city against the our sworn enemies. We have been tracking their
                movements in secret for weeks. General Malnor has devised a brilliant plan to not only defend the city but
                destory the orc horde for good!'

                The King turns to Malnor, 'Tell him of his role.'

                'Yes my liege.', Malnor responds. 
                
                He turns to you and says, 'I have fortified each tower and barricaded every entrance to the city. We have
                enough rations for 60 days and 3 companies of archers to keep the Orcs at bay for the time being. But this 
                will not save us. We must strike when the time is right, so the The Grand Wizard has prepared a powerful 
                spell that will instantly send fear through the entire Orc army. The simple minded grunts will retreat as we
                bombard them with arrows from our archers and boulders from our ballistas. This will give our soldiers time 
                to enter the battle field and run down their fleeing army.

                But this will not win us the day... The Orcs still out number us 6 to 1, they are twice the size of our 
                largest foot soldier and they will quickly reorganize. Their Chieftain, Ogthar, is not so weak... He will 
                rally them quickly and violently. If they reform their lines we are doomed.'

                The King quickly intercedes, 'Our plan can only succeed if the Chieftain and his Lieutenants are dead. 
                We cannot allow them to rally the horde once they are in retreat. You are hereby commanded to track down 
                and kill them before the Dawn breaks and our army attacks."

                Malnor pushes a large piece of parchment towards you.

                'Our scouts have constructed a map of the enemy position. We have laid out two paths to your prey. 
                Neither will garauntee you success but they will give you a fighting chance to get within striking 
                distance of Ogthar and his Lieutenants. Study it well and choose your path.' 

                _____________________________________________________________________________________
               |                  \__________________________________________/                       |
               |    1. *                          | Main Gate |                         2.*          |
               |      *                           |___________|                            *         | 
               |     *                                                                      *        | 
               |    *                                                                        *      /|
               |   *                                                                          *    / |
               |  *                                                                            *  /  |
               |\*                                                                              */   |
               |*\          | Wargs |    | Wargs |     | Grunts |     | Grunts |    | Grunts |  /*   |
               |* \                                                                            /  *  |
               | * \                                                                          /   *  |
               |  * \                                                                        /    *  |
               |   * \   | Archers |    | Archers |   | Archers |   | Berserkers |          /     *  |
               |Trees |                                                                    |  Trees  |
               |     / *                                                   | Berserkers |  |      *  |
               |    /   *                            | Chieftain |                          \     *  |
               |   /      * * * * * * * * * * * * * X              X * * * * * * * * * * * * \* * *  |
               |  /                                                                           \      |
               |_/_____________________________________________________________________________\_____|

                1. The first path leads past Wargs and Archers.
                2. The second path leads past Grunts and Berserkers.
                
                (Enter 1 or 2 to continue)
            ''',
            'actions': ['DISPLAY_VIEW', 'GET_INPUT', 'SET_MONSTERS'],
            'validations': ['1_OR_2']
        },
        {
            'view':
            '''
                PART 2 - continued
                -----------------------------

                'With that, you exit the hall deep in thought. Who among the King's guard you will call to fight by your side...'
                
                1. PALADIN, Thrack. Fast, strong and fearless.
                2. SORCERESS, Quill. Cunning and powerful.
                3. RANGER, Rafe. Precise and quick.
                4. MONK, Cathos. Patient, calm and unrelenting.
                5. ROGUE, Selwyn. Quiet and deadly.

                Choose your companion (by number)
            ''',
            'actions': ['DISPLAY_VIEW', 'GET_INPUT', 'CREATE_COMPANION'],
            'validations': ['IS_1_TO_5']
        },
        {
            'view':
            '''
                PART 2 - continued
                -----------------------------

                You know where the King's Guard will be at a time like this... preparing for battle in the Hall of Might.
                As you open the iron doors to their infamous barracks, you immediately hear the distinct sounds of swords
                being sheathed, armour clasped and bows strung. You round the corner and behold the members of the mighty 
                King's Guard... readying for war. 

                You quietly scan the room and your eyes land on {name}, who is standing silently, ready and primed for battle.

                '{name}, with me.', you say firmly. 

                They stride to your side without hesitation.

                Staring directly at your new companion you issue your first command,
                
                'You will be my companion for this battle. We will fight as one, an unseparable thing, an extension of the 
                King's Will. Our goal is simple, find the Orc Chief and kill him before the army can breach the walls.' 
                
                'As you command, it will be done. For kin and King!', {name} yells as the remaining Guard begin to cheer.

                You turn to address the remaining Guard,
                
                'The rest of you will report to the main gate and fulfill your mandate.'

                In unison the King's Guard chant, 'Protect the King, Kill our enemies!'

                With that, you call for your armour and sword. Once armed, you exit the Hall with {name} and head for the front.

                (Hit enter to continue)
            ''',
            'actions': ['DISPLAY_VIEW_WITH_COMPANION_NAME', 'GET_INPUT'],
            'validations': []
        },
        {
            'view':
            '''
                PART 2 - continued
                -----------------------------

                You quickly move to the West side of the castle and turn down a muddy alley filled with barrels and broken stone.
                The light and noise fade as the street begins to narrow. The massive castle wall to your left looks completely solid
                until you notice a small blemish on the wall and stop. After a closer look you confirm it is a symbol of the Snake 
                God Siryen. 

                Good, you are in the right place. {name} takes watch while you pull out a small leather book adorned with the
                same symbol. You quietly say the magic words,

                'Sylvan ne Sondare quant valis on snayth'.

                A thin blue light appears in the form of a large rectangle around the symbol...

                ________________
                |      _       |
                |     / \      |   
                |     \//      |
                |      /       |
                |              |
                |              |
                |              |

                {name} turns to you with a smrik and says, 'Still works after all these years. 
                Let's go!', and then jumps through the seemingly solid wall to the otherside.

                Do you follow?

                Y. Hell yeah, let's go!
                N. No way! Things are getting too intense, run away and save your own skin!

                (Enter Y to continue or N to exit the game like a coward)
            ''',
            'actions': ['DISPLAY_VIEW_WITH_COMPANION_NAME', 'GET_INPUT',],
            'validations': ['Y_OR_N']
        },
        {
            'view':
            '''
                PART 3 - To Battle
                -----------------------------
                
                You slip across the plains under cover of darkness towards the forest. In the
                distance you see camp fires and hear the movements of your enemies from around the
                battlefield.

                IMAGE

                After carefully following the silhouette of a small hill you see the tree line...
                The coast looks clear and you make your move.

                (Hit enter to continue)
            ''',
            'actions': ['DISPLAY_VIEW', 'GET_INPUT'],
            'validations': []
        },
        {
            'view':
            '''
                PART 3 - continued
                -----------------------------
                
                Just before you enter the trees a growl escapes from the darkness.

                A group of {monsters} emerge from the dark forest ready to fight! 

                (Hit enter to start the battle)
            ''',
            'actions': ['DISPLAY_VIEW_MONSTER_NAME', 'GET_INPUT'],
            'validations': []
        },
        {
            'view':
            '''
                PART 3 - continued
                -----------------------------
            {text}
                Choose your action (by number)
            ''',
            'actions': ['DISPLAY_VIEW_FIRST_BATTLE', 'GET_INPUT', 'HANDLE_SURPRISE_ATTACK'],
            'validations': ['1_OR_2']
        },
        {
            'view':
            '''
            PART 3 - continued
            -----------------------------
            
            The remaining {monsters} howl in unison, enraged by the death of there companion. 

            Your companion looks at you and says, 'Do you want them or shall I?'
            
            1. You want the glory! (Attack)
            2. Let your companion have some fun (Let your companion Attack)

            Choose your action (by number)
            ''',
            'actions': ['DISPLAY_VIEW_MONSTER_NAME', 'GET_INPUT', 'DISPLAY_END_FIRST_BATTLE'],
            'validations': ['1_OR_2']
        },
        {
            'view':
            '''
            PART 4 - Across the Battlefield
            -----------------------------
            
            You and {name} make your way to the edge of the forest. It won't be 
            long until a scout finds the bodies you left behind...

            Across the plain you see the next encampment of orcs. Some how you 
            have to get passed them without raising the alarm.

            Just then, {name} taps your shoulder and points South.

            There is a field out boulders just big enough to hide creatures roughly
            the size of a human. You spy an obvious path that will hide 
            your silouettes from preying eyes...

             _____________________________________________________________________
            |          ______                                                     |
            |         /      \                x                    ________       |
            |        /        |               x                   /        |      |
            |        |        |               x                  /         |      |
            |         \       |               x                 /          |      |
            |      ____\_____/_____           x                /           |      |
            |                                 x      _________/____________|_____ |
            |                     ____         x                                  |
            |                    /    \         x                                 |
            |                    |     |         x                                |
            |                   /      |          x                               |
            |                  /       |          x                               |
            |             ____/________\____      x                               |
            |                                     x                               |
            |_____________________________________________________________________|
            
            It looks like your only chance to sneak around the army...

            (Hit enter to cross the field)

            ''',
            'actions': ['DISPLAY_VIEW_WITH_COMPANION_NAME', 'GET_INPUT'],
            'validations': []
        },
        {
            'view':
            '''
            PART 4 - continued
            -----------------------------
            
            {name} follows behind as you wind through the massive boulders. 

            Weapons at the ready, you are prepared for a surprise attack
            at any moment...

            You deftly sweep from one boulder to the next, finding cover
            where ever you can. Finally, you reach the shelter of a mammouth, 
            20 foot tall rock, and wait in the shadows.
            
            At first, there is nothing but the wind and the sway of the grass. 
            In the distance, you hear the movement of orc troops preparing for 
            their assault. 

            You remain quiet, focused, listening...

            Not 50 feet from your hiding spot, you hear it. The crackle of 
            leather being tightened, metal clinking, followed by a low grunt. 

            The enemy is waiting...

            There is no time to lose, you signal {name} to cut left, behind the
            rock while you charge them head on.

            (Hit enter to begin your attack)

            ''',
            'actions': ['DISPLAY_VIEW_WITH_COMPANION_NAME', 'GET_INPUT'],
            'validations': []
        },
        {
            'view':
            '''
            PART 4 - continued
            -----------------------------
            
            There is no time to lose, do you charge with a shield bash, slamming
            into what ever waits for you around the bend?

            Or pull your sword and cut down the first thing you see?

            1. Shield bash!
            2. Chop them in half with your sword!

            Choose your action (by number)

            ''',
            'actions': ['DISPLAY_VIEW', 'GET_INPUT', 'CHOOSE_WEAPON'],
            'validations': ['1_OR_2']
        },
        {
            'view':
            '''
            PART 5 - The final battle
            -----------------------------
            
            You and {name} make it to the last rock large enough for cover in the
            boulder field.

            In the distance you see a massive fire and a battle hall made of tents.
            You can see the orc Chieftain's sigil on banners flying high around the 
            camp.

            The sky is beginning to lighten... it is almost dawn. 
            
            Your time to attack is nearly at hand.

            (Hit enter to continue)
            
            ''',
            'actions': ['DISPLAY_VIEW_WITH_COMPANION_NAME', 'GET_INPUT'],
            'validations': []
        },
        {
            'view':
            '''
            PART 5 - continued
            -----------------------------
            
            Suddenly a horn blows and armoured Orc Captains stream out of the main
            tent.

            They are chanting in unison... the final battle is about to begin.

            As they split off toward their respective units, three final beasts 
            emerge. Giant orcs covered in spikes and black armour.

            It is Ogthar and his Lieutenants. 

            Both Lieutenants carry massive war hammers, while Ogthar carries a 
            deadly axe.

            They stop and scan the battlefield. Ogthar looks to the East just as 
            the sun spills out over the plains. He nods to his first Lieutenant.

            The giant orc pulls out a vicious looking bow, lights an arrow on 
            fire and shoots it high into the sky above the orc forces.

            A moment later, a chorus of roars roll across the plains as every orc
            unit advances in union.

            This is your moment!

            Do you attack head on or sneak up behind them to land your first blow?

            1. Head on, let's get some!
            2. They are pretty big... let's catch them off guard.

            Choose your action (by number)
            
            ''',
            'actions': ['DISPLAY_VIEW', 'GET_INPUT', 'DISPLAY_LAST_BATTLE_START'],
            'validations': ['1_OR_2']
        },
        {
            'view':
            '''
            PART 5 - continued
            -----------------------------
            
            In a rage, Ogthar roars at the top of his lungs and charges! His remaining 
            Lieutenant bounds along beside him aiming right for you.

            You stand strong, ready to parry and counter attack at the last possible
            moment. But then suddenly both monsters turn in union away from you, towards
            {name}. 

            With blazing speed they are suddenly upon your weakend companion. As Ogthar 
            rends {name}'s head off with his axe, the hammer wielding Lieutenant
            splatter's {name}'s body to the ground.

            They turn to you and begin to laughing with deep gutteral breaths.

            'You will die now small thing!', yells Ogthar as they begin to circle you.

            (Hit enter to continue the battle)
            
            ''',
            'actions': ['DISPLAY_VIEW_WITH_COMPANION_NAME', 'GET_INPUT'],
            'validations': ['']
        },
        {
            'view':
            '''
            PART 5 - continued
            -----------------------------
            
            Rage fills your body, heat rising to the surface of your face. You are about
            to explode when you stop.

            You take a deep breath, collect your focus and remember the mission. It is
            almost time.

            From your defensive stance you explode into the air toward Ogthar's 
            final Lieutenant. You throw your shield at his face, obscuring your next
            move. He easily bats it out of the way, making just enough space for you to 
            plunge the tip of your sword through his chest. You impale him into the ground 
            as you land on his lifeless body.

            Ogther pulls away and roars once again, ready to fight.

            You look passed his right shoulder and see a blue light erupt from the castle
            walls in the distance.

            The spell has been cast.

            Time to finish the mission!

            You charge Ogthar, knowing that he will try to cut you in half with a single 
            swing.

            The monster's axe comes down towards your head with incredible speed, but you
            deflect it by just enough.

            You counter with a swing at his abdomen but the old Orc parrys and catches you
            in the faces with the butt of his axe. 

            Blood spurts from your mouth as you fall backward. The axe blade is coming again.

            You roll left and it misses your shoulder by an inch. Ogthar is strong and fast.

            But he is still an Orc... 

            (Hit enter to end the battle)
            
            ''',
            'actions': ['DISPLAY_VIEW', 'GET_INPUT'],
            'validations': ['']
        },
        {
            'view':
            '''
            PART 5 - continued
            -----------------------------
            
            You grab your final hidden throwing knife from your left boot and wait till Ogthar 
            is almost in range. You launch it into the sky with every ounce of your strength.

            The beast stops short and looks up, bewildered.

            You close the final distance and swing hard across your body. Ogthar turns his axe
            and both blades lock together. You are now in a shoving contest with an Orc 
            Chieftan.

            Ogthar smiles and roars in your face confidently. You can feel his massive body 
            lurch backward just before he launches you off your feet.

            You pivot your back foot and twist as Ogthar thrusts his shouldered forward. As
            you twist, the momentum takes him past you, your blades still locked in a steely 
            embrace.

            Ogthar has overshot, and just as his body is passing yours, the dagger glints in the
            air above him on its way back to earth. You release your right hand from your sword 
            as you twist, letting the Orc pass unimpeeded and catch the dagger from the air 
            plunging it into his neck.

            You twirl away with precision, immediately comming back to a fighting stance with 
            two hands on your sword.

            Purple blood spurts from the wounds as Ogthar screams and turns to face you. He limps
            covering the grevious wound with his hand. He roars in desparation and charges you.

            You dash forward, ducking his lazy attack and cutting his belly open in one swing.

            Ogthar collapses, breathing heavily, leaking onto the battle field. A moment later
            his chest is still.

            In the distance, the Orc army is in dissary, they are turning on themseleves and 
            the human army is cutting them down as they panic. 

            No help will come. The Orc threat is no more.

            (Hit enter to continue)
            
            ''',
            'actions': ['DISPLAY_VIEW', 'GET_INPUT'],
            'validations': ['']
        },
    ]
}
