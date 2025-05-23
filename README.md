# Game Library

A simple Python game development library built on top of Pygame.

## Features

- Game window management
- Sprite system
- Physics engine
- Collision detection
- Score tracking
- Animation support

## Installation

```bash
pip install .
```

## Usage

```python
from game_library import GameWindow, Sprite, Physics

# Create game window
window = GameWindow("My Game", 800, 600)

# Create player sprite
player = Sprite(100, 100, 50, 50, (0, 255, 0))
window.add_sprite(player)

# Create physics
physics = Physics()

# Main game loop
while window.running:
    window.handle_events()
    physics.apply_gravity(player)
    window.update()
    window.draw()
```

## Example Games

Check out the `examples` directory for sample games using the library.

## License

MIT License
