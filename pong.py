import pygame
import sys

# Inicializar pygame
pygame.init()

# Tamaño de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Clásico")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Jugadores
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
player1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Pelota
BALL_SIZE = 20
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = 5
ball_speed_y = 5

# Velocidad de las paletas
paddle_speed = 6

# Reloj para el framerate
clock = pygame.time.Clock()

# Función para reiniciar la pelota
def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_speed_x *= -1
    ball_speed_y *= -1

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controles del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= paddle_speed
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += paddle_speed
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= paddle_speed
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += paddle_speed

    # Movimiento de la pelota
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Rebote contra paredes
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Rebote con paletas
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    # Puntos
    if ball.left <= 0 or ball.right >= WIDTH:
        reset_ball()

    # Dibujar
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    pygame.display.flip()
    clock.tick(60)
