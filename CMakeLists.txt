cmake_minimum_required(VERSION 3.28)
project(codegen)

set(CMAKE_CXX_STANDARD 17)

add_custom_target(run_codegen
    COMMAND "./build_cog.bat"
    COMMENT "Running codegen"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
)

add_executable(codegen main.cpp)
add_dependencies(codegen run_codegen)
