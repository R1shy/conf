#include "./all.h"

	void handle_input(Vector2 pos) {
	if (IsKeyDown(KEY_LEFT)) pos.x -= 2.0f;
	if (key_down(KEY_RIGHT)) pos.x += 2.0f;
	if (key_down(KEY_UP)) pos.y -= 2.0f;
	if (key_down(KEY_DOWN)) pos.y += 2.0f;
	}
