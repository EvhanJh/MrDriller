from constante import *


def pixel_case(pixel, level, default=0, current_height=0):
    """
    Convert a number of pixels to a number of boxes
    :param pixel: number of pixels (int)
    :param level: level number (int)
    :param default: default number of pixels (int)
    :param current_height: current height of the character (int)
    :return: number of boxes (int)
    """
    if PROFONDEUR * level - current_height - 1 <= 11:
        current_height = PROFONDEUR * level - 12
    return math.floor((pixel - default + (current_height * SIZE_CASE)) / (SIZE_CASE + 1))


def case_pixel(case, level, default=0, current_height=0):
    """
    Convert a number of boxes to a number of pixels
    :param case: number of boxes (int)
    :param level: level number (int)
    :param default: default number of pixels (int)
    :param current_height: current height of the character (int)
    :return: number of pixels (int)
    """
    if PROFONDEUR * level - current_height - 1 <= 11:
        current_height = PROFONDEUR * level - 12
    return case * (SIZE_CASE + 1) + default - (current_height * SIZE_CASE)


def new_board(level):
    """
    Create a new game board with a random draw of the blocks
    :param level: level number (int)
    :return: game board (array of int)
    """
    nb_capsules_air = 0
    board = [[0] * LARGEUR for i in range(PROFONDEUR * level)]
    for x in range(LARGEUR):
        board[0][x] = [0, 0]
    if level == 1:
        for y in range(1, 6):
            for x in range(LARGEUR):
                board[y][x] = [5, 5]
        start = LARGEUR // 2
        end = start + 1
        type_bloc = 1
        for y in range(1, 6):
            for x in range(start, end):
                board[y][x] = [type_bloc, 1]
            start -= 1
            end += 1
            if type_bloc == 4:
                type_bloc = 1
            else:
                type_bloc += 1
        type_bloc = 3
        for y in range(6, 8):
            for x in range(LARGEUR):
                board[y][x] = [type_bloc, 1]
            type_bloc += 1
        board[7][start] = [6, 1]
        for y in range(8, PROFONDEUR * level):
            for x in range(LARGEUR):
                while True:
                    num_bloc = random.randint(1, 6)
                    if num_bloc == 6:
                        if not nb_capsules_air >= MAX_CAPSULES - 2 * level:
                            nb_capsules_air += 1
                            break
                    else:
                        break
                if num_bloc == 5:
                    value = [num_bloc, 5]
                else:
                    value = [num_bloc, 1]
                board[y][x] = value
    else:
        for x in range(LARGEUR):
            board[1][x] = [random.randint(1, 4), 1]
        for y in range(2, PROFONDEUR * level):
            for x in range(LARGEUR):
                while True:
                    num_bloc = random.randint(1, 6)
                    if num_bloc == 6:
                        if not nb_capsules_air >= MAX_CAPSULES - 2 * level:
                            nb_capsules_air += 1
                            break
                    else:
                        break
                if num_bloc == 5:
                    value = [num_bloc, 5]
                else:
                    value = [num_bloc, 1]
                board[y][x] = value
    return board


def display_character(position, posX, posY, current_height, level):
    """
    Displays the character's view at a given position
    :param position: indicates the view of the character (string)
    :param posX: position in X (int)
    :param posY: position in Y (int)
    :param current_height: current height of the character (int)
    :param level: level number (int)
    """
    if position == "FACE":
        character = PERSO[0]
    elif position == "DOWN":
        character = PERSO[1]
    elif position == "RIGHT":
        character = PERSO[2]
    elif position == "LEFT":
        character = PERSO[3]
    elif position == "UP":
        character = PERSO[4]
    WINDOW.blit(character, (posX, normalisationPixel(current_height, posY, level)))


