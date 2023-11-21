import os

from calibrate_helper import Calibrator


def main():
    img_dir = "./pic/RGB_camera_calib_img"
    shape_inner_corner = (11, 8)
    size_grid = 0.02
    # create calibrator
    calibrator = Calibrator(img_dir, shape_inner_corner, size_grid)
    # calibrate the camera
    mat_intri, coff_dis = calibrator.calibrate_camera()

if __name__ == '__main__':
    main()
