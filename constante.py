from library import *


def get_image(name):
    return "image\\" + name


HAUTEUR = 800
LONGUEUR = 800
LARGEUR = 11
PROFONDEUR = 20

GREY = (143, 143, 143)
BROWN = (103, 81, 60)
BLACK = (0, 0, 0)
DARK_BROWN = (84, 64, 44)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
DARK_BLUE = (28, 59, 77)
POLICE = "ArcadeAlternate.ttf"
TRANSPARENT = (255, 255, 255, 0)
SIZE_CASE = 49
DEFAULT_Y = 150
MAX_CAPSULES = 20

pygame.init()
WINDOW = pygame.display.set_mode((LONGUEUR, HAUTEUR))

TITLE_INFO = [pygame.image.load(get_image("altitude_title.png")), pygame.image.load(get_image("air_title.png")),
              pygame.image.load(get_image("vie_title.png")), pygame.image.load(get_image("score_title.png")),
              pygame.image.load(get_image("best_score_title.png"))]

HEART = [pygame.image.load(get_image("heart.png")), pygame.image.load(get_image("heart_dead.png"))]
PERSO = [pygame.image.load(get_image("init_mineur.png")), pygame.image.load(get_image("bas_mineur.png")),
         pygame.image.load(get_image("droite_mineur.png")), pygame.image.load(get_image("gauche_mineur.png")),
         pygame.image.load(get_image("haut_mineur.png"))]

GREEN_BLOC = [0] * 16
RED_BLOC = [0] * 16
YELLOW_BLOC = [0] * 16
BLUE_BLOC = [0] * 16

GREEN_BLOC[0] = pygame.image.load(get_image("bloc_green.png"))
GREEN_BLOC[1] = pygame.image.load(get_image("horizontal_left_green.png"))
GREEN_BLOC[2] = pygame.image.load(get_image("vertical_top_green.png"))
GREEN_BLOC[3] = pygame.image.load(get_image("corner_top_left_green.png"))
GREEN_BLOC[4] = pygame.image.load(get_image("vertical_bottom_green.png"))
GREEN_BLOC[5] = pygame.image.load(get_image("corner_bottom_left_green.png"))
GREEN_BLOC[6] = pygame.image.load(get_image("vertical_middle_green.png"))
GREEN_BLOC[7] = pygame.image.load(get_image("full_border_left_green.png"))
GREEN_BLOC[8] = pygame.image.load(get_image("horizontal_right_green.png"))
GREEN_BLOC[9] = pygame.image.load(get_image("horizontal_middle_green.png"))
GREEN_BLOC[10] = pygame.image.load(get_image("corner_top_right_green.png"))
GREEN_BLOC[11] = pygame.image.load(get_image("full_border_top_green.png"))
GREEN_BLOC[12] = pygame.image.load(get_image("corner_bottom_right_green.png"))
GREEN_BLOC[13] = pygame.image.load(get_image("full_border_bottom_green.png"))
GREEN_BLOC[14] = pygame.image.load(get_image("full_border_right_green.png"))
GREEN_BLOC[15] = pygame.image.load(get_image("full_bloc_green.png"))

RED_BLOC[0] = pygame.image.load(get_image("bloc_red.png"))
RED_BLOC[1] = pygame.image.load(get_image("horizontal_left_red.png"))
RED_BLOC[2] = pygame.image.load(get_image("vertical_top_red.png"))
RED_BLOC[3] = pygame.image.load(get_image("corner_top_left_red.png"))
RED_BLOC[4] = pygame.image.load(get_image("vertical_bottom_red.png"))
RED_BLOC[5] = pygame.image.load(get_image("corner_bottom_left_red.png"))
RED_BLOC[6] = pygame.image.load(get_image("vertical_middle_red.png"))
RED_BLOC[7] = pygame.image.load(get_image("full_border_left_red.png"))
RED_BLOC[8] = pygame.image.load(get_image("horizontal_right_red.png"))
RED_BLOC[9] = pygame.image.load(get_image("horizontal_middle_red.png"))
RED_BLOC[10] = pygame.image.load(get_image("corner_top_right_red.png"))
RED_BLOC[11] = pygame.image.load(get_image("full_border_top_red.png"))
RED_BLOC[12] = pygame.image.load(get_image("corner_bottom_right_red.png"))
RED_BLOC[13] = pygame.image.load(get_image("full_border_bottom_red.png"))
RED_BLOC[14] = pygame.image.load(get_image("full_border_right_red.png"))
RED_BLOC[15] = pygame.image.load(get_image("full_bloc_red.png"))

