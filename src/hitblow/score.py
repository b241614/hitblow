"""スコア（★表示）管理機能"""

import math

def get_star_count(digits, remaining_lives):
    """桁数と残りライフから★の数を計算する（全桁共通：ノーミスで★3）"""
    if remaining_lives <= 0:
        return 0

    # ノーミスクリア（1回もミスしていない）
    if remaining_lives == digits:
        return 3
    # 半分以上のライフを残してクリア
    elif remaining_lives >= math.ceil(digits / 2):
        return 2
    # ライフを残してクリア
    else:
        return 1


def display_score(digits, remaining_lives, secret, tries):
    """リザルト画面を表示し、星の数を返す"""
    star_count = get_star_count(digits, remaining_lives)
    
    # 星の文字列（★ ★ ★ や ★ ★ ☆）
    stars_str = " ".join(["★" if i < star_count else "☆" for i in range(3)])
    
    # ライフのハート表記（♥♥♥♡♡）
    hearts_str = "♥" * remaining_lives + "♡" * (digits - remaining_lives)
    
    # 正解の文字を [ 3 ] [ 8 ] [ 1 ] [ 5 ] の形式に整形
    formatted_secret = " ".join([f"[ {char} ]" for char in str(secret)])

    # リザルト画面の出力
    print("\n======================================")
    print("           STAGE CLEAR!")
    print("======================================\n")
    print(f"          {stars_str}  (獲得スター)\n")
    print(f"  正解 :  {formatted_secret}\n")
    print("  ----------------------------------")
    print(f"  残りライフ :  {hearts_str}  ({remaining_lives} / {digits})")
    print(f"  挑戦回数   :  {tries}回")
    print("  ----------------------------------")
    print("======================================\n")

    return star_count