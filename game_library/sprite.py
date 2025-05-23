import pygame

class Sprite:
    def __init__(self, x, y, width, height, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        
        # Movement properties
        self.velocity = [0, 0]      # Current velocity (x, y)
        self.acceleration = [0, 0]  # Current acceleration (x, y)
        self.max_speed = 10         # Maximum speed
        self.friction = 0.9         # Friction coefficient (0 to 1)
        self.jump_power = -15       # Jump power
        self.can_jump = True        # Can jump flag
        self.on_ground = False      # Grounded state
        
    def update(self):
        """Update sprite position and movement"""
        # Apply acceleration
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        
        # Limit velocity by max speed
        if abs(self.velocity[0]) > self.max_speed:
            self.velocity[0] = self.max_speed if self.velocity[0] > 0 else -self.max_speed
            
        # Apply friction to horizontal movement
        if self.velocity[0] != 0:
            self.velocity[0] *= self.friction
            
        # Update position
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.rect.x = self.x
        self.rect.y = self.y
        
    def move_left(self, speed):
        """Move sprite left"""
        self.velocity[0] = -speed
        
    def move_right(self, speed):
        """Move sprite right"""
        self.velocity[0] = speed
        
    def stop_horizontal(self):
        """Stop horizontal movement"""
        self.velocity[0] = 0
        
    def jump(self):
        """Make sprite jump"""
        if self.can_jump:
            self.velocity[1] = self.jump_power
            self.can_jump = False
            
    def set_on_ground(self, is_on_ground):
        """Set if sprite is on ground"""
        self.on_ground = is_on_ground
        if is_on_ground:
            self.velocity[1] = 0
            self.can_jump = True
            
    def draw(self, screen):
        """Draw sprite on screen"""
        pygame.draw.rect(screen, self.color, self.rect)
        
    def move(self, dx, dy):
        """Move sprite by dx and dy"""
        self.x += dx
        self.y += dy
        self.rect.x = self.x
        self.rect.y = self.y
        
    def set_velocity(self, vx, vy):
        """Set sprite velocity"""
        self.velocity = [vx, vy]
        
    def stop(self):
        """Stop sprite movement"""
        self.velocity = [0, 0]
