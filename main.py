from function import *

best_scores = download()  # Loading High scores
while True:
    pygame.display.set_caption("Mr'Driller")  # Initialization of the worksdow and the main variables
    icon = pygame.image.load(get_image("icon.png"))
    pygame.display.set_icon(icon)
    works, vie, score, page, level, restart = 1, 3, 0, 0, 0, False
    # As long as the game is open
    while works:
        if page == 0:  # selection of the menu page
            page = menu()
            print(page)
        elif page == 1:  # selection of the rules page
            page = rules()
            print(page)
        elif page == 2:  # selection of the game page
            if not restart:
                level += 1
            board = new_board(level)  # creating a new game board
            if level > 15:  # Maximum Level
                break
            text_level = "Niveau " + str(level)  # level initialization
            pygame.display.set_caption(text_level)
            posX, posY, position, current_height, value, air = 250, DEFAULT_Y, "FACE", 0, [0, 0], 100
            mixer.init()
            game_sound = mixer.Sound("sonJeu.ogg")
            # Level flow
            while True:
                game_sound.play()
                for event in pygame.event.get():
                    if event.type == QUIT:  # Leave the Game
                        pygame.quit()
                        exit(0)
                    if event.type == MOUSEBUTTONUP:  # Pause
                        if 601 < event.pos[0] < 749:
                            if 740 < event.pos[1] < 783:
                                pause()
                if lose(vie):  # All lives are lost
                    works = 0
                    best_scores.append(score)
                    display(board, posX, posY, position, current_height, vie, air, score, best_scores, level)
                    display_lose()
                    time.sleep(8)
                    game_sound.stop()
                    mixer.quit()
                    break
                elif winner(posY, current_height, level):  # The level is won
                    display(board, posX, posY, position, current_height, vie, air, score, best_scores, level)
                    time.sleep(1)
                    break
                air, vie = percentAir(air, vie, value)  # air management
                display(board, posX, posY, position, current_height, vie, air, score, best_scores, level)  # display management
                posX, posY, position, value, score, air = move(board, posX, posY, position, current_height, score, level, air)  # displacement management
                board, posY, current_height = gravity(board, posX, posY, current_height, level)  # gravity management
                vie, air, restart = checkPosition(board, posY, posX, score, air, vie, level, current_height)  # position management
                if restart:  # We have to restart the level
                    break
        elif page == 3:  # selection of the rules page
            page = scores(best_scores)
            print(page)
        save(best_scores)  # save high scores