BLUE_BLOC[0] = pygame.image.load(get_image("bloc_blue.png"))
BLUE_BLOC[1] = pygame.image.load(get_image("horizontal_left_blue.png"))
BLUE_BLOC[2] = pygame.image.load(get_image("vertical_top_blue.png"))
BLUE_BLOC[3] = pygame.image.load(get_image("corner_top_left_blue.png"))
BLUE_BLOC[4] = pygame.image.load(get_image("vertical_bottom_blue.png"))
BLUE_BLOC[5] = pygame.image.load(get_image("corner_bottom_left_blue.png"))
BLUE_BLOC[6] = pygame.image.load(get_image("vertical_middle_blue.png"))
BLUE_BLOC[7] = pygame.image.load(get_image("full_border_left_blue.png"))
BLUE_BLOC[8] = pygame.image.load(get_image("horizontal_right_blue.png"))
BLUE_BLOC[9] = pygame.image.load(get_image("horizontal_middle_blue.png"))
BLUE_BLOC[10] = pygame.image.load(get_image("corner_top_right_blue.png"))
BLUE_BLOC[11] = pygame.image.load(get_image("full_border_top_blue.png"))
BLUE_BLOC[12] = pygame.image.load(get_image("corner_bottom_right_blue.png"))
BLUE_BLOC[13] = pygame.image.load(get_image("full_border_bottom_blue.png"))
BLUE_BLOC[14] = pygame.image.load(get_image("full_border_right_blue.png"))
BLUE_BLOC[15] = pygame.image.load(get_image("full_bloc_blue.png"))

YELLOW_BLOC[0] = pygame.image.load(get_image("bloc_yellow.png"))
YELLOW_BLOC[1] = pygame.image.load(get_image("horizontal_left_yellow.png"))
YELLOW_BLOC[2] = pygame.image.load(get_image("vertical_top_yellow.png"))
YELLOW_BLOC[3] = pygame.image.load(get_image("corner_top_left_yellow.png"))
YELLOW_BLOC[4] = pygame.image.load(get_image("vertical_bottom_yellow.png"))
YELLOW_BLOC[5] = pygame.image.load(get_image("corner_bottom_left_yellow.png"))
YELLOW_BLOC[6] = pygame.image.load(get_image("vertical_middle_yellow.png"))
YELLOW_BLOC[7] = pygame.image.load(get_image("full_border_left_yellow.png"))
YELLOW_BLOC[8] = pygame.image.load(get_image("horizontal_right_yellow.png"))
YELLOW_BLOC[9] = pygame.image.load(get_image("horizontal_middle_yellow.png"))
YELLOW_BLOC[10] = pygame.image.load(get_image("corner_top_right_yellow.png"))
YELLOW_BLOC[11] = pygame.image.load(get_image("full_border_top_yellow.png"))
YELLOW_BLOC[12] = pygame.image.load(get_image("corner_bottom_right_yellow.png"))
YELLOW_BLOC[13] = pygame.image.load(get_image("full_border_bottom_yellow.png"))
YELLOW_BLOC[14] = pygame.image.load(get_image("full_border_right_yellow.png"))
YELLOW_BLOC[15] = pygame.image.load(get_image("full_bloc_yellow.png"))
