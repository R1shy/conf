#include <raylib.h> 
#include "input/all.h"
#include <stdio.h>

int main() { 
	InitWindow(500, 500, "WINDOW"); 
	SetTargetFPS(60);




	while (!WindowShouldClose()) {

		Vector2 pos = {(float)500.0/2, (float)500.0/2};

		handle_input(pos);
		
		BeginDrawing();
		
		ClearBackground(BLACK);
		DrawCircleV(pos, 10, RED);

		EndDrawing();
	}

	CloseWindow();
	return 0;
}
