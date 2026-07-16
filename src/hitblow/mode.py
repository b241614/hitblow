def select_mode():
    """プレイヤーにゲームモード（数字 or アルファベット）を選択させます。

    Returns:
        str: "number" または "alphabet"
    """
    while True:
        print("=== モード選択 ===")
        print("1: 通常モード（数字）")
        print("2: アルファベットモード")
        choice = input("モードを選択してください (1 または 2) > ").strip()

        if choice == "1":
            return "number"
        elif choice == "2":
            return "alphabet"
        else:
            print("無効な入力です。1 または 2 を入力してください。\n")