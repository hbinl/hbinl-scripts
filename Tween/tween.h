#include "frame.h"

/*
 * Given 2 frames and the tween options, it generates a tweened frame
 * arg prev_frame	: The  first input frame used for tweening
 * arg next_frame	: The second input frame used for tweening
 * arg tween_frame	: The output frame
 * arg int i		: How close is the resultant tweened frame relative to the tween_factor
 * arg tween_factor	: How many frames to insert between the prev_frame and next_frame
 *
 * returns the resultant tweened frame
 */
FRAME * get_tweened_frame(FRAME * prev_frame, FRAME * next_frame, FRAME * tween_frame, int i, int tween_factor);
