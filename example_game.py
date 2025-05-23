from game_library import GameWindow, Sprite, Physics
import pygame

def main():
    # Create game window
    window = GameWindow("Example Game", 800, 600)
    
    # Create player sprite
    player = Sprite(100, 100, 50, 50, (0, 255, 0))
    window.add_sprite(player)
    
    # Create physics
    physics = Physics()
    
    # Create walls
    walls = [
        Sprite(0, 550, 800, 50, (255, 0, 0)),  # Floor
        Sprite(0, 0, 50, 600, (255, 0, 0)),    # Left wall
        Sprite(750, 0, 50, 600, (255, 0, 0))   # Right wall
    ]
    for wall in walls:
        window.add_sprite(wall)
    
    def game_loop():
        # Handle player movement
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            player.velocity[0] = -5
        elif keys[pygame.K_RIGHT]:
            player.velocity[0] = 5
        else:
            player.velocity[0] = 0
            
        if keys[pygame.K_SPACE] and player.rect.bottom == 550:
            player.velocity[1] = -15
            
        # Apply physics
        physics.apply_gravity(player)
        physics.apply_friction(player)
        physics.check_collision(player, walls)
        
        # Update and draw
        window.update()
        window.draw()
    
    # Run the game
    window.run()

if __name__ == "__main__":
    main()
