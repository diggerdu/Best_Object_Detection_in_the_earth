from utils import *
from darknet import Darknet
import cv2

def demo(cfgfile, weightfile):
    m = Darknet(cfgfile)
    m.print_network()
    m.load_weights(weightfile)
    print('Loading weights from %s... Done!' % (weightfile))

    if m.num_classes == 20:
        namesfile = 'data/voc.names'
    elif m.num_classes == 80:
        namesfile = 'data/coco.names'
    else:
        namesfile = 'data/names'
    class_names = load_class_names(namesfile)

    use_cuda = 0
    if use_cuda:
        m.cuda()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Unable to open camera")
        exit(-1)

    tracker = cv2.TrackerMIL_create()
    trackerList = list()

    while True:
        res, img = cap.read()
        if res:
            sized = cv2.resize(img,((m.width, m.height)))
            bboxes = do_detect(m, sized, 0.5, 0.4, use_cuda)
            if bboxes.__len__() != 0:
                for k in range(n):
                     trackList.append(cv2.TrackerMIL_create().__init__(img,tuple(bboxes[k][:4])))
                     break

    i = 1
    while True:
        if i>10:
            i = 1
            res, img = cap.read()
            if res:
                sized = cv2.resize(img, (m.width, m.height))
                bboxes = do_detect(m, sized, 0.5, 0.4, use_cuda)
                bboxes = tuple(bboxes)
                ok = tracker.init(img, bboxes)
            else:
                 print("Unable to read image")
                 exit(-1)
        else:
            ok, bboxes = tracker.update(image)
            i += 1


        print('------')
        draw_img = plot_boxes_cv2(img, bboxes, None, class_names)
        cv2.imshow(cfgfile, draw_img)
        cv2.waitKey(1)

############################################
if __name__ == '__main__':

    #if len(sys.argv) == 3:
    #    cfgfile = sys.argv[1]
    #    weightfile = sys.argv[2]
    #    demo(cfgfile, weightfile)

    demo('cfg/yolo.cfg', 'yolo.weights')

    #else:
    #    print('Usage:')
    #    print('    python demo.py cfgfile weightfile')
    #    print('')
    #    print('    perform detection on camera')
