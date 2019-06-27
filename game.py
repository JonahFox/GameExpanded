from random import randint
game_running = True
#player = {'name': 'Jonah', 'attack_min': 10, 'attack_max': 15, 'buff': 5, 'heal': 15, 'health': 100, 'mana':100, 'mana_cost': 10}

def calculate_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])
def calculate_player_attack():
    return randint(player['attack_min'], player['attack_max'])
def mean():
    return (player['attack_min'] // player['attack_max'])

while game_running == True:
    new_round = True
    
    player = {'name': 'Jonah', 'attack_min': 10, 'attack_max': 15, 'buff': 5, 'heal': 15, 'health': 100, 'mana':100, 'mana_cost': 10}
    monster = {'name': 'Black', 'attack_min': 10, 'attack_max': 20, 'health': 100}    

    print('---' * 7)
    print('Enter Player Name')
    player['name'] = input("Input name here: ") 

    print('---' * 7)
    print(player['name'] + ' has ' + str(player['health']) + ' health ')
    print(player['name'] + ' has ' + str(player['mana']) + ' mana left')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health ')



    while new_round == True:
        player_buffed = False
        player_won = False
        monster_won = False
        has_mana = True
        

        print('---' * 7)
        print('please select action')
        print('1) Attack')
        print('2) Heal')
        print('3) Buff')
        print('4) Exit Game')
        print('---' * 7)
        player_choice = input('Enter your choice here: ')
        print('---' * 7)

        if player_choice == '1':
            monster['health'] = monster['health'] - calculate_player_attack()
            player['health'] = player['health'] - calculate_monster_attack()
            if player['health'] <= 0:
                    monster_won = True 
            if monster['health'] <= 0:
                player_won = True
              #  player_buffed = False
                


        
        if player['mana'] <= 0:
                has_mana = False    
        if player_choice == '2' and has_mana == False:
            print('You are out of mana')  

        elif player_choice == '2' and player['mana'] >= player['mana_cost']:
            player['health'] = player['health'] + player['heal']
            player['mana'] = player['mana'] - player['mana_cost']
            player['health'] = player['health'] - calculate_monster_attack()
            if player['health'] <= 0:
                monster_won = True 
                player_buffed = False
        

        elif player_choice =='3':
            player_buffed = True
            if player_buffed == True:
                mean() + player['buff']
                print('Player has been buffed!')
                print('---' * 7)
                player['health'] = player['health'] - calculate_monster_attack()
                print('The Monster blindsides you while buffing!')
                print('---' * 7)
          
            
        elif player_choice == '4':
            new_round = False
            game_running = False 

       # else:
        #    print('Invalid Input')

        if player_won == False and monster_won == False:
            print(player['name'] + ' has ' + str(player['health']) + ' health left')
            print(monster['name'] + ' has ' + str(monster['health']) + ' health left')
            print(player['name'] + ' has ' + str(player['mana']) + ' mana left')
            print('---' * 7)
        if player_choice >= '5':
            print('Invalid Input')
            
        elif player_won:
            print(player['name'] + ' has won!')
            new_round = False
        elif monster_won:
            new_round = False
            print('The Monster won')


