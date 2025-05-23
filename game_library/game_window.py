import pygame
import sys

class GameWindow:
    def __init__(self, title="Game Window", width=800, height=600, fps=60):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True
        self.sprites = []
        
    def add_sprite(self, sprite):
        """Add a sprite to the game window"""
        self.sprites.append(sprite)
        
    def remove_sprite(self, sprite):
        """Remove a sprite from the game window"""
        if sprite in self.sprites:
            self.sprites.remove(sprite)
            
    def handle_events(self):
        """Handle game events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
        
    def update(self):
        """Update game state"""
        for sprite in self.sprites:
            sprite.update()
        
    def draw(self):
        """Draw all sprites"""
        self.screen.fill((0, 0, 0))  # Clear screen with black
        for sprite in self.sprites:
            sprite.draw(self.screen)
        pygame.display.flip()
        
    def run(self):
        """Run the game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        pygame.quit()
        sys.exit()
