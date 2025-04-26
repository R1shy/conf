#include "./all.h"
#include <stdio.h>

void handle_input(Vector2 *pos) {
	if (IsKeyDown(KEY_LEFT)) pos.x -= 2.0f;
	if (IsKeyDown(KEY_RIGHT)) pos.x += 2.0f;
	if (IsKeyDown(KEY_UP)) pos.y -= 2.0f;
	if (IsKeyDown(KEY_DOWN)) pos.y += 2.0f;
	printf("X: %f Y: %f\n", pos.x, pos.y);
	}
