import pygame

class Score:
    def __init__(self, x=10, y=10, font_size=36, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.score = 0
        self.font = pygame.font.Font(None, font_size)
        self.color = color
        
    def add_points(self, points):
        """Add points to the score"""
        self.score += points
        
    def reset(self):
        """Reset the score"""
        self.score = 0
        
    def draw(self, screen):
        """Draw the score on the screen"""
        score_text = self.font.render(f"Score: {self.score}", True, self.color)
        screen.blit(score_text, (self.x, self.y))
