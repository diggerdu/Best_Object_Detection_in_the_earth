"""
    res, img = cap.read()
    if res:
        sized = cv2.resize(img, (m.width, m.height))
        bboxes = do_detect(m, sized, 0.5, 0.4, use_cuda)
        bboxes = tuple(bboxes)
        print (bboxes)
        ok = tracker.init(img, bboxes)
    else:
        print("Unable to read image")
        exit(-1)
"""
