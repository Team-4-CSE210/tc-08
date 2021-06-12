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

        

    def _ball_wall_collision(cast):
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        wall = cast["wall"]
        for side in wall:
            if ball.get_position().get_x().equals(side.get_position().get_x()):
                #change direction of ball
                point = ball.get_velocity()
                newVel = Point(-point.get_x(), point.get_y())
                ball.set_velocity(newVel)
            
            if paddle.get_position().get_x().equals(side.get_position().get_x()):
                #don't let paddle pass
                point = paddle.get_position()
                paddle.set_possition(point)


