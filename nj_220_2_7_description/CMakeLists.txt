cmake_minimum_required(VERSION 3.8)
project(nj_220_2_7_description)

find_package(ament_cmake REQUIRED)

install(
    DIRECTORY
        config 
        launch 
        meshes
        urdf
    DESTINATION
        share/${PROJECT_NAME}
)

ament_package()