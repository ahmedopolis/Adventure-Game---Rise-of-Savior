import sys
import os
import time
import random
import keyboard
from console.screen import sc
from rich.console import Console


mythical_creature_list = None
male_name_list = None
both_sex_name_list = None
name_of_queen = None
weapon_type_list = None
your_weapon_type = None
name_of_trainer = None


def print_speed(speed):
    i = speed
    return i
    

def print_delay(message):
    console = Console()
    i = 0.05
    for c in '\n' + message: 
        with sc.location(0, 0):
            console.print('Press [Backspace] to skip conversations', style='reverse')
        if keyboard.is_pressed('backspace'): 
            i = 0
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering 
        time.sleep(random.random() * i)
            

def print_delay_dialogue(name, message):
    print_delay(f"{name}: \"{message}\"")


def binary_decision(request1, request2):
    print("\nEnter 1 to" + request1)
    print("Enter 2 to" + request2)
    print("What would you like to do?")
    answer = input("(Please Enter 1 or 2)\n")
    while answer != "1" and answer != "2":
        answer = binary_decision(request1, request2)
    return answer


def binary_outcome(choice, path1, path2):
    if choice == "1":
        path1()
    elif choice == "2":
        path2()


def retry_path():
        print_delay("Let's run this back.")
        start()


def exit_path():
    print_delay("Goodbye!")
    quit()


def prompt_try_again(outcome_boolean):
    if outcome_boolean:
        print_delay("CONGRULATION, YOU WIN!")
    else:
        print_delay("Clearly, you lose …")
        print_delay("GAME OVER!")
    choice_try_again = binary_decision(" try again", " quit.")
    binary_outcome(choice_try_again, retry_path, exit_path)


def start():
    os.system("title Rise of Savior")
    os.system('cls')

    print_delay("You are having a hard time falling asleep,"
                " so you decided to go for a stroll in your neighborhood.")
    print_delay("As you are walking, you notice a large vintage-looking"
                " leather book laying on a pile of garbage.")
    print_delay("Despite the distasteful smell, you decide to pick up the"
                " book and you read the cover title:")
    print_delay("\n-------------- REPRISE OF THE HOLY HERO --------------")
    print_delay("You open the book and it only has one page with writing."
                " It reads as follow:")
    print_delay("A legendary hero is needed to save our world."
                " Will you be our savior?")
    choice1 = binary_decision(" be a savior.", " be a bystander.")
    binary_outcome(choice1, choice1_path1, choice1_path2)


def choice1_path2():
    print_delay("You have chosen to be a bystander and you are privileged"
                " enough to witness something.")
    print_delay("Kick back. Grab some popcorn and watch the destruction of"
                " their world as well as yours!")
    print_delay("In a flash, the book burns and the whole area is engulfed"
                " in complete calamity.")
    prompt_try_again(False)


def queen_weapon_comment(weapon):
    if weapon == "sword":
        return "This sword will allow you to slice through your enemies."
    elif weapon == "axe":
        return "You have received a weapon with great"\
               "brut force. Use it wisely!"
    elif weapon == "gun":
        return "With this weapon, you will become a"\
               "master of long-range combat."
    elif weapon == "shield":
        return "You're ability to defend and counter will be unmatched"\
               "with this holy shield."
    elif weapon == "spear":
        return "You have received a very versatile weapon."


