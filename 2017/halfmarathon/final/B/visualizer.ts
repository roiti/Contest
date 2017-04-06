module visualizer {
    // RDLU-
    const DY = [0, 1, 0, -1, 0];
    const DX = [1, 0, -1, 0, 0];
    const A_TO_DIR = {'R': 0, 'D': 1, 'L': 2, 'U': 3, '-': 4};
    const WIDTH = 1600, HEIGHT = 1600;
    let lineEnabled = true;

    const loadTo = (file, callback) => {
        const reader = new FileReader();
        reader.readAsText(file);
        reader.onloadend = function () {
            callback(reader.result);
        }
    };

    const getInt = (s: string, lineno: number) => {
        if (s == null) {
            throw new Error(`数値のパースに失敗しました at line: ${lineno}`);
        }
        s = s.trim();
        if (s.match(/^\d+$/)) {
            return parseInt(s);
        }
        throw new Error(`数値のパースに失敗しました at line: ${lineno}`);
    };

    const calcManhattan = (y1, x1, y2, x2) => {
        return Math.abs(y1 - y2) + Math.abs(x1 - x2);
    };

    const aToDir = (a: string): number => {
        if (!A_TO_DIR.hasOwnProperty(a)) {
            throw new Error(`WA: 行動に 'RDLU-' 以外の文字があります: '${a}'`);
        }
        return A_TO_DIR[a];
    };

    class Frame {
        public board: Board;
        public state: number[][];  // b[y][x] : b[y][x] にいる車番号。いないとき -1
        public y: number[] = [];  // 車 i の y
        public x: number[] = [];  // 車 i の x
        public pd: number;
        public score: number;
        public turn: number;
        public d: number[] = [];  // 車 i が直前にどう移動して今の位置に来たのか。dir が入っている。初期フレームは 4 が入っている

        public calcScore() {
            this.pd = 20.0;
            for (let i = 0; i < this.board.k; i++) {
                this.pd += calcManhattan(this.y[i], this.x[i], this.board.dy[i], this.board.dx[i]);
            }
            const pt = this.turn * 0.01 + 10;
            this.score = Math.ceil(1e7 / (this.pd * pt));
        }

        public next(line: string): Frame {
            const next: Frame = new Frame();
            next.board = this.board;
            next.turn = this.turn + 1;
            next.state = [];

            for (let i = 0; i < this.board.h; i++) {
                next.state[i] = [];
                for (let j = 0; j < this.board.w; j++) {
                    next.state[i][j] = -1;
                }
            }

            for (let i = 0; i < this.board.k; i++) {
                const dir = aToDir(line[i]);
                const y = this.y[i];
                const x = this.x[i];
                const ny = y + DY[dir];
                const nx = x + DX[dir];
                if (!this.board.inside(ny, nx)) {
                    console.log(this);
                    throw new Error(`WA: 盤面の外に移動しようとしています: ターン: ${next.turn}, ` +
                        `移動する車ID: ${i + 1}, 位置: (${ny + 1}, ${nx + 1})`);
                }
                if (dir != 4 && this.state[ny][nx] != -1) {
                    console.log(this);
                    throw new Error(`WA: 移動先に車がいます: ターン: ${next.turn}, 移動する車ID: ${i + 1}, ` +
                        `既にいる車ID: ${this.state[ny][nx] + 1}, 位置: (${ny + 1}, ${nx + 1})`);
                }
                if (next.state[ny][nx] != -1) {
                    console.log(this);
                    throw new Error(`WA: 移動先に車がいます: ターン: ${next.turn}, 移動する車ID: ${i + 1}, ` +
                        `既にいる車ID: ${next.state[ny][nx] + 1}, 位置: (${ny + 1}, ${nx + 1})`);
                }
                next.d[i] = dir;
                next.y[i] = ny;
                next.x[i] = nx;
                next.state[ny][nx] = i;
            }
            next.calcScore();
            return next;
        }
    }

    class Board {
        public h: number;
        public w: number;
        public k: number;
        public t: number;
        public sy: number[] = [];  // 車 i の初期地 y
        public sx: number[] = [];  // 車 i の初期地 x
        public dy: number[] = [];  // 車 i の目的地 y
        public dx: number[] = [];  // 車 i の目的地 x

        constructor(value1: string) {
            const lines = value1.trim().split("\n");
            const l1 = lines[0].trim().split(" ");
            this.h = getInt(l1[0], 1);
            this.w = getInt(l1[1], 1);
            this.k = getInt(l1[2], 1);
            this.t = getInt(l1[3], 1);

            for (let i = 0; i < this.k; i++) {
                const l = lines[i + 1].trim().split(" ");
                this.sy[i] = getInt(l[0], i + 1) - 1;
                this.sx[i] = getInt(l[1], i + 1) - 1;
                this.dy[i] = getInt(l[2], i + 1) - 1;
                this.dx[i] = getInt(l[3], i + 1) - 1;
            }
        }

        public initialFrame() {
            const frame: Frame = new Frame();
            frame.board = this;
            frame.turn = 0;

            frame.state = [];

            for (let i = 0; i < this.h; i++) {
                frame.state[i] = [];
                for (let j = 0; j < this.w; j++) {
                    frame.state[i][j] = -1;
                }
            }
            for (let i = 0; i < this.k; i++) {
                frame.state[this.sy[i]][this.sx[i]] = i;
                frame.y[i] = this.sy[i];
                frame.x[i] = this.sx[i];
                frame.d[i] = 4;
            }
            frame.calcScore();
            return frame;
        }

        public calc(actions: string): Frame[] {
            const lines = actions.trim().split("\n");
            const c = getInt(lines[0].trim(), 1);
            if (c > this.t) {
                throw new Error(`WA: 操作回数 C が T を超えています: C=${c}, T=${this.t}`);
            }

            const frames: Frame[] = [];

            let cur = this.initialFrame();
            frames.push(cur);

            for (let i = 0; i < c; i++) {
                const line = lines[i + 1].trim();
                if (line.length != this.k) {
                    throw new Error(`WA: 操作回数 ${i + 1} の長さが K と一致しません: ${line.length} 文字, K: ${this.k}`);
                }
                cur = cur.next(line);
                frames.push(cur);
            }
            return frames;
        }

        public inside(y, x): boolean {
            return (0 <= y) && (y < this.h) && (0 <= x) && (x < this.w);
        }
    }

    class MathTable {
        public static FIX = 10000;
        public h: number;
        public w: number;
        public pad = 2;
        public width: number;
        public height: number;
        public cellSize: number;
        public halfSize: number;
        public MD: string[] = [];
        public ARROW: number[][] = [];

        private ATAN2: number[][] = [];
        private SIN: number[] = [];
        private COS: number[] = [];
        private DEGFIX: number[] = [];

        public constructor(h: number, w: number) {
            this.h = h;
            this.w = w;
            this.pad = 1;
            this.width = WIDTH - this.pad * 2;
            this.height = HEIGHT - this.pad * 2;
            this.cellSize = Math.floor(Math.min(this.height / h, this.width / w));
            if (this.cellSize % 2) this.cellSize--;
            this.halfSize = this.cellSize / 2;

            // atan2 事前計算
            for (let dy = -h; dy <= h; dy++) {
                this.ATAN2[dy + h] = [];
                for (let dx = -w; dx <= w; dx++) {
                    let rad = Math.atan2(dy, dx);
                    if (rad < 0) {
                        // -PI から PI を 0 から 2PI に直す
                        rad += Math.PI * 2;
                    }
                    // 固定小数点に
                    this.ATAN2[dy + h][dx + w] = Math.round(rad / (Math.PI * 2) * MathTable.FIX);
                }
            }

            // 三角関数事前計算
            for (let i = 0; i < MathTable.FIX; i++) {
                const theta = i / MathTable.FIX * Math.PI * 2;
                this.SIN[i] = Math.round(Math.sin(theta) * this.halfSize * 0.70);
                this.COS[i] = Math.round(Math.cos(theta) * this.halfSize * 0.70);
            }

            // 固定小数点の角度事前計算
            for (let i = 0; i < 360; i++) {
                this.DEGFIX[i] = Math.round(i / 360 * MathTable.FIX);
            }

            // 距離ごとの色
            {
                const max = (w + h) * 0.3;
                for (let d = 0; d < h + w; d++) {
                    const ratio = Math.min(1.0, d / max);
                    let h, l;
                    h = ratio * 30;
                    l = ratio * 50 + 10;
                    this.MD[d] = `hsl(${Math.floor(h)}, 100%, ${Math.floor(l)}%)`;
                }
            }

            // 移動方向の三角形
            {
                const f = this.cellSize * 0.6;
                const h = this.halfSize;
                const l2 = h * 0.35;
                const l3 = h * 0.12;

                // R
                let t;
                t = this.ARROW[0] = [];
                t[ 0] = -f + l2; t[ 1] = 0;
                t[ 2] = -f;      t[ 3] = -l2;
                t[ 4] = -f;      t[ 5] = -l3;
                t[ 6] = -f - l2; t[ 7] = -l3;
                t[ 8] = -f - l2; t[ 9] = +l3;
                t[10] = -f;      t[11] = +l3;
                t[12] = -f;      t[13] = +l2;

                // D
                t = this.ARROW[1] = [];
                t[ 0] = 0;   t[ 1] = -f + l2;
                t[ 2] = -l2; t[ 3] = -f;
                t[ 4] = -l3; t[ 5] = -f;
                t[ 6] = -l3; t[ 7] = -f - l2;
                t[ 8] = +l3; t[ 9] = -f - l2;
                t[10] = +l3; t[11] = -f;
                t[12] = +l2; t[13] = -f;

                // L
                t = this.ARROW[2] = [];
                t[ 0] = +f - l2; t[ 1] = 0;
                t[ 2] = +f;      t[ 3] = -l2;
                t[ 4] = +f;      t[ 5] = -l3;
                t[ 6] = +f + l2; t[ 7] = -l3;
                t[ 8] = +f + l2; t[ 9] = +l3;
                t[10] = +f;      t[11] = +l3;
                t[12] = +f;      t[13] = +l2;

                // U
                t = this.ARROW[3] = [];
                t[ 0] = 0;   t[ 1] = +f - l2;
                t[ 2] = -l2; t[ 3] = +f;
                t[ 4] = -l3; t[ 5] = +f;
                t[ 6] = -l3; t[ 7] = +f + l2;
                t[ 8] = +l3; t[ 9] = +f + l2;
                t[10] = +l3; t[11] = +f;
                t[12] = +l2; t[13] = +f;
            }

        }

        public atan2(y, x): number {
            return this.ATAN2[y + this.h][x + this.w];
        }

        public sin(fixnum): number {
            if (fixnum > MathTable.FIX) fixnum %= MathTable.FIX;
            return this.SIN[fixnum];
        }

        public cos(fixnum): number {
            if (fixnum > MathTable.FIX) fixnum %= MathTable.FIX;
            return this.COS[fixnum];
        }

        public degfix(deg): number {
            return this.DEGFIX[deg];
        }
    }

    export const init = () => {
        const file1 = <HTMLInputElement> document.getElementById("file1");
        const file2 = <HTMLInputElement> document.getElementById("file2");
        const pd = <HTMLInputElement> document.getElementById("pd");
        const result = <HTMLInputElement> document.getElementById("result");

        // controls
        const seek = <HTMLInputElement> document.getElementById("seek");
        const pos = <HTMLInputElement> document.getElementById("pos");
        const firstButton = <HTMLInputElement> document.getElementById("firstButton");
        const prevButton = <HTMLInputElement> document.getElementById("prevButton");
        const playButton = <HTMLInputElement> document.getElementById("playButton");
        const nextButton = <HTMLInputElement> document.getElementById("nextButton");
        const lastButton = <HTMLInputElement> document.getElementById("lastButton");

        const wrapper = document.getElementById("wrapper");
        const canvas = <HTMLCanvasElement> document.getElementById("canvas");
        const ctx = canvas.getContext('2d');

        canvas.width = WIDTH;
        canvas.height = HEIGHT;

        const draw = (frame: Frame, mathTable: MathTable) => {
            const board = frame.board;
            const h = mathTable.h;
            const w = mathTable.w;

            const pad = mathTable.pad;
            const cellSize = mathTable.cellSize;

            const ctop = (y) => {
                return y * cellSize + pad;
            };

            const clef = (x) => {
                return x * cellSize + pad;
            };

            const cmidy = (y) => {
                return (ctop(y) + ctop(y + 1)) / 2;
            };

            const cmidx = (x) => {
                return (clef(x) + clef(x + 1)) / 2;
            };

            const drawFloor = () => {
                ctx.clearRect(clef(0), ctop(0), clef(w), ctop(h));

                ctx.beginPath();
                ctx.strokeStyle = 'black';

                // 縦線
                for (let x = 0; x < w + 1; x++) {
                    ctx.moveTo(clef(x), ctop(0));
                    ctx.lineTo(clef(x), ctop(h));
                }
                // 横線
                for (let y = 0; y < h + 1; y++) {
                    ctx.moveTo(clef(0), ctop(y));
                    ctx.lineTo(clef(w), ctop(y));
                }
                ctx.stroke();
            };

            const okSize = cellSize * 0.5;
            const okHalf = okSize / 2;

            const drawCar = (i) => {
                const cy = frame.y[i];
                const cx = frame.x[i];
                const dy = board.dy[i];
                const dx = board.dx[i];
                const my = cmidy(cy);
                const mx = cmidx(cx);
                const md = calcManhattan(cy, cx, dy, dx);

                ctx.fillStyle = mathTable.MD[md];

                if (cy == dy && cx == dx) {
                    // 到着
                    ctx.fillRect(cmidx(cx) - okHalf, cmidy(cy) - okHalf, okSize, okSize);
                }
                else {
                    const a0 = mathTable.atan2(dy - cy, dx - cx);  // y は上下が逆
                    const a1 = a0 + mathTable.degfix(40);
                    const a2 = a0 + mathTable.degfix(140);
                    const a3 = a0 + mathTable.degfix(220);
                    const a4 = a0 + mathTable.degfix(320);
                    const y0 = mathTable.sin(a0) * 1.25 + my;
                    const x0 = mathTable.cos(a0) * 1.25 + mx;
                    const y1 = mathTable.sin(a1) + my;
                    const x1 = mathTable.cos(a1) + mx;
                    const y2 = mathTable.sin(a2) + my;
                    const x2 = mathTable.cos(a2) + mx;
                    const y3 = mathTable.sin(a3) + my;
                    const x3 = mathTable.cos(a3) + mx;
                    const y4 = mathTable.sin(a4) + my;
                    const x4 = mathTable.cos(a4) + mx;
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
                    const d = frame.d[i];
                    const n = mathTable.ARROW[d].length / 2;
                    ctx.beginPath();
                    ctx.moveTo(mathTable.ARROW[d][0] + mx, mathTable.ARROW[d][1] + my);
                    for (let i = 1; i < n; i++) {
                        ctx.lineTo(mathTable.ARROW[d][i * 2] + mx, mathTable.ARROW[d][i * 2 + 1] + my);
                    }
                    ctx.fill();
                }
            };

            const drawLine = (i) => {
                const cy = frame.y[i];
                const cx = frame.x[i];
                const dy = board.dy[i];
                const dx = board.dx[i];
                const my = cmidy(cy);
                const mx = cmidx(cx);

                if (cy == dy && cx == dx) return;
                const md = calcManhattan(cy, cx, dy, dx);
                ctx.beginPath();
                ctx.strokeStyle = mathTable.MD[md];
                ctx.moveTo(mx, my);
                ctx.lineTo(cmidx(dx), cmidy(dy));
                ctx.stroke();
            };

            drawFloor();
            for (let i = 0; i < board.k; i++) {
                drawCar(i);
            }
            if (lineEnabled) {
                for (let i = 0; i < board.k; i++) {
                    drawLine(i);
                }
            }
        };

        const run = (value1, value2) => {
            result.value = '0';
            seek.min = seek.max = pos.value = seek.value = '0';
            pos.step = seek.step = '1';

            const lineCheck = <HTMLInputElement> document.getElementById("line");
            lineEnabled = lineCheck.checked;

            let board;
            try {
                board = new Board(value1);
            }
            catch (e) {
                alert(e);
                console.warn(e);
                result.value = 'ERROR at input';
                return;
            }

            let frames;
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

            const mathTable = new MathTable(board.h, board.w);

            // 表示するやつ
            const d = () => {
                let frame = frames[parseInt(seek.value)];
                draw(frame, mathTable);
                pd.value = frame.pd.toString();
                result.value = frame.score.toString();
            };

            // 最終フレームを表示
            pos.value = pos.max = seek.value = seek.max = (frames.length - 1).toString();
            d();

            // 矢印キー左右で移動
            window.onkeydown = (e: KeyboardEvent) => {
                if (e.target == seek) return;
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

            lineCheck.onchange = () => {
                lineEnabled = lineCheck.checked;
                d();
            };

            seek.onchange = seek.oninput = () => {
                pos.value = seek.value;
                d();
            };
            pos.onchange = () => {
                seek.value = pos.value;
                d();
            };
            firstButton.onclick = () => {
                seek.value = pos.value = seek.min;
                d();
            };
            prevButton.onclick = () => {
                let f = parseInt(seek.value);
                if (f > 0) {
                    f--;
                    pos.value = seek.value = f.toString();
                    d();
                }
            };
            nextButton.onclick = () => {
                let f = parseInt(seek.value);
                if (f < frames.length - 1) {
                    f++;
                    pos.value = seek.value = f.toString();
                    d();
                }
            };
            lastButton.onclick = () => {
                pos.value = seek.value = seek.max;
                d();
            };

            // 再生ボタンを制御するやつ
            let id;

            const play = () => {
                if (seek.value == seek.max) {
                    seek.value = '0';
                }
                const stop = () => {
                    clearInterval(id);
                    playButton.onclick = play;
                };
                id = setInterval(() => {
                    let f = parseInt(seek.value);
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

        return () => {
            if (file1.files[0]) {
                loadTo(file1.files[0], (value1) => {
                    loadTo(file2.files[0], (value2) => {
                        run(value1.trim(), value2.trim());
                    });
                });
            }
        };
    };
}

window.onload = () => {
    document.getElementById("run").onclick = visualizer.init();
};
