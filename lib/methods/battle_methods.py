import os

class Battle_Methods:
    def __init__(
        self,
        state,
        curr_step,
        curr_input
    ) -> None:
        self.state = state
        self.curr_step = curr_step
        self.curr_input = curr_input
        self.hero = state['hero']
        self.companion = state['companion']
        self.monsters = state['monsters']

    def display_view_monster_name(self):
        if self.monsters[0] == 'WARGS' or self.monsters[0] == 'GRUNTS':
            print(self.curr_step['view'].format(monsters=self.monsters[0]))
        else:
            print(self.curr_step['view'].format(monsters=self.monsters[1]))

    def display_view_first_battle(self):
        result = ''
        if self.monsters[0] == 'WARGS':
            result = result + '''
                One of the beasts on your left charges in a maddened rage, split flying from 
                its mouth, the creature opens its mouth!

                What do you do?!

                1. Dodge the sudden attack
                2. Strike the Warg before it lands a blow
            '''
        if self.monsters[0] == 'GRUNTS':
            result = result + '''
                A grunt on your left charges in a maddened rage, split flying from 
                its mouth, it raises an axe to strike you down!

                What do you do?!

                1. Dodge its attack
                2. Strike the Orc before it lands a blow
            '''
        print(self.curr_step['view'].format(text=result))

    def set_monsters(self):
        choice = self.curr_input
        if choice == '1':
            self.monsters = ['WARGS', 'ARCHERS']
        if choice == '2':
            self.monsters = ['GRUNTS', 'BERSERKERS']
    
    def handle_surprise_attack(self):
        choice = self.curr_input
        result = '''
            PART 3 - continued
            -----------------------------
        '''
        if choice == '1':
            result = result + ''' 
            You leap out of the way, but don't quite make it!
            
            Lucky for you, the attack harmlessly grazes off your armour.
            You snap out your sword, quickly turn and decapitate the beast
            in a single stroke.

            (Hit enter to continue)
            '''
        if choice == '2':
            result = result + '''
            Good call!

            You pull out your sword and charge the beast head on, stabbing it 
            through the heart.

            (Hit enter to continue)
            '''
        print(result)
        # catch input
        input('>>> ')
        os.system('clear')
        # exit logic?
        self.curr_input = ''

    def display_end_first_battle(self):
        choice = self.curr_input
        result = '''
            PART 3 - continued
            -----------------------------
        '''
        if choice == '1':
            result = result + '''
            You charge the remaining creatures moving faster than any of them 
            thought possible. Your sword cuts through the face of the closest 
            beast and the last attacks while your back is turned. 
            
            But you dive side ways before it is in range and throw a dagger 
            that was hidden in your left boot. 

            The metal penetrates the middle of the disgusting creatures' 
            forehead, instantly killing it. 

            And with that, the first battle is over.

            (Hit enter to continue)
            '''
        elif choice == '2':
            companion_name = self.companion.get_name()
            monster = self.monsters[0].lower()
            action_dict = {
            'Thrack': f'''
            Thrack unsheaths his sword and strides toward his prey.
            The {monster} charge him with a horrible roar!

            He stops and raises his shield. The first enemy slams into him
            bouncing off his shield like a pebble off a mountain side. 

            Thrack is unphased as he charges the next creature, impaling it 
            on his sword in a single blow. 

            The second {monster} recovers from its dazwe and charges him 
            again. This time Thrack spins cutting through its head in one 
            smooth motion. 
            ''',
            'Quill': f'''
            Wasting no time, Quill connects her hands together and whispers
            some ancient words.

            Suddenly a blue mass of shimmering ice appears between her
            hands. The {monster}'s have already beguin to charge in an attempt 
            to catch her before the spell is ready.

            But they are too late...

            A moment later the blue sphere explodes sending a hunderd razor sharp 
            icicles threw each of the remaing creatures. They die instantly.
            ''',
            'Rafe': f'''
            Before you can turn your head Rafe lets 2 perfectly aimed arrows go
            at the remaining {monster}s. The arrows find their targets heads.
            They died before even taking a step toward him.
            ''', 
            'Cathos': f'''
            The patient Monk Cathos, unfurls his robes and slowly approaches the 
            {monster}s. His walk is slow and deliberate, with no sign of tension.

            The fiends surround him from both sides. They wait for a moment...

            Cathos' eyes are closed now and his breathing is calm, as if he is in
            no danger at all.

            Suddenly, the monsters attack in unison from both sides. Charging 
            headlong at the Monk, their attacks... miss. 

            As their momentum takes them past Cathos, he is suddenly in between 
            them. Then the sound of thunder as he strikes both enemies,
            simultaneously cracking their skulls. 

            They land on the ground... lifeless.
            ''', 
            'Selwyn': f'''
            You turn to signal Selywn.

            But he is gone...

            Your enemies begin to howl, almost laughing. They think your companion
            has retreated and left you for dead.

            Suddenly, something glimmers in a shadow next to one of the creatures. 
            Blood spurts from its neck and the beast crumbles to the ground, 
            choking as it dies. It's companion charges, growling, looking for 
            the assassin. 

            But nothing is there... No sign of anything but its dead comrade. 

            A slight rustle in the trees above, are followed by a figure dropping 
            silently from the canopy. It is Selwyn, who falls directly onto the 
            head of the last {monster}... dagger first.

            He lands perfectly, striking the dagger right through its skull in 
            one fluid motion. Selwyn casually lands on his feet before the 
            beast can fall to the ground.

            '''
            }
            result = result + action_dict[companion_name] + '''
            And with that, the first battle is over.

            (Hit enter to continue)
            '''     
        print(result)
        input('>>> ')
        os.system('clear')
        # exit logic?
        self.curr_input = ''

    def choose_weapon(self):
        choice = self.curr_input
        result = '''
            PART 4 - continued
            -----------------------------
        '''
        if choice == '1':
            companion_name = self.companion.get_name()
            result = result + f'''
            You charge the right corner of the boulder and hoist your shield up
            just in time.

            You smash into the face of an unsuspecting orc who looks rather
            surprised.

            Blood spurts from its face just as you see {companion_name} round
            the other side of the boulder. 
        '''
        if choice == '2':
            companion_name = self.companion.get_name()
            result = result + f'''
            You charge the right corner of the boulder and pull your mighty
            sword overhead.

            As you round the corner you swing down, catching a somewhat
            surprised looking orc right between the eyes, cleaving its ugly
            head in half.

            Blood spurts from the gaping wound just as you see {companion_name} 
            round the other side of the boulder.
        '''
        result = result + f'''
            It's ugly companion is facing the other way and suddenly you hear a
            snap, the monsters' neck breaks and its head spins 180 degrees. 
            Blood is pouring from every orifice in its face.

            {companion_name} wasn't holding back today...

            You both spin, waiting for the next attack. 

            But nothing comes... 

            Everything is silent once again.

            {companion_name} slowly turns to you and says, 
            
            'I don't think they really expected an attack this far behind their 
            lines. I mean... they are kind of dumb. They're Orcs after all...'

            Nothing moves but the wind and grass...

            It's true, they really are quite stupid.

            (Hit enter to continue)
        '''
        print(result)
        input('>>> ')
        os.system('clear')
        # exit logic?
        self.curr_input = ''

    def display_last_battle_start(self):
        choice = self.curr_input
        result = '''
            PART 5 - continued
            -----------------------------
        '''
        if choice == '1':
            result = result + f'''
            'Here is our chance, the wizard will cast his spell soon and 
            reverse the attack. Let's kill these monsters before they know 
            what hit them!'

            You turn back towards the lumbering Orc leaders and charge
            across the field.

            You are within 50 feet of the monsters when they finally notice
            your attack.

            They turn to meet you head first!

            The Lieutenant on the left swings his mighty hammer just as
            you crouch and deflect the blow upwards with your shield.

            You simultaneously cut its belly open with a hortizontal 
            strike, finding flesh in between the breastplate of his 
            horrible black armour.

            The other beast hurls its hammer straight at {self.companion.get_name()},
            clipping their right shoulder, sending them spinning to the ground.

            Ogthar roars in defiance! 

            'You pathetic worms... Death is upon you!'

            He charges you and swings at your head with brutal speed. You duck and 
            raise your shield in defense. The edge of the axe catches your shield 
            and shears off the bottom quarter as you leap backwards.

            {self.companion.get_name()} rallies to your side.

            (Hit enter to continue the battle)
        '''
        if choice == '2':
            result = result + f'''
            'The wizard will cast his spell soon and push back the invaders. This is
            our only chance to kill Ogthar and his Lieutenants. But they are too 
            dangerous to attack head on... Let's take them by surprise'

            You scan the camp, 'I don't see a way to get behind them without being seen. 
            Distract them, while I circle around behind.'

            'Will do.', {self.companion.get_name()} responds. You begin to arc around 
            the camp just as your companion emerges 100 feet in front of the ugly beasts.

            'What is this pathetic thing?' roars one of the Lieutenants, as they begin to
            approach the lone figure.

            'Stupid humans send only one champion to kill Ogthar, how disrespectful!',
            Ogthar yells.

            The Lieutenant on his left roars and charges with incredible speed. Suddenly,
            its battle hammer is flying toward {self.companion.get_name()} lightning speed. 
            They are caught off guard by a split second and the hammer clips their right 
            shoulder, sending them spinning to the ground.

            You emerge from behind your enemies just as {self.companion.get_name()} hits the
            ground.

            No time to think, you must save your companion.

            You sprint with inhuman speed, leaping over Ogthar and his remaining guard.
            They roar in surpirse, ready for an attack but you sprint past them like a blur.

            Your sword penetrates through the back of your companion's assailant, the tip
            pokes through his stomach covered in fresh blood.

            The monster roars in pain, gurgles blood in its mouth and falls to the ground.

            {self.companion.get_name()} rallies to your side.

            (Hit enter to continue the battle)
        '''
        print(result)
        input('>>> ')
        os.system('clear')
        # exit logic?
        self.curr_input = ''

if __name__ == '__main__':
    Battle_Methods