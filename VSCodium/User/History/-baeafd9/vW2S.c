#include <raylib.h> 
#include "input/all.h"
#include <stdio.h>

int main() { 
	InitWindow(500, 500, "WINDOW"); 
	SetTargetFPS(60);




	while (!WindowShouldClose()) {

		
		handle_input();
		
		BeginDrawing();
		
		ClearBackground(BLACK);
		DrawCircleV(pos, 10, RED);

		EndDrawing();
	}

	CloseWindow();
	return 0;
}
