# 导入opencv工具包
import cv2
# 导入numpy
import numpy as np
# 导入姿势识别器
from poseutil import PoseDetector

# 打开视频文件
# cap = cv2.VideoCapture('videos/pushup.mp4')
cap = cv2.VideoCapture(r"C:\Users\77006\Desktop\PushUpCounter-main\test\videos.mp4")
# 姿势识别器
detector = PoseDetector()

# 方向与个数
dir = 0  # 0为下，1为上
count = 0

# 视频宽度高度
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 录制视频设置
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('videos/pushupoutput.mp4', fourcc, 30.0, (width, height))

while True:
    # 读取摄像头，img为每帧图片
    success, img = cap.read()
    if success:
        h, w, c = img.shape
        # 识别姿势
        img = detector.find_pose(img, draw=True)
        # 获取姿势数据
        positions = detector.find_positions(img)

        if positions:
            # 获取俯卧撑的角度
            angle1 = detector.find_angle(img, 12, 24, 26)
            angle2 = detector.find_angle(img, 12, 14, 16)
            # 进度条长度
            bar = np.interp(angle2, (45, 150), (w // 2 - 100, w // 2 + 100))
            cv2.rectangle(img, (w // 2 - 100, h - 150), (int(bar), h - 100), (0, 255, 0), cv2.FILLED)
            # 角度小于50度认为撑下
            if angle2 <= 50 and angle1 >= 165 and angle1 <= 175:
                if dir == 0:
                    count = count + 0.5
                    dir = 1
            # 角度大于125度认为撑起
            if angle2 >= 125 and angle1 >= 165 and angle1 <= 175:
                if dir == 1:
                    count = count + 0.5
                    dir = 0
            cv2.putText(img, str(int(count)), (w // 2, h // 2), cv2.FONT_HERSHEY_SIMPLEX, 10, (255, 255, 255), 20, cv2.LINE_AA)

        # 打开一个Image窗口显示视频图片
        cv2.imshow('Image', img)

        # 录制视频
        out.write(img)
    else:
        # 视频结束退出
        break

    # 如果按下q键，程序退出
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

# 关闭视频保存器
out.release()
# 关闭摄像头
cap.release()
# 关闭程序窗口
cv2.destroyAllWindows()