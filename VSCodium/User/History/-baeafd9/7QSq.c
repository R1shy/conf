#include <raylib.h> 
#include "input/all.h"
#include <stdio.h>

int main() { 
	InitWindow(500, 500, "WINDOW"); 
	SetTargetFPS(60);




	while (!WindowShouldClose()) {

		
	if (IsKeyDown(KEY_LEFT)) pos.x -= 2.0f;
	if (IsKeyDown(KEY_RIGHT)) pos.x += 2.0f;
	if (IsKeyDown(KEY_UP)) pos.y -= 2.0f;
	if (IsKeyDown(KEY_DOWN)) pos.y += 2.0f;
		printf("X: %f Y: %f\n", pos.x, pos.y);
		BeginDrawing();
		
		ClearBackground(BLACK);
		DrawCircleV(pos, 10, RED);

		EndDrawing();
	}

	CloseWindow();
	return 0;
}
