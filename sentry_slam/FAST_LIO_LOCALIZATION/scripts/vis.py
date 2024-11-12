import open3d as o3d

# 加载 PCD 文件
pcd = o3d.io.read_point_cloud("/home/yanzj/nav_ws/src/sentry_nav/sentry_slam/FAST_LIO/PCD/scans.pcd")

# 显示点云
o3d.visualization.draw_geometries([pcd])