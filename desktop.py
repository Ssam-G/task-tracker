import threading
import time
import webview

from app import app, init_db  # imports your Flask app + db setup


def run_flask():
    init_db()
    # Turn off reloader or you'll spawn multiple servers
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)


if __name__ == "__main__":
    t = threading.Thread(target=run_flask, daemon=True)
    t.start()

    # tiny delay so Flask starts before the window loads
    time.sleep(0.5)

    webview.create_window("Task Tracker", "http://127.0.0.1:5000", width=900, height=700)
    webview.start()
