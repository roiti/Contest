#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
template<typename T> using Graph = vector<vector<T>>;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define HAS(a, x) (a.find(x) != a.end())
#define endl '\n'

int H, W, N;
ll a[405][405], b[405][405];
ll d[405][405], dd[405][405];

void imos() {
  rep(i, H + 1) rep(j, W + 1) d[i][j] = dd[i][j] = 0;
  // imos for rows
  rep(i, H) {
    rep(j, W) {
      d[i + 1][j + 1] = d[i + 1][j] + a[i][j];
    }
  }

  // imos for 2d
  rep(i, H) {
    rep(j, W) {
      dd[i + 1][j + 1] = dd[i][j + 1] + d[i + 1][j + 1];
    }
  }

//  cout << endl;
//  rep(i, H + 1) {
//    rep(j, W + 1) {
//      cout << dd[i][j] << " ";
//    }
//    cout << endl;
//  }
//  cout << endl;
}

// (x1, y1) = top left cell, (x2, y2) = bottom right cell 
ll area(int x1, int y1, int x2, int y2) {
  if (x1 > x2 || y1 > y2) return 0;
  if (x1 < 0 || x2 >= W || y2 >= H || y1 < 0) return 0;

  ll res = dd[y2 + 1][x2 + 1] - dd[y1][x2 + 1];
  if (x1 > 0) res -= dd[y2 + 1][x1] - dd[y1][x1];
  return res;
}

ll solve2() {
  ll res = 0;
  rep(h, H - 1) {
    ll area1 = area(0, 0, W - 1, h);
    ll area2 = area(0, h + 1, W - 1, H - 1);
    res = max(res, min(area1, area2));
  }
  return res;
}

ll solve3() {
  ll res = 0;
  rep(h1, H - 1) REP(h2, h1 + 1, H - 1) {
    ll area1 = area(0, 0, W - 1, h1);
    ll area2 = area(0, h1 + 1, W - 1, h2);
    ll area3 = area(0, h2 + 1, W - 1, H - 1);
    res = max(res, min(area1, min(area2, area3)));
  }

  rep(h, H) rep(w, W) {
    ll area1 = area(0, 0, W - 1, h);
    ll area2 = area(0, h + 1, w, H - 1);
    ll area3 = area(w + 1, h + 1, W - 1, H - 1);
    res = max(res, min(area1, min(area2, area3)));
  } 

  rep(h, H) rep(w, W) {
    ll area1 = area(0, h + 1, W - 1, H - 1);
    ll area2 = area(0, 0, w, h);
    ll area3 = area(w + 1, 0, W - 1, h);
    res = max(res, min(area1, min(area2, area3)));
  } 

  return res;
}

