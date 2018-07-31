# lesson11
Pong, make the paddle move

### Notes and Coding
Mr. Gerwin will lecture about how to make the paddles and make them move.  It would be best if you started with your working pong0-2.py program but if you don't have one, you can use the one provided.
You should save your working program as pong0-3.py and upload it to your lesson11 repository.

### Enhancements
1. Make a paddle for player B, you will need to write a function that will handle the movement of paddle B

2. Program it so that different keys control the movement of paddle B such that paddle A still works with the up and down arrows and paddle B works with two different keys for up and down (I used the keypad 8 and 2 for up and down)  See pygame docs "keys" for codes for other keys on the keyboard.

3. Use the same collide function that was programmed previously to determine if paddleB collides with the ball.  That is "collide" should show up in the console when the ball is in contact with the paddle on the right.

4. Feel free to experiment with the paddle speed.  See what works for your game.  Save your enhanced version as pong0-4.py and upload it to your repository.

### Discussion Questions
1. How was drawing the rectangle for paddle B different than with paddle A?
2. Why did we need to draw the paddles before drawing the ball?
3. Use what you know about how the ball bounces on the walls.  Even though you cannot see how the Rect class is programmed, how do you think pygame detects collisions in the Rect class?
