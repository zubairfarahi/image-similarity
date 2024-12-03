import cv2


def feature_matching(img1, img2, ratio_thresh, match_threshold):
    """
    Matches features between two images using the SIFT algorithm.

    Parameters:
    - img1: First image.
    - img2: Second image.
    - ratio_thresh: Ratio threshold for Lowe's ratio test (default is 0.60).
    - match_threshold: Minimum number of good matches required to consider images as matching.

    Returns:
    - True if the number of good matches exceeds the match_threshold, otherwise False.
    """

    # Detecting keypoints and descriptors using SIFT
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    good_matches = []
    # If the number of good matches exceeds the threshold, return True; otherwise, return False
    for m, n in matches:
        if m.distance < float(ratio_thresh) * n.distance:
            good_matches.append(m)

    if len(good_matches) > float(match_threshold):
        return True
    else:
        return False