def choice1_path1():
    global mythical_creature_list
    print_delay("As you finished reading the prompt and ponder on the idea"
                " of being a hero, the book heats up and a huge flash of"
                " light stuns you.")
    print_delay("Suddenly …")
    color_list = ['blue', 'red', 'yellow', 'green', 'orange', 'purple',
                  'brown', 'black', 'white', 'grey']
    color_of_cloak = random.choice(color_list)
    print_delay("You wake up and find yourself surrounded by individuals"
                f"in {color_of_cloak} cloaks.")
    mythical_creature_list = ['Elf', 'Titan', 'Dwarf', 'Fairy', 'Ogre',
                              'Werewolf', 'Slim', 'Chimera', 'Ghost',
                              'Dragon']
    female_name_list = ['Ruth', 'Eleanor', 'Prudence', 'Sylvia', 'Wihelmina',
                        'Deborah', 'Hazel', 'Adeline', 'Geraldine', 'Zenobia']
    global male_name_list
    male_name_list = ['Furman', 'Huxley', 'Alaric', 'Geoffrey', 'Jasper',
                      'Edison', 'Gert', 'Lamont', 'Manfred', 'Ragnar']
    global both_sex_name_list
    both_sex_name_list = female_name_list + male_name_list
    global name_of_queen
    name_of_queen = random.choice(female_name_list)
    female_name_list.remove(name_of_queen)
    tribe_of_queen = random.choice(mythical_creature_list)
    timeline_before_battle_list = [3, 6, 9, 12, 24, 48]
    timeline_before_battle = random.choice(timeline_before_battle_list)
    print_delay(f"She then says: \"My name is {name_of_queen}, I am the"
                f" leader of the {tribe_of_queen} tribe and the"
                " representative of all the tribes in our world.")
    print_delay_dialogue(name_of_queen, "We have summoned you from your"
                         " world through great sacrifice to defeat an evil"
                         " malice that will threaten the very existence of"
                         " both our worlds.")
    print_delay_dialogue(name_of_queen, "We need your strength and courage to"
                         " defeat this foe. This foe will invade our worlds in"
                         f" {timeline_before_battle} months.")
    print_delay("You tell them that in your world that humans have nuclear"
                " weapons, heavy artillery, robotics, biological weapons and"
                " possibly a billion soldiers.")
    print_delay("However, they inform you that only one person can travel"
                " between worlds every 2000 years and both parallel worlds"
                " are linked via Muller High-Dimensional Strings.")
    print_delay("As a result, if this parallel world is destroyed, so shall"
                " Earth suffer the same fate.")
    print_delay(f"The reality sinks in but {name_of_queen} says that she has"
                " something to give you.")
    print_delay_dialogue(name_of_queen, "In our world, they are 5 holy weapon"
                         " types in our world: sword, axe, gun, shield and"
                         " spear.")
    print_delay_dialogue(name_of_queen, "Every individual in our world"
                         " including you has a weapon-type.")
    print_delay_dialogue(name_of_queen, "We shall give you a vessel"
                         " weapon that will transform into either of those"
                         " 5 types upon contact.")
    global weapon_type_list
    weapon_type_list = ["sword", "axe", "gun", "shield", "spear"]
    global your_weapon_type
    your_weapon_type = random.choice(weapon_type_list)
    print_delay("You grab the vessel weapon that feels like"
                f" clay and it looks like it's a {your_weapon_type}.")
    print_delay_dialogue(name_of_queen, "Congragulation, you have acquired"
                                        f" a holy {your_weapon_type}.")
    print_delay_dialogue(name_of_queen, queen_weapon_comment(your_weapon_type))
    print_delay_dialogue(name_of_queen, "We shall also provide you with only"
                         " 4 support-warriors for battle due to the"
                         " constraints of an evil barrier"
                         " protecting its realm.")
    print_delay_dialogue(name_of_queen, "You will get to build your team"
                         " to invade the evil realm very soon!")
    global name_of_trainer
    name_of_trainer = random.choice(male_name_list)
    male_name_list.remove(name_of_trainer)
    trainer_tribe = random.choice(mythical_creature_list)
    print_delay("She then provides you with exquisite armor, money,"
                " accommodations as well as a trainer"
                f" named: {name_of_trainer} of the {trainer_tribe} tribe.")
    print_delay("He marchs towards you.")
    print_delay_dialogue(name_of_trainer, "Will you accept me as"
                         " your trainer?")
    choice2 = binary_decision(f" accept {name_of_trainer}'s offer.",
                              f" reject {name_of_trainer}'s offer.")
    binary_outcome(choice2, choice2path1, choice2path2)


def choice2path2():
    print_delay("You tell him that you are more of a lone wolf"
                " and that you would like to figure things out"
                " on your own but …")
    print_delay_dialogue(name_of_trainer, f"I understand but are"
                         " you sure that I cannot assist you or"
                         " provide any help?")
    choice2_1 = binary_decision(f" accept {name_of_trainer}'s"
                                " final offer.", " reject"
                                f" {name_of_trainer}'s final offer.")
    binary_outcome(choice2_1, choice2_1path2, choice2_2path2)


def choice2_2path2():
    print_delay_dialogue(name_of_trainer, "Very well, I will"
                         " respect your wishes.")
    solo_path3()


def choice2_1path2():
    print_delay_dialogue(name_of_trainer, "I am glad that you"
                         " reco1nsidered my offer, let's start"
                         " right away our training.")
    trainer_path3()


def choice2path1():
    print_delay_dialogue(name_of_trainer, "Thank you for accepting"
                         " me as your trainer, we shall start your"
                         " training immediately.")
    trainer_path3()


