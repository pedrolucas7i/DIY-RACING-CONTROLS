#include <stdio.h>
#include <stdbool.h>
#include <windows.h>

#define SCREEN_WIDTH 1360
#define SCREEN_HEIGHT 768

void pressKey(WORD key, bool press) {
    INPUT input = {0};
    input.type = INPUT_KEYBOARD;
    input.ki.wVk = key;
    if (press) {
        SendInput(1, &input, sizeof(INPUT));
    } else {
        input.ki.dwFlags = KEYEVENTF_KEYUP;
        SendInput(1, &input, sizeof(INPUT));
    }
}

int main() {
    bool running = false;
    bool ctrlPressed = false;
    bool f12Pressed = false;

    printf("Pressione Ctrl + F12 para ligar/desligar o script.\n");

    while (true) {
        // Verifica se Ctrl e F12 estão pressionados
        if ((GetAsyncKeyState(VK_CONTROL) & 0x8000) && (GetAsyncKeyState(VK_F12) & 0x8000)) {
            if (!ctrlPressed && !f12Pressed) {
                running = !running;
                if (running) {
                    printf("Script ativado.\n");
                } else {
                    printf("Script desativado.\n");
                }
            }
            ctrlPressed = true;
            f12Pressed = true;
        } else {
            ctrlPressed = false;
            f12Pressed = false;
        }

        if (running) {
            POINT cursorPos;
            GetCursorPos(&cursorPos);
            float x = cursorPos.x;
            int y = cursorPos.y;
            pressKey('W', false);
            pressKey('S', false);
            
            if (y < SCREEN_HEIGHT * 0.40) {
                pressKey('W', true);
            } else if (y > SCREEN_HEIGHT * 0.60) {
                pressKey('S', true);
            }
            
            if (x < (SCREEN_WIDTH * 0.99)) {
                pressKey(VK_SPACE, false);
            } else if (x > (SCREEN_WIDTH * 0.99)) {
                pressKey(VK_SPACE, true);
            }
            
            if ((GetAsyncKeyState('A') & 0x8000) || (GetAsyncKeyState('a') & 0x8000)) {
            	pressKey('A', true);
			} else {
				pressKey('A', false);
			}
			
			if ((GetAsyncKeyState('D') & 0x8000) || (GetAsyncKeyState('d') & 0x8000)) {
            	pressKey('D', true);
			} else {
				pressKey('D', false);
			}
        }

        Sleep(1);
    }

    return 0;
}


