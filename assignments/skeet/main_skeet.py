"""
File: skeet.py
Original Author: Br. Burton
Designed to be completed by others
This program implements an awesome version of skeet.
"""
import arcade
import math
import random
from point import Point
from velocity import Velocity
from target import *
from bullet import Bullet
from globals import *
from rifle import Rifle

GAME_START = 0
GAME_RUN = 1


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.rifle = Rifle()
        self.score = 0
        
        # create a list of all bullets
        self.bullets = []
        
        # create a list for all targets
        self.targets = []
        
        self.display_go = False
        self.display_win = False
        self.current_state = GAME_START
        self.remember_time = 0.0
        
        # loading beginning sound file
        self.announcer_sound = arcade.sound.load_sound("sfx_level_announcer_0002_b.wav")
        self.sound_counter = 0

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()
        
        # always draw rifle, even before game starts
        self.rifle.draw()
        
        if self.current_state == GAME_START:
            # this starts true and switches to false
            # after less than 2 seconds (see update function) 
            self.draw_game_start()
            
        # rest of the game begins playing
        else:

        
            # draw each bullet in bullet list
            for bullet in self.bullets:
                bullet.draw()
            
            # draw each target in target list    
            for target in self.targets:
                target.draw()

            # always draw score
            self.draw_score()
            
            if self.display_go:
                self.draw_GO()
                
            if self.display_win:
                self.draw_game_win()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.NAVY_BLUE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()
        self.check_off_screen()
        
        self.remember_time += delta_time
        
        # changes current state to GAME_RUN after
        # approx 1.2 secs, then turns on the "okay"
        # to display the "GO!"
        if self.remember_time > 1.2 and self.remember_time < 2.7:
            self.current_state = GAME_RUN
            self.display_go = True
            # if sound has not played, then play it.
            if self.sound_counter == 0:
                arcade.sound.play_sound(self.announcer_sound)
                self.sound_counter += 1
        # after approx 2.7 seconds have past it will
        # turn off the "okay" to display the "GO!"
        if self.remember_time > 2.7:
            self.display_go = False
        # if the score reaches 25 then the display_game_win function
        # is given the okay to run
        # (note that the game will keep running even after the win) 
        if self.score > 24:
            self.display_win = True
        
        # decide if we should start a target
        # per frame has 1/50 probability of creating a target
        if self.current_state == GAME_RUN:
            if random.randint(1, 50) == 1:
                self.create_target()

            # Iterates through the bullets and tells them to advance
            for bullet in self.bullets:
                bullet.advance()
                
            # Iterates through the targets and tells them to advance
            for target in self.targets:
                target.advance()

        
    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """
        
        # Decides what type of target to create and appends it to the list
        random_x = random.randint(1, 50)
        if random_x < 26: # 1/2 probability of a regular target being created
            self.targets.append(regularTarget())
        elif random_x < 41 and random_x > 25: # 3/10 probability of a strong target
            self.targets.append(strongTarget())
        else: # 1/5 probability of a safe target
            self.targets.append(safeTarget())
            
        


    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        for bullet in self.bullets:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                                abs(bullet.center.y - target.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        self.score += target.hit()

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()
    
    
    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        # removes bullet if it is no longer alive
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)
        
        # removes target if it is no longer alive
        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)
    

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen():
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen():
                self.targets.remove(target)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # set the rifle angle in degrees
        self.rifle.angle = self._get_angle_degrees(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!
        
        angle = self._get_angle_degrees(x, y)

        bullet = Bullet(angle)

        self.bullets.append(bullet)

    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.
        Note: This could be a static method, but we
        haven't discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)

        # convert to degrees
        # converted to degrees because the rifle class needs degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees
    
    def draw_game_start(self):
        """
        Draw "READY?" across the screen when game starts.
        will disappear shortly and the game is on.
        """
        output1 = "READY?"
        arcade.draw_text(output1, 200, 300, arcade.color.BLACK, 54)
        
        
    def draw_GO(self):
        """
        Draw "GO!" across the screen after "READY?" is displayed.
        will disappear shortly there after.
        """
        output2 = "GO!"
        arcade.draw_text(output2, 240, 200, arcade.color.BLACK, 54)
        
    def draw_game_win(self):
        """
        Draw "YOU WIN!" across the screen when score goes above 25
        """
        output1 = "YOU WIN!"
        arcade.draw_text(output1, 170, 300, arcade.color.BLACK, 54)
        
# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()