import random
from PIL import Image, ImageDraw, ImageFont
import tweepy
import os

HIRAGANA = list("あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをんゐゑぁぃぅぇぉ○！？")

def generate_random_4kana():
    return ''.join(random.choices(HIRAGANA, k=4))

def create_image_with_text(text, out_path='output.png'):
    img = Image.new('RGB', (512, 256), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
    w, h = draw.textsize(text, font=font)
    draw.text(((512-w)/2, (256-h)/2), text, font=font, fill=(0, 0, 0))
    img.save(out_path)

def tweet_image(text):
    auth = tweepy.OAuth1UserHandler(
        os.environ[tGvzTQUEKswuVCkJn5zKoudc2],
        os.environ[SM1K571d8KwiCyWECPsSVPtbsIweENldvCrnF7mGJmFEIpGPYS],
        os.environ[1899010131423289344-QwW7hKAAlPs6KEsgdM1rR9rtCZGjy7],
        os.environ[Vaa36lDn2ljhix8zGbsuCBVhWtsKzwWkc3IciULnkPSCp]
    )
    api = tweepy.API(auth)
    create_image_with_text(text)
    api.update_status_with_media(status=text, filename='output.png')

if __name__ == "__main__":
    word = generate_random_4kana()
    tweet_image(word)