def display_info(current_height, life, air, best_scores, score):
    """
    Displays character information and scores
    :param current_height: current height of the character (int)
    :param life: number of life of the character (int)
    :param air: percentage of air remaining (int)
    :param best_scores: high score table (array of int)
    :param score: current score of the character (int)
    """
    zone_y = 0
    high_led = pygame.image.load(get_image("lampe_allumee.png"))
    for i in range(len(TITLE_INFO)):
        WINDOW.blit(TITLE_INFO[i], (560, zone_y))
        contour_aire = pygame.image.load(get_image("contour_aire.png"))
        WINDOW.blit(contour_aire, (634, 201))
        if random.randint(0, 1):
            WINDOW.blit(high_led, (560, zone_y + 2))
        if i == 0:
            altitude = current_height * 25
            text_altitude = pygame.font.Font(POLICE, 25).render("{:06d}".format(altitude), True, BLACK)
            WINDOW.blit(text_altitude, (650, zone_y + 55))
        if i == 1:
            pygame.draw.line(WINDOW, WHITE, (635, zone_y + 70), (760, zone_y + 70), 20)
            pygame.draw.line(WINDOW, DARK_BLUE, (640, zone_y + 70), (655 + air, zone_y + 70), 10)
        if i == 2:
            heart = HEART[0]
            broken_heart = HEART[1]
            if life == 3:
                WINDOW.blit(heart, (710, zone_y + 55))
                WINDOW.blit(heart, (680, zone_y + 55))
                WINDOW.blit(heart, (650, zone_y + 55))
            elif life == 2:
                WINDOW.blit(heart, (710, zone_y + 55))
                WINDOW.blit(heart, (680, zone_y + 55))
                WINDOW.blit(broken_heart, (650, zone_y + 55))
            elif life == 1:
                WINDOW.blit(heart, (710, zone_y + 55))
                WINDOW.blit(broken_heart, (680, zone_y + 55))
                WINDOW.blit(broken_heart, (650, zone_y + 55))
            else:
                WINDOW.blit(broken_heart, (710, zone_y + 55))
                WINDOW.blit(broken_heart, (680, zone_y + 55))
                WINDOW.blit(broken_heart, (650, zone_y + 55))
        if i == 3:
            text_score = pygame.font.Font(POLICE, 25).render("{:06d}".format(score), True, BLACK)
            WINDOW.blit(text_score, (650, zone_y + 55))
        if i == 4:
            text_best_scores = pygame.font.Font(POLICE, 25).render("{:06d}".format(max(best_scores)), True, BLACK)
            WINDOW.blit(text_best_scores, (650, zone_y + 55))
        zone_y += 140


def display_bloc(board, start, height, level):
    """
    Displays the correct concrete blocks according to the overall positioning
    :param board: Board Game (array of int)
    :param start: starting point to display the blocks (int)
    :param height: block height (int)
    :param level: level number (int)
    """
    hauteur = PROFONDEUR * level
    for y in range(start, hauteur):
        abs = 0
        for x in range(0, LARGEUR):
            if board[y][x][0] == 1:
                bloc = chooseBloc(board, x, y, 1, level)
                WINDOW.blit(bloc, (abs, height))
            elif board[y][x][0] == 2:
                bloc = chooseBloc(board, x, y, 2, level)
                WINDOW.blit(bloc, (abs, height))
            elif board[y][x][0] == 3:
                bloc = chooseBloc(board, x, y, 3, level)
                WINDOW.blit(bloc, (abs, height))
            elif board[y][x][0] == 4:
                bloc = chooseBloc(board, x, y, 4, level)
                WINDOW.blit(bloc, (abs, height))
            elif board[y][x][0] == 5:
                status_tnt = ("bloc_tnt" + str(board[y][x][1]) + ".png")
                bloc = pygame.image.load(get_image(status_tnt))
                WINDOW.blit(bloc, (abs, height))
            elif board[y][x][0] == 6:
                bloc = pygame.image.load(get_image("air.png"))
                WINDOW.blit(bloc, (abs, height))
            abs += 50
        height += 50


