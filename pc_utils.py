#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# '''=================================================
# @Project -> File  :skeletons-from-poincloud -> pc_utils.py
# @Author           : Bare Luka Žagar
# @Time             : 12/30/2022 1:59 PM
# @License          : MIT License
# '''=================================================
import open3d as o3d
import numpy as np
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ply_in', help='path to input point cloud file')
    parser.add_argument('--ply_out', help='path to output point cloud file')
    args = parser.parse_args()

    ply_load = o3d.io.read_point_cloud(args.ply_in)
    print("Opened: ", args.ply_in)

    xyz_load = np.asarray(ply_load.points)

    print(xyz_load.shape)

    np.save(args.ply_out, xyz_load)
    print("Saved: ", args.ply_out)


if __name__ == "__main__":
    main()
