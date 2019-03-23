#include <math.h>

#include "tween.h"
#include "frame.h"

FRAME * get_tweened_frame(FRAME * prev_frame, FRAME * next_frame, FRAME * tween_frame, int i, int tween_factor) {

	int width  = prev_frame->width;
	int height = prev_frame->height;

	if (tween_frame == NULL) {
		tween_frame = create_frame(width, height);
	}

	double tween_ratio = tween_factor + 1;
	double prev_ratio  = (tween_ratio - i) / tween_ratio;
	double next_ratio  = i / tween_ratio;

	int pixels = width * height;

	double result;
	for (int i = 0; i < pixels; i++) {

		result    = (prev_frame->R[i] * prev_ratio) + (next_frame->R[i] * next_ratio);
		tween_frame->R[i] = floor(result);

		result    = (prev_frame->G[i] * prev_ratio) + (next_frame->G[i] * next_ratio);
		tween_frame->G[i] = floor(result);

		result    = (prev_frame->B[i] * prev_ratio) + (next_frame->B[i] * next_ratio);
		tween_frame->B[i] = floor(result);

	}

	return tween_frame;

}