def chooseBloc(board, x, y, typeBloc, level):
    """
    Choose the right block according to the arrangement
    :param board: Board game (array of int)
    :param x: X position of the block (int)
    :param y: Y position of the block (int)
    :param typeBloc: block color (int)
    :param level: level number (int)
    :return: picture corresponding to the block
    """
    position = fusion_bloc(board, x, y, typeBloc, level)
    if typeBloc == 1:
        table = YELLOW_BLOC
    elif typeBloc == 2:
        table = RED_BLOC
    elif typeBloc == 3:
        table = BLUE_BLOC
    elif typeBloc == 4:
        table = GREEN_BLOC
    bloc = table[0]
    if position == [0, 0, 0, 1]:
        bloc = table[1]
    elif position == [0, 0, 1, 0]:
        bloc = table[2]
    elif position == [0, 0, 1, 1]:
        bloc = table[3]
    elif position == [0, 1, 0, 0]:
        bloc = table[4]
    elif position == [0, 1, 0, 1]:
        bloc = table[5]
    elif position == [0, 1, 1, 0]:
        bloc = table[6]
    elif position == [0, 1, 1, 1]:
        bloc = table[7]
    elif position == [1, 0, 0, 0]:
        bloc = table[8]
    elif position == [1, 0, 0, 1]:
        bloc = table[9]
    elif position == [1, 0, 1, 0]:
        bloc = table[10]
    elif position == [1, 0, 1, 1]:
        bloc = table[11]
    elif position == [1, 1, 0, 0]:
        bloc = table[12]
    elif position == [1, 1, 0, 1]:
        bloc = table[13]
    elif position == [1, 1, 1, 0]:
        bloc = table[14]
    elif position == [1, 1, 1, 1]:
        bloc = table[15]
    return bloc


def fusion_bloc(board, x, y, typeBloc, level):
    """
    Lets you know the formation of block groupings
    :param board: Board Game (array of int)
    :param x: X position of the block (int)
    :param y: Y position of the block (int)
    :param typeBloc: block color (int)
    :param level: level number (int)
    :return: code corresponding to the good formation of the block
    """
    position = [0] * 4
    # 1ère case gauche / 2ème haut / 3 ème bas / 4ème droite
    if x + 1 < LARGEUR:
        if board[y][x + 1][0] == typeBloc:
            position[3] = 1
    if x - 1 >= 0:
        if board[y][x - 1][0] == typeBloc:
            position[0] = 1
    if y + 1 < PROFONDEUR * level:
        if board[y + 1][x][0] == typeBloc:
            position[2] = 1
    if y - 1 >= 0:
        if board[y - 1][x][0] == typeBloc:
            position[1] = 1
    return position


def display_title(current_height, level):
    """
    Shows the title in the right place and calculates the block run limit
    :param current_height: current height of the character (int)
    :param level: level number (int)
    :return: title height and run limit (int)
    """
    tmp = 0
    title = pygame.image.load(get_image("game_title.png"))
    if current_height == 0:
        height = 150
        WINDOW.blit(title, (115, 0))
    elif current_height == 1:
        height = 100
        WINDOW.blit(title, (115, -50))
    elif current_height == 2:
        height = 50
        WINDOW.blit(title, (115, -100))
    else:
        height = 0
        if (PROFONDEUR * level) - 1 - current_height < 12:
            tmp = (PROFONDEUR - 1) * level - 15 + level
            footer_brouette = pygame.image.load(get_image("brouette.png"))
            WINDOW.blit(footer_brouette, (110, 750))
            footer_duck = pygame.image.load(get_image("duck.png"))
            WINDOW.blit(footer_duck, (50, 760))
            footer_barriere = pygame.image.load(get_image("barriere.png"))
            WINDOW.blit(footer_barriere, (270, 770))
            footer_brouette = pygame.image.load(get_image("buldozer.png"))
            WINDOW.blit(footer_brouette, (350, 760))
        else:
            tmp = current_height - 3
    return height, tmp


