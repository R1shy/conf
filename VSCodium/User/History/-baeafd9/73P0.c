#include <raylib.h> 
#include "input/all.h"

int main() { 
	InitWindow(500, 500, "WINDOW"); 
	SetTargetFPS(60);


	Vector2 pos = {(float) 500.0/2, (float)500.0/2};

	while (!WindowShouldClose()) {

		handle_input(pos);
		printf("X: %s Y: %S", pos.x, pos.y)
		BeginDrawing();
		
		ClearBackground(BLACK);
		DrawCircleV(pos, 10, RED);

		EndDrawing();
	}

	CloseWindow();
	return 0;
}
