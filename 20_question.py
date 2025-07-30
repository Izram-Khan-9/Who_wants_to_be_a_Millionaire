# Questions
Question1 = ['What is the chemical symbol for potassium?', 'P', 'Pt', 'K', 'Sn'] # c
Question2 = ['In which year was Google founded?', '1997', '1998', '1999', '2000'] # b
Question3 = ['What is the cube root of 729?', '7', '9', '13', '17'] # b
Question4 = ['In economics, what does GDP measure?', 'Imports', 'Stock prices', 'Total output', 'Tax revenue'] # c
Question5 = ['Which country has the most time zones (including overseas territories)?', 'France', 'Russia', 'Canada', 'China'] # a
Question6 = ['In which country would you find the city of Timbuktu?', 'Nigeria', 'Mali', 'Egypt', 'Sudan'] # b
Question7 = ['Which operating system does the Nintendo Switch use as its core?', 'Android', 'BSD', 'Linux', 'FreeBSD'] # d
Question8 = ['What element has the highest melting point?', 'Iron', 'Osmium', 'Tungsten', 'Carbon'] # c
Question9 = ['What is the standard port number for HTTPS?', '80', '443', '22', '25'] # b
Question10 = ['Who is the author of Blood Meridian?', 'Cormac McCarthy', 'Ernest Hemingway', 'William Faulkner', 'Haruki Murakami'] #a
Question11 = ['What\'s the name of the largest moon of Saturn?', 'Iapetus', 'Titan', 'Hyperion', 'Enceladus'] # b
Question12 = ['What\'s the only number that is both the sum and product of three positive integers?', '6', '12', '18', '24'] # a
Question13 = ['Who painted The Garden of Earthly Delights?','Pablo Picasso','Salvador Dali','Hieronymus Bosch','Vincent van Gogh'] # c
Question14 = ['What programming paradigm is most associated with Haskell?', 'Functional', 'Object-Oriented', 'Logic', 'Procedural'] # a
Question15 = ['Which language is considered the mother of most modern programming languages?', 'Lisp', 'COBOL', 'C', 'Smalltalk'] # c
Question16 = ['Who is the final boss in the original Dark Souls game?', 'Artorias', 'Gwyn', 'Manus', 'Seath'] # b
Question17 = ['What was the first console video game to feature a save function?', 'Metroid', 'Pac-Man', 'Final Fantasy', 'Zelda'] # d
Question18 = ['What is the derivative of sin(x)?', '-sin(x)', 'tan(x)', 'sec(x)', 'cos(x)'] # d
Question19 = ['Who was responsible for poisoning Joffrey Baratheon in Game of Thrones?', 'Cersei', 'Tyrion', 'Olenna', 'Littlefinger'] #c
Question20 = ['Which country has the highest number of neighboring countries?', 'Brazil', 'India', 'Chile', 'China'] # d

# Prize money
prize1 = 100
prize2 = 200
prize3 = 300
prize4 = 500
prize5 = 1000 # Checkpoint
prize6 = 2000
prize7 = 3000
prize8 = 5000
prize9 = 7500
prize10 = 10000 # Checkpoint
prize11 = 20000
prize12 = 30000
prize13 = 50000
prize14 = 75000
prize15 = 100000 # Checkpoint
prize16 = 150000
prize17 = 250000
prize18 = 500000
prize19 = 750000
prize20 = 1000000 # Jackpot
# Checkpoints will be made in version 2.0

# Introduction
player_name = input('Enter your name: ') # User's name
print(f'\nWelcome to the game show {player_name}\n') # Welcome message
print('Enter h for help.') # Help message
print('Enter p to play!') # Play message