def display(board, posX, posY, position, current_height, life, air, score, best_scores, level):
    """
    Displays all the graphics on the game board
    :param board: Board Game (array of int)
    :param posX: X position of the character (int)
    :param posY: Y position of the character (int)
    :param position: indicates the view of the character (string)
    :param current_height: current height of the character (int)
    :param life: number of life of the character (int)
    :param air: percentage of air remaining (int)
    :param score: player score (int)
    :param best_scores: high score table (array of int)
    :param level: level number (int)
    """
    background = pygame.image.load(get_image("background.png"))
    WINDOW.blit(background, (0, 0))
    pygame.draw.rect(WINDOW, BROWN, (553, 0, 800, 800))
    background_info = pygame.image.load(get_image("font_concrete.png"))
    WINDOW.blit(background_info, (WINDOW.get_width() - background_info.get_width(), 0))
    pygame.draw.line(WINDOW, DARK_BROWN, (552, 0), (552, 800), 5)
    bloc_pause = pygame.image.load(get_image("pause.png"))
    WINDOW.blit(bloc_pause, (WINDOW.get_width() - background_info.get_width() / 2 - bloc_pause.get_width() / 2,
                             WINDOW.get_height() - bloc_pause.get_height()))
    switch_pause = pygame.image.load(get_image("variateur_pause.png"))
    WINDOW.blit(switch_pause, (671, 776))
    ordo, tmp = display_title(current_height, level)
    display_bloc(board, tmp, ordo, level)
    display_character(position, posX, posY, current_height, level)
    display_info(current_height, life, air, best_scores, score)
    pygame.display.update()


def move(board, posX, posY, position, current_height, score, level, air):
    """
    Realize the movement of the character and its consequences
    :param board: Board Game (array of int)
    :param posX: X position of the character (int)
    :param posY: Y position of the character (int)
    :param position: indicates the view of the character (string)
    :param current_height: current height of the character (int)
    :param score: player score (int)
    :param level: level number (int)
    :param air: percentage of air remaining (int)
    :return: the coordinates and consequences of the displacement
    """
    size_move, value = 25, [0, 0]
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(0)
        if event.type == MOUSEBUTTONUP:
            if 671 < event.pos[0] < 671 + 14:
                if 776 < event.pos[1] < 776 + 19:
                    check_pause = pygame.image.load(get_image("on_green.png"))
                    WINDOW.blit(check_pause, (694, 725))
                    close_pause = pygame.image.load(get_image("on_red.png"))
                    WINDOW.blit(close_pause, (641, 725))
                    pause()
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                posY += size_move
                if not check_move(board, "K_DOWN", posX, posY, current_height, level):
                    posY -= size_move
                position = "DOWN"
            elif event.key == K_RIGHT:
                posX += size_move
                if not check_move(board, "K_RIGHT", posX, posY, current_height, level):
                    posX -= size_move
                    if position == "RIGHT":
                        posX, posY = check_move_jump(board, "K_RIGHT", posX, posY, current_height, level)
                position = "RIGHT"
            elif event.key == K_LEFT:
                posX -= size_move
                if not check_move(board, "K_LEFT", posX, posY, current_height, level):
                    posX += size_move
                    if position == "LEFT":
                        posX, posY = check_move_jump(board, "K_LEFT", posX, posY, current_height, level)
                position = "LEFT"
            elif event.key == K_UP:
                position = "UP"
            elif event.key == K_SPACE:
                if position == "RIGHT":
                    if pixel_case(posX, level) + 1 < LARGEUR:
                        parameters = [pixel_case(posX, level) + 1, pixel_case(posY, level, DEFAULT_Y, current_height)]
                        board, score, value, air = moveAndScore(board, score,
                                                                board[
                                                                    pixel_case(posY, level, DEFAULT_Y, current_height)][
                                                                    pixel_case(posX, level) + 1], parameters, air)
                elif position == "LEFT":
                    if pixel_case(posX, level) - 1 >= 0:
                        parameters = [pixel_case(posX, level) - 1, pixel_case(posY, level, DEFAULT_Y, current_height)]
                        board, score, value, air = moveAndScore(board, score,
                                                                board[
                                                                    pixel_case(posY, level, DEFAULT_Y, current_height)][
                                                                    pixel_case(posX, level) - 1], parameters, air)
                elif position == "DOWN":
                    if pixel_case(posY, DEFAULT_Y, current_height) + 1 < PROFONDEUR * level:
                        parameters = [pixel_case(posX, level), pixel_case(posY, level, DEFAULT_Y, current_height) + 1]

                        board, score, value, air = moveAndScore(board, score,
                                                                board[
                                                                    pixel_case(posY, level, DEFAULT_Y,
                                                                               current_height) + 1][
                                                                    pixel_case(posX, level)], parameters, air)
                elif position == "UP":
                    if pixel_case(posY, DEFAULT_Y, current_height) - 1 >= 0:
                        parameters = [pixel_case(posX, level), pixel_case(posY, level, DEFAULT_Y, current_height) - 1]
                        board, score, value, air = moveAndScore(board, score,
                                                                board[
                                                                    pixel_case(posY, level, DEFAULT_Y,
                                                                               current_height) - 1][
                                                                    pixel_case(posX, level)], parameters, air)
    return posX, posY, position, value, score, air


