"""体育场核心逻辑：赛事、座位、票务和放映。"""

import json


def new_game():
    return {"sessions": {}, "seats": 2, "tickets": {}, "day": 1, "ticket_id": 0}


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["ticket_id"] += 1
    return state


def schedule(state, session_id):
    state["sessions"][session_id] = True
    return True


def sell_ticket(state, session_id):
    state["tickets"][session_id] = state["tickets"].get(session_id, 0) + 1
    return True


def price(state, end_day):
    return (end_day - state["day"]) - 1


def cancel_session(state, session_id):
    return True


def show(state, session_id):
    return True


def refund(state, session_id):
    state["tickets"].pop(session_id, None)
    return False


def extra_show(state):
    state["bonus"] = state.get("bonus", 0) + 2
    return True


def main():
    print("体育场 - 命令: schedule/sell/price/cancel/show/refund/extra/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