while True: # Loop until valid input
  player_choice = input('\nWhat would you like to do: ') # Asking user what they want to do

  # Help
  if player_choice == 'h':
      print('\nHelp:\n')
      print('You will be asked 20 questions.')
      print('Each question has 4 possible answers: a, b, c, or d.')
      print('You must answer each question correctly to win the corresponding prize money.')
      print('If you answer incorrectly, the game ends and you will win money based on the last checkpoint you reached.')
      print('The checkpoints are at $1,000, $10,000, and $100,000. Note: Checkpoints will be implemented in version 2.0.')
      print('After reding help the program will exit. Run the program again to play.')
      print('Good luck!\n')

  # Play
  elif player_choice == 'p':
    print('\n_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-💸🤑WHO WANTS TO BE A MILLIONAIRE🤑💸_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n')


    # players bank
    player_bank = 0
    # Game state
    game_over = False

    # Question 1
    while True:
        print('1.',Question1[0],'\n')
        print(f'a) {Question1[1]}  b) {Question1[2]}')
        print(f'c) {Question1[3]}  d) {Question1[4]}')
        player_answer = input('What is your answer? a/b/c/d: ')

        if player_answer == 'c': # Correct answer
            print('\nCorrect!!!✅')
            print('(K is the chemical symbol for potassium)\n')
            print(f'You have won ${prize1}!\n')
            player_bank = prize1

            # Question 2
            while True:
                print('2.',Question2[0],'\n')
                print(f'a) {Question2[1]}  b) {Question2[2]}')
                print(f'c) {Question2[3]}  d) {Question2[4]}')
                player_answer = input('What is your answer? a/b/c/d: ')

                if player_answer == 'b': # Correct answer
                    print('\nCorrect!!!✅')
                    print('(Google was founded in 1998)\n')
                    print(f'You have won ${prize2}!')
                    player_bank = prize2
                    print(f'Your total is now ${player_bank}\n')

                    # Question 3
                    while True:
                        print('3.',Question3[0],'\n')
                        print(f'a) {Question3[1]}  b) {Question3[2]}')
                        print(f'c) {Question3[3]}  d) {Question3[4]}')
                        player_answer = input('What is your answer? a/b/c/d: ')

                        if player_answer == 'b': # Correct answer
                            print('\nCorrect!!!✅')
                            print('(The cube root of 729 is 9)\n')
                            print(f'You have won ${prize3}!')
                            player_bank = prize3
                            print(f'Your total is now ${player_bank}\n')

                            # Question 4
                            while True:
                                print('4.',Question4[0],'\n')
                                print(f'a) {Question4[1]}  b) {Question4[2]}')
                                print(f'c) {Question4[3]}  d) {Question4[4]}')
                                player_answer = input('What is your answer? a/b/c/d: ')

                                if player_answer == 'c': # Correct answer
                                    print('\nCorrect!!!✅')
                                    print('(GDP measures total output)\n')
                                    print(f'You have won ${prize4}!')
                                    player_bank = prize4
                                    print(f'Your total is now ${player_bank}\n')

                                    # Question 5
                                    while True:
                                        print('5.',Question5[0],'\n')
                                        print(f'a) {Question5[1]}  b) {Question5[2]}')
                                        print(f'c) {Question5[3]}  d) {Question5[4]}')
                                        player_answer = input('What is your answer? a/b/c/d: ')

                                        if player_answer == 'a': # Correct answer
                                            print('\nCorrect!!!✅')
                                            print('(France has the most time zones)\n')
                                            print(f'You have won ${prize5}!')
                                            player_bank = prize5
                                            print(f'Your total is now ${player_bank}\n')

                                            # Question 6
                                            while True:
                                                print('6.',Question6[0],'\n')
                                                print(f'a) {Question6[1]}  b) {Question6[2]}')
                                                print(f'c) {Question6[3]}  d) {Question6[4]}')
                                                player_answer = input('What is your answer? a/b/c/d: ')

                                                if player_answer == 'b': # Correct answer
                                                    print('\nCorrect!!!✅')
                                                    print('(Timbuktu is in Mali)\n')
                                                    print(f'You have won ${prize6}!')
                                                    player_bank = prize6
                                                    print(f'Your total is now ${player_bank}\n')

                                                    # Question 7
                                                    while True:
                                                        print('7.',Question7[0],'\n')
                                                        print(f'a) {Question7[1]}  b) {Question7[2]}')
                                                        print(f'c) {Question7[3]}  d) {Question7[4]}')
                                                        player_answer = input('What is your answer? a/b/c/d: ')

                                                        if player_answer == 'd': # Correct answer
                                                            print('\nCorrect!!!✅')
                                                            print('(The Nintendo Switch uses FreeBSD as its core)\n')
                                                            print(f'You have won ${prize7}!')
                                                            player_bank = prize7
                                                            print(f'Your total is now ${player_bank}\n')

                                                            # Question 8
                                                            while True:
                                                                print('8.',Question8[0],'\n')
                                                                print(f'a) {Question8[1]}  b) {Question8[2]}')
                                                                print(f'c) {Question8[3]}  d) {Question8[4]}')
                                                                player_answer = input('What is your answer? a/b/c/d: ')

                                                                if player_answer == 'c': # Correct answer
                                                                    print('\nCorrect!!!✅')
                                                                    print('(Tungsten has the highest melting point)\n')
                                                                    print(f'You have won ${prize8}!')
                                                                    player_bank = prize8
                                                                    print(f'Your total is now ${player_bank}\n')

                                                                    # Question 9
                                                                    while True:
                                                                        print('9.',Question9[0],'\n')
                                                                        print(f'a) {Question9[1]}  b) {Question9[2]}')
                                                                        print(f'c) {Question9[3]}  d) {Question9[4]}')
                                                                        player_answer = input('What is your answer? a/b/c/d: ')

                                                                        if player_answer == 'b': # Correct answer
                                                                            print('\nCorrect!!!✅')
                                                                            print('(The standard port number for HTTPS is 443)\n')
                                                                            print(f'You have won ${prize9}!')
                                                                            player_bank = prize9
                                                                            print(f'Your total is now ${player_bank}\n')

                                                                            # Question 10
                                                                            while True:
                                                                                print('10.',Question10[0],'\n')
                                                                                print(f'a) {Question10[1]}  b) {Question10[2]}')
                                                                                print(f'c) {Question10[3]}  d) {Question10[4]}')
                                                                                player_answer = input('What is your answer? a/b/c/d: ')

                                                                                if player_answer == 'a': # Correct answer
                                                                                    print('\nCorrect!!!✅')
                                                                                    print('(Blood Meridian was written by Cormac McCarthy)\n')
                                                                                    print(f'You have won ${prize10}!')
                                                                                    player_bank = prize10
                                                                                    print(f'Your total is now ${player_bank}\n')

                                                                                    # Question 11
                                                                                    while True:
                                                                                        print('11.',Question11[0],'\n')
                                                                                        print(f'a) {Question11[1]}  b) {Question11[2]}')
                                                                                        print(f'c) {Question11[3]}  d) {Question11[4]}')
                                                                                        player_answer = input('What is your answer? a/b/c/d: ')

                                                                                        if player_answer == 'b': # Correct answer
                                                                                            print('\nCorrect!!!✅')
                                                                                            print('(Titan is the largest moon of Saturn)\n')
                                                                                            print(f'You have won ${prize11}!')
                                                                                            player_bank = prize11
                                                                                            print(f'Your total is now ${player_bank}\n')

                                                                                            # Question 12
                                                                                            while True:
                                                                                                print('12.',Question12[0],'\n')
                                                                                                print(f'a) {Question12[1]}  b) {Question12[2]}')
                                                                                                print(f'c) {Question12[3]}  d) {Question12[4]}')
                                                                                                player_answer = input('What is your answer? a/b/c/d: ')

                                                                                                if player_answer == 'a': # Correct answer
                                                                                                    print('\nCorrect!!!✅')
                                                                                                    print('(6 is the only integer that is both sum and product of 3 positive integers)\n')
                                                                                                    print(f'You have won ${prize12}!')
                                                                                                    player_bank = prize12
                                                                                                    print(f'Your total is now ${player_bank}\n')

                                                                                                    # Question 13
                                                                                                    while True:
                                                                                                        print('13.',Question13[0],'\n')
                                                                                                        print(f'a) {Question13[1]}  b) {Question13[2]}')
                                                                                                        print(f'c) {Question13[3]}  d) {Question13[4]}')
                                                                                                        player_answer = input('What is your answer? a/b/c/d: ')

                                                                                                        if player_answer == 'c': # Correct answer
                                                                                                            print('\nCorrect!!!✅')
                                                                                                            print('(Hieronymus Bosch painted The Garden of Earthly Delights)\n')
                                                                                                            print(f'You have won ${prize13}!')
                                                                                                            player_bank = prize13
                                                                                                            print(f'Your total is now ${player_bank}\n')

                                                                                                            # Question 14
                                                                                                            while True:
                                                                                                                print('14.',Question14[0],'\n')
                                                                                                                print(f'a) {Question14[1]}  b) {Question14[2]}')
                                                                                                                print(f'c) {Question14[3]}  d) {Question14[4]}')
                                                                                                                player_answer = input('What is your answer? a/b/c/d: ')

                                                                                                                if player_answer == 'a': # Correct answer
                                                                                                                    print('\nCorrect!!!✅')
                                                                                                                    print('(Haskell is associated with the functional programming paradigm)\n')
                                                                                                                    print(f'You have won ${prize14}!')
                                                                                                                    player_bank = prize14
                                                                                                                    print(f'Your total is now ${player_bank}\n')

                                                                                                                    # Question 15
                                                                                                                    while True:
                                                                                                                        print('15.',Question15[0],'\n')
                                                                                                                        print(f'a) {Question15[1]}  b) {Question15[2]}')
                                                                                                                        print(f'c) {Question15[3]}  d) {Question15[4]}')
                                                                                                                        player_answer = input('What is your answer? a/b/c/d: ')

                                                                                                                        if player_answer == 'c': # Correct answer
                                                                                                                            print('\nCorrect!!!✅')
                                                                                                                            print('(C is the mother of most modern programming languages)\n')
                                                                                                                            print(f'You have won ${prize15}!')
                                                                                                                            player_bank = prize15
                                                                                                                            print(f'Your total is now ${player_bank}\n')

                                                                                                                            # Question 16
                                                                                                                            while True:
                                                                                                                                print('16.',Question16[0],'\n')
                                                                                                                                print(f'a) {Question16[1]}  b) {Question16[2]}')
                                                                                                                                print(f'c) {Question16[3]}  d) {Question16[4]}')
                                                                                                                                player_answer = input('What is your answer? a/b/c/d: ')

                                                                                                                                if player_answer == 'b': # Correct answer
                                                                                                                                    print('\nCorrect!!!✅')
                                                                                                                                    print('(Gwyn is the final boss in the original Dark Souls game)\n')
                                                                                                                                    print(f'You have won ${prize16}!')
                                                                                                                                    player_bank = prize16
                                                                                                                                    print(f'Your total is now ${player_bank}\n')

                                                                                                                                    # Question 17
                                                                                                                                    while True:
                                                                                                                                        print('17.',Question17[0],'\n')
                                                                                                                                        print(f'a) {Question17[1]}  b) {Question17[2]}')
                                                                                                                                        print(f'c) {Question17[3]}  d) {Question17[4]}')
                                                                                                                                        player_answer = input('What is your answer? a/b/c/d: ')

                                                                                                                                        if player_answer == 'd': # Correct answer
                                                                                                                                            print('\nCorrect!!!✅')
                                                                                                                                            print('(Zelda was the first console video game to feature a save function)\n')
                                                                                                                                            print(f'You have won ${prize17}!')
                                                                                                                                            player_bank = prize17
                                                                                                                                            print(f'Your total is now ${player_bank}\n')

                                                                                                                                            # Question 18
                                                                                                                                            while True:
                                                                                                                                                print('18.',Question18[0],'\n')
                                                                                                                                                print(f'a) {Question18[1]}  b) {Question18[2]}')
                                                                                                                                                print(f'c) {Question18[3]}  d) {Question18[4]}')
                                                                                                                                                player_answer = input('What is your answer? a/b/c/d: ')

                                                                                                                                                if player_answer == 'd': # Correct answer
                                                                                                                                                    print('\nCorrect!!!✅')
                                                                                                                                                    print('(The derivative of sin(x) is cos(x))\n')
                                                                                                                                                    print(f'You have won ${prize18}!')
                                                                                                                                                    player_bank = prize18
                                                                                                                                                    print(f'Your total is now ${player_bank}\n')

                                                                                                                                                    # Question 19
                                                                                                                                                    while True:
                                                                                                                                                        print('19.',Question19[0],'\n')
                                                                                                                                                        print(f'a) {Question19[1]}  b) {Question19[2]}')
                                                                                                                                                        print(f'c) {Question19[3]}  d) {Question19[4]}')
                                                                                                                                                        player_answer = input('What is your answer? a/b/c/d: ')

                                                                                                                                                        if player_answer == 'c': # Correct answer
                                                                                                                                                            print('\nCorrect!!!✅')
                                                                                                                                                            print('(Olenna Tyrell was responsible for poisoning Joffrey)\n')
                                                                                                                                                            print(f'You have won ${prize19}!')
                                                                                                                                                            player_bank = prize19
                                                                                                                                                            print(f'Your total is now ${player_bank}\n')

                                                                                                                                                            # Question 20 - Final Question!
                                                                                                                                                            while True:
                                                                                                                                                                print('20.',Question20[0],'\n')
                                                                                                                                                                print(f'a) {Question20[1]}  b) {Question20[2]}')
                                                                                                                                                                print(f'c) {Question20[3]}  d) {Question20[4]}')
                                                                                                                                                                player_answer = input('What is your answer? a/b/c/d: ')

                                                                                                                                                                if player_answer == 'd': # Correct answer
                                                                                                                                                                    print('\nCorrect!!!✅')
                                                                                                                                                                    print('(China has the highest number of neighboring countries)\n')
                                                                                                                                                                    print(f'You have won ${prize20}!')
                                                                                                                                                                    player_bank = prize20
                                                                                                                                                                    print(f'Your total is now ${player_bank}\n')
                                                                                                                                                                    print('🎉💸🤑 CONGRATULATIONS! YOU ARE A MILLIONAIRE! 🤑💸🎉')
                                                                                                                                                                    break

                                                                                                                                                                elif player_answer == 'a' or player_answer == 'b' or player_answer == 'c':
                                                                                                                                                                    print('\nIncorrect!❌')
                                                                                                                                                                    print('The correct answer was d) China\n')
                                                                                                                                                                    game_over = True
                                                                                                                                                                    break

                                                                                                                                                                else:
                                                                                                                                                                    print('Please enter a/b/c/d\n')

                                                                                                                                                            break

                                                                                                                                                        elif player_answer == 'a' or player_answer == 'b' or player_answer == 'd':
                                                                                                                                                            print('\nIncorrect!❌')
                                                                                                                                                            print('The correct answer was c) Olenna\n')
                                                                                                                                                            game_over = True
                                                                                                                                                            break

                                                                                                                                                        else:
                                                                                                                                                            print('Please enter a/b/c/d\n')

                                                                                                                                                    break

                                                                                                                                                elif player_answer == 'a' or player_answer == 'b' or player_answer == 'c':
                                                                                                                                                    print('\nIncorrect!❌')
                                                                                                                                                    print('The correct answer was d) cos(x)\n')
                                                                                                                                                    game_over = True
                                                                                                                                                    break

                                                                                                                                                else:
                                                                                                                                                    print('Please enter a/b/c/d\n')

                                                                                                                                            break

                                                                                                                                        elif player_answer == 'a' or player_answer == 'b' or player_answer == 'c':
                                                                                                                                            print('\nIncorrect!❌')
                                                                                                                                            print('The correct answer was d) Zelda\n')
                                                                                                                                            game_over = True
                                                                                                                                            break

                                                                                                                                        else:
                                                                                                                                            print('Please enter a/b/c/d\n')

                                                                                                                                    break

                                                                                                                                elif player_answer == 'a' or player_answer == 'c' or player_answer == 'd':
                                                                                                                                    print('\nIncorrect!❌')
                                                                                                                                    print('The correct answer was b) Gwyn\n')
                                                                                                                                    game_over = True
                                                                                                                                    break

                                                                                                                                else:
                                                                                                                                    print('Please enter a/b/c/d\n')

                                                                                                                            break

                                                                                                                        elif player_answer == 'a' or player_answer == 'b' or player_answer == 'd':
                                                                                                                            print('\nIncorrect!❌')
                                                                                                                            print('The correct answer was c) C\n')
                                                                                                                            game_over = True
                                                                                                                            break

                                                                                                                        else:
                                                                                                                            print('Please enter a/b/c/d\n')

                                                                                                                    break

                                                                                                                elif player_answer == 'b' or player_answer == 'c' or player_answer == 'd':
                                                                                                                    print('\nIncorrect!❌')
                                                                                                                    print('The correct answer was a) Functional\n')
                                                                                                                    game_over = True
                                                                                                                    break

                                                                                                                else:
                                                                                                                    print('Please enter a/b/c/d\n')

                                                                                                            break

                                                                                                        elif player_answer == 'a' or player_answer == 'b' or player_answer == 'd':
                                                                                                            print('\nIncorrect!❌')
                                                                                                            print('The correct answer was c) Hieronymus Bosch\n')
                                                                                                            game_over = True
                                                                                                            break

                                                                                                        else:
                                                                                                            print('Please enter a/b/c/d\n')

                                                                                                    break

                                                                                                elif player_answer == 'b' or player_answer == 'c' or player_answer == 'd':
                                                                                                    print('\nIncorrect!❌')
                                                                                                    print('The correct answer was a) 6\n')
                                                                                                    game_over = True
                                                                                                    break

                                                                                                else:
                                                                                                    print('Please enter a/b/c/d\n')

                                                                                            break

                                                                                        elif player_answer == 'a' or player_answer == 'c' or player_answer == 'd':
                                                                                            print('\nIncorrect!❌')
                                                                                            print('The correct answer was b) Titan\n')
                                                                                            game_over = True
                                                                                            break

                                                                                        else:
                                                                                            print('Please enter a/b/c/d\n')

                                                                                    break

                                                                                elif player_answer == 'b' or player_answer == 'c' or player_answer == 'd':
                                                                                    print('\nIncorrect!❌')
                                                                                    print('The correct answer was a) Cormac McCarthy\n')
                                                                                    game_over = True
                                                                                    break

                                                                                else:
                                                                                    print('Please enter a/b/c/d\n')

                                                                            break

                                                                        elif player_answer == 'a' or player_answer == 'c' or player_answer == 'd':
                                                                            print('\nIncorrect!❌')
                                                                            print('The correct answer was b) 443\n')
                                                                            game_over = True
                                                                            break

                                                                        else:
                                                                            print('Please enter a/b/c/d\n')

                                                                    break

                                                                elif player_answer == 'a' or player_answer == 'b' or player_answer == 'd':
                                                                    print('\nIncorrect!❌')
                                                                    print('The correct answer was c) Tungsten\n')
                                                                    game_over = True
                                                                    break

                                                                else:
                                                                    print('Please enter a/b/c/d\n')

                                                            break

                                                        elif player_answer == 'a' or player_answer == 'b' or player_answer == 'c':
                                                            print('\nIncorrect!❌')
                                                            print('The correct answer was d) FreeBSD\n')
                                                            game_over = True
                                                            break

                                                        else:
                                                            print('Please enter a/b/c/d\n')

                                                    break

                                                elif player_answer == 'a' or player_answer == 'c' or player_answer == 'd':
                                                    print('\nIncorrect!❌')
                                                    print('The correct answer was b) Mali\n')
                                                    game_over = True
                                                    break

                                                else:
                                                    print('Please enter a/b/c/d\n')

                                            break

                                        elif player_answer == 'b' or player_answer == 'c' or player_answer == 'd':
                                            print('\nIncorrect!❌')
                                            print('The correct answer was a) France\n')
                                            game_over = True
                                            break

                                        else:
                                            print('Please enter a/b/c/d\n')

                                    break

                                elif player_answer == 'a' or player_answer == 'b' or player_answer == 'd':
                                    print('\nIncorrect!❌')
                                    print('The correct answer was c) Total output\n')
                                    game_over = True
                                    break

                                else:
                                    print('Please enter a/b/c/d\n')

                            break

                        elif player_answer == 'a' or player_answer == 'c' or player_answer == 'd':
                            print('\nIncorrect!❌')
                            print('The correct answer was b) 9\n')
                            game_over = True
                            break

                        else:
                            print('Please enter a/b/c/d\n')

                    break

                elif player_answer == 'a' or player_answer == 'c' or player_answer == 'd':
                    print('\nIncorrect!❌')
                    print('The correct answer was b) 1998\n')
                    game_over = True
                    break

                else:
                    print('Please enter a/b/c/d\n')

            break

        elif player_answer == 'a' or player_answer == 'b' or player_answer == 'd':
            print('\nIncorrect!❌')
            print('The correct answer was c) K\n')
            game_over = True
            break

        else:
            print('Please enter a/b/c/d\n')

    if game_over:
        print('Game Over')
        print(f'You are taking home ${player_bank}\n')

  else:
    print('Enter p to play or h to view the help menu\n')      