def check_move(board, type_move, posX, posY, current_height, level):
    """
    Check if the movement of the character is possible
    :param board: Board Game (array of int)
    :param type_move: desired movement (string)
    :param posX: X position of the character (int)
    :param posY: Y position of the character (int)
    :param current_height: current height of the character (int)
    :param level: level number (int)
    :return: (bool)
    """
    if type_move == "K_DOWN":
        if pixel_case(posY + SIZE_CASE, level, DEFAULT_Y) < PROFONDEUR * level and pixel_case(posX + SIZE_CASE,
                                                                                              level) < LARGEUR:
            if board[pixel_case(posY + SIZE_CASE, level, DEFAULT_Y)][pixel_case(posX, level)][0] == 0:
                if board[pixel_case(posY + SIZE_CASE, level, DEFAULT_Y)][pixel_case(posX + SIZE_CASE, level)][0] == 0:
                    return True
                elif board[pixel_case(posY + SIZE_CASE, level, DEFAULT_Y)][pixel_case(posX + SIZE_CASE, level)][0] == 6:
                    return True
    elif type_move == "K_RIGHT":
        if pixel_case(posX + SIZE_CASE, level) < LARGEUR:
            if board[pixel_case(posY, level, DEFAULT_Y, current_height)][pixel_case(posX + SIZE_CASE, level)][0] == 0:
                return True
            elif board[pixel_case(posY, level, DEFAULT_Y, current_height)][pixel_case(posX + SIZE_CASE, level)][0] == 6:
                return True
    elif type_move == "K_LEFT":
        if pixel_case(posX, level) >= 0:
            if board[pixel_case(posY, level, DEFAULT_Y, current_height)][pixel_case(posX, level)][0] == 0:
                return True
            elif board[pixel_case(posY, level, DEFAULT_Y, current_height)][pixel_case(posX, level)][0] == 6:
                return True
    return False


def check_move_jump(board, type_move, posX, posY, current_height, level):
    """
    Check that the jumps of the character above the blocks are possible
    :param board: Board game (array of int)
    :param type_move: desired movement (string)
    :param posX: X position of the character (int)
    :param posY: Y position of the character (int)
    :param current_height: current height of the character (int)
    :param level: level number (int)
    :return: the coordinates (int)
    """
    if type_move == "K_RIGHT":
        if pixel_case(posX, level) + 1 < LARGEUR and posY > 0:
            if board[pixel_case(posY, level, DEFAULT_Y, current_height) - 1][pixel_case(posX, level) + 1][0] == 0 or \
                    board[pixel_case(posY, level, DEFAULT_Y, current_height) - 1][pixel_case(posX, level) + 1][0] == 6:
                posY = case_pixel(pixel_case(posY, level, DEFAULT_Y, current_height) - 1, level, DEFAULT_Y,
                                  current_height)
                posX = case_pixel(pixel_case(posX, level) + 1, level)
    elif type_move == "K_LEFT":
        if pixel_case(posX, level) - 1 > 0 and posY > 0:
            if board[pixel_case(posY, level, DEFAULT_Y, current_height) - 1][pixel_case(posX, level) - 1][0] == 0 or \
                    board[pixel_case(posY, level, DEFAULT_Y, current_height) - 1][pixel_case(posX, level) - 1][0] == 6:
                posY = case_pixel(pixel_case(posY, level, DEFAULT_Y, current_height) - 1, level, DEFAULT_Y,
                                  current_height)
                posX = case_pixel(pixel_case(posX, level) - 1, level)
    return posX, posY


