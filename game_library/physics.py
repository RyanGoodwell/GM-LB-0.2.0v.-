class Physics:
    def __init__(self, gravity=0.5, friction=0.95):
        self.gravity = gravity
        self.friction = friction
        
    def apply_gravity(self, sprite):
        """Apply gravity to sprite"""
        sprite.velocity[1] += self.gravity
        
    def apply_friction(self, sprite):
        """Apply friction to sprite"""
        sprite.velocity[0] *= self.friction
        sprite.velocity[1] *= self.friction
        
    def check_collision(self, sprite, walls):
        """Check collision with walls"""
        for wall in walls:
            if sprite.rect.colliderect(wall.rect):
                # Horizontal collision
                if sprite.velocity[0] > 0:
                    sprite.rect.right = wall.rect.left
                    sprite.x = sprite.rect.x
                elif sprite.velocity[0] < 0:
                    sprite.rect.left = wall.rect.right
                    sprite.x = sprite.rect.x
                
                # Vertical collision
                if sprite.velocity[1] > 0:
                    sprite.rect.bottom = wall.rect.top
                    sprite.y = sprite.rect.y
                    sprite.velocity[1] = 0
                elif sprite.velocity[1] < 0:
                    sprite.rect.top = wall.rect.bottom
                    sprite.y = sprite.rect.y
                    sprite.velocity[1] = 0
