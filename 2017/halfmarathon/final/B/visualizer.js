var visualizer;
(function (visualizer) {
    // RDLU-
    var DY = [0, 1, 0, -1, 0];
    var DX = [1, 0, -1, 0, 0];
    var A_TO_DIR = { 'R': 0, 'D': 1, 'L': 2, 'U': 3, '-': 4 };
    var WIDTH = 1600, HEIGHT = 1600;
    var lineEnabled = true;
    var loadTo = function (file, callback) {
        var reader = new FileReader();
        reader.readAsText(file);
        reader.onloadend = function () {
            callback(reader.result);
        };
    };
    var getInt = function (s, lineno) {
        if (s == null) {
            throw new Error("\u6570\u5024\u306E\u30D1\u30FC\u30B9\u306B\u5931\u6557\u3057\u307E\u3057\u305F at line: " + lineno);
        }
        s = s.trim();
        if (s.match(/^\d+$/)) {
            return parseInt(s);
        }
        throw new Error("\u6570\u5024\u306E\u30D1\u30FC\u30B9\u306B\u5931\u6557\u3057\u307E\u3057\u305F at line: " + lineno);
    };
    var calcManhattan = function (y1, x1, y2, x2) {
        return Math.abs(y1 - y2) + Math.abs(x1 - x2);
    };
    var aToDir = function (a) {
        if (!A_TO_DIR.hasOwnProperty(a)) {
            throw new Error("WA: \u884C\u52D5\u306B 'RDLU-' \u4EE5\u5916\u306E\u6587\u5B57\u304C\u3042\u308A\u307E\u3059: '" + a + "'");
        }
        return A_TO_DIR[a];
    };
    var Frame = (function () {
        function Frame() {
            this.y = []; // 車 i の y
            this.x = []; // 車 i の x
            this.d = []; // 車 i が直前にどう移動して今の位置に来たのか。dir が入っている。初期フレームは 4 が入っている
        }
        Frame.prototype.calcScore = function () {
            this.pd = 20.0;
            for (var i = 0; i < this.board.k; i++) {
                this.pd += calcManhattan(this.y[i], this.x[i], this.board.dy[i], this.board.dx[i]);
            }
            var pt = this.turn * 0.01 + 10;
            this.score = Math.ceil(1e7 / (this.pd * pt));
        };
        Frame.prototype.next = function (line) {
            var next = new Frame();
            next.board = this.board;
            next.turn = this.turn + 1;
            next.state = [];
            for (var i = 0; i < this.board.h; i++) {
                next.state[i] = [];
                for (var j = 0; j < this.board.w; j++) {
                    next.state[i][j] = -1;
                }
            }
            for (var i = 0; i < this.board.k; i++) {
                var dir = aToDir(line[i]);
                var y = this.y[i];
                var x = this.x[i];
                var ny = y + DY[dir];
                var nx = x + DX[dir];
                if (!this.board.inside(ny, nx)) {
                    console.log(this);
                    throw new Error("WA: \u76E4\u9762\u306E\u5916\u306B\u79FB\u52D5\u3057\u3088\u3046\u3068\u3057\u3066\u3044\u307E\u3059: \u30BF\u30FC\u30F3: " + next.turn + ", " +
                        ("\u79FB\u52D5\u3059\u308B\u8ECAID: " + (i + 1) + ", \u4F4D\u7F6E: (" + (ny + 1) + ", " + (nx + 1) + ")"));
                }
                if (dir != 4 && this.state[ny][nx] != -1) {
                    console.log(this);
                    throw new Error("WA: \u79FB\u52D5\u5148\u306B\u8ECA\u304C\u3044\u307E\u3059: \u30BF\u30FC\u30F3: " + next.turn + ", \u79FB\u52D5\u3059\u308B\u8ECAID: " + (i + 1) + ", " +
                        ("\u65E2\u306B\u3044\u308B\u8ECAID: " + (this.state[ny][nx] + 1) + ", \u4F4D\u7F6E: (" + (ny + 1) + ", " + (nx + 1) + ")"));
                }
                if (next.state[ny][nx] != -1) {
                    console.log(this);
                    throw new Error("WA: \u79FB\u52D5\u5148\u306B\u8ECA\u304C\u3044\u307E\u3059: \u30BF\u30FC\u30F3: " + next.turn + ", \u79FB\u52D5\u3059\u308B\u8ECAID: " + (i + 1) + ", " +
                        ("\u65E2\u306B\u3044\u308B\u8ECAID: " + (next.state[ny][nx] + 1) + ", \u4F4D\u7F6E: (" + (ny + 1) + ", " + (nx + 1) + ")"));
                }
                next.d[i] = dir;
                next.y[i] = ny;
                next.x[i] = nx;
                next.state[ny][nx] = i;
            }
            next.calcScore();
            return next;
        };
        return Frame;
    }());
    var Board = (function () {
        function Board(value1) {
            this.sy = []; // 車 i の初期地 y
            this.sx = []; // 車 i の初期地 x
            this.dy = []; // 車 i の目的地 y
            this.dx = []; // 車 i の目的地 x
            var lines = value1.trim().split("\n");
            var l1 = lines[0].trim().split(" ");
            this.h = getInt(l1[0], 1);
            this.w = getInt(l1[1], 1);
            this.k = getInt(l1[2], 1);
            this.t = getInt(l1[3], 1);
            for (var i = 0; i < this.k; i++) {
                var l = lines[i + 1].trim().split(" ");
                this.sy[i] = getInt(l[0], i + 1) - 1;
                this.sx[i] = getInt(l[1], i + 1) - 1;
                this.dy[i] = getInt(l[2], i + 1) - 1;
                this.dx[i] = getInt(l[3], i + 1) - 1;
            }
        }
        Board.prototype.initialFrame = function () {
            var frame = new Frame();
            frame.board = this;
            frame.turn = 0;
            frame.state = [];
            for (var i = 0; i < this.h; i++) {
                frame.state[i] = [];
                for (var j = 0; j < this.w; j++) {
                    frame.state[i][j] = -1;
                }
            }
            for (var i = 0; i < this.k; i++) {
                frame.state[this.sy[i]][this.sx[i]] = i;
                frame.y[i] = this.sy[i];
                frame.x[i] = this.sx[i];
                frame.d[i] = 4;
            }
            frame.calcScore();
            return frame;
        };
        Board.prototype.calc = function (actions) {
            var lines = actions.trim().split("\n");
            var c = getInt(lines[0].trim(), 1);
            if (c > this.t) {
                throw new Error("WA: \u64CD\u4F5C\u56DE\u6570 C \u304C T \u3092\u8D85\u3048\u3066\u3044\u307E\u3059: C=" + c + ", T=" + this.t);
            }
            var frames = [];
            var cur = this.initialFrame();
            frames.push(cur);
            for (var i = 0; i < c; i++) {
                var line = lines[i + 1].trim();
                if (line.length != this.k) {
                    throw new Error("WA: \u64CD\u4F5C\u56DE\u6570 " + (i + 1) + " \u306E\u9577\u3055\u304C K \u3068\u4E00\u81F4\u3057\u307E\u305B\u3093: " + line.length + " \u6587\u5B57, K: " + this.k);
                }
                cur = cur.next(line);
                frames.push(cur);
            }
            return frames;
        };
        Board.prototype.inside = function (y, x) {
            return (0 <= y) && (y < this.h) && (0 <= x) && (x < this.w);
        };
        return Board;
    }());
    var MathTable = (function () {
        function MathTable(h, w) {
            this.pad = 2;
            this.MD = [];
            this.ARROW = [];
            this.ATAN2 = [];
            this.SIN = [];
            this.COS = [];
            this.DEGFIX = [];
            this.h = h;
            this.w = w;
            this.pad = 1;
            this.width = WIDTH - this.pad * 2;
            this.height = HEIGHT - this.pad * 2;
            this.cellSize = Math.floor(Math.min(this.height / h, this.width / w));
            if (this.cellSize % 2)
                this.cellSize--;
            this.halfSize = this.cellSize / 2;
            // atan2 事前計算
            for (var dy = -h; dy <= h; dy++) {
                this.ATAN2[dy + h] = [];
                for (var dx = -w; dx <= w; dx++) {
                    var rad = Math.atan2(dy, dx);
                    if (rad < 0) {
                        // -PI から PI を 0 から 2PI に直す
                        rad += Math.PI * 2;
                    }
                    // 固定小数点に
                    this.ATAN2[dy + h][dx + w] = Math.round(rad / (Math.PI * 2) * MathTable.FIX);
                }
            }
            // 三角関数事前計算
            for (var i = 0; i < MathTable.FIX; i++) {
                var theta = i / MathTable.FIX * Math.PI * 2;
                this.SIN[i] = Math.round(Math.sin(theta) * this.halfSize * 0.70);
                this.COS[i] = Math.round(Math.cos(theta) * this.halfSize * 0.70);
            }
            // 固定小数点の角度事前計算
            for (var i = 0; i < 360; i++) {
                this.DEGFIX[i] = Math.round(i / 360 * MathTable.FIX);
            }
            // 距離ごとの色
            {
                var max = (w + h) * 0.3;
                for (var d = 0; d < h + w; d++) {
                    var ratio = Math.min(1.0, d / max);
                    var h_1 = void 0, l = void 0;
                    h_1 = ratio * 30;
                    l = ratio * 50 + 10;
                    this.MD[d] = "hsl(" + Math.floor(h_1) + ", 100%, " + Math.floor(l) + "%)";
                }
            }
            // 移動方向の三角形
            {
                var f = this.cellSize * 0.6;
                var h_2 = this.halfSize;
                var l2 = h_2 * 0.35;
                var l3 = h_2 * 0.12;
                // R
                var t;
                t = this.ARROW[0] = [];
                t[0] = -f + l2;
                t[1] = 0;
                t[2] = -f;
                t[3] = -l2;
                t[4] = -f;
                t[5] = -l3;
                t[6] = -f - l2;
                t[7] = -l3;
                t[8] = -f - l2;
                t[9] = +l3;
                t[10] = -f;
                t[11] = +l3;
                t[12] = -f;
                t[13] = +l2;
                // D
                t = this.ARROW[1] = [];
                t[0] = 0;
                t[1] = -f + l2;
                t[2] = -l2;
                t[3] = -f;
                t[4] = -l3;
                t[5] = -f;
                t[6] = -l3;
                t[7] = -f - l2;
                t[8] = +l3;
                t[9] = -f - l2;
                t[10] = +l3;
                t[11] = -f;
                t[12] = +l2;
                t[13] = -f;
                // L
                t = this.ARROW[2] = [];
                t[0] = +f - l2;
                t[1] = 0;
                t[2] = +f;
                t[3] = -l2;
                t[4] = +f;
                t[5] = -l3;
                t[6] = +f + l2;
                t[7] = -l3;
                t[8] = +f + l2;
                t[9] = +l3;
                t[10] = +f;
                t[11] = +l3;
                t[12] = +f;
                t[13] = +l2;
                // U
                t = this.ARROW[3] = [];
                t[0] = 0;
                t[1] = +f - l2;
                t[2] = -l2;
                t[3] = +f;
                t[4] = -l3;
                t[5] = +f;
                t[6] = -l3;
                t[7] = +f + l2;
                t[8] = +l3;
                t[9] = +f + l2;
                t[10] = +l3;
                t[11] = +f;
                t[12] = +l2;
                t[13] = +f;
            }
        }
        MathTable.prototype.atan2 = function (y, x) {
            return this.ATAN2[y + this.h][x + this.w];
        };
        MathTable.prototype.sin = function (fixnum) {
            if (fixnum > MathTable.FIX)
                fixnum %= MathTable.FIX;
            return this.SIN[fixnum];
        };
        MathTable.prototype.cos = function (fixnum) {
            if (fixnum > MathTable.FIX)
                fixnum %= MathTable.FIX;
            return this.COS[fixnum];
        };
        MathTable.prototype.degfix = function (deg) {
            return this.DEGFIX[deg];
        };
        return MathTable;
    }());
    MathTable.FIX = 10000;
    visualizer.init = function () {
        var file1 = document.getElementById("file1");
        var file2 = document.getElementById("file2");
        var pd = document.getElementById("pd");
        var result = document.getElementById("result");
        // controls
        var seek = document.getElementById("seek");
        var pos = document.getElementById("pos");
        var firstButton = document.getElementById("firstButton");
        var prevButton = document.getElementById("prevButton");
        var playButton = document.getElementById("playButton");
        var nextButton = document.getElementById("nextButton");
        var lastButton = document.getElementById("lastButton");
        var wrapper = document.getElementById("wrapper");
        var canvas = document.getElementById("canvas");
        var ctx = canvas.getContext('2d');
        canvas.width = WIDTH;
        canvas.height = HEIGHT;
        var draw = function (frame, mathTable) {
            var board = frame.board;
            var h = mathTable.h;
            var w = mathTable.w;
            var pad = mathTable.pad;
            var cellSize = mathTable.cellSize;
            var ctop = function (y) {
                return y * cellSize + pad;
            };
            var clef = function (x) {
                return x * cellSize + pad;
            };
            var cmidy = function (y) {
                return (ctop(y) + ctop(y + 1)) / 2;
            };
            var cmidx = function (x) {
                return (clef(x) + clef(x + 1)) / 2;
            };
            var drawFloor = function () {
                ctx.clearRect(clef(0), ctop(0), clef(w), ctop(h));
                ctx.beginPath();
                ctx.strokeStyle = 'black';
                // 縦線
                for (var x = 0; x < w + 1; x++) {
                    ctx.moveTo(clef(x), ctop(0));
                    ctx.lineTo(clef(x), ctop(h));
                }
                // 横線
                for (var y = 0; y < h + 1; y++) {
                    ctx.moveTo(clef(0), ctop(y));
                    ctx.lineTo(clef(w), ctop(y));
                }
                ctx.stroke();
            };
            var okSize = cellSize * 0.5;
            var okHalf = okSize / 2;
            var drawCar = function (i) {
                var cy = frame.y[i];
                var cx = frame.x[i];
                var dy = board.dy[i];
                var dx = board.dx[i];
                var my = cmidy(cy);
                var mx = cmidx(cx);
                var md = calcManhattan(cy, cx, dy, dx);
                ctx.fillStyle = mathTable.MD[md];
                if (cy == dy && cx == dx) {
                    // 到着
                    ctx.fillRect(cmidx(cx) - okHalf, cmidy(cy) - okHalf, okSize, okSize);
                }
                else {
                    var a0 = mathTable.atan2(dy - cy, dx - cx); // y は上下が逆
                    var a1 = a0 + mathTable.degfix(40);
                    var a2 = a0 + mathTable.degfix(140);
                    var a3 = a0 + mathTable.degfix(220);
                    var a4 = a0 + mathTable.degfix(320);
                    var y0 = mathTable.sin(a0) * 1.25 + my;
                    var x0 = mathTable.cos(a0) * 1.25 + mx;
                    var y1 = mathTable.sin(a1) + my;
                    var x1 = mathTable.cos(a1) + mx;
                    var y2 = mathTable.sin(a2) + my;
                    var x2 = mathTable.cos(a2) + mx;
                    var y3 = mathTable.sin(a3) + my;
                    var x3 = mathTable.cos(a3) + mx;
                    var y4 = mathTable.sin(a4) + my;
                    var x4 = mathTable.cos(a4) + mx;
                    ctx.beginPath();
                    ctx.strokeStyle = 'black';
                    ctx.moveTo(x0, y0);
                    ctx.lineTo(x1, y1);
                    ctx.lineTo(x2, y2);
                    ctx.lineTo(x3, y3);
                    ctx.lineTo(x4, y4);
                    ctx.fill();
                }
                // 移動元を表す情報を描画
                ctx.fillStyle = 'black';
                if (frame.d[i] != 4) {
                    var d = frame.d[i];
                    var n = mathTable.ARROW[d].length / 2;
                    ctx.beginPath();
                    ctx.moveTo(mathTable.ARROW[d][0] + mx, mathTable.ARROW[d][1] + my);
                    for (var i_1 = 1; i_1 < n; i_1++) {
                        ctx.lineTo(mathTable.ARROW[d][i_1 * 2] + mx, mathTable.ARROW[d][i_1 * 2 + 1] + my);
                    }
                    ctx.fill();
                }
            };
            var drawLine = function (i) {
                var cy = frame.y[i];
                var cx = frame.x[i];
                var dy = board.dy[i];
                var dx = board.dx[i];
                var my = cmidy(cy);
                var mx = cmidx(cx);
                if (cy == dy && cx == dx)
                    return;
                var md = calcManhattan(cy, cx, dy, dx);
                ctx.beginPath();
                ctx.strokeStyle = mathTable.MD[md];
                ctx.moveTo(mx, my);
                ctx.lineTo(cmidx(dx), cmidy(dy));
                ctx.stroke();
            };
            drawFloor();
            for (var i = 0; i < board.k; i++) {
                drawCar(i);
            }
            if (lineEnabled) {
                for (var i = 0; i < board.k; i++) {
                    drawLine(i);
                }
            }
        };
        var run = function (value1, value2) {
            result.value = '0';
            seek.min = seek.max = pos.value = seek.value = '0';
            pos.step = seek.step = '1';
            var lineCheck = document.getElementById("line");
            lineEnabled = lineCheck.checked;
            var board;
            try {
                board = new Board(value1);
            }
            catch (e) {
                alert(e);
                console.warn(e);
                result.value = 'ERROR at input';
                return;
            }
            var frames;
            try {
                frames = board.calc(value2);
            }
            catch (e) {
                alert(e);
                console.warn(e);
                result.value = 'WA';
                return;
            }
            ctx.fillStyle = "white";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            var mathTable = new MathTable(board.h, board.w);
            // 表示するやつ
            var d = function () {
                var frame = frames[parseInt(seek.value)];
                draw(frame, mathTable);
                pd.value = frame.pd.toString();
                result.value = frame.score.toString();
            };
            // 最終フレームを表示
            pos.value = pos.max = seek.value = seek.max = (frames.length - 1).toString();
            d();
            // 矢印キー左右で移動
            window.onkeydown = function (e) {
                if (e.target == seek)
                    return;
                switch (e.keyCode) {
                    case 37:
                        prevButton.onclick(null);
                        break;
                    case 39:
                        nextButton.onclick(null);
                        break;
                }
            };
            // control類の listener
            lineCheck.onchange = function () {
                lineEnabled = lineCheck.checked;
                d();
            };
            seek.onchange = seek.oninput = function () {
                pos.value = seek.value;
                d();
            };
            pos.onchange = function () {
                seek.value = pos.value;
                d();
            };
            firstButton.onclick = function () {
                seek.value = pos.value = seek.min;
                d();
            };
            prevButton.onclick = function () {
                var f = parseInt(seek.value);
                if (f > 0) {
                    f--;
                    pos.value = seek.value = f.toString();
                    d();
                }
            };
            nextButton.onclick = function () {
                var f = parseInt(seek.value);
                if (f < frames.length - 1) {
                    f++;
                    pos.value = seek.value = f.toString();
                    d();
                }
            };
            lastButton.onclick = function () {
                pos.value = seek.value = seek.max;
                d();
            };
            // 再生ボタンを制御するやつ
            var id;
            var play = function () {
                if (seek.value == seek.max) {
                    seek.value = '0';
                }
                var stop = function () {
                    clearInterval(id);
                    playButton.onclick = play;
                };
                id = setInterval(function () {
                    var f = parseInt(seek.value);
                    if (f < frames.length - 1) {
                        f++;
                        pos.value = seek.value = f.toString();
                        d();
                    }
                    else {
                        stop();
                    }
                }, 1000 / 30);
                playButton.onclick = stop;
            };
            playButton.onclick = play;
            seek.focus();
        };
        return function () {
            if (file1.files[0]) {
                loadTo(file1.files[0], function (value1) {
                    loadTo(file2.files[0], function (value2) {
                        run(value1.trim(), value2.trim());
                    });
                });
            }
        };
    };
})(visualizer || (visualizer = {}));
window.onload = function () {
    document.getElementById("run").onclick = visualizer.init();
};