def gravity(board, posX, posY, current_height, level):
    """
    Manages gravity in its entirety
    :param board: Board Game (array of int)
    :param posX: X position of the character (int)
    :param posY: Y position of the character (int)
    :param current_height: current height of the character (int)
    :param level: level number (int)
    :return: the game board (array of int) and the new coordinates (int)
    """
    while True:
        i = 0
        for x in range(LARGEUR):
            for y in range(PROFONDEUR * level):
                if board[y][x][0] >= 1:
                    type_bloc = board[y][x][0]
                    if x + 1 < LARGEUR and x - 1 >= 0:
                        if (type_bloc != board[y][x + 1][0] and type_bloc != board[y][x - 1][0]) or (
                                type_bloc == 5 and y > 5):
                            i, board = gravityEffect(board, x, y, level, i, current_height)
                        else:
                            board, i = groupGravity(board, y, x, level, i, current_height)
                    elif x == LARGEUR - 1:
                        if type_bloc != board[y][x - 1]:
                            i, board = gravityEffect(board, x, y, level, i, current_height)
                        else:
                            board, i = groupGravity(board, y, x, level, i, current_height)
                    elif x == 0:
                        if type_bloc != board[y][x + 1]:
                            i, board = gravityEffect(board, x, y, level, i, current_height)
                        else:
                            board, i = groupGravity(board, y, x, level, i, current_height)
        if i == 0:
            break
    posXX, posX = pixel_case(posX + SIZE_CASE, level), pixel_case(posX, level)
    while True:
        posYY = pixel_case(posY + SIZE_CASE, level, DEFAULT_Y, current_height)
        posY = pixel_case(posY, level, DEFAULT_Y, current_height)
        if posY + 1 < PROFONDEUR * level and posYY + 1 < PROFONDEUR * level:
            if board[posY + 1][posX][0] == 0 or board[posY + 1][posX][0] == 6:
                if board[posYY + 1][posXX][0] == 0 or board[posYY + 1][posXX][0] == 6:
                    posY += 1
                    if posY > current_height:
                        current_height += 1
                    posY = case_pixel(posY, level, DEFAULT_Y, current_height)
                else:
                    break
            else:
                break
        else:
            break
    posY = case_pixel(posY, level, DEFAULT_Y, current_height)
    return board, posY, current_height


def checkPosition(board, posY, posX, score, air, vie, level, current_height):
    """
    Check if the character has a correct position,
    more exactly if it is not overwritten by a block
    :param board: Board Game (array of int)
    :param posY: Y position of the character (int)
    :param posX: X position of the character (int)
    :param score: player score (int)
    :param air: percentage of air remaining (int)
    :param vie: number of lives of the characters
    :param level: level number (int)
    :param current_height: current height of the character (int)
    :return: the characters info (int)
    """
    restart = False
    posX = pixel_case(posX, level)
    posY = pixel_case(posY, level, DEFAULT_Y, current_height)
    if board[posY][posX][0] != 0 and board[posY][posX][0] != 6:
        vie -= 1
        restart = True
    elif board[posY][posX][0] == 6:
        board[posY][posX] = (0, 0)
        score += 10
        air += 20
    return vie, air, restart


def gravityEffect(board, x, y, level, i, current_height):
    """
    Manages fall effects for gravity
    :param board: Board Game (array of int)
    :param x: X position of the character (int)
    :param y: Y position of the character (int)
    :param level: level number (int)
    :param i: testifies if a block has dropped (int)
    :param current_height: current height of the character (int)
    :return: Board Game (array of int)
    """
    if y + 1 < PROFONDEUR * level and board[y + 1][x][0] == 0:
        tmp_value = board[y][x]
        board[y][x] = (0, 0)
        board[y + 1][x] = tmp_value
        i += 1
        board = gravityDestruction(board, y, x)
    return i, board


def groupGravity(board, y, x, level, i, current_height):
    """
    Organize block grouping
    :param board: Board Game (array of int)
    :param y: Y position of the character (int)
    :param x: X position of the character (int)
    :param level: level number (int)
    :param i: testifies if a block has dropped (int)
    :param current_height: current height of the character (int)
    :return: Board Game (array of int)
    """
    posBloc = propagation(board, x, y)
    possibleFall = True
    for bloc in posBloc:
        if bloc[0] + 1 < PROFONDEUR and board[bloc[0] + 1][bloc[1]][0] != 0:
            possibleFall = False
            break
    if possibleFall:
        i, board = gravityEffect(board, x, y, level, i, current_height)
    return board, i