def solo_path3():
    print_delay("You’re training vigorously by yourself"
                " in the outskirt of the home base.")
    print_delay("You are using a trial-and-error approach"
                " to figure out how to use your weapon.")
    print_delay("You're inexperience with your weapon"
                " leads to a fatal injury.")
    print_delay("No one was there to save you and the"
                " worlds are left without their faithful hero.")
    prompt_try_again(False)


def trainer_path3():
    print_delay("Your training is fierce, and you are dedicated to the cause.")
    team_selection_path4()


def warrior_template_maker(name_list, race_list, weapon_type_list):
    name = random.choice(name_list)
    race = random.choice(race_list)
    weapon_type = random.choice(weapon_type_list)
    warrior_template = [name, race, weapon_type]
    return warrior_template


def warrior_list(team_size, name_list, race_list, weapon_type_list):
    index = 0
    warrior_list = []
    while index < team_size:
        warrior_template = warrior_template_maker(name_list,
                                                  race_list,
                                                  weapon_type_list)
        name_list.remove(warrior_template[0])
        warrior_list.append(warrior_template)
        index += 1
    return warrior_list


def warrior_list_print(warrior, index):
    print(f"\nIndividual #{index+1}")
    print(f"Name: {warrior[0]}")
    print(f"Race: {warrior[1]}")
    print(f"Weapon-type: {warrior[2]}")


def warrior_selection_print(warrior_list, round, round_boolean):
    if round_boolean:
        print(f"\n-------------- ROUND #{round} --------------")
    index = 0
    for warriors in range(len(warrior_list)):
        warrior_list_print(warrior_list[index], index)
        index += 1


def team_size_list(choice, warrior_list_round):
    if choice == '1':
        return warrior_list_round[0]
    elif choice == '2':
        return warrior_list_round[1]


def warrior_selection_process():
    round = 1
    round_boolean = True
    team_list = []
    while round < 5:
        warrior_list_round = warrior_list(2, both_sex_name_list,
                                          mythical_creature_list,
                                          weapon_type_list)
        warrior_selection_print(warrior_list_round, round, round_boolean)
        choice3 = binary_decision(" select individual #1.",
                                  " select individual #2.")
        warrior_selected = team_size_list(choice3, warrior_list_round)
        team_list.append(warrior_selected)
        round += 1
    your_warrior_template = ["Yourself", "Human", your_weapon_type]
    team_list.append(your_warrior_template)
    return team_list


def team_selection_path4():
    print_delay("Suddenly...")
    print_delay("A white-bearded fellow approaches you.")
    name_of_scout = random.choice(male_name_list)
    male_name_list.remove(name_of_scout)
    scout_tribe = random.choice(mythical_creature_list)
    print_delay_dialogue("White-bearded fellow", "Dear hero, my name is"
                         f" {name_of_scout} of the"
                         f" {scout_tribe} tribe and"
                         " I am the weapon designer for our faction.")
    print_delay_dialogue(name_of_scout, "We shall go through 4 selection"
                         " rounds and you shall choose one warrior among"
                         " the pairs that are presented to you.")
    print_delay_dialogue(name_of_scout, "Please remember creating a balanced"
                         " team is key! All warriors will be presented based"
                         " on their names, race and most importantly"
                         " weapon-type.")
    print_delay_dialogue(name_of_scout, "Let’s begin: ")
    teammates_list = warrior_selection_process()
    print_delay_dialogue(name_of_scout, "You have now selected your team;"
                         " you may proceed to train together.")
    print_delay("You train with your team for months and"
                " the time has finally come to go to the evil realm.")
    print_delay_dialogue(name_of_queen, "You are guide by"
                         f" {name_of_queen} to the barrier.")
    print_delay_dialogue(name_of_queen, "Good luck my heroes!")
    barrier_battle_path5(teammates_list)


def warrior_binary_list_round(warrior_list):
    warrior_binary_list = []
    index_list = range(len(warrior_list))
    for warriors in range(2):
        index = random.choice(index_list)
        warrior_binary_list.append(warrior_list[index])
    return warrior_binary_list


