import java.util.ArrayList;
import java.util.Scanner;
import java.util.SplittableRandom;
 
public class Main {
 
    static long startTime = System.currentTimeMillis();
    static final int TL = 3990;
    static final int[] DR = new int[]{1, 0, -1, 0, 0};
    static final int[] DC = new int[]{0, 1, 0, -1, 0};
    static final char[] DIR_CHARS = "DRUL-".toCharArray();
    static Scanner sc = new Scanner(System.in);
    static SplittableRandom rnd = new SplittableRandom(42);
    static int H, W, K, T;
    static int[][] carPos, origCarPos, convergePos;
    static char[][] moves;
    static int[] order;
    static int time;
    static int sumDist;
    static int[][] used;
    static int usedIdx;
 
    public static void main(String[] args) {
        H = sc.nextInt();
        W = sc.nextInt();
        K = sc.nextInt();
        T = sc.nextInt();
        carPos = new int[4][K];
        origCarPos = new int[4][K];
        convergePos = new int[4][K];
        order = new int[K];
        for (int i = 0; i < K; i++) {
            for (int j = 0; j < 4; j++) {
                origCarPos[j][i] = sc.nextInt() - 1;
            }
            order[i] = i;
        }
        moves = new char[T][K];
        used = new int[H][W];
        ArrayList<String> ans = new ArrayList<>();
        double ansScore = 0;
 
        long worstTime = 0;
        for (int turn = 0; ; turn++) {
            long beforeTime = System.currentTimeMillis() - startTime;
            if (beforeTime + worstTime > TL) {
                System.err.println("turn:" + turn);
                break;
            }
            for (int i = 0; i < 4; i++) {
                System.arraycopy(origCarPos[i], 0, carPos[i], 0, K);
            }
            sumDist = 0;
            for (int i = 0; i < K; i++) {
                sumDist += Math.abs(carPos[0][i] - carPos[2][i]) + Math.abs(carPos[1][i] - carPos[3][i]);
            }
 
            int bestTime = 0;
            double bestScore = calcScore(sumDist, 0);
            for (time = 1; time <= T; time++) {
                boolean update = move();
                if (!update) break;
                double score = calcScore(sumDist, time);
                if (score > bestScore) {
                    bestScore = score;
                    bestTime = time;
                }
                if (calcScore(0, time) < ansScore) {
                    System.err.println("time:" + time);
                    break;
                }
            }
            System.err.println("bestScore:" + bestScore);
            if (bestScore > ansScore) {
                ansScore = bestScore;
                ans.clear();
                for (int i = 0; i < bestTime; i++) {
                    ans.add(String.valueOf(moves[i]));
                }
            }
 
            worstTime = Math.max(worstTime, System.currentTimeMillis() - startTime - beforeTime);
        }
        System.out.println(ans.size());
        for (String s : ans) {
            System.out.println(s);
        }
    }
 
    static boolean move() {
        usedIdx++;
        for (int i = 0; i < K; i++) {
            int pos = rnd.nextInt(K - i) + i;
            int tmp = order[i];
            order[i] = order[pos];
            order[pos] = tmp;
            used[carPos[0][i]][carPos[1][i]] = usedIdx;
        }
        ArrayList<Integer> nearList = new ArrayList<>();
        ArrayList<Integer> farList = new ArrayList<>();
        int stayFactor;
        if (sumDist < 100) {
            stayFactor = 99;
        } else if (sumDist < 200) {
            stayFactor = 4;
        } else if (sumDist < 300) {
            stayFactor = 2;
        } else if (sumDist < 500) {
            stayFactor = 2;
        } else if (sumDist < 1000) {
            stayFactor = 1;
        } else {
            stayFactor = 0;
        }
 
        sumDist = 0;
        boolean update = false;
        for (int i = 0; i < K; i++) {
            nearList.clear();
            farList.clear();
            int ci = order[i];
            int dist = Math.abs(carPos[1][ci] - carPos[3][ci]) + Math.abs(carPos[0][ci] - carPos[2][ci]);
            for (int j = 0; j < 4; j++) {
                int nr = carPos[0][ci] + DR[j];
                int nc = carPos[1][ci] + DC[j];
                if (nr < 0 || H <= nr || nc < 0 || W <= nc) continue;
                if (used[nr][nc] == usedIdx) continue;
                int nDist = Math.abs(nr - carPos[2][ci]) + Math.abs(nc - carPos[3][ci]);
                if (dist > nDist) {
                    nearList.add(j);
                } else {
                    farList.add(j);
                }
            }
            int dir;
            if (dist == 0 && stayFactor == 99) {
                dir = 4;
            } else if (nearList.size() == 1) {
                dir = nearList.get(0);
                --dist;
            } else if (nearList.size() == 2) {
                int nr0 = carPos[0][ci] + DR[nearList.get(0)];
                int nc0 = carPos[1][ci] + DC[nearList.get(0)];
                int distFromEdge0 = distFromEdge(nr0, nc0);
                int nr1 = carPos[0][ci] + DR[nearList.get(1)];
                int nc1 = carPos[1][ci] + DC[nearList.get(1)];
                int distFromEdge1 = distFromEdge(nr1, nc1);
                if (distFromEdge0 < distFromEdge1) {
                    nearList.add(nearList.get(0));
                } else if (distFromEdge0 > distFromEdge1) {
                    nearList.add(nearList.get(1));
                }
                dir = nearList.get(rnd.nextInt(nearList.size()));
                --dist;
            } else if (!farList.isEmpty()) {
                if (stayFactor == 0 && farList.size() >= 2) {
                    int nr0 = carPos[0][ci] + DR[farList.get(0)];
                    int nc0 = carPos[1][ci] + DC[farList.get(0)];
                    int distFromEdge0 = distFromEdge(nr0, nc0);
                    int nr1 = carPos[0][ci] + DR[farList.get(1)];
                    int nc1 = carPos[1][ci] + DC[farList.get(1)];
                    int distFromEdge1 = distFromEdge(nr1, nc1);
                    if (distFromEdge0 < distFromEdge1) {
                        farList.add(farList.get(0));
                    } else if (distFromEdge0 > distFromEdge1) {
                        farList.add(farList.get(1));
                    }
                }
                for (int j = 0; j < stayFactor; j++) {
                    farList.add(4);
                }
                dir = farList.get(rnd.nextInt(farList.size()));
                if (dir != 4) dist++;
            } else {
                dir = 4;
            }
            moves[time - 1][ci] = DIR_CHARS[dir];
            carPos[0][ci] += DR[dir];
            carPos[1][ci] += DC[dir];
            used[carPos[0][ci]][carPos[1][ci]] = usedIdx;
            sumDist += dist;
            if (dir != 4) update = true;
        }
        return update;
    }
 
    static int distFromEdge(int r, int c) {
        return Math.min(Math.min(r, H - 1 - r), Math.min(c, W - 1 - c));
    }
 
    static double calcScore(int dist, int time) {
        double distFactor = 20 + dist;
        double timeFactor = 10 + 0.01 * time;
        return 10_000_000.0 / (distFactor * timeFactor);
    }
}
