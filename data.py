
STRETCHES = [
    # Pre-Ride (Dynamic)
    {
        "id": 1,
        "name": "レッグスイング",
        "mode": "pre",
        "description": "壁や自転車に手を置き、片足を前後に大きく振ります。股関節の可動域を広げます。",
        "duration": "左右各10回",
        "image_file": "leg_swing.svg"
    },
    {
        "id": 2,
        "name": "腕回し",
        "mode": "pre",
        "description": "肩甲骨を意識して、腕を前回し・後ろ回しに大きく動かします。",
        "duration": "各10回",
        "image_file": "arm_circles.svg"
    },
    {
        "id": 3,
        "name": "股関節ローテーション",
        "mode": "pre",
        "description": "膝を高く上げ、外側に開いて下ろす動きを繰り返します。",
        "duration": "左右各10回",
        "image_file": "hip_rotation.svg"
    },

    # Mid-Ride (Convenience/Discrete)
    {
        "id": 4,
        "name": "首のストレッチ",
        "mode": "mid",
        "filter": "discrete",
        "description": "首をゆっくり左右に傾け、僧帽筋を伸ばします。手で軽く補助すると効果的。",
        "duration": "左右20秒",
        "image_file": "neck_stretch.svg"
    },
    {
        "id": 5,
        "name": "手首・前腕ストレッチ",
        "mode": "mid",
        "filter": "discrete",
        "description": "腕を前に出し、指先を自分の方へ引いて前腕を伸ばします。ハンドルを持つ手の疲れに。",
        "duration": "左右20秒",
        "image_file": "wrist_stretch.svg"
    },
    {
        "id": 6,
        "name": "肩甲骨寄せ",
        "mode": "mid",
        "filter": "discrete",
        "description": "後ろで手を組み、胸を開いて肩甲骨を寄せます。猫背姿勢のリセットに。",
        "duration": "20秒",
        "image_file": "chest_opener.svg"
    },

    # Mid-Ride (Park/Active)
    {
        "id": 7,
        "name": "深いアキレス腱伸ばし",
        "mode": "mid",
        "filter": "active",
        "description": "片足を大きく後ろに引き、ふくらはぎを伸ばします。ペダリングで疲れた足に。",
        "duration": "左右30秒",
        "image_file": "calf_stretch.svg"
    },
    {
        "id": 8,
        "name": "腸腰筋ストレッチ",
        "mode": "mid",
        "filter": "active",
        "description": "片膝を立てて前屈みになり、後ろ足の付け根（股関節前部）を伸ばします。",
        "duration": "左右30秒",
        "image_file": "placeholder.png"
    },

    # Post-Ride (Static)
    {
        "id": 9,
        "name": "太もも前（大腿四頭筋）",
        "mode": "post",
        "description": "立った状態で足首を持ち、お尻に近づけます。膝を後ろに引くとより伸びます。",
        "duration": "左右30秒",
        "image_file": "quad_stretch.svg"
    },
    {
        "id": 10,
        "name": "ハムストリングス",
        "mode": "post",
        "description": "足を投げ出して座り、体を前に倒して太ももの裏側を伸ばします。",
        "duration": "左右30秒",
        "image_file": "hamstring_stretch.svg"
    },
    {
        "id": 11,
        "name": "お尻（大殿筋）",
        "mode": "post",
        "description": "仰向けで片膝を抱え、胸の方へ引き寄せます。腰痛予防にもなります。",
        "duration": "左右30秒",
        "image_file": "glute_stretch.svg"
    },
    {
        "id": 12,
        "name": "ふくらはぎ",
        "mode": "post",
        "description": "壁に手をき、片足を後ろに引いてかかとを床につけたまま前へ重心移動します。",
        "duration": "左右30秒",
        "image_file": "calf_stretch.svg"
    }
]

def get_stretches(mode, filter_type=None):
    results = [s for s in STRETCHES if s['mode'] == mode]
    if filter_type:
        results = [s for s in results if s.get('filter') == filter_type]
    return results
