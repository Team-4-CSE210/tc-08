from game.point import Point
import random
from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._ball_wall_collision(cast)
        self._ball_ceiling_collision(cast)
        self._ball_paddle_collision(cast)

    def _ball_wall_collision(self, cast):
        """Handles the times when the ball or the paddle hits either wall.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        leftWall = 0
        rightWall = constants.MAX_X
        if ball.get_position().get_x() >= rightWall or ball.get_position().get_x() <= leftWall:
            #change direction of ball
            point = ball.get_velocity()
            newVel = Point(-point.get_x(), point.get_y())
            ball.set_velocity(newVel)
            
        if paddle.get_position().get_x() >= rightWall or paddle.get_position().get_x() <= leftWall:
            #don't let paddle pass
            point = paddle.get_position()
            paddle.set_position(point)


    def _ball_ceiling_collision(self, cast):
        """Handles the times when the ball hits the ceiling.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        ceiling = constants.MAX_Y

        if ball.get_position().get_y() >= ceiling:
            #change direction of ball
            point = ball.get_velocity()
            newVel = Point(point.get_x(), -point.get_y())
            ball.set_velocity(newVel)


    def _ball_paddle_collision(self, cast):
        """Handles the collision of the ball hitting the paddle.

        Args:
            cast (dict): the game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0]
        paddle = cast["paddle"][0] 
        if ball.get_position().equals(paddle.get_position()):
            point = ball.get_velocity()
            newVel = Point(point.get_x(), point.get_y())
            ball.set_velocity(newVel)
