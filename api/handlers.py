from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, HTTPException, Query, Request
from fastapi.templating import Jinja2Templates

from data.ros_commands import ROS_MEDIA_BASE, ros_commands

ros_command_router = APIRouter()
ros_templates = Jinja2Templates(directory=Path(__file__).resolve().parents[1] / "templates")
ros_action_icons = {"straight": "forward", "left": "turn-left", "right": "turn-right"}


def ros_command_view(ros_command):
    ros_action_icon = ros_action_icons[ros_command["ros_command_action"]]
    return {**ros_command, "ros_likes_count": len(ros_command["ros_liked_user_ids"]),
            "ros_action_icon": ros_action_icon,
            "ros_video_poster_url": f"{ROS_MEDIA_BASE}/{ros_action_icon}-poster.png"}


@ros_command_router.get("/", name="ros_command_grid")
async def ros_command_grid(request: Request, ros_distance_min: Annotated[float | None, Query(ge=0, allow_inf_nan=False)] = None):
    ros_visible_commands = [ros_command_view(command) for command in ros_commands
                            if command["ros_command_status"] == "published"
                            and (ros_distance_min is None or command["ros_distance_m"] >= ros_distance_min)]
    return ros_templates.TemplateResponse(request=request, name="ros-command-grid.html", context={
        "ros_commands": ros_visible_commands, "ros_distance_min": ros_distance_min, "ros_active_page": "grid"})


@ros_command_router.get("/ros-commands/draft", name="ros_command_draft")
async def ros_command_draft(request: Request):
    ros_draft = next(command for command in ros_commands if command["ros_command_status"] == "draft")
    return ros_templates.TemplateResponse(request=request, name="ros-command-create.html", context={
        "ros_command": ros_command_view(ros_draft), "ros_active_page": "create"})


@ros_command_router.get("/ros-commands/feed", name="ros_command_feed")
async def ros_command_feed(request: Request, ros_command_id: int | None = None,
                           ros_next: Annotated[bool, Query(alias="next")] = False):
    ros_published = sorted((command for command in ros_commands if command["ros_command_status"] == "published"),
                           key=lambda command: command["ros_command_id"])
    if not ros_published:
        raise HTTPException(status_code=404)
    if ros_command_id is None:
        ros_selected = ros_published[0]
    else:
        ros_selected = next((command for command in ros_published if command["ros_command_id"] == ros_command_id), None)
        if ros_selected is None:
            raise HTTPException(status_code=404)
        if ros_next:
            ros_selected = ros_published[(ros_published.index(ros_selected) + 1) % len(ros_published)]
    return ros_templates.TemplateResponse(request=request, name="ros-command-feed.html", context={
        "ros_command": ros_command_view(ros_selected), "ros_active_page": "feed"})