def warrior_binary_options_print(warrior_binary_list, evil_leader_name,
                                 evil_team_boolean):
    if warrior_binary_list[0] == warrior_binary_list[1]:
        if evil_team_boolean and warrior_binary_list[0][0] == evil_leader_name:
            print_delay_dialogue(evil_leader_name, "It seems the dice has"
                                 " chosen myself as the contestant"
                                 " for this round.")
        elif evil_team_boolean and \
                warrior_binary_list[0][0] != evil_leader_name:
            print_delay_dialogue(evil_leader_name, "It seems the dice has"
                                 " chosen one of my fateful warriors.")
        elif not evil_team_boolean and warrior_binary_list[0][0] == "Yourself":
            print_delay("You will be the fighter for this round.")
        elif not evil_team_boolean and warrior_binary_list[0][0] != "Yourself":
            print_delay("Your dice role has yielded two identical names.")
    else:
        if evil_team_boolean:
            print_delay_dialogue(evil_leader_name, f"I will choose between"
                                 " two of my fateful warriors for"
                                 " this fight.")
        elif not evil_team_boolean:
            print_delay("You must choose between your two provided options.")


def round_introduction_print(round):
    print_delay(f"THIS IS ROUND #{round}.")
    print_delay("It is time to roll the dices.")
    print_delay("Here are the results for the dice roll.")


def input_dictionnary_check(keys, values, weapon):
    if weapon in keys:
        dictionnary = dict(zip(keys, values))
        return dictionnary
    else:
        print("Wrong weapon was passed.")


def battle_result(weapon_avenger, weapon_enemy):
    weapons_list = ["axe", "gun", "shield", "spear", "sword"]
    results_lists = [{0: 0, 1: -1, 2: 1, 3: 1, 4: -1},
                     {0: 1, 1: 0, 2: -1, 3: -1, 4: 1},
                     {0: -1, 1: 1, 2: 0, 3: 1, 4: -1},
                     {0: -1, 1: 1, 2: -1, 3: 0, 4: 1},
                     {0: 1, 1: -1, 2: 1, 3: -1, 4: 0}]
    integer_list = [0, 1, 2, 3, 4]
    converter_dictionnary = input_dictionnary_check(weapons_list,
                                                    integer_list,
                                                    weapon_enemy)
    results_nested_dictionnary = input_dictionnary_check(weapons_list,
                                                         results_lists,
                                                         weapon_avenger)
    interger_weapon_enemy = converter_dictionnary.get(weapon_enemy)
    avenger_match_result = results_nested_dictionnary[weapon_avenger][
                           interger_weapon_enemy]
    return avenger_match_result


def score_updater(value, your_team_total_score, enemy_team_total_score):
    team_score_list = [your_team_total_score, enemy_team_total_score]
    if value == 1:
        print_delay("You win this round.")
        team_score_list[0] += 1
        print_delay("The total score on your party is"
                    f" {team_score_list[0]} and the enemy's"
                    f" is {team_score_list[1]}.")
        return team_score_list
    elif value == -1:
        print_delay("You lose this round.")
        team_score_list[1] += 1
        print_delay("The total score on your party is"
                    f" {team_score_list[0]} and the enemy's is"
                    f" {team_score_list[1]}.")
        return team_score_list
    elif value == 0:
        print_delay("It's a tie for this round")
        print_delay("The total score on your party is"
                    f" {team_score_list[0]} and the enemy's is"
                    f" {team_score_list[1]}.")
        return team_score_list


def game_outcome(your_team_total_score, enemy_team_total_score,
                 evil_leader_name):
    if your_team_total_score > enemy_team_total_score:
        print_delay("It seems you have won the fiend's game.")
        print_delay_dialogue(evil_leader_name, "Congrats on your victory"
                             " as promised we will surrender.")
        print_delay_dialogue(evil_leader_name, "Farewell!")
        print_delay("The evil creatures start to fadeaway"
                    " and so does the barrier.")
        prompt_try_again(True)
    elif enemy_team_total_score > your_team_total_score:
        print_delay_dialogue(evil_leader_name, "I guess we are victorious.")
        print_delay_dialogue(evil_leader_name, "Enjoy oblivion!")
        prompt_try_again(False)


