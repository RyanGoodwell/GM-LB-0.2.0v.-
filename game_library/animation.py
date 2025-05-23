import pygame

class Animation:
    def __init__(self, frames, frame_duration=100):
        """
        Create an animation
        :param frames: List of pygame.Surface objects
        :param frame_duration: Duration of each frame in milliseconds
        """
        self.frames = frames
        self.frame_duration = frame_duration
        self.current_frame = 0
        self.last_update = 0
        self.running = True
        
    def update(self, current_time):
        """Update animation frame"""
        if not self.running:
            return
            
        if current_time - self.last_update > self.frame_duration:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.last_update = current_time
            
    def draw(self, screen, x, y):
        """Draw current frame"""
        if self.frames:
            screen.blit(self.frames[self.current_frame], (x, y))
            
    def stop(self):
        """Stop the animation"""
        self.running = False
        
    def play(self):
        """Start the animation"""
        self.running = True
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()
