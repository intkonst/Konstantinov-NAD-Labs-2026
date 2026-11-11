import os

# Для сдачи файлы с этими ключами размещаются в публичном бакете Silo.
ROS_MEDIA_BASE = os.environ.get("ROS_MEDIA_BASE", "http://localhost:9000/ros-commands").rstrip("/")

ros_commands = [
    {"ros_command_id": 1, "ros_command_name": "Поворот направо", "ros_command_action": "right",
     "ros_command_description": "Робот поворачивается на месте по часовой стрелке. Линейное перемещение отсутствует, направление изменяется на заданный угол.",
     "ros_distance_m": 0, "ros_turn_degrees": 90, "ros_start_x_m": 0, "ros_start_y_m": 0, "ros_start_heading_degrees": 0,
     "ros_command_status": "published", "ros_image_url": f"{ROS_MEDIA_BASE}/turn-right.svg", "ros_video_url": f"{ROS_MEDIA_BASE}/turn-right.mp4", "ros_liked_user_ids": [1, 3, 5, 7]},
    {"ros_command_id": 2, "ros_command_name": "Поворот налево", "ros_command_action": "left",
     "ros_command_description": "Поворот робота на месте против часовой стрелки. Начальные координаты остаются прежними, изменяется только направление.",
     "ros_distance_m": 0, "ros_turn_degrees": 90, "ros_start_x_m": 0, "ros_start_y_m": 0, "ros_start_heading_degrees": 0,
     "ros_command_status": "published", "ros_image_url": f"{ROS_MEDIA_BASE}/turn-left.svg", "ros_video_url": f"{ROS_MEDIA_BASE}/turn-left.mp4", "ros_liked_user_ids": [2, 4, 6]},
    {"ros_command_id": 3, "ros_command_name": "Движение вперёд", "ros_command_action": "straight",
     "ros_command_description": "Прямолинейное движение на два метра вдоль текущего направления робота. Угол поворота равен нулю.",
     "ros_distance_m": 2, "ros_turn_degrees": 0, "ros_start_x_m": 0, "ros_start_y_m": 0, "ros_start_heading_degrees": 0,
     "ros_command_status": "published", "ros_image_url": f"{ROS_MEDIA_BASE}/forward.svg", "ros_video_url": f"{ROS_MEDIA_BASE}/forward.mp4", "ros_liked_user_ids": [1, 2, 3, 8, 10]},
    {"ros_command_id": 4, "ros_command_name": "Движение вперёд", "ros_command_action": "straight",
     "ros_command_description": "Прямолинейное движение робота с заданным начальным положением.",
     "ros_distance_m": 2, "ros_turn_degrees": 0, "ros_start_x_m": 0, "ros_start_y_m": 0, "ros_start_heading_degrees": 0,
     "ros_command_status": "draft", "ros_image_url": f"{ROS_MEDIA_BASE}/forward.svg", "ros_video_url": f"{ROS_MEDIA_BASE}/forward.mp4", "ros_liked_user_ids": []},
    {"ros_command_id": 5, "ros_command_name": "Поворот на 180°", "ros_command_action": "right",
     "ros_command_description": "Удалённая команда.", "ros_distance_m": 0, "ros_turn_degrees": 180,
     "ros_start_x_m": 0, "ros_start_y_m": 0, "ros_start_heading_degrees": 0,
     "ros_command_status": "deleted", "ros_image_url": f"{ROS_MEDIA_BASE}/turn-right.svg", "ros_video_url": f"{ROS_MEDIA_BASE}/turn-right.mp4", "ros_liked_user_ids": []},
]
