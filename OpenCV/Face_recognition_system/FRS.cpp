#include <opencv2/opencv.hpp>
#include <iostream>
#include <ctime>

int main(int argc, char** argv)
{
    cv::VideoCapture cap(0); // open the default camera
    if(!cap.isOpened())  // check if we succeeded
    {
        std::cout << "Camera is not available" << '\n';
        return -1;
    }

    int width = cap.get(cv::CAP_PROP_FRAME_WIDTH);
    int height = cap.get(cv::CAP_PROP_FRAME_HEIGHT);
    int fps = cap.get(cv::CAP_PROP_FPS);
    std::cout << width << "x" << height << " " << fps << "fps" << '\n';

    cv::namedWindow("FRS",1);
    cv::namedWindow("FRS enhanced",1);
    cv::Mat img, img_enhanced;

    for(;;)
    {
        cap >> img; // get a new frame from camera
        if(img.empty())
        {
            std::cout << "Camera is not available" << '\n';
            break;
        }

        cv::imshow("FRS", img);

        cv::Mat kernel = (cv::Mat_<float>(3,3) << -1,-1,-1, -1,9,-1, -1,-1,-1);
        cv::filter2D(img, img_enhanced, -1 , kernel);
        cv::imshow("FRS enhanced", img_enhanced);

        char key = (char)cv::waitKey(1);
        if(key == 27) // ESC
            break;
        else if(key == 13) // Enter
        {
            time_t now = time(0);
            tm *ltm = localtime(&now);
            std::string file_name = "ScreenShot " + std::to_string(ltm->tm_hour) + ":" + std::to_string(ltm->tm_min) + ":" + std::to_string(ltm->tm_sec) + ".jpeg";
            cv::imwrite(file_name, img_enhanced);
        }
    }

    // the camera will be deinitialized automatically in VideoCapture destructor
    return 0;
}
