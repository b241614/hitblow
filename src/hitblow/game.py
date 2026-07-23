"""ゲームの進行（入力・表示・ループ）。

★ チームで足す機能は **自分の担当の場所**に書く（1機能=1ファイル）。
   下の「ここに足す」場所は3か所（① 開始時 ② 入力コマンド ③ 勝利時）。
   ペアごとに**別の場所**を直すので、並行作業でも衝突しない。
   import も自分の場所の近くに書くこと（ファイル先頭にまとめない＝衝突回避）。
"""

from .core import judge, make_secret


def play(digits=3):
    from .difficulty import select_digits
    # ===== ① 開始時に足す（難易度・あいさつ など）: ここに書く =====
    from .mode import select_mode
    from .life import init_lives, update_lives, display_lives


    mode = select_mode()
    digits = select_digits()
    secret = make_secret(digits)

    mode_name = "数字" if mode == "number" else "アルファベット" 

    secret = make_secret(digits, mode=mode)
    lives = init_lives(digits)

    print(f"Hit & Blow（{digits} 桁・重複なし）")
    tries = 0
    while True:
        print(f"\nライフ：{display_lives(lives)}")
        guess = input("予想 > ").strip()

        # ===== ② 入力コマンドに足す（ヒント など）: ここに書く（import もここに） =====
        # 例:  from .hint import hint
        #      if guess == "h":
        #          print(hint(secret)); continue

        is_valid = False
        if mode == "number" and guess.isdigit():
            is_valid = True
        elif mode == "alphabet" and guess.isalpha():
            guess = guess.upper()
            is_valid = True

        if len(guess) != digits or not is_valid:
            print(f"{digits} 桁の{mode_name}で入力してね")
            continue
        tries += 1
        hit, blow = judge(secret, guess)
        print(f"  Hit={hit}  Blow={blow}")

        old_lives = lives
        lives = update_lives(lives, hit, blow)

        if lives < old_lives:
           print("💔 HitもBlowも0だったためライフが1減りました！")

        if lives == 0:
           print(f"\nゲームオーバー！ 答えは {secret} でした。")
           break
        if hit == digits:

            # ===== ③ 勝利時に足す（スコア・履歴 など）: ここに書く =====
            from .score import display_score
            display_score(digits, lives, secret, tries)

            break