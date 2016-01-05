from src.hash_tools import Hashing
from src import config
from PIL import Image


def test(run_times=1):
    avg_duration = 0.0
    for i in range(run_times):
        hashing = Hashing()

        img1 = Image.open(config.images_dir + 'derevo1.jpg')
        img2 = Image.open(config.images_dir + 'derevo8.jpg')

        hash1 = hashing.build_dhash(img1)
        hash2 = hashing.build_dhash(img2)

        dist = hashing.hamming_distance(hash1, hash2)

        print "Image 1 hash: " + hash1 + "\nImage 2 hash: " + hash2 + "\nThe same?: " + str(
            hashing.similarity(dist)) + "\nHamming distance is: " + str(
            dist) + "\nDuration: " + hashing.current_duration

        avg_duration += float(hashing.current_duration)

    print "Average duration for " + str(run_times) + " runs is: " + str(avg_duration / run_times) + " ms"


if __name__ == "__main__":
    test()