ll solve4() {
  ll res = 0;
  // 1
  rep(h1, H - 1) REP(h2, h1 + 1, H) {
    ll area1 = area(0, 0, W - 1, h1);
    ll area2 = area(0, h1 + 1, W - 1, h2);
    int lo = h2 + 1, hi = H - 1;
    while (hi - lo > 0) {
      int mid = (lo + hi)/2;
      ll area3 = area(0, h2 + 1, W - 1, mid);
      ll area4 = area(0, mid + 1, W - 1, H - 1);
      if (area3 - area4 < 0) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }
    ll area34 = 0;
    REP(i, -2, 3) {
      area34 = max(area34, min(area(0, h2 + 1, W - 1, hi + i), area(0, hi + i + 1, W - 1, H - 1)));
    }
    res = max(res, min(area1, min(area2, area34)));
  }

  // 3
  REP(h1, 1, H - 1) REP(h2, h1 + 1, H) {
    ll area1 = area(0, h1 + 1, W - 1, h2);
    ll area2 = area(0, h2 + 1, W - 1, H - 1);
    int lo = 0, hi = W - 1;
    while (hi - lo > 0) {
      int mid = (lo + hi)/2;
      ll area3 = area(0, 0, mid, h1);
      ll area4 = area(mid + 1, 0, W - 1, h1);
      if (area3 - area4 < 0) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }
    ll area34 = 0;
    REP(i, -2, 3) {
      area34 = max(area34, min(area(0, 0, hi + i, h1), area(hi + 1 + i, 0,  W - 1, h1)));
    }
    res = max(res, min(area1, min(area2, area34)));
  }

  // 3
  rep(h1, H - 1) rep(h2, H) {
    ll area1 = area(0, 0, W - 1, h1);
    ll area2 = area(0, h2 + 1, W - 1, H - 1);
    int lo = 0, hi = W - 1;
    while (hi - lo > 0) {
      int mid = (lo + hi)/2;
      ll area3 = area(0, h1 + 1, mid, h2);
      ll area4 = area(mid + 1, hi + 1, W - 1, h2);
      if (area3 - area4 < 0) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }
    ll area34 = 0;
    REP(i, -2, 3) {
      area34 = max(area34, min(area(0, h1 + 1, hi + i, h2), area(hi + 1 + i, h1 + 1,  W - 1, h2)));
    }
    res = max(res, min(area1, min(area2, area34)));
  }

  // 4
  rep(h, H) {
    ll area12 = 0, area34 = 0;
    rep(w, W) {
      area12 = max(area12, min(area(0, 0, w, h), area(w + 1, 0, W - 1, h))); 
      area34 = max(area34, min(area(0, h + 1, w, H - 1), area(w + 1, h + 1, W - 1, H - 1))); 
    }
    res = max(res, min(area12, area34));
  }
  
  // 5
  rep(h, H) {
    ll area1 = area(0, h + 1, W - 1, H - 1);
    rep(w, W) {
      ll area2 = area(w + 1, 0, W - 1, h); 
      int lo = 0, hi = h;
      while (hi - lo > 0) {
        int mid = (lo + hi)/2;
        ll area3 = area(0, 0, w, mid);
        ll area4 = area(0, mid + 1, w, h);
        if (area3 - area4 < 0) {
          lo = mid + 1;
        } else {
          hi = mid;
        }
      }
      ll area34 = 0;
      REP(i, -2, 3) {
        area34 = max(area34, min(area(0, 0, w, hi + i), area(0, hi + i + 1, w, h)));
      }
      res = max(res, min(area1, min(area2, area34)));
    } 
  }

  // 6
  rep(h, H) {
    ll area1 = area(0, h + 1, W - 1, H - 1); 
    REP(w, 2, W) {
      ll area2 = area(w + 1, 0, W - 1, h); 
      int lo = 0, hi = w;
      while (hi - lo > 0) {
        int mid = (lo + hi)/2;
        ll area3 = area(0, 0, mid, h);
        ll area4 = area(mid + 1, 0, w, h);
        if (area3 - area4 < 0) {
          lo = mid + 1;
        } else {
          hi = mid;
        }
      }
      ll area34 = 0;
      REP(i, -2, 3) {
        area34 = max(area34, min(area(0, 0, hi + i, h), area(hi + 1 + i, 0,  w, h)));
      }
      res = max(res, min(area1, min(area2, area34)));
    }
  }

  return res;
}

ll solve(int N) {
  if (N == 2) return solve2();
  if (N == 3) return solve3();
  if (N == 4) return solve4();
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);
  
  cin >> H >> W >> N;
  rep(i, H) rep(j, W) cin >> a[i][j];

  ll ans = 0;

  rep(loop, 2) {
    imos();
    ans = max(ans, solve(N));

    // swap left and right
    rep(j, W/2) {
      rep(i, H) swap(a[i][j], a[i][W - 1 - j]);
    }
    imos();
    ans = max(ans, solve(N));

    // swap top and bottom
    rep(i, H/2) {
      rep(j, W) swap(a[i][j], a[H - 1 - i][j]);
    }
    imos();
    ans = max(ans, solve(N));

    // swap left and right
    rep(j, W/2) {
      rep(i, H) swap(a[i][j], a[i][W - 1 - j]);
    }
    imos();
    ans = max(ans, solve(N));

    // swap top and bottom
    rep(i, H/2) {
      rep(j, W) swap(a[i][j], a[H - 1 - i][j]);
    }
    imos();
    ans = max(ans, solve(N));

    // swap rows and columns
    rep(i, H) rep(j, W) b[j][i] = a[i][j];
    rep(i, H) rep(j, W) a[i][j] = 0;
    swap(H, W);
    rep(i, H) rep(j, W) a[j][i] = b[j][i];
  }

  cout << ans << endl;
  return 0;
}
