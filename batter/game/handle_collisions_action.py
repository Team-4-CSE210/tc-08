from game.point import Point
import random
from game import constants
from game.action import Action
from time import sleep
import sys


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
        self._ball_brick_collision(cast)
        self._ball_floor_collision(cast)

    def _ball_wall_collision(self, cast):
        """Handles the times when the ball or the paddle hits either wall.
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0]  # there's only one
        paddle = cast["paddle"][0]  # there's only one
        leftWall = 0
        rightWall = constants.MAX_X - 1
        if (
            ball.get_position().get_x() >= rightWall
            or ball.get_position().get_x() <= leftWall
        ):
            # change direction of ball
            point = ball.get_velocity()
            newVel = Point(-point.get_x(), point.get_y())
            ball.set_velocity(newVel)

        if (
            paddle.get_position().get_x() >= rightWall
            or paddle.get_position().get_x() <= leftWall
        ):
            # don't let paddle pass
            point = paddle.get_position()
            paddle.set_position(point)

    def _ball_ceiling_collision(self, cast):
        """Handles the times when the ball hits the ceiling.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0]  # there's only one
        # ceiling = constants.MAX_Y
        # (AH) ceiling is (0, 0)
        ceiling = 0

        # if ball.get_position().get_y() >= ceiling:
        # (AH) test for ceiling and below.
        if ball.get_position().get_y() <= ceiling:
            # change direction of ball
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

        # (AH) cannot use paddle.get_position() because paddle not a pt.
        # if ball.get_position().equals(paddle.get_position()):
        #   point = ball.get_velocity()
        #   newVel = Point(point.get_x(), point.get_y())
        #   ball.set_velocity(newVel)
        #   (AH) ball should bounce off paddle.

        # (AH edited MVL).
        paddle_pt = paddle.get_position()
        paddle_pt_x = paddle_pt.get_x()
        paddle_pt_y = paddle_pt.get_y()
        ball_vel = ball.get_velocity()

        # (AH) check if ball and paddle on same y-coord.
        if ball.get_position().get_y() == paddle_pt_y:

            # (AH) check if ball is between left and right edges of paddle.
            if (
                paddle_pt_x
                <= ball.get_position().get_x()
                <= paddle_pt_x + constants.LEN_PADDLE - 1
            ):

                # (AH) change ball velocity to opposite y-direction.
                opp_vel = Point(ball_vel.get_x(), -ball_vel.get_y())
                ball.set_velocity(opp_vel)

    def _ball_brick_collision(self, cast):
        """Handles the times when the ball or the paddle hits either wall.

            Args:
                cast (dict): The game actors {key: tag, value: list}.
        """
        # (AH) User controlled Actor is Paddle, removed Robot.
        # (AH) Stationary Actor is Brick, removed Artifact.
        # (AH) Indept Batter's Ball Actor instead of RfK's Marquee Actor.
        # marquee = cast["marquee"][0] # there's only one

        ball = cast["ball"][0]

        # (AH) Block:  Ball-to-Brick Collision.
        bricks = cast["brick"]
        # marquee.set_text("")

        # (AH) Loop to find position of brick.
        for index, brick in enumerate(bricks):
            if ball.get_position().equals(brick.get_position()):

                # (AH) Conditional block:
                # (AH) Ball deciding direction to bounce == 3 cases.
                point = ball.get_velocity()

                # (AH) Case where ball bounced straight up.
                # (AH) Ball bounce back on original bounce path.
                if point.get_x() == 0:
                    reverse_vel = point.reverse()
                    ball.set_velocity(reverse_vel)

                # (AH) Case where ball bounced from left at an angle.
                # (AH) Ball bounce in opposite direction, both horizontal+vertical.
                elif point.get_x() > 0 and point.get_y() < 0:
                    opp_vel = Point(point.get_x(), -point.get_y())
                    ball.set_velocity(opp_vel)

                # (AH) Case where ball bounced from right at an angle.
                # (AH) Ball bounce in opposite direction, both horizontal+vertical.
                elif point.get_x() < 0 and point.get_y() > 0:
                    opp_vel = Point(point.get_x(), -point.get_y())
                    ball.set_velocity(opp_vel)

                # (AH) Delete brick when ball collides.
                # (AH) then exit loop because loop has changed after pop.
                bricks.pop(index)
                break

    def _ball_floor_collision(self, cast):
        """Handles the collision of the ball hitting the floor.

        Args:
            cast (dict): the game actors {key: tag, value: list}.
        """
        p_ball_y = cast["ball"][0].get_position().get_y()
        # if p_ball_y > constants.MAX_Y + 2:
        # (AH) up to but not including constants.MAX_Y
        if p_ball_y > constants.MAX_Y - 1:
            sleep(2)
            sys.exit()