def gravityDestruction(board, y, x):
    """
    Manages the destruction of the blocks at the fall
    :param board: Board Game (array of int)
    :param y: Y position of the character (int)
    :param x: X position of the character (int)
    :return: Board Game (array of int)
    """
    if y + 1 < PROFONDEUR:
        posBloc = propagation(board, x, y + 1)
        if len(posBloc) >= 4:
            board = destruction(posBloc, board)
    return board


def moveAndScore(board, score, case, parameters, air):
    """
    Manages the scores
    :param board: Board Game (array of int)
    :param score: player score (int)
    :param case:
    :param parameters: the coordinates
    :param air: percentage of air remaining
    :return: Game board and modified character settings (int)
    """
    value = [0, 0]
    if case[1] != 0:
        case[1] -= 1
        value[0] = case[0]
        value[1] = case[1]
        if case[1] == 0:
            posBloc = propagation(board, parameters[0], parameters[1])
            if case[0] == 5:
                score -= 20
                air -= 20
                board = destruction([(parameters[1], parameters[0])], board)
            elif case[0] == 6:
                score += 10
                air += 20
                board = destruction([(parameters[1], parameters[0])], board)
            else:
                score += 5 * len(posBloc)
                board = destruction(posBloc, board)
        else:
            score -= 1

    return board, score, value, air


def normalisationPixel(current_height, posY, level):
    if current_height <= PROFONDEUR * level - 12:
        if posY > 150:
            return 150
    if current_height == 0:
        return posY - current_height
    else:
        return posY - current_height + 5


def percentAir(air, vie, value):
    """
    Calculates the percentage of remaining air
    :param air: percentage of remaining air (int)
    :param vie: number of remaining lifes (int)
    :param value: 2-dimensional table to know the type of block used
    :return: percentage of air and number of lives remaining (int)
    """
    air -= 0.1
    if value[0] == 6:
        air += 20
    elif value[1] == 5:
        air -= 20
    if air > 100:
        air = 100
    elif air <= 0:
        vie -= 1
        air = 100
    return air, vie


def winner(posY, current_height, level):
    """
    Check if the player has won
    :param posY: Y position of the character (int)
    :param current_height: current height of the character (int)
    :param level: level number (int)
    :return: (bool)
    """
    if pixel_case(posY, level, DEFAULT_Y, current_height) == (PROFONDEUR * level) - 1:
        return True
    return False


def lose(vie):
    """
    Check if the player has lost all their lives
    :param vie: number of remaining lifes (int)
    :return: (bool)
    """
    if vie == 0:
        return True
    return False


def display_lose():
    """
    Display in case the player has lost
    """
    lost_banner = pygame.image.load(get_image("info_lose.png"))
    WINDOW.blit(lost_banner, (225, 0))
    pygame.display.update()


def menu():
    """
    View and manage the menu
    :return: code of the selected page
    """
    menu = pygame.image.load(get_image("menu.png"))
    WINDOW.blit(menu, (0, 0))
    run_banner = pygame.image.load(get_image("run_banner.png"))
    WINDOW.blit(run_banner, (253, 454))
    rules_banner = pygame.image.load(get_image("rules_banner.png"))
    WINDOW.blit(rules_banner, (236, 544))
    trophy_best_score = pygame.image.load(get_image("trophy_best_score.png"))
    WINDOW.blit(trophy_best_score, (439, 454))
    pygame.display.update()

    pressed = False
    mixer.init()
    son = mixer.Sound("sonMenu.ogg")
    while not pressed:
        son.play()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(0)
            if event.type == MOUSEBUTTONUP:
                if 253 < event.pos[0] < 253 + 117 and 454 < event.pos[1] < 454 + 60:
                    son.stop()
                    mixer.quit()
                    return 2
                if 236 < event.pos[0] < 236 + 117:
                    if 544 < event.pos[1] < 544 + 60:
                        return 1
                if 439 < event.pos[0] < 439 + 62:
                    if 454 < event.pos[1] < 454 + 114:
                        return 3


