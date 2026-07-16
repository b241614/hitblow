def init_lives(digits):
    """桁数に応じた初期ライフを返す"""
    return digits


def update_lives(lives, hit, blow):
    """Hit・Blowがともに0ならライフを1減らす"""
    if hit == 0 and blow == 0:
        lives -= 1
    return lives


def display_lives(lives):
    """ライフをハートで表示する"""
    return "❤️" * lives
