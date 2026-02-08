import threading
import time
import webview

from app import app, init_db


def run_flask():
    init_db()
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)


def auto_resize_loop(window: webview.Window):
    # Give the page time to load
    time.sleep(0.8)

    last_w, last_h = 0, 0

    while True:
        try:
            dims = window.evaluate_js("""
                (() => {
                    const note = document.querySelector('.note');
                    const r = note.getBoundingClientRect();
                    return {
                        w: r.width,
                        h: r.height
                    };
                })();
            """)

            if dims and "w" in dims and "h" in dims:
                # Add padding to account for window borders/title bar
                new_w = dims["w"]
                new_h = dims["h"] + 20

                # Only resize if it actually changed (prevents jitter)
                if abs(new_w - last_w) > 2 or abs(new_h - last_h) > 2:
                    window.resize(new_w, new_h)
                    last_w, last_h = new_w, new_h

        except Exception:
            pass

        time.sleep(0.4)


if __name__ == "__main__":
    t = threading.Thread(target=run_flask, daemon=True)
    t.start()

    window = webview.create_window(
        "Task Tracker",
        "http://127.0.0.1:5000",
        width=600,
        height=760,
        resizable=True
    )

    threading.Thread(target=auto_resize_loop, args=(window,), daemon=True).start()
    webview.start()