def warrior_games(team_list, evil_warriors_list, evil_leader_name):
    round = 1
    your_team_total_score = 0
    enemy_team_total_score = 0
    while your_team_total_score < 4 and enemy_team_total_score < 3:
        your_team_options = warrior_binary_list_round(team_list)
        enemy_team_options = warrior_binary_list_round(evil_warriors_list)
        round_introduction_print(round)
        print_delay("ENEMY TEAM:")
        warrior_selection_print(enemy_team_options, round, False)
        print_delay("Your TEAM:")
        warrior_selection_print(your_team_options, round, False)
        warrior_binary_options_print(enemy_team_options,
                                     evil_leader_name, True)
        warrior_binary_options_print(your_team_options,
                                     evil_leader_name, False)
        choice4 = binary_decision(" select individual #1.",
                                  " select individual #2.")
        your_warrior_selected = team_size_list(choice4, your_team_options)
        enemy_warrior_selected = random.choice(enemy_team_options)
        weapon_of_your_warrior = your_warrior_selected[2]
        weapon_of_your_enemy = enemy_warrior_selected[2]
        value_round = battle_result(weapon_of_your_warrior,
                                    weapon_of_your_enemy)
        score_list = score_updater(value_round, your_team_total_score,
                                   enemy_team_total_score)
        your_team_total_score = score_list[0]
        enemy_team_total_score = score_list[1]
        round += 1
    game_outcome(your_team_total_score, enemy_team_total_score,
                 evil_leader_name)


def barrier_battle_path5(team_list):
    villain_name_list = ['Frieza', 'Voldermort', 'Moro', 'Scar', 'Madara',
                         'Loki', 'Hans Landa', 'Darth Vader', 'Envy', 'Dante']
    evil_creature_list = ['Devil', 'Goblin', 'Satan Moth', 'Dark Sorcerer',
                          'Dark Elf', 'Vampire', 'Draugr', 'Arachne',
                          'Cerberus', 'Ammit']
    evil_leader_tribe = random.choice(evil_creature_list)
    evil_leader_name = random.choice(villain_name_list)
    villain_name_list.remove(evil_leader_name)
    print_delay("You penetrate the barrier with your team, and"
                " you are greeted by a fiend.")
    print_delay("As it approaches you, your whole team including"
                " yourself is unable to move.")
    print_delay_dialogue("Fiend", f"My name is {evil_leader_name} of the"
                         f" {evil_leader_tribe} tribe.")
    print_delay_dialogue(evil_leader_name, "I am the leader of the wonderful"
                         " movement that will reshape our worlds.")
    print_delay_dialogue(evil_leader_name, "Don’t worry I will not hurt you"
                         " yet!")
    print_delay_dialogue(evil_leader_name, "Let’s play a game to decide"
                         " the fate of our worlds.")
    evil_warriors_list = warrior_list(4, villain_name_list, evil_creature_list,
                                      weapon_type_list)
    evil_leader_weapon = random.choice(weapon_type_list)
    evil_leader_warrior_template = [evil_leader_name, evil_leader_tribe,
                                    evil_leader_weapon]
    evil_warriors_list.append(evil_leader_warrior_template)
    print_delay_dialogue(evil_leader_name, "I have 4 supporting teammates so"
                         " both parties have 5 members in total including the"
                         " leaders of course.")
    print_delay_dialogue(evil_leader_name, "We shall have 1-on-1 fights where"
                         " a contestant will come from each party.")
    print_delay_dialogue(evil_leader_name, "A victory in a fight will result"
                         " in that party receiving a point.")
    print_delay_dialogue(evil_leader_name, "First team to win 3 rounds wins"
                         " the game.")
    print_delay_dialogue(evil_leader_name, "You win and we will surrender."
                         " On the other hand, if you lose hahahaah…")
    print_delay_dialogue(evil_leader_name, "I don’t have to tell you what will"
                         " happen.")
    print_delay_dialogue(evil_leader_name, "Each team will be handed two"
                         " five-faced dices with each face will have the name"
                         " of the contestant.")
    print_delay_dialogue(evil_leader_name, "We both roll our dices and"
                         " based on the names presented on the dice; each"
                         " team shall decide whom from the two names presented"
                         " shall represent their team for that round.")
    print_delay_dialogue(evil_leader_name, "This decision of each team"
                         " will only be revealed right before a round"
                         " must begin.")
    print_delay_dialogue(evil_leader_name, "If both dices result in the"
                         " same name that contestant must represent the"
                         " team for that round.")
    print_delay_dialogue(evil_leader_name, "A contestant can participate"
                         " in more than one round.")
    print_delay("You notice the enemies have similar weapons as yours.")
    print_delay("You remember that each weapon-type can beat two types,"
                " lose to two other types and come in a stalemate"
                " in a mirror match.")
    print_delay("unfortunately, you don't remember the"
                " advantageous matchups but suddenly ...")
    print_delay_dialogue(evil_leader_name, "Let's begin the games!")
    warrior_games(team_list, evil_warriors_list, evil_leader_name)

if __name__ == "__main__":
    start()
