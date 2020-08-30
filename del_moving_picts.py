from multiprocessing.dummy import Pool as ThreadPool
from pathlib import Path


def find_animation(image):
    if image.name.endswith(".gif") or image.name.endswith(".mp4"):
        try:
            image.unlink()
        except IOError as e:
            print(e)


if __name__ == "__main__":
    image_path = Path("/media/cody/250GB_Int/MEGAsync/piz/new")
    images = [image for image in image_path.rglob("*")]

    pool = ThreadPool(8)  # Make a thread pool of 8
    pool.map(find_animation, images)
    pool.close()
    pool.join()
