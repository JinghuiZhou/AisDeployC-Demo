cmake_minimum_required(VERSION 3.10)
project(AisDeployC-Demo)

if (${CMAKE_SYSTEM_NAME} MATCHES "Linux")
    message(STATUS "Set ONNX_RUNTIME_PATH  for Linux")
    set(ONNX_RUNTIME_PATH /home/N3_3090U5/packages/onnxruntime-linux-x64-gpu-1.8.1)
    find_package(OpenCV REQUIRED)
    INCLUDE_DIRECTORIES(${OpenCV_INCLUDE_DIRS})
    LINK_DIRECTORIES(/home/N3_3090U5/projects/actions-runner/_work/AisDeployC/AisDeployC/build/)
    set(LINK_FILES AisDeployC)

elseif(${CMAKE_SYSTEM_NAME} MATCHES "Windows")
    set(OpenCV_DIR thirdparty/opencv3)
    set(ONNX_RUNTIME_PATH E:\\onnxruntime-win-gpu-x64-1.8.1)
    #    set(ONNX_RUNTIME_PATH E:\\onnxruntime-win-cpu-x64-1.8.1)
    SET(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /MT")
    SET(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} /MT")
    SET(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_RELEASE} /MTd")
    SET(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_RELEASE} /MTd")
    add_definitions(-DDEPLOY_ON_WINDOWS)
    set(BUILD_FOR_WIN_VS  "vs2017")
    if (${BUILD_FOR_WIN_VS} MATCHES "vs2017")
        set(WIN_VC vc15)
    endif()
    INCLUDE_DIRECTORIES("${OpenCV_DIR}/include")
    LINK_DIRECTORIES(${OpenCV_DIR}/lib/${CMAKE_SYSTEM_NAME})
    LINK_DIRECTORIES(E:\\actions-runner\\_work\\AisDeployC\\AisDeployC\\cmake-build-release)
    set(LINK_FILES AisDeployC)
    list(APPEND LINK_FILES IlmImf ippicvmt ippiw ittnotify libjasper libjpeg-turbo libpng libprotobuf libtiff libwebp opencv_imgproc3416 opencv_imgcodecs3416 opencv_core3416 zlib)
else()
    message(STATUS "Set ONNX_RUNTIME_PATH  for MacOs")
    find_package(OpenCV REQUIRED)
    INCLUDE_DIRECTORIES(${OpenCV_INCLUDE_DIRS})
    file(GLOB LIBRARIES "/Users/zhoujinghui/CLionProjects/AisDeployC/cmake-build-debug/libAisDeployC.dylib")
    list(APPEND LINK_FILES opencv_imgproc opencv_imgcodecs opencv_core z dl)
endif()

INCLUDE_DIRECTORIES(./)
INCLUDE_DIRECTORIES(thirdparty/)
INCLUDE_DIRECTORIES(interface/)




set(target_name_basic "basic")
ADD_EXECUTABLE(${target_name_basic} example/basic.cpp)

if (${CMAKE_SYSTEM_NAME} MATCHES "Windows")
    TARGET_LINK_LIBRARIES(${target_name_basic} ${LINK_FILES} ${LIBRARIES})
else()
    TARGET_LINK_LIBRARIES(${target_name_basic} ${LINK_FILES}  ${OpenCV_LIBS})
endif()