def rules():
    """
    View and manage the rules page
    :return: Leave the page (int)
    """
    rules = pygame.image.load(get_image("rules_page.png"))
    WINDOW.blit(rules, (0, 0))
    button_exit = pygame.image.load(get_image("button_exit.png"))
    WINDOW.blit(button_exit, (576, 610))
    pygame.display.update()

    pressed = False

    while not pressed:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(0)
            if event.type == MOUSEBUTTONUP:
                if 576 < event.pos[0] < 576 + 117 and 610 < event.pos[1] < 610 + 60:
                    return 0


def scores(best_scores):
    """
    Display of the scores page
    :param best_scores:
    :return:
    """
    page_score = pygame.image.load(get_image("score_page.png"))
    WINDOW.blit(page_score, (0, 0))
    button_exit = pygame.image.load(get_image("button_exit.png"))
    WINDOW.blit(button_exit, (576, 610))
    pygame.display.update()
    pressed = False
    best_scores.sort(reverse=True)
    for i in range(3):
        text = pygame.font.Font(POLICE, 20).render(str(best_scores[i]), True, (70, 44, 19))
        WINDOW.blit(text, (436, 360 + 120 * i))
        pygame.display.update()
    while not pressed:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(0)
            if event.type == MOUSEBUTTONUP:
                if 576 < event.pos[0] < 576 + 117 and 610 < event.pos[1] < 610 + 60:
                    return 0


def save(best_scores):
    """
    Manages the backup of high scores
    :param best_scores: high score table (array of int)
    """
    file = open('score.json', "w")
    file.write(json.dumps(best_scores))
    file.close()


def download():
    """
    Manages the recovery of high scores
    :return: high score table (array of int)
    """
    file = open("score.json", "r")
    best_scores = json.loads(file.readline())
    file.close()
    return best_scores


def pause():
    """
    Manages the page and pause position
    """
    background = pygame.image.load(get_image("background.png"))
    WINDOW.blit(background, (0, 0))
    iddle = pygame.image.load(get_image("iddle.png"))
    WINDOW.blit(iddle, (150, 260))
    pygame.display.update()
    go = True
    while go:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(0)
            if event.type == MOUSEBUTTONUP:
                if 671 < event.pos[0] < 671 + 14:
                    if 776 < event.pos[1] < 776 + 19:
                        check_pause = pygame.image.load(get_image("on_green.png"))
                        WINDOW.blit(check_pause, (671, 776))
                        go = False
                        break


def propagation(board, posX, posY):
    """
    Calculate the position of all the identical blocks and glued to the base block
    :param board: Board Game (array of int)
    :param posX: X position of the character (int)
    :param posY: Y position of the character (int)
    :return: table of the position of all the blocks (array of int)
    """
    posBloc = [(posY, posX)]
    while True:
        change = False
        for i in range(0, len(posBloc)):
            y = posBloc[i][0]
            x = posBloc[i][1]
            value = board[y][x][0]
            if value != 6:
                if x - 1 >= 0 and board[y][x - 1][0] == value:
                    if not (y, x - 1) in posBloc:
                        posBloc.append((y, x - 1))
                        change = True
                if x + 1 < LARGEUR and board[y][x + 1][0] == value:
                    if not (y, x + 1) in posBloc:
                        posBloc.append((y, x + 1))
                        change = True
                if y + 1 < PROFONDEUR and board[y + 1][x][0] == value:
                    if not (y + 1, x) in posBloc:
                        posBloc.append((y + 1, x))
                        change = True
                if y - 1 >= 0 and board[y - 1][x][0] == value:
                    if not (y - 1, x) in posBloc:
                        posBloc.append((y - 1, x))
                        change = True
        if not change:
            break
    return posBloc


def destruction(posBloc, board):
    """
    Manages the destruction of a group of blocks that falls
    :param posBloc: array of coordinates of all the identical blocks glued to the central block (array of int)
    :param board: Game Board (array of int)
    :return: Game Board
    """
    for pos in posBloc:
        board[pos[0]][pos[1]] = (0, 0)
    return board


