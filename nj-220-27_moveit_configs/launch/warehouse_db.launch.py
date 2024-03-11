from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_warehouse_db_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("nj-220-27", package_name="nj-220-27_moveit_configs").to_moveit_configs()
    return generate_warehouse_db_launch(moveit_config)
