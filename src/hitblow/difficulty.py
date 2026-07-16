def select_digits():
    """遊ぶ桁数を入力して返す"""
    while True:
        try:
            digits = int(input("何桁で遊びますか？（3～10）: "))
            if 3 <= digits <= 10:
                return digits
            print("3～10の数字を入力してください。")
        except ValueError:
            print("数字を入力してください。")
