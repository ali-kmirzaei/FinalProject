# Using YOLOv3 for object detection
After 6000 iteration on 700 train data and 200 test data, result is: <br />

-On TrainSet: <br />
detections_count = 1347, unique_truth_count = 1200 <br />
class_id = 0, name = Card, ap = 99.41%           (TP = 199, FP = 1) <br />
class_id = 1, name = Avatar, ap = 99.41%         (TP = 199, FP = 2) <br />
class_id = 2, name = Id, ap = 99.02%             (TP = 199, FP = 2) <br />
class_id = 3, name = Fname, ap = 99.44%          (TP = 198, FP = 2) <br />
class_id = 4, name = Lname, ap = 97.99%          (TP = 199, FP = 1) <br />
class_id = 5, name = Pname, ap = 99.55%          (TP = 198, FP = 2) <br />
<br />
 for conf_thresh = 0.25, precision = 0.99, recall = 0.99, F1-score = 0.99 <br />
 for conf_thresh = 0.25, TP = 1192, FP = 10, FN = 8, average IoU = 84.66 % <br />
<br />
 IoU threshold = 50 %, used Area-Under-Curve for each unique Recall <br />
 mean average precision (mAP@0.50) = 0.991370, or 99.14 % <br />

 -------------------------------------------------------------------------------------
 <br />
-on TestSet:<br />
detections_count = 1368, unique_truth_count = 1200<br />
class_id = 0, name = Card, ap = 99.42%           (TP = 199, FP = 1)<br />
class_id = 1, name = Avatar, ap = 99.41%         (TP = 199, FP = 2)<br />
class_id = 2, name = Id, ap = 99.03%             (TP = 199, FP = 2)<br />
class_id = 3, name = Fname, ap = 99.46%          (TP = 198, FP = 2)<br />
class_id = 4, name = Lname, ap = 97.99%          (TP = 199, FP = 1)<br />
class_id = 5, name = Pname, ap = 99.55%          (TP = 198, FP = 2)<br />
<br />
 for conf_thresh = 0.25, precision = 0.99, recall = 0.99, F1-score = 0.99<br />
 for conf_thresh = 0.25, TP = 1192, FP = 10, FN = 8, average IoU = 84.76 %<br />
<br />
 IoU threshold = 50 %, used Area-Under-Curve for each unique Recall<br />
 mean average precision (mAP@0.50) = 0.991436, or 99.14 %<br />

