import pygame
from config import BUTTON_SOUND, TICK_SOUND, SESSION_START_SOUND, CYCLE_END_SOUND


class SoundManager:
    def __init__(self):
        pygame.mixer.init()

    def play_sound(self, sound):
        pygame.mixer.Sound(sound).play()

    def play_button_sound(self):
        self.play_sound(BUTTON_SOUND)

    def play_tick_sound(self):
        self.play_sound(TICK_SOUND)

    def play_session_start_sound(self):
        self.play_sound(SESSION_START_SOUND)

    def play_cycle_end_sound(self):
        self.play_sound(CYCLE_END_SOUND)
