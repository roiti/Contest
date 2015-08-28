#include <iostream>
using namespace std;

int xy[101][4];

bool cross(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4) {
    int tc=(x1-x2)*(y3-y1)+(y1-y2)*(x1-x3);
    int td=(x1-x2)*(y4-y1)+(y1-y2)*(x1-x4);
    return tc * td <= 0;
}

int main(void) {
    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> xy[i][0] >> xy[i][1] >> xy[i][2] >> xy[i][3];
    }

    int ans = 0;
    for (int d1 = 0; d1 < 2; d1++) {
        for (int i = 0; i < N; i++) {
            int x1 = xy[i][2 * d1], y1 = xy[i][2 * d1 + 1];
            for (int d2 = 0; d2 < 2; d2++) {
                for (int j = 0; j < N; j++) {
                    int x2 = xy[j][2 * d2], y2 = xy[j][2 * d2 + 1];
                    if (x1 == x2 && y1 == y2) continue;
                    int tmp = 0;
                    for (int k = 0; k < N; k++) {
                        int x3 = xy[k][0], y3 = xy[k][1];
                        int x4 = xy[k][2], y4 = xy[k][3];
                        if (cross(x1, y1, x2, y2, x3, y3, x4, y4)) tmp++;
                    }
                    ans = max(ans, tmp);
                }
            }
        }
    }


    cout << ans << endl;

    return 0;
}
