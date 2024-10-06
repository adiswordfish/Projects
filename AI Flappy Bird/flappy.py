import pygame
import random
import numpy as np

# Define constants
SCREEN_WIDTH = 288
SCREEN_HEIGHT = 512
GRAVITY = 0.25
FLAP_STRENGTH = 6.5
PIPE_GAP = 100
PIPE_FREQUENCY = 100
PIPE_SPEED = 2
BIRD_WIDTH = 34
BIRD_HEIGHT = 24
PIPE_WIDTH = 52  # Define the width of the pipes
PIPE_HEIGHT = 320  # Define the height of the pipes

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Load images
bird_img = pygame.image.load('bird.png')
pipe_img = pygame.image.load('pipe.png')
background_img = pygame.image.load('background.png')

# Define Q-learning parameters
epsilon = 0.1  # Exploration rate
alpha = 0.1    # Learning rate
gamma = 0.99   # Discount factor

# Initialize Q-table
num_actions = 2
q_table = np.zeros((SCREEN_HEIGHT + 20, num_actions))

def get_state(bird_y, pipe_x):
     
    # Ensure that the normalized values are within the range of the Q-table
    bird_y_normalized = max(0, min(bird_y_normalized, SCREEN_HEIGHT - 1))
    pipe_x_normalized = max(0, min(pipe_x_normalized, SCREEN_WIDTH - PIPE_WIDTH))  # Adjusted for pipe width

    return (bird_y_normalized, pipe_x_normalized)

def get_state(bird_y, pipe_x):
    # Normalize bird_y to fit within the range of the Q-table
    bird_y_normalized = int((bird_y / SCREEN_HEIGHT) * (SCREEN_HEIGHT - 1)) 
    pipe_x_normalized = int((pipe_x / SCREEN_WIDTH) * (SCREEN_WIDTH - 1))
    # Ensure that the normalized values are within the range of the Q-table
    bird_y_normalized = max(0, min(bird_y_normalized, SCREEN_HEIGHT - 1)) 
    pipe_x_normalized = max(0, min(pipe_x_normalized, SCREEN_WIDTH - PIPE_WIDTH))  # Adjusted for pipe width

    return (bird_y_normalized, pipe_x_normalized)





def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        return random.randint(0, num_actions - 1)  # Explore
    else:
        return np.argmax(q_table[state])           # Exploit

def update_q_table(state, action, reward, next_state):
    best_next_action = np.argmax(q_table[next_state])
    td_target = reward + gamma * q_table[next_state][best_next_action]
    td_error = td_target - q_table[state][action]
    q_table[state][action] += alpha * td_error

def game_loop():
    bird_y = SCREEN_HEIGHT // 2
    pipe_x = SCREEN_WIDTH
    pipe_gap_y = random.randint(50, SCREEN_HEIGHT - PIPE_GAP - 50)
    score = 0

    while True:
        screen.blit(background_img, (0, 0))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Choose action
        state = get_state(bird_y, pipe_x)
        action = choose_action(state)

        # Update bird position
        bird_y += GRAVITY
        if action == 0:
            bird_y -= FLAP_STRENGTH

        # Update pipe position
        pipe_x -= PIPE_SPEED
        if pipe_x < -PIPE_WIDTH:
            pipe_x = SCREEN_WIDTH
            pipe_gap_y = random.randint(50, SCREEN_HEIGHT - PIPE_GAP - 50)
            score += 1

        # Check for collision
        if bird_y < 0 or bird_y > SCREEN_HEIGHT - BIRD_HEIGHT:
            return score
        if pipe_x < BIRD_WIDTH and bird_y < pipe_gap_y or bird_y > pipe_gap_y + PIPE_GAP:
            return score

        # Update Q-table
        next_state = get_state(bird_y, pipe_x)
        reward = 1 if pipe_x < BIRD_WIDTH else 0
        update_q_table(state, action, reward, next_state)

        # Draw objects
        screen.blit(bird_img, (50, bird_y))
        screen.blit(pipe_img, (pipe_x, pipe_gap_y - PIPE_HEIGHT))
        screen.blit(pipe_img, (pipe_x, pipe_gap_y + PIPE_GAP))
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    game_loop()
