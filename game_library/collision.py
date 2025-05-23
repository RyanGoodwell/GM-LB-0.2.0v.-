import pygame

class Collision:
    @staticmethod
    def check_collision(sprite1, sprite2):
        """Check if two sprites are colliding"""
        return sprite1.rect.colliderect(sprite2.rect)
    
    @staticmethod
    def check_wall_collision(sprite, walls):
        """Check collision with walls"""
        collisions = []
        for wall in walls:
            if sprite.rect.colliderect(wall.rect):
                collisions.append(wall)
        return collisions
    
    @staticmethod
    def resolve_collision(sprite, walls):
        """Resolve collision with walls"""
        collisions = Collision.check_wall_collision(sprite, walls)
        
        for wall in collisions:
            # Horizontal collision
            if sprite.velocity[0] > 0:  # Moving right
                sprite.rect.right = wall.rect.left
                sprite.x = sprite.rect.x
            elif sprite.velocity[0] < 0:  # Moving left
                sprite.rect.left = wall.rect.right
                sprite.x = sprite.rect.x
            
            # Vertical collision
            if sprite.velocity[1] > 0:  # Moving down
                sprite.rect.bottom = wall.rect.top
                sprite.y = sprite.rect.y
                sprite.velocity[1] = 0
            elif sprite.velocity[1] < 0:  # Moving up
                sprite.rect.top = wall.rect.bottom
                sprite.y = sprite.rect.y
                sprite.velocity[1] = 0
