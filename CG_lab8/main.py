import numpy as np
import random
import cv2


def getRandomNoise():
    return random.random() / 3


def unsharpMask(image, kernel_size=(5, 5), sigma=1.0, amount=2.0, threshold=0):
    blurred = cv2.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened



def noiseByGaus(image, value):
    row, col, ch = image.shape
    gauss = np.random.randn(row, col, ch)
    gauss = gauss.reshape(row, col, ch)
    return image + image * gauss * value


def findTV(image, edged):
    cont, hier = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    amount = 0
    for c in cont:
        epsilon = 0.15 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)
        if len(approx) == 4:
            cv2.drawContours(image, [approx], -1, (0, 255, 255), 4)
            amount += 1
    print(f"Знайдено {amount} телевізор(ів) на цій картинці")
    cv2.imwrite("foundTVOnPicture.jpg", image)


def main():
    picture = cv2.imread("picture.jpg", cv2.IMREAD_COLOR)
    noised = noiseByGaus(picture, getRandomNoise())
    cv2.imwrite("noisedPicture.jpg", noised)
    blurred = cv2.GaussianBlur(noised, (5, 5), 0)
    cv2.imwrite("blurredPicture.jpg", blurred)
    normalized = cv2.normalize(blurred, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    cv2.imwrite("normalizedPicture.jpg", normalized)
    normalized = unsharpMask(normalized)
    cv2.imwrite("unsharpMaskedPicture.jpg", normalized)
    gray = cv2.imread('unsharpMaskedPicture.jpg', 0)
    cv2.imwrite("grayPicture.jpg", gray)
    edged = cv2.Canny(gray, 10, 250)
    cv2.imwrite("edgedPicture.jpg", edged)
    findTV(picture, edged)


if __name__ == '__main__':
    main()
