# katakana-regularizer
This program regularizes Katakana (especially person-names) with some heuristic rules.
The rules are as follows:
1. Non-standard Katakana characters are standardized; e.g., (ヲ→オ), (ヅ→ズ) (ヂ→ジ)
2. Non-standard use of small characters (小書き文字) is standardized; e.g., (レァ→レア), (シィ→シー), (デェ→デー), (タィ→タイ)
3. Unnecessary consecutive characters are omitted; e.g., (ーー→ー), (ンン→ン)
# Examples
- エマ**ヌュ**エル（Emanuel）→エマ**ニュ**エル  
- デカダンス**ドュ**ショコラ（Decadence du Chocolat）→デカダンス**デュ**ショコラ  
