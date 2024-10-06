import pygame
import random
import os
import time
import neat
import visualize
import pickle
pygame.font.init()  # init font
gen = 0
WIN_WIDTH = 600
WIN_HEIGHT = 800
FLOOR = 730
STAT_FONT = pygame.font.SysFont("comicsans", 50)
END_FONT = pygame.font.SysFont("comicsans", 70)
DRAW_LINES = False

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png")).convert_alpha())
bg_img = pygame.transform.scale(pygame.image.load(os.path.join("imgs","bg.png")).convert_alpha(), (600, 900))
bird_images = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird" + str(x) + ".png"))) for x in range(1,4)]
base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png")).convert_alpha())
stat_font = pygame.font.SysFont("comicsans", 50)

class Bird:
    imgs = bird_images
    max_rotation = 25
    rot_vel = 20
    animation_time = 5

    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        self.tilt = 0  # degrees to tilt
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.imgs[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        # for downward acceleration
        displacement = self.vel*(self.tick_count) + 0.5*(3)*(self.tick_count)**2  # calculate displacement

        # terminal velocity
        if displacement >= 16:
            displacement = (displacement/abs(displacement)) * 16

        if displacement < 0:
            displacement -= 2

        self.y = self.y + displacement

        if displacement < 0 or self.y < self.height + 50:  # tilt up
            if self.tilt < self.max_rotation:
                self.tilt = self.max_rotation
        else:  # tilt down
            if self.tilt > -90:
                self.tilt -= self.rot_vel

    def draw(self, win):
        
        self.img_count += 1

        # For animation of bird, loop through three images
        if self.img_count <= self.animation_time:
            self.img = self.imgs[0]
        elif self.img_count <= self.animation_time*2:
            self.img = self.imgs[1]
        elif self.img_count <= self.animation_time*3:
            self.img = self.imgs[2]
        elif self.img_count <= self.animation_time*4:
            self.img = self.imgs[1]
        elif self.img_count == self.animation_time*5:
            self.img = self.imgs[0]
            self.img_count = 0

        # so when bird is nose diving it isn't flapping
        if self.tilt <= -80:
            self.img = self.imgs[1]
            self.img_count = self.animation_time*2


        # tilt the bird
        blitRotateCenter(win, self.img, (self.x, self.y), self.tilt)

    def get_mask(self):
    
        return pygame.mask.from_surface(self.img)
    
def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)

class Pipe:
    gap = 200
    vel = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        
        self.top = 0
        self.bottom = 0
        self.pipe_top = pygame.transform.flip(pipe_img, False, True)
        self.pipe_bottom = pipe_img
        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.pipe_top.get_height()
        self.bottom = self.height + self.gap

    def move(self):
        self.x -= self.vel

    def draw(self, win):
        win.blit(self.pipe_top, (self.x, self.top))
        win.blit(self.pipe_bottom, (self.x, self.bottom))
        
    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.pipe_top)
        bottom_mask = pygame.mask.from_surface(self.pipe_bottom)
        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask,top_offset)

        if b_point or t_point:
            return True

        return False
        
class Base:
    vel = 5
    width = base_img.get_width()
    img = base_img

    def __init__(self,y):
        self.y = y
        self.x1 = 0
        self.x2 = self.width

    def move(self):
        self.x1 -= self.vel
        self.x2 -= self.vel

        if self.x1 + self.width < 0:
            self.x1 = self.x2 + self.width

        if self.x2 + self.width < 0:
            self.x2 = self.x1 + self.width

    def draw(self, win):
        win.blit(self.img, (self.x1, self.y))
        win.blit(self.img, (self.x2, self.y))

def draw_window(win, birds, pipes, base, score, gen):
    win.blit(bg_img, (0,0))

    for pipe in pipes:
        pipe.draw(win)

    text = stat_font.render("Score:" + str(score), 1, (255,255,255))
    win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))

    text = stat_font.render("Gen:" + str(gen), 1, (255,255,255))
    win.blit(text, (10, 10))

    base.draw(win)
    for bird in birds:

        bird.draw(win)
    pygame.display.update()

def main(genomes, config):
    global gen
    gen+=1
    nets = []
    ge = []
    birds = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(230, 250))
        g.fitness = 0
        ge.append(g)


    base = Base(730)
    pipes = [Pipe(600)]
    run = True
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        
        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].pipe_top.get_width():
                pipe_ind = 1 
        else:
            run = False
            break

        for x, bird in enumerate(birds):
            bird.move()
            ge[x].fitness += 0.1

            output = nets[birds.index(bird)].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom)))

            if output[0] > 0.5:
                bird.jump()


        rem = []
        add_pipe = False
        for pipe in pipes:
            for x, bird in enumerate(birds):
                if pipe.collide(bird):
                    ge[x].fitness - 1
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)
            
                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            if pipe.x + pipe.pipe_top.get_width()< 0:
                rem.append(pipe)

            pipe.move()

        if add_pipe:
            score +=1
            for g in ge:
                g.fitness += 5
            pipes.append(Pipe(600))

        for r in rem:
            pipes.remove(r)

        for x, bird in enumerate(birds):
            if bird.y + bird.img.get_height() >= 750 or bird.y < 0:
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)

        if bird.y + bird.img.get_height() >= 730:
            pass
            
        base.move()
        draw_window(win ,birds, pipes, base, score, gen)
                
    # pygame.quit()
    # quit()

# main()

def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    
    p = neat.Population(config)

    
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    #p.add_reporter(neat.Checkpointer(5))

    
    winner = p.run(main, 50)

    
    print('\nBest genome:\n{!s}'.format(winner))

